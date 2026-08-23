#!/usr/bin/env python3
"""Precompute waveform peak data for the custom audio player.

For every audio file under assets/media/**/audio/ (archive/ excluded), write
assets/data/peaks/<slug>.json holding a normalised array of amplitude peaks.
The player fetches that instead of decoding a multi-megabyte file in the browser.

    python3 tools/generate-peaks.py            # only missing or stale peaks
    python3 tools/generate-peaks.py --force    # rebuild everything

Requires ffmpeg. If ffmpeg is absent the script warns and exits 0 — the player
degrades to a flat progress line, which is not worth failing a build over. CI
installs ffmpeg, so peaks are always present in production.

Adding a new track: drop the MP3 into that project's audio/ folder and run this.
The GitHub Actions build runs it automatically.
"""

import array
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "assets", "media")
OUT = os.path.join(ROOT, "assets", "data", "peaks")
BUCKETS = 400
EXTS = (".mp3", ".wav", ".flac", ".m4a", ".ogg", ".opus")


def slug_for(path):
    """assets/media/projects/neurorack/audio/raster-demo.mp3
       -> projects-neurorack-raster-demo"""
    rel = os.path.relpath(path, MEDIA)
    rel = os.path.splitext(rel)[0]
    parts = [p for p in rel.split(os.sep) if p != "audio"]
    return "-".join(parts)


def peaks_for(path):
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "8000",
         "-f", "s16le", "-acodec", "pcm_s16le", "-"],
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace")[:200])

    raw = proc.stdout
    samples = array.array("h")
    samples.frombytes(raw[: len(raw) - (len(raw) % 2)])
    if not samples:
        return [0.0] * BUCKETS

    size = max(1, len(samples) // BUCKETS)
    out = []
    for i in range(BUCKETS):
        chunk = samples[i * size:(i + 1) * size]
        out.append((max((abs(x) for x in chunk), default=0)) / 32768.0)
    top = max(out) or 1.0
    return [round(v / top, 4) for v in out]


def main():
    force = "--force" in sys.argv

    if not shutil.which("ffmpeg"):
        print("generate-peaks: ffmpeg not found — skipping "
              "(player falls back to a flat bar)", file=sys.stderr)
        os.makedirs(OUT, exist_ok=True)
        return 0

    os.makedirs(OUT, exist_ok=True)
    written = skipped = failed = 0

    for dirpath, _dirnames, filenames in os.walk(MEDIA):
        if f"{os.sep}archive{os.sep}" in dirpath + os.sep:
            continue
        for fn in sorted(filenames):
            if not fn.lower().endswith(EXTS):
                continue
            src = os.path.join(dirpath, fn)
            dest = os.path.join(OUT, slug_for(src) + ".json")

            if not force and os.path.exists(dest) and \
               os.path.getmtime(dest) >= os.path.getmtime(src):
                skipped += 1
                continue

            try:
                data = {"version": 1, "buckets": BUCKETS, "peaks": peaks_for(src)}
            except Exception as exc:                       # noqa: BLE001
                print(f"  FAILED {fn}: {exc}", file=sys.stderr)
                failed += 1
                continue

            with open(dest, "w") as fh:
                json.dump(data, fh, separators=(",", ":"))
            print(f"  peaks: {os.path.basename(dest)} "
                  f"({os.path.getsize(dest)} bytes)")
            written += 1

    print(f"generate-peaks: {written} written, {skipped} up to date, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
