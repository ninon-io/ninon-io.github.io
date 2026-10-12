---
layout: performance
permalink: /sound/saule/
title: "Säule, Berghain"
eyebrow: "Live · Berlin · September 2026"
excerpt: "A live set composed specifically for Säule, treating the venue not simply as the place where the music would be heard but as one of the instruments through which it took shape, alongside the Neurorack."
description: "A live set at Säule, Berghain, Berlin, 24 September 2026. The room's low-frequency resonances were measured in advance and used as musical material, alongside the Neurorack, a neural synthesiser developed during a doctorate at IRCAM."
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

On 24 September 2026, I performed a live set at Säule, Berghain. I had composed
the music specifically for the occasion, with the intention of treating the venue
not simply as the place where the work would be heard, but as one of the
instruments through which it would take shape.

The idea was to explore the acoustic properties of the room, particularly its
low-frequency resonances, and to incorporate them into the composition itself.
Rather than attempting to neutralise the peculiarities of the space, I wanted to
understand what it naturally amplifies, what it absorbs, and how these behaviours
might become part of the musical material.

Alongside this experiment, I brought the [Neurorack](/work/neurorack/), a neural
synthesiser I originally developed during my [doctorate](/research/thesis/) at
IRCAM and had been rebuilding and extending over the preceding months. Both
projects came together within a techno performance, connecting two strands of my
work that have long interested me: the relationship between sound and its
environment, and the design of instruments that open up new forms of musical
interaction.

## The room as an instrument

A room is never acoustically neutral. Its dimensions, geometry and materials
shape the propagation of sound, reinforcing certain frequencies while attenuating
others. At low frequencies, this behaviour is particularly noticeable. Sound
waves interact with the boundaries of the space, creating resonances, or *room
modes*, whose amplitude and decay vary according to where one listens.

Anyone who has spent time in a club will have experienced this, whether
consciously or not. A bass note that feels almost physical in one part of the
dancefloor may be considerably weaker a few metres away. Another might linger
longer than expected, its energy sustained by the room after the original sound
has stopped.

These phenomena are generally approached as acoustic problems to be controlled.
Room treatment, loudspeaker placement and digital correction all seek, to varying
degrees, to reduce their influence and obtain a more consistent response.

For Säule, I wanted to reverse that perspective.

What happens if these resonances are considered not as imperfections, but as
musical possibilities? Could the room contribute its own pitches, durations and
spatial variations to a composition? And could I write music that deliberately
activates these properties, rather than simply accommodating them?

I had wanted to explore this approach for several years. Säule offered the
opportunity to test it in an actual performance space, using the sound system
through which the music would eventually be played.

## Listening through measurement

Before the performance, I was given access to the empty venue to carry out a
series of acoustic measurements.

I used logarithmic sine sweeps played through the installed subwoofer system and
recorded the responses at several positions throughout the room. The venue's
processing chain, including its crossover, DSP and protection systems, remained
active. This was important: I was not trying to characterise an abstract
architectural space, but the electroacoustic system as it would actually behave
during the performance.

The microphone positions were chosen to reveal different aspects of the
low-frequency response. Measurements near boundaries helped identify prominent
resonances; comparisons between positions and between heights provided
information about their spatial distribution. Other recordings were made at
approximately standing ear height, closer to the conditions experienced by the
audience.

From these recordings, I could examine the frequency response, identify prominent
resonant peaks and study their decay. The measurements also made visible an
essential limitation: the acoustic behaviour of the space was not uniform, and a
resonance that appeared strongly at one position could be much less pronounced
elsewhere.

The most musically relevant behaviour was concentrated in the lower part of the
spectrum, within the range reproduced by the subwoofer system. Above that region
the modes crowd together into a denser, more statistical response, and individual
resonances become far less useful to address compositionally.

## Composing with the room

This distinction informed the way I approached the music. I did not want to
construct an entire tuning system around the room, or pretend that its resonances
formed a coherent scale. They do not. What the measurements offered was something
more modest and more usable: a small number of regions where the room would
respond generously, and a sense of how quickly it would release that energy
again.

I therefore wrote toward those regions at particular moments rather than
continuously. When the music settles there, the architecture joins in. The sound
leaves the subwoofers, the room resonates along with it, and part of the decay
belongs to the building rather than to the synthesiser. The result is not
reverberation applied to a signal; it is the hall responding at its own rate.

Moving away from those regions proved equally important. A resonance is only
perceptible as an event if the material surrounding it is not already occupying
the same part of the spectrum. Much of the compositional work consisted of
deciding when to let the room speak and when to keep it quiet.

## The Neurorack

The Neurorack is a Eurorack module with a neural network running on embedded
hardware inside it, generating sound in real time as a playable voice. I built it
during my doctorate at IRCAM, and spent the months before Säule extending it,
both in how it sounds and in how it is played.

It now holds two means of producing sound: neural resynthesis of a trained model,
and a granular engine reading the same material. These are not two modes with a
switch between them. They blend continuously, so an intermediate setting is
genuinely both engines at once rather than a crossfade between two finished
results.

Sound sets can be morphed into one another, traversing between the darkest and
the brightest material available to the model. They can also be hybridised,
taking the body of one sound and the tail of another, which a morph cannot
produce, since morphing moves every characteristic together.

The controls are what matters most musically. Instead of exposing synthesis
parameters, the module exposes perceptual descriptors: weight, brightness,
noisiness, the grain of a sound. These can be turned by hand, or patched to
control voltage and swept across a single note. They do not correspond to any one
component of a synthesiser, which is why no conventional module offers them. They
describe properties of the result, and they are the terms in which a musician
actually thinks.

A held gate allows generation to continue beyond the natural length of the source
material, drifting as it does so, which gives a module built around percussive
hits the ability to sustain. Generation is also deterministic: identical
conditioning produces identical audio. In the studio this is a convenience. In a
live set it is closer to a precondition, since a sound found in rehearsal has to
still be there at one in the morning.

## The performance

The set itself remained a techno set, and deliberately so. Neither the room nor
the instrument was presented as a demonstration. Both only become convincing when
they are doing musical work rather than illustrating a method, and the clearest
way to test that was to place them inside a performance that had to function on
its own terms.

I could not hear the result from the booth. Whether the room was behaving as I
had designed it to was something I only learned afterwards, from people who had
been standing out on the floor.

It is the most demanding project I have made, and I was not certain it would work
until the night itself.

## Credits

Säule gave me access to the empty room and to the sound system in order to carry
out the measurements, which is not a small thing to ask of a venue. My thanks to
the Säule team, and in particular to Krishan and Martin, for their
professionalism and their help throughout.

The invitation came from Egregore and Terenor Records, who supported an unusual
proposal and gave me the freedom to pursue it properly.
