# Site assets

Everything under this folder is Ninon's own material. The two sibling folders
`css/` and `js/` belong to the vendored Minimal Mistakes theme — leave those alone.

```
assets/
├── css/                    theme (do not reorganise)
├── js/                     theme (do not reorganise)
├── documents/
│   ├── cv/                 ← current CV lives here
│   ├── research/
│   └── teaching/{ableton,pure-data,cryptology,java}/
└── media/
    ├── about/              portraits
    ├── projects/
    │   ├── neurorack/{images,audio}/
    │   ├── wilding-ai/{images,audio}/
    │   └── frave/{images,audio}/     empty, ready for material
    ├── research/
    │   ├── images/
    │   └── thesis/{images,audio}/    audio = listening references
    ├── teaching/images/
    ├── site/               page headers not tied to one project
    └── archive/            unreferenced material kept for triage
```

## Conventions

- lowercase, ASCII, hyphen-separated filenames; no spaces, no accents
- every project folder has `images/` and `audio/` so new work needs no restructuring
- reference assets from Markdown with an absolute path, e.g.
  `/assets/media/projects/neurorack/images/faceplate.png`

## Where to add new material

| What | Where |
|---|---|
| New CV | `assets/documents/cv/` — then update the link in `_pages/about.md` |
| Wilding AI spatial sketch | `assets/media/projects/wilding-ai/audio/ninon-jun-spatial-sketch.wav` |
| More Wilding AI photos | `assets/media/projects/wilding-ai/images/` + add a `gallery:` entry in `_pages/projects_ctm.md` |
| A new project's audio | `assets/media/projects/<project>/audio/` |
| A new project's photos | `assets/media/projects/<project>/images/` |
