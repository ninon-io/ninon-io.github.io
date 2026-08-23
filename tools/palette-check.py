#!/usr/bin/env python3
"""Compare candidate palettes against WCAG 2.2 AA.

Derived from the colours Ninon had already chosen in _sass/minimal-mistakes/skins/_dark.scss:
  #8E1A27 oxblood · #EAC67A / #d5b110 gold · #078dab / #155765 blue · #f5f2f0 warm off-white

AA thresholds: 4.5:1 body text, 3.0:1 large text (>=24px or >=18.66px bold) and UI borders.
"""

def srgb_to_lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


VARIANTS = {
    "A — Panel (neutral graphite, ochre signal)": {
        "dark": dict(ground="#101113", panel="#17181B", rule="#282A2E", ink="#EDE9E3",
                     muted="#A09B93", faint="#6E6A64", accent="#D2A64B",
                     oxblood="#C56A5C", blue="#7FA3C4"),
        "light": dict(ground="#F4F2EE", panel="#FFFFFF", rule="#D8D3CA", ink="#16171A",
                      muted="#5D5952", faint="#8A857D", accent="#8A6410",
                      oxblood="#9B3124", blue="#2F5A80"),
    },
    "B — Brass (warm ground, richer gold)": {
        "dark": dict(ground="#121110", panel="#1A1917", rule="#2C2A26", ink="#F0EBE3",
                     muted="#A29B8F", faint="#726C62", accent="#C9A227",
                     oxblood="#C2604C", blue="#6E97BE"),
        "light": dict(ground="#F5F2EB", panel="#FFFFFF", rule="#DAD3C6", ink="#1A1815",
                      muted="#5E584E", faint="#8B857A", accent="#7E5B0C",
                      oxblood="#94301F", blue="#2C5578"),
    },
    "C — Ink (cool near-black, blue more present)": {
        "dark": dict(ground="#0C0D10", panel="#141619", rule="#252932", ink="#E9E9EC",
                     muted="#989CA4", faint="#686C75", accent="#C6A052",
                     oxblood="#C2645C", blue="#8AAFD4"),
        "light": dict(ground="#F1F2F4", panel="#FFFFFF", rule="#D2D5DB", ink="#101216",
                      muted="#565B63", faint="#848992", accent="#836011",
                      oxblood="#98352A", blue="#2B5686"),
    },
}

# (label, foreground token, background token, required ratio)
CHECKS = [
    ("body text",        "ink",     "ground", 4.5),
    ("body on panel",    "ink",     "panel",  4.5),
    ("muted text",       "muted",   "ground", 4.5),
    ("faint / labels*",  "faint",   "ground", 3.0),
    ("accent as text",   "accent",  "ground", 4.5),
    ("accent on panel",  "accent",  "panel",  4.5),
    ("oxblood as text",  "oxblood", "ground", 4.5),
    ("blue as text",     "blue",    "ground", 4.5),
    ("hairline rule*",   "rule",    "ground", 1.2),
]

print("WCAG 2.2 AA — * = large-text/UI threshold (3.0), rules exempt (decorative)\n")
summary = {}
for name, modes in VARIANTS.items():
    print("=" * 78)
    print(name)
    fails_total = 0
    for mode in ("dark", "light"):
        p = modes[mode]
        print(f"  {mode.upper():<6}", end="")
        rows, fails = [], 0
        for label, fg, bg, need in CHECKS:
            r = ratio(p[fg], p[bg])
            ok = r >= need
            if not ok and need > 1.2:
                fails += 1
            rows.append((label, p[fg], p[bg], r, need, ok))
        print(f"  {'PASS' if fails == 0 else str(fails) + ' FAIL'}")
        for label, fg, bg, r, need, ok in rows:
            flag = "  " if ok else "<-"
            print(f"      {label:<17} {fg} on {bg}  {r:5.2f}:1  (need {need})  {flag}")
        fails_total += fails
    summary[name] = fails_total
    print()

print("=" * 78)
for k, v in summary.items():
    print(f"  {'PASS' if v == 0 else f'{v} failures':<14} {k}")
