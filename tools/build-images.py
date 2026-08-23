#!/usr/bin/env python3
"""Generate responsive derivatives for the site's canonical photography.

For each image under assets/media (archive excluded) that is large enough to be
worth it, write AVIF and WebP derivatives at a small set of widths into
assets/media/derived/, and record them in _data/imagemeta.yml so the image
component can emit srcset.

Design decisions:
  - Widths are chosen from what the layout actually renders, not a generic ladder.
  - Nothing is upscaled: a width is skipped if it exceeds the source.
  - EXIF orientation is applied before resizing, so rotated phone photographs
    are not silently sideways.
  - The original stays in place and remains the <img src> fallback, so an old
    browser and every legacy URL still work.
  - Diagrams, logos and small UI captures are skipped; re-encoding them wins
    nothing and can blur text.

    python3 tools/build-images.py           # only what is missing or stale
    python3 tools/build-images.py --force
"""

import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    print("build-images: Pillow not installed; skipping", file=sys.stderr)
    sys.exit(0)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "assets", "media")
DERIVED = os.path.join(MEDIA, "derived")

# The widths the layout actually asks for: the reading column, the field, and
# their 2x counterparts, plus a small one for phones.
WIDTHS = [480, 760, 1024, 1440, 1960]
MIN_SOURCE_WIDTH = 700          # below this, a derivative is not worth a request
SKIP = ("acids-logo", "jetson-nano", "sinc-nsf", "architecture-overview",
        "neurorack-banner", "neurorack-logo", "og-image", "faceplate",
        "neurorack-interface", "absynth-6-key-art")
EXTS = (".jpg", ".jpeg", ".png")


def derivatives_for(path, force=False):
    name = os.path.splitext(os.path.basename(path))[0]
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)          # honour EXIF orientation
        sw, sh = im.size
        if sw < MIN_SOURCE_WIDTH:
            return []
        rgb = im.convert("RGB")

        made = []
        for w in WIDTHS:
            if w > sw:                            # never upscale
                continue
            h = round(sh * w / sw)
            for fmt, ext, kw in (
                ("AVIF", ".avif", dict(quality=55)),
                ("WEBP", ".webp", dict(quality=76, method=5)),
            ):
                out = os.path.join(DERIVED, f"{name}-{w}{ext}")
                if not force and os.path.exists(out) and \
                   os.path.getmtime(out) >= os.path.getmtime(path):
                    made.append((w, ext))
                    continue
                try:
                    rgb.resize((w, h), Image.LANCZOS).save(out, fmt, **kw)
                    made.append((w, ext))
                except Exception as exc:          # AVIF support is optional
                    if fmt == "AVIF":
                        continue
                    print(f"  {name} {w}{ext}: {exc}", file=sys.stderr)
        return made


def main():
    force = "--force" in sys.argv
    os.makedirs(DERIVED, exist_ok=True)

    index = {}
    count = skipped = 0
    for dirpath, _dirs, files in os.walk(MEDIA):
        if "derived" in dirpath or f"{os.sep}archive{os.sep}" in dirpath + os.sep:
            continue
        for fn in sorted(files):
            if not fn.lower().endswith(EXTS):
                continue
            if any(s in fn.lower() for s in SKIP):
                skipped += 1
                continue
            path = os.path.join(dirpath, fn)
            made = derivatives_for(path, force)
            if made:
                widths = sorted({w for w, _ in made})
                exts = sorted({e for _, e in made})
                index[fn] = (widths, exts)
                count += 1
            else:
                skipped += 1

    # merge into the metadata the image component already reads
    meta_path = os.path.join(ROOT, "_data", "imagemeta.yml")
    lines = open(meta_path).read().splitlines() if os.path.exists(meta_path) else []
    out, current = [], None
    for line in lines:
        if line.startswith('"'):
            current = line.strip().strip(":").strip('"')
        if line.strip().startswith(("srcw:", "srcf:")):
            continue
        out.append(line)
        if line.strip().startswith("max:") and current in index:
            widths, exts = index[current]
            out.append("  srcw: [" + ", ".join(str(w) for w in widths) + "]")
            out.append("  srcf: [" + ", ".join(e.lstrip(".") for e in exts) + "]")
    open(meta_path, "w").write("\n".join(out) + "\n")

    total = sum(os.path.getsize(os.path.join(DERIVED, f))
                for f in os.listdir(DERIVED)) if os.path.isdir(DERIVED) else 0
    print(f"build-images: {count} images with derivatives, {skipped} skipped "
          f"(too small or excluded), {total // 1024} KB generated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
