---
layout: performance
permalink: /sound/saule/
title: "Säule, Berghain"
eyebrow: "Live · Berlin · September 2026"
excerpt: "A live set built from two instruments: the Neurorack, and the room itself. Säule was measured beforehand for the low frequencies its architecture reinforces, and those resonances were played as material rather than corrected away."
description: "A live set at Säule, Berghain, Berlin, September 2026. The room's low-frequency response was measured in advance and used as compositional material, alongside the Neurorack — a neural synthesiser built during a PhD at IRCAM."
kind: "Live"
years: "2026"

lead:
  src: /assets/media/sound/saule/saule-berghain-arrival.jpg
  alt: "Ninon seen from behind on the path outside Berghain at night, in a long black and white coat, holding flowers, a modular synthesiser case and a suitcase standing beside her, the lit facade of the building behind the trees"
  present: natural

credits:
  role: "Live"
  venues:
    - name: "Säule, Berghain"
      city: "Berlin"
      year: "2026"

gallery:
  - src: /assets/media/sound/saule/saule-project-still-life.jpg
    alt: "A card reading Säule Project pinned on brown paper above dried dark flowers and ivy, with a red artist wristband dated 24.09 at the edge of the frame"
    present: natural
---

A live set at **Säule**, at Berghain, on 24 September 2026 — research turned into
instruments, and a set that moved out of techno into more experimental and
cinematic forms as it went.

Two instruments were played that night. One of them was the building.

## The room as an instrument

Every room reinforces some frequencies and suppresses others. Its dimensions,
its materials and its geometry decide which — the behaviour is called a room
mode, and in the low end a small number of them dominate everything an audience
hears. Depending on where you stand, certain notes bloom, hang on long after
they should have stopped, or disappear altogether.

In acoustics this is usually a defect. The standard response is to suppress it:
absorption, bass traps, correction in the DSP. Säule was approached the other way
round. Ahead of the show I measured how the room answers through its own
subwoofer system — which low frequencies its architecture reinforces, how long
they ring, and how that changes as you move across the floor — and then used what
the room does as compositional material.

## Measuring it

The method was deliberately conservative, because the aim was to describe the
room as it would actually be played rather than an idealised version of it that
would not exist on the night.

A swept measurement was sent through the installed subwoofers and captured at
several positions across the floor, with the venue's crossover, DSP, limiters and
protection left active throughout. Correcting those out would have produced a
cleaner characterisation of a system nobody was going to hear.

Positions were chosen to answer specific questions rather than to cover the room
evenly:

- **No two symmetric about the centre line.** A symmetric pair returns the same
  reading twice and adds nothing.
- **One in a corner**, where every mode reaches its maximum and the weak ones
  become visible at all.
- **One on the floor**, directly beneath the reference position. A vertical mode
  is strongest at floor level and almost nothing else in a room behaves that way,
  so comparing the two heights is the only dependable way to separate a vertical
  resonance from one running the length of the hall.
- **The rest at standing ear height**, so the result describes what an audience
  hears rather than what a microphone on a stand hears.
- **All of them clear of the structural pillars**, which scatter the field
  locally and would otherwise contaminate a reading with something that is not a
  property of the room as a whole.

There is a hard ceiling on this way of working, and it is physical rather than
practical. Above a certain frequency the modes of any room crowd together and
overlap into a continuous, statistical response; individual resonances stop being
individually meaningful, and the room stops being a thing you can play note by
note. That transition is where the method stops. It is the reason the whole
exercise lives in the low end.

## Playing it

What came back was not a correction curve. It was an understanding of where the
room is disposed to amplify and sustain, and where it is not.

Played deliberately, those are notes the building finishes for you. The sound
leaves the subwoofers, the architecture resonates along with it, and the decay
belongs to the room rather than to the synthesiser — the rumble is not an effect
on the signal, it is the hall responding at its own rate.

The honest qualification is that a room's response is not uniform. The effect is
strongest in some parts of the floor and thinner in others, and no amount of
measurement changes that. Treating resonance as material means accepting that the
piece is not identical everywhere in the room. In a concrete hall with a crowd
that moves through it, that seemed like the right trade.

## The Neurorack

The second instrument was the [Neurorack](/work/neurorack/), the synthesiser
built during my [doctorate](/research/thesis/) at IRCAM: a Eurorack module with a
neural network running inside it on embedded hardware, generating audio live as a
playable voice rather than rendering files offline.

Recent work has changed what it can do.

The module now carries two ways of producing sound — neural resynthesis of a
trained model, and a granular engine reading the same material — and they are not
two modes with a switch between them. They blend continuously, so an intermediate
setting is genuinely both engines running at once, not a crossfade between two
finished results.

Sound sets can be morphed into one another, traversing between the darkest and
the brightest material in the pool. They can also be hybridised: the body of one
sound with the tail of another, which a morph cannot produce, because morphing
moves every characteristic together.

The controls are the part that matters musically. Rather than exposing synthesis
parameters, the module exposes perceptual descriptors — weight, brightness,
noisiness, the grain in a sound — as axes you can turn, or patch to CV and sweep
across a note. These are not controls a conventional module has, because they do
not correspond to any single component of a synthesiser. They are properties of
the result, and they are the terms a musician actually thinks in.

A held gate keeps generation running past the natural length of the source
material, drifting as it goes, which turns a module built around percussive hits
into one that can also sustain. And generation is deterministic: the same
conditioning produces the same audio every time. For a live set that is not a
technical nicety — it means a sound found in rehearsal is still there at one in
the morning.

## Both

The two instruments pull in the same direction. In each case something normally
treated as a fixed condition — the acoustics you are given, the model you are
handed — is opened up and made playable.

That is also why the set drifted out of techno as it ran. It is less a change of
genre than what follows from the material: when the instruments are a building
and a generative model, the music tends toward the cinematic on its own.

Standing in the room while it rang back is the part I will remember.
