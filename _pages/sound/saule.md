---
layout: performance
permalink: /sound/saule/
title: "Säule, Berghain"
eyebrow: "Live · Berlin · September 2026"
excerpt: "A techno set composed from scratch for Säule. The low frequencies the hall itself reinforces were measured in advance and played as material, alongside the Neurorack, the neural synthesiser I built during my doctorate at IRCAM."
description: "A live set at Säule, Berghain, Berlin, September 2026. The room's low-frequency response was measured in advance and used as musical material, alongside the Neurorack, a neural synthesiser built during a doctorate at IRCAM."
kind: "Live"
years: "2026"

lead:
  src: /assets/media/sound/saule/saule-berghain-arrival.jpg
  alt: "Black and white photograph: Ninon seen from behind on the path outside Berghain at night, in a long patterned coat, holding flowers, a modular synthesiser case and a suitcase standing beside her, the lit facade of the building behind the trees"
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

A live set at **Säule**, at Berghain, on 24 September 2026, composed from scratch
for that room.

It stayed close to techno for most of its length. What made it specific to Säule
was the material underneath it: the low frequencies the hall itself reinforces,
measured in advance and played deliberately, and the [Neurorack](/work/neurorack/),
the synthesiser I built during my [doctorate](/research/thesis/) at IRCAM and
spent the preceding months rebuilding. Both of those sat inside my usual live
setup rather than replacing it.

## The room

Every room reinforces some frequencies and suppresses others. Its dimensions, its
materials and its geometry decide which ones. The behaviour is called a room
mode, and in the low end a small number of them dominate what an audience
actually hears: depending on where you stand, certain notes bloom, hang on long
after they should have stopped, or disappear.

In acoustics this is a defect, and the usual response is to suppress it with
absorption, with bass traps, or with correction in the DSP. Säule was approached
the other way round. I measured how the room answers through its own subwoofer
system, which low frequencies its architecture reinforces, how long they ring,
and how that changes as you move across the floor, and then used what the room
does as material.

Measuring a space in order to play it rather than to fix it is something I had
wanted to do for years. Säule was the first room where it was possible.

## Measuring it

The method was deliberately conservative, because the aim was to describe the
room as it would actually be played, not an idealised version of it that would
not exist on the night.

A swept measurement was sent through the installed subwoofers and captured at
several positions across the floor, with the venue's crossover, DSP, limiters and
protection left active throughout. Correcting those out would have produced a
cleaner characterisation of a system nobody was going to hear.

Positions were chosen to answer specific questions, not to cover the room evenly:

- **No two symmetric about the centre line.** A symmetric pair returns the same
  reading twice and adds nothing.
- **One in a corner**, where every mode reaches its maximum and the weaker ones
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

There is a ceiling on this way of working, and it is physical rather than
practical. Above a certain frequency the modes of any room crowd together into a
continuous, statistical response, and individual resonances stop being
individually meaningful. That transition is where the method stops. It is the
reason the whole exercise lives in the low end.

## Playing it

What came back was not a correction curve. It was an understanding of where the
room is disposed to amplify and sustain, and where it is not.

Played deliberately, those are notes the building finishes for you. The sound
leaves the subwoofers, the architecture resonates along with it, and the decay
belongs to the room rather than to the synthesiser. The rumble is not an effect
applied to the signal. It is the hall answering at its own rate.

The qualification worth stating is that a room's response is never uniform. The
effect is strong in some parts of the floor and thinner in others, and no amount
of measurement changes that. Working this way means accepting that the piece is
not the same in every part of the room, which is a condition of the material and
not a flaw in it.

From the booth I could not hear any of it. Whether the room was doing what I had
designed it to do was something I only found out afterwards, from people who had
been standing out on the floor.

## The Neurorack

The Neurorack is a Eurorack module with a neural network running on embedded
hardware inside it, generating audio as a playable voice. I built it during my
doctorate; I spent the months before Säule developing it further, both in how it
sounds and in how it is played.

It now carries two ways of producing sound, neural resynthesis of a trained model
and a granular engine reading the same material, and they are not two modes with
a switch between them. They blend continuously, so an intermediate setting is
genuinely both engines running at once rather than a crossfade between two
finished results.

Sound sets can be morphed into one another, traversing between the darkest and
the brightest material in the pool. They can also be hybridised, taking the body
of one sound and the tail of another, which a morph cannot produce, because
morphing moves every characteristic together.

The controls are the part that matters musically. Instead of exposing synthesis
parameters, the module exposes perceptual descriptors, weight, brightness,
noisiness, the grain in a sound, as axes you can turn, or patch to CV and sweep
across a note. No conventional module has these controls, because they do not
correspond to any single component of a synthesiser. They are properties of the
result, and they are the terms a musician actually thinks in.

A held gate keeps generation running past the natural length of the source
material, drifting as it goes, which turns a module built around percussive hits
into one that can also sustain. Generation is deterministic as well: the same
conditioning produces the same audio every time. For a live set that is not a
technical nicety. It means a sound found in rehearsal is still there at one in
the morning.

## Both

What the room and the instrument have in common is that each is normally a fixed
condition. The acoustics of a venue are something you work around. A generative
model is something whose output you accept. Opening either one up is the same
gesture, and this was an attempt to do it to both at once, inside a techno set
rather than apart from one.

It is the most demanding thing I have made, and I was not sure it would work
until the night itself. Säule's team gave me the empty room and the system to
measure it with, which is not a small thing to ask of a venue.
