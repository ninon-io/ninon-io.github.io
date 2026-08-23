# Fonts

Self-hosted WOFF2, latin subset. No Google Fonts or other CDN request is made —
visitor IPs are never sent to a third party.

| File | Family | Notes |
|---|---|---|
| `archivo-variable.woff2` | Archivo | variable weight axis, used 500–700 |
| `newsreader-variable.woff2` | Newsreader | variable weight axis, used 300–500 |
| `newsreader-italic-variable.woff2` | Newsreader Italic | variable weight axis |
| `ibm-plex-mono-400.woff2` | IBM Plex Mono | static 400 |
| `ibm-plex-mono-500.woff2` | IBM Plex Mono | static 500 |

All three families are licensed under the **SIL Open Font License 1.1**, which
permits web embedding and redistribution provided the licence travels with the
files. Full text: <https://scripts.sil.org/OFL>

- Archivo — Omnibus-Type. <https://github.com/Omnibus-Type/Archivo>
- Newsreader — Production Type. <https://github.com/productiontype/Newsreader>
- IBM Plex Mono — IBM. <https://github.com/IBM/plex>

## Updating

Fetch the latin subset from the Google Fonts CSS API with a modern browser
User-Agent (it serves WOFF2 only to browsers that support it), then save the
files here. Google returns one variable file per family, so several declared
weights resolve to the same file — dedupe by content hash before committing.
