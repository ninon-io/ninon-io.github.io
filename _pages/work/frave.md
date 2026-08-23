---
layout: project-single
permalink: /work/frave/
title: "Descriptor-controlled synthesis"
eyebrow: "Research system · IRCAM / ACIDS"
excerpt: "Continuous, knob-like control over a neural synthesiser: remove salient features from the latent space, then hand them back to the musician as parameters."
kind: "Research System"
years: "2023"
toc: true
credits:
  role: "Model design, experiments, first author"
  collaborators:
    - name: "Nils Demerlé"
    - name: "Sarah Nabi"
    - name: "David Genova"
    - name: "Philippe Esling"
  support: "ACIDS group, IRCAM–STMS. Published at ICASSP 2023."
---

Deep generative audio models sound impressive and are almost impossible to play.
The latent space that gives them their range is not a set of controls a musician
can reach for; it is a coordinate system nobody asked for.

This work makes that space playable. Salient musical features are explicitly
removed from the latent representation using an adversarial confusion criterion,
then reintroduced as separate conditioning information — so the feature you care
about becomes an independent parameter rather than something entangled with
everything else. The result behaves like a synthesiser knob: continuous, direct,
and predictable in the direction it moves.

The model stays small enough to embed in hardware, which is what connects it to
the [Neurorack](/work/neurorack/). It was evaluated across instrumental,
percussive and speech recordings, supporting both timbre transfer and attribute
transfer.

[Paper (arXiv)](https://arxiv.org/abs/2302.13542){: .btn .btn--primary}
[Companion website](https://neurorave.github.io/neurorave/){: .btn}
[All publications](/research/publications/){: .btn}
