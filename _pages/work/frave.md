---
layout: project-single
permalink: /work/frave/
title: "FRAVE"
eyebrow: "Research system · IRCAM / ACIDS"
excerpt: "Fader networks meet RAVE: a neural synthesiser whose latent space has been pulled apart so that the things a musician cares about become knobs."
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

**FRAVE** is a synthesis system, not a paper. The name is the method: *fader
networks* applied to the *RAVE* architecture.

Deep generative audio models sound impressive and are almost impossible to play.
The latent space that gives them their range is not a set of controls a musician
can reach for; it is a coordinate system nobody asked for. FRAVE exists to make
one playable.

This work makes that space playable. Salient musical features are explicitly
removed from the latent representation using an adversarial confusion criterion,
then reintroduced as separate conditioning information — so the feature you care
about becomes an independent parameter rather than something entangled with
everything else. The result behaves like a synthesiser knob: continuous, direct,
and predictable in the direction it moves.

Because it stays small enough to embed, FRAVE is the engine behind the second
generation of the [Neurorack](/work/neurorack/) — the system moves off the bench
and into a module a performer can patch. It was evaluated across instrumental,
percussive and speech recordings, and supports both timbre transfer and attribute
transfer.

The argument it makes is the same one running through the
[thesis](/research/thesis/) and through the
[Absynth Preset Explorer](/work/absynth-preset-explorer/): a model is only useful
to a musician at the point where it becomes controllable.

[Paper (arXiv)](https://arxiv.org/abs/2302.13542){: .btn .btn--primary}
[Companion website](https://neurorave.github.io/neurorave/){: .btn}
[All publications](/research/publications/){: .btn}
