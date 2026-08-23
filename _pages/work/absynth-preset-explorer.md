---
layout: project-single
permalink: /work/absynth-preset-explorer/
title: "Absynth 6 Preset Explorer"
eyebrow: "Native Instruments · shipped"
excerpt: "A way to browse a large preset library by sound rather than by name — presets positioned by what they actually sound like, in a space you move through."
kind: "Product R&D"
years: "2025"
toc: true

credits:
  role: "Research engineering — audio analysis, preset organisation, and the spatial and kinetic logic behind the map"
  collaborators:
    - name: "Eric Oake"
      role: "Product Design, interaction prototyping"
    - name: "Hannah Lockwood"
      role: "Lead Product Design"
  support: "Built with the Native Instruments research and product teams."
---

Absynth has an enormous preset library, and for most of its life the only way in
was a list of names. Names are a poor index for sound: they tell you what someone
called a patch, not what it does. The Preset Explorer replaces the list with a
map, where position means something — presets sit near the sounds they resemble.

I worked on this from the early research prototypes through to the shipped
feature, on the audio analysis and preset organisation, and on the spatial and
kinetic logic that turns that analysis into something you can move through.

## Listening instead of generating

The analysis extracts each patch's perceptual character — brightness, sustain,
noisiness and related qualities — and uses it to place the patch. Nothing here
generates audio. As the article puts it, rather than using AI to generate sound,
we use it to *listen*: analysing and organising presets to reveal relationships
that already exist in the library.

That distinction is the whole design. The system does not decide what you should
play. It arranges what is already there so that your ear can do the deciding.

## A space with physics

Presets behave as particles: each is drawn toward its own sonic coordinates while
pushing away from its neighbours. Similar sounds settle into clusters, contrasts
open up as gaps, and the structure of the library becomes visible rather than
alphabetical. Moving through it with the mouse or the keyboard, with an audition
mode for fast previewing, turns browsing into listening. Filters narrow the field
in real time as your intent sharpens.

Absynth's creator Brian Clevinger described the effect as removing language from
the search process — music and language, as he put it, usually occupy different
parts of the mind.

## Why it matters to me

Most of my research is about giving musicians control over models rather than
outcomes from them. This is the same argument in a product: AI used for
navigation, orientation and agency, not for automatic generation. It is also the
first piece of my work at Native Instruments that shipped to players rather than
to a paper.

[Read the full article on the NI blog](https://blog.native-instruments.com/absynth-preset-explorer/){: .btn .btn--primary}
[Absynth 6](https://www.native-instruments.com/en/products/komplete/synths/absynth-6/){: .btn}
