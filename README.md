# ninon-io.github.io

Source for **ninon-io.github.io**, the personal site of Ninon Devis Salvy —
audio research, instruments and music.

Static site built with Jekyll 4 and deployed to GitHub Pages by GitHub Actions.
No theme: the layouts, components and stylesheet in this repository are the site.

---

## Local setup

Ruby 4.0 (see `.ruby-version`). The system Ruby on macOS is too old.

```sh
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:$PATH"

gem install bundler
bundle config set --local path vendor/bundle
bundle install
```

Optional, for waveforms: `brew install ffmpeg`.

## Running it

```sh
bundle exec jekyll serve            # http://localhost:4000, live reload
bundle exec jekyll build            # one-off build into _site/
```

Before committing anything substantial:

```sh
python3 tools/generate-peaks.py     # waveform data for any new audio
bundle exec jekyll build
./tools/check-build.sh _site        # links, assets, Liquid, legacy URLs
```

## Deployment

`.github/workflows/pages.yml` builds **every** branch and pull request, so
breakage surfaces immediately — but **only `master` is deployed**. Pushing
`phase-2-design-system` or any other working branch cannot replace the live site;
both the artifact upload and the deploy job are guarded on
`github.ref == 'refs/heads/master'`.

To publish: merge into `master`. There is no other path to production.

---

## Where things live

| What | Where |
|---|---|
| Pages | `_pages/*.md` — one file per page, `permalink` sets the URL |
| Layouts | `_layouts/` — `base`, `index`, `prose`, `project-single`, `listing` |
| Components | `_includes/site/` |
| Styles | `_sass/` — `_tokens` first, then `_base`, `_layout`, `_components`, `_player` |
| Navigation | `_data/navigation.yml` |
| Fonts | `assets/fonts/` — self-hosted WOFF2, no CDN |
| Build scripts | `tools/` |

### Adding content

| To add | Put it in | Then |
|---|---|---|
| A new CV | `assets/documents/cv/ninon-devis-salvy-cv-<year>.pdf` | update the link in `_pages/about.md` and the note in `assets/documents/cv/README.md` |
| Project photographs | `assets/media/projects/<project>/images/` | append an entry to that page's `gallery:` |
| Project audio | `assets/media/projects/<project>/audio/` | run `tools/generate-peaks.py`, then reference it with the player include |
| Course documents | `assets/documents/teaching/<course>/` | link it from the course page |

Filenames are lowercase ASCII with hyphens — no spaces, no accents. Reference
assets from Markdown with an absolute path (`/assets/media/...`).

### Audio policy

Ninon's own work is served as **320 kbps MP3**. Masters are not published when an
MP3 derivative is enough. Third-party listening references use the plain
`site/ref-audio.html` include so they read as citations, never as her releases;
her own work uses `site/player.html`.

```liquid
{% include site/player.html src="/assets/media/projects/x/audio/track.mp3"
                            title="Track" meta="Context · year" %}
```

Set `has_player: true` in the page's front matter so the JavaScript loads.

### Waveform peaks

`tools/generate-peaks.py` decodes each audio file with ffmpeg and writes 400
normalised amplitude peaks to `assets/data/peaks/<slug>.json` (~2.8 KB each). The
player fetches that instead of decoding a multi-megabyte file in the browser.
CI runs it on every build. Locally, run it after adding audio; `--force` rebuilds
everything. If ffmpeg is missing the script exits cleanly and the player falls
back to a flat progress bar.

---

## Legacy compatibility folders — do not delete

`documents/`, `images/` and `audio/` at the repository root look like duplicates
of `assets/`. **They are deliberate.** They are frozen byte-identical copies that
keep URLs public before the August 2026 reorganisation returning 200 instead of
404 — course PDFs that students bookmarked and search engines indexed.

GitHub Pages performs no server-side redirection, and a redirect stub named
`*.pdf` would be served with a PDF content type, so physical copies are the only
mechanism that works for binary files without a plugin. Because the content is
byte-identical, Git stores one blob per pair: they cost nothing in history.

**Canonical is always `assets/`.** Never point a page at a legacy path, and never
edit a legacy copy. Each folder has its own README. `tools/check_build.py`
verifies the coverage on every build and fails if it regresses.

---

## Checks

| Script | Does |
|---|---|
| `tools/check-build.sh _site` | broken internal links, missing assets, unrendered Liquid, legacy URL coverage, peaks present |
| `tools/run-visual-checks.py` | drives headless Chrome over every page at 390/768/1440 px: horizontal overflow, missing alt text, heading order, visible focus |
| `tools/palette-check.py` | WCAG 2.2 AA contrast for the palette in both modes |

`run-visual-checks.py` renders each page inside a fixed-width iframe. Headless
Chrome clamps its own layout viewport at about 485 px, so `--window-size` cannot
test real phone widths — the iframe can.

## Design system

Palette, type scale and spacing live in `_sass/_tokens.scss`. Colours descend
from the ones chosen by hand in the previous site: gold is the single accent,
with oxblood and blue used sparingly as semantic markings — the way markings sit
on an instrument panel, not as branding. Dark-first with a separately designed
light mode via `prefers-color-scheme`. Border radius is 0 everywhere; there are
no gradients, glass or drop shadows.

Fonts are Archivo (display), Newsreader (body) and IBM Plex Mono (utility), all
SIL OFL, self-hosted so no visitor IP reaches a third party. See
`assets/fonts/README.md`.

---

## History

This repository began as a fork of
[Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by Michael
Rose. All of that theme's code has been removed. `LICENSE` (MIT) is retained to
cover the inherited history; it does not grant rights over site content.
