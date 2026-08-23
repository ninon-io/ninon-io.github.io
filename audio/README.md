# /audio — LEGACY COMPATIBILITY PATHS. DO NOT EDIT.

Copies kept so that audio URLs the site once surfaced in a player keep returning
200 instead of 404.

**Canonical sources live in `assets/media/`.** Edit those, never these.

Aliased here: the eight listening references from the thesis companion page plus
the Neurorack demo — every audio file any page ever pointed at, and therefore the
only audio URLs a visitor could have saved or a crawler could have indexed.

Deliberately **not** aliased: eleven files that no page has ever referenced. They
were reachable only by guessing a filename, and copying them would add roughly
155 MB to the published site. They are unchanged in
`assets/media/archive/audio/`, awaiting identification.

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
