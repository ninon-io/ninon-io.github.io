---
title: "Neurorack"
layout: single
permalink: /projects/neurorack
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/neurorizontal.jpeg
excerpt: "AI-based Eurorack synthesizer"
toc: true
toc_label: "Contents"
toc_sticky: true
sidebar:
  nav: "projects"
---

<style>
audio {
  width: 100%;
  margin: 2rem 0;
  border-radius: 0.5rem;
  background: #111;
}

img {
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  margin: 2rem auto;
  display: block;
  max-width: 100%;
  height: auto;
  transition: transform 0.3s ease;
}

img:hover {
  transform: scale(1.015);
}

table {
  font-size: 0.95rem;
  border-collapse: collapse;
  margin: 2rem 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.02);
  color: #ccc;
}

table th,
table td {
  border: 1px solid #333;
  padding: 0.75rem;
  text-align: left;
}

blockquote {
  font-style: italic;
  background: rgba(255,255,255,0.05);
  border-left: 4px solid #666;
  padding: 1rem 1.25rem;
  margin: 2rem 0;
  color: #aaa;
  border-radius: 4px;
}

h1, h2, h3 {
  font-weight: 600;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  padding-bottom: 0.3rem;
  margin-top: 3rem;
}

hr {
  border: none;
  height: 1px;
  background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.1), rgba(255,255,255,0));
  margin: 2.5rem 0;
}
</style>

# Neurorack

The **Neurorack** is a modular synthesizer that integrates deep learning directly into the Eurorack format. It enables real-time, descriptor-driven sound synthesis with AI models running on embedded hardware. This page documents its philosophy, design, and evolution — from technical details to creative use.

---

## Overview

Neurorack’s mission is to make AI-based sound design tactile, expressive, and performance-ready. Built around the NVIDIA Jetson Nano, it runs a deep synthesis model in real-time, controlled via standard CV/Gate. No laptop required.

It targets **impact sounds** — complex, cinematic, transient-rich events — difficult to generate with traditional subtractive or FM synthesis.

---

## Design

- **Embedded AI:** Jetson Nano (quad-core CPU, CUDA GPU)
- **Modular Hardware:** 3U/11hp faceplate, Eurorack CV/Gate I/O
- **Real-Time Synthesis Model:** descriptor-conditioned Sinc-NSF

![](/images/jetson.png)

![](/images/interface_neurorack.png)

---

## Sound Engine

Neurorack uses curated impact sounds (3,500 samples from Splice), each analyzed for:

- Loudness (RMS)
- Percussivity (ZCR)
- Brightness (Centroid)
- Tone-like qualities (Roll-off)
- Richness (Bandwidth)
- Noisiness (Flatness)
- Pitch ($f_0$)

These **7 descriptors** condition the neural synthesis model.

### Model Highlights

- Adapted **Sinc-NSF** architecture
- One-pass audio generation
- Spectral loss optimization
- Real-time inference on embedded hardware

![](/images/steps.png)

---

## Interface & Control

The Neurorack faceplate includes:

- **OLED Display**
- **Rotary Encoder + Push Button**
- **2 Gate Inputs**
  - Gate 1: trigger generation
  - Gate 2: loop a granular buffer
- **4 CV Inputs**
  - CV1: interpolate between two descriptor sets
  - CV2: scrub descriptor time window
  - CV3: shape transients (RMS/Bandwidth)
  - CV4: stochastic variation

All signals follow Eurorack standards.

---

## Listen

<audio controls>
  <source src="/audio/raster_demo.wav" type="audio/wav">
</audio>

A full-length track composed entirely with Neurorack-generated impacts.

---

## Development Timeline

### V1: First Prototype

- Jetson-based design
- Exposed cabling, external power
- Impact-only synthesis, fixed descriptor presets

### V2: Second Prototype

- Refined faceplate, internal wiring
- FRAVE model support
- Enhanced CV interaction
- In-progress UI for descriptor design

![](/images/front_croped.jpg)

---

## In the Wild

- 🎤 **IRCAM Manifest**: with Raster-Noton
- 🎛️ **Superbooth Berlin**: 15,000+ attendees
- 🎚️ **SynthFest France**: 5,000+ visitors

Featured by:
- NVIDIA Developer Blog
- Synthtopia
- Sonic State
- Keyboards.de

🎬 [Watch the teaser](https://www.youtube.com/watch?v=64VpQenCHVs)

---

## Learn More

- 📄 [Full Scientific Paper (EPFL)](https://infoscience.epfl.ch/record/291222)
- 💾 [GitHub Repository](https://github.com/acids-ircam/neurorack)
- 🏆 [NVIDIA Jetson Project of the Month](https://developer.nvidia.com/blog/jetson-neurorack-deep-ai-synthesizer/)

---

## Credits

Project by Ninon (IRCAM/EPFL), Philippe Esling, Martin Vert, Corentin Vercoustre.






