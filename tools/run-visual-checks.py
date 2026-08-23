#!/usr/bin/env python3
"""Drive headless Chrome over every page at several viewports and report
responsive / accessibility problems.

    python3 tools/run-visual-checks.py http://localhost:4322

Expects a build instrumented with tools/check-visual.js (see the README).
Exits non-zero if any page reports a problem.
"""

import html
import json
import os
import re
import subprocess
import sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIEWPORTS = [390, 768, 1440]
PAGES = [
    "/", "/work/", "/work/n-v/", "/work/neurorack/",
    "/work/absynth-preset-explorer/", "/work/wilding-ai/", "/work/frave/",
    "/sound/",
    "/research/", "/research/thesis/", "/research/thesis/companion/",
    "/research/publications/", "/research/talks/",
    "/research/teaching/", "/research/teaching/ableton/",
    "/research/teaching/pure-data/", "/research/teaching/cryptology/",
    "/research/teaching/java/", "/about/", "/about/press/",
]


HARNESS = """<!doctype html><meta charset="utf-8"><title>vp</title>
<style>html,body{{margin:0}}iframe{{border:0;display:block}}</style>
<iframe id="f" src="{path}" width="{width}" height="1400"></iframe>
<script>
// Headless Chrome clamps its own layout viewport at ~485px, so --window-size
// cannot test real phone widths. A static iframe of exact CSS width can.
document.getElementById('f').onload = function () {{
  var doc = this.contentDocument, de = doc.documentElement, probs = [];
  if (de.scrollWidth > de.clientWidth + 1) {{
    var wide = [];
    doc.querySelectorAll('body *').forEach(function (el) {{
      var r = el.getBoundingClientRect();
      if (r.right > de.clientWidth + 1 && r.width > 0)
        wide.push(el.tagName.toLowerCase() + '.' + (el.className || '').toString().split(' ')[0] + '@' + Math.round(r.right));
    }});
    probs.push('overflow ' + de.scrollWidth + '>' + de.clientWidth + ' [' + wide.slice(0,4).join(', ') + ']');
  }}
  var noAlt = [];
  doc.querySelectorAll('img').forEach(function (i) {{ if (!i.hasAttribute('alt')) noAlt.push(i.getAttribute('src')); }});
  if (noAlt.length) probs.push('img missing alt: ' + noAlt.join(','));
  var last = 0, bad = [];
  doc.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(function (h) {{
    var l = +h.tagName[1];
    if (last && l > last + 1) bad.push(h.tagName + ' after H' + last);
    last = l;
  }});
  if (bad.length) probs.push('heading order: ' + bad.join(', '));
  var fs = doc.querySelectorAll("a[href],button,[tabindex]:not([tabindex='-1'])"), noRing = 0;
  fs.forEach(function (el) {{
    el.focus();
    var cs = doc.defaultView.getComputedStyle(el);
    if (!(cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) &&
        !(parseFloat(cs.borderBottomWidth) > 0)) noRing++;
  }});
  if (noRing) probs.push(noRing + ' focusable(s) without a visible focus ring');
  document.title = 'VP:' + JSON.stringify({{w: de.clientWidth, focusables: fs.length, problems: probs}});
}};
</script>"""


def probe(base, path, width, servedir):
    name = "_vp_%s_%d.html" % (re.sub(r"[^a-z0-9]+", "-", path).strip("-") or "root", width)
    with open(os.path.join(servedir, name), "w") as fh:
        fh.write(HARNESS.format(path=path, width=width))
    dom = subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--window-size=1800,1600",
         "--virtual-time-budget=5000", "--dump-dom", f"{base}/{name}"],
        capture_output=True, text=True,
    ).stdout
    m = re.search(r"<title>VP:(.*?)</title>", dom, re.S)
    if not m:
        return None
    try:
        return json.loads(html.unescape(m.group(1)))
    except json.JSONDecodeError:
        return None


def main(base, servedir):
    problems = 0
    for w in VIEWPORTS:
        print(f"═══ viewport {w}px ═══")
        clean = 0
        for p in PAGES:
            r = probe(base, p, w, servedir)
            if r is None:
                print(f"  {p:<28} NO RESULT")
                problems += 1
                continue
            if r.get("problems"):
                problems += len(r["problems"])
                for msg in r["problems"]:
                    print(f"  {p:<28} [{r.get('w')}px] {msg}")
            else:
                clean += 1
        print(f"  {clean}/{len(PAGES)} pages clean")
    print()
    print(f"visual checks: {problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4322",
                  sys.argv[2] if len(sys.argv) > 2 else "/tmp/nio_check"))
