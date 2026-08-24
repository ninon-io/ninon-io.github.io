---
layout: project-single
permalink: /research/singularity-and-creation/
title: "Singularity and Creation in the Age of AI"
eyebrow: "CNC Lab · with Jun Suzuki"
excerpt: "Where does originality live when the model producing it averages everything it has seen? Two experiments, one on text and one on images, locating the narrow band in which a generative system diverges without falling apart."
opening: direct   # provenance block already opens the page
kind: "Paper"
years: "2026"
toc: true

lead:
  src: /assets/media/research/cnc-singularity/images/ninon-jun-cnc.png
  alt: "Diptych: Ninon and Jun Suzuki performing in silhouette, each against a different high-contrast generative projection"
  present: natural

credits:
  role: "Co-author — experiment design, text and image experiments, analysis"
  collaborators:
    - name: "Jun Suzuki"
      role: "Co-author"
      url: "https://blog.junsuzuki.xyz/"
  support: "Written for the CNC Lab, the R&D branch of the Centre national du cinéma et de l'image animée, in response to its second call for contributions on AI and creation. Published in French, April 2026."
---

Generative models are trained on very large piles of existing material, and left
alone they return the average of that pile. Text that reads like text. Images
that look like images. For summarising a document or answering a question that is
exactly what you want. For anything creative it is a ceiling.

*Singularité et Création à l'Ère de l'Intelligence Artificielle* asks where
originality can live under that condition. Philosophy offers several ways in —
intuition under algorithms, the algorithmic image, art after aesthetics. We took
the empirical route instead: two experiments, one on language and one on images,
looking for the settings at which a model stops returning its own centre.

[Read the paper (French, PDF)](https://www.cnc.fr/documents/36995/2568943/CNC+Lab+-+Singularit%C3%A9+et+Cr%C3%A9ation+%C3%A0+l%E2%80%99%C3%88re+de+l%E2%80%99Intelligence+Artificielle+-+Ninon+Devis+Salvy%2C+Jun+Suzuki.pdf/feeb200e-2502-4512-fe27-91ec422befc0?t=1775143018736){: .btn .btn--primary}
[CNC Lab call](https://www.cnc.fr/professionnels/actualites/deuxieme-appel-a-contributions-du-cnc-lab_2167679){: .btn}
[Jun Suzuki's companion article](https://blog.junsuzuki.xyz/blog/singularity-controlled-divergence){: .btn}

## How hot can language get before it breaks

Language models expose a parameter called temperature. Low temperature and the
model takes the likeliest next word; the output is smooth and foreseeable. Raise
it and the model reaches for less likely words. Raise it far enough and it stops
meaning anything at all.

We swept the full range GPT-4.1 exposes, 0 to 2 in steps of 0.1, across three
kinds of input — a synopsis, a dialogue, a storyboard description — with ten
outputs at every setting. Each output was measured three ways: whether it was
still valid language, how varied its vocabulary was, and how close it stayed to
the meaning of the prompt.

Three regimes appeared.

{% include site/regime-diagram.html %}

Below 1.2 the model sits on a **plateau**: coherent, competent, and leaving most
of the variation it is capable of untouched. Between 1.2 and 1.4 is the
**singularity zone**, where the output genuinely departs from the default and
remains readable. From 1.5 the model **ruptures** — languages mix, tokens are
invented, meaning drifts away from the prompt and does not come back.

The same opening line at three settings makes the shape concrete. At temperature
0 the model produces a plausible pandemic, competently narrated. At 1.4 it
produces a luminous wave of unknown origin and a civilisation rebuilding itself
around other senses. At 2.0 it produces a sentence that has stopped being a
sentence.

The zone is narrow, and it sits immediately before the collapse. Its exact
position belongs to the model we tested; what generalises is not the numbers but
the shape — a thin band just before the break. Worth noting that newer models
increasingly do not expose the dial at all. Every hidden parameter is one fewer
lever for pushing a system past its defaults.

## Images, and a frontier of trade-offs

For images the question is the same and the controls are different. Using Stable
Diffusion 1.5 we generated several thousand images from the same science-fiction
premise, varying three things: how strictly the model was held to the prompt, how
much random noise was injected during generation, and how much weight was placed
on particular stylistic terms.

Each image was then asked two questions. Does it actually illustrate this brief,
or would it serve any brief equally well? And does it look like anything other
than what the model wants to give you by default?

Those two goals pull against each other. Hold to the prompt and the image comes
back average. Push for difference and it drifts off the brief. Only a narrow set
of settings satisfies both — in optimisation the shape has a name, a **Pareto
frontier**, a set of trade-offs rather than a single correct answer.

{% include site/img.html src="/assets/media/research/cnc-singularity/images/figure-9-sweet-spot.png" present="bleed" alt="A generated image from the sweet-spot regime: a face in close-up, dissolving into beaded, liquid texture — evoked rather than illustrated" caption="From the sweet-spot regime. The baseline illustrates the brief; chaos is unusable; this sits between the two — evoked rather than illustrated." %}

One honest limit, which the paper states plainly: the frontier is measured, but
the labels along it are aesthetic judgements. LPIPS, the metric used, captures how
different two images are from one another. It has nothing to say about whether
either is any good. Composition, emotional weight and narrative coherence would
need a qualitative study with human judges.

## Controlled divergence

Both experiments converge on the same finding, which the paper calls **controlled
divergence**. Singularity in generative work lives in a narrow band where the
system departs from its statistical centre without losing coherence. Push too
gently and the result stays average. Push too hard and it becomes noise.

That changes what the artist is actually doing. The work is not writing a prompt
and choosing a favourite from four returns. It is shaping the space those returns
come out of: which parameters, held in what range, under which constraints, from
what seed. The image or the paragraph is downstream of that shaping. The paper's
term for this is the **architect of generative conditions** rather than the author
of generated results — authorship moves upstream of the output.

## Against frictionless iteration

If the band is that narrow, no amount of free iteration will land you in it. You
have to commit to something.

When trying again costs nothing, every choice becomes trivial. A decision to keep
an image that could be regenerated at no cost is barely a decision at all, and a
process assembled out of barely-decisions produces work that feels like nobody
made it.

Against this the paper proposes **methodical friction**: constrain the loop on
purpose. Fixed iteration budgets. Locked seeds. Choices you cannot take back.
Rules you have to live inside. The claim runs against intuition — friction is what
makes a gesture a gesture, and removing all of it leaves curation at best.

This is not only true of work made with generative models. It applies wherever the
marginal cost of trying one more thing has collapsed. But it is urgent here,
because the whole direction of travel in the field is toward removing friction:
cheaper, faster, fewer parameters, more automation. Follow that far enough and
what is left is a set of interchangeable options and nobody's signature on any of
them.

A gesture only counts when choosing differently would have cost you something.

## Related

The residency behind much of this thinking was [Wilding AI](/work/wilding-ai/) at
MONOM in January 2025, where the brief was to hack, misuse and break generative
tools for a week. The argument continues in
[*Aux abords de l'abîme*](/research/aux-abords-de-labime/), and it is the same one
running through the [thesis](/research/thesis/): a model becomes useful to an
artist at the point where it becomes controllable.
