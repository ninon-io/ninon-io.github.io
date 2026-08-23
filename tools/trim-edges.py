#!/usr/bin/env python3
"""Remove 1–2 px light edges baked into source photographs.

Several files arrived with a pure-white row or column along one side, an artifact
of the crop or screen capture they came from. Against a dark ground that reads as
an accidental hairline around the photograph.

This trims the artifact from the source itself, so both the responsive
derivatives and the original fallback are clean. It is deliberately conservative:

  - photographs only; diagrams, logos, UI captures and figures are skipped,
    because a border there may be part of the content
  - an edge is trimmed only when it is BOTH much brighter than the row three
    pixels inside it AND close to uniform along its length, which is what an
    artifact looks like and what real image content does not
  - at most 2 px per side, so composition is untouched

    python3 tools/trim-edges.py --dry-run   # report only
    python3 tools/trim-edges.py             # apply
"""

import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    print("trim-edges: Pillow not installed; skipping", file=sys.stderr)
    sys.exit(0)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "assets", "media")

# Content where a border may be meaningful — never touched.
SKIP = ("architecture-overview", "sinc-nsf", "jetson-nano", "neurorack-banner",
        "neurorack-interface", "neurorack-logo", "acids-logo", "faceplate",
        "og-image", "absynth-6-key-art", "preset-explorer-map", "figure-")

BRIGHTER_THAN_INNER = 25     # an artifact edge is markedly lighter than its neighbour
MAX_SPREAD = 40              # ...and close to uniform along its length
MAX_TRIM = 2                 # never remove more than this


def edge_stats(g, side, offset):
    w, h = g.size
    step_x = max(1, w // 300)
    step_y = max(1, h // 300)
    if side == "top":
        px = [g.getpixel((x, offset)) for x in range(0, w, step_x)]
    elif side == "bottom":
        px = [g.getpixel((x, h - 1 - offset)) for x in range(0, w, step_x)]
    elif side == "left":
        px = [g.getpixel((offset, y)) for y in range(0, h, step_y)]
    else:
        px = [g.getpixel((w - 1 - offset, y)) for y in range(0, h, step_y)]
    return sum(px) / len(px), max(px) - min(px)


def trim_for(path):
    """How many pixels to remove from each side: (left, top, right, bottom)."""
    with Image.open(path) as im:
        g = ImageOps.exif_transpose(im).convert("L")
        cuts = {}
        for side in ("top", "bottom", "left", "right"):
            n = 0
            while n < MAX_TRIM:
                mean, spread = edge_stats(g, side, n)
                inner, _ = edge_stats(g, side, n + 3)
                if mean - inner > BRIGHTER_THAN_INNER and spread < MAX_SPREAD:
                    n += 1
                else:
                    break
            cuts[side] = n
        return cuts


def main():
    dry = "--dry-run" in sys.argv
    touched = 0

    for dirpath, _dirs, files in os.walk(MEDIA):
        if "derived" in dirpath or f"{os.sep}archive{os.sep}" in dirpath + os.sep:
            continue
        for fn in sorted(files):
            if not fn.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            if any(s in fn.lower() for s in SKIP):
                continue
            path = os.path.join(dirpath, fn)
            cuts = trim_for(path)
            if not any(cuts.values()):
                continue

            with Image.open(path) as im:
                im = ImageOps.exif_transpose(im)
                w, h = im.size
                box = (cuts["left"], cuts["top"], w - cuts["right"], h - cuts["bottom"])
                sides = ", ".join(f"{k} {v}px" for k, v in cuts.items() if v)
                print(f"  {fn:<44} trim {sides}")
                if not dry:
                    out = im.crop(box)
                    if path.lower().endswith(".png"):
                        out.save(path, "PNG", optimize=True)
                    else:
                        out.save(path, "JPEG", quality=94, subsampling=0)
            touched += 1

    print(f"trim-edges: {touched} image(s) {'would be ' if dry else ''}trimmed")
    if touched and not dry:
        print("  now re-run tools/index-images.py and tools/build-images.py --force")
    return 0


if __name__ == "__main__":
    sys.exit(main())
