---
title: "Neurorack"
layout: single
permalink: /projects/neurorack
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/project2.jpeg
excerpt: "AI based synthesizer"
toc: true
toc_label: "Table of content"
---

# Eurorack Impact synthesizer

The Neurorack is the first ever AI-based real-time synthesizer, which comes in many formats and more specifically in the Eurorack format. The current prototype relies on the Jetson Nano and the Eurorack hardware and software have been developed by our team with [Philippe Esling](https://esling.github.io/) and Martin Vert.

### Introduction

The goal of this project is to design the next generation of music instrument, providing a new tool for musician while enhancing the musician's creativity. It proposes a novel approach to think and compose music. We deeply think that AI can be used to achieve this quest.

> Problematique

Deep learning models have provided extremely successful methods in most application fields, by enabling unprecedented accuracy in various tasks, including audio generation. However, the consistently overlooked downside of deep models is their massive complexity and tremendous computation cost.
In the context of music creation and composition, model reduction becomes eminently important to provide these systems to users in real-time settings and on dedicated lightweight embedded hardware, which are particularly pervasive in the audio generation domain. Hence, in order to design a stand alone and real time instrument, we first need to craft an extremely lightweight model in terms of computation and memory footprint. To make this task even more easier, we relied on the Nvidia Jetson Nano which is a nanocomputer containing 128-core GPUs (graphical unit processors) and 4 CPUs.

![jetson](images/jetsonnano.PNG)

The compression problem is the core of my PhD and a full description can be found [here](https://ninon-io.github.io/research/phd/).

> Targets of our instrument

We designed our instrument so that it follows several aspects that we found crucial:

- Musical: the generative model we choose is particularly interesting as it produces sounds that are impossible to synthesize without using samples.
- Controllable: the interface was relevantly chosen, being handy and easy to manipulate.
- Real-time: the hardware behaves as traditional instrument and is as reactive.
- Stand alone: it is playable without any computer.

### Design Process

The work was divided between three major steps:
![steps](images/steps.PNG)

We set our sights on the generation of impacts as it is a very complex sound to reproduce. 
