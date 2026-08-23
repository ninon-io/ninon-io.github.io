# /images — LEGACY COMPATIBILITY PATHS. DO NOT EDIT.

Copies kept so that image URLs which were public before the August 2026 asset
reorganisation keep returning 200 instead of 404 — these may be hotlinked from
elsewhere or indexed by image search.

**Canonical sources live in `assets/media/`.** Edit those, never these.

All 45 previously public `/images/*` URLs are preserved, byte-identical. The one
omission is `/images/neurorack/init.md`, a 1-byte placeholder that only ever
existed to make the folder appear on GitHub.

Why copies rather than redirects: GitHub Pages performs no server-side
redirection, and a redirect stub named `*.pdf` or `*.mp3` would be served with that
file type’s content type, so the browser would fail to render it. Physical copies
are the only approach that works for binary files without adding a Jekyll plugin.
Because the content is byte-identical, Git stores a single blob per pair — these
copies add **zero** bytes to repository history.

Filenames here are preserved exactly as they were, including spaces and accents,
because URL fidelity is the entire point. The canonical copies under `assets/`
use the lowercase ASCII convention.

If you ever replace a canonical file, refresh its alias here too — or delete the
alias if the old URL no longer matters.
