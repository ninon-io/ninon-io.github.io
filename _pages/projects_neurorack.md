---
title: "Neurorack"
layout: single
permalink: /projects/neurorack
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/project2.jpeg
excerpt: "AI-based Eurorack synthesizer"
toc: true
toc_label: "Contents"
toc_sticky: true
---

# Neurorack

The **Neurorack** is a modular synthesizer that integrates deep learning directly into the Eurorack format. It enables real-time, descriptor-driven sound synthesis with AI models running on embedded hardware. This page documents its design, technical details, software, hardware, and community impact.

---

## Introduction

Recent advances in deep generative models (e.g., WaveNet, GANs, diffusion) have revolutionized audio synthesis. But these models often require powerful GPUs and large memory footprints, making real-time use in musical instruments difficult. The Neurorack tackles this challenge by embedding a lightweight deep learning model in a compact modular system using an NVIDIA Jetson Nano.

Its objective: **real-time, standalone AI sound generation**, optimized for **impact sounds** — complex, cinematic, transient-heavy timbres — with direct control via **modular synthesis interfaces**.

---

## Modular Synthesizers

### Overview
Modular synthesizers offer unmatched flexibility through patchable modules and open signal flow. Eurorack — the most popular format — standardizes physical and electrical specs, encouraging a vibrant ecosystem.

### Interface
- **CV (Control Voltage):** Modulate parameters like pitch, filter cutoff, amplitude.
- **Gate:** Triggers events (note on/off, loops, etc.).
- **Physicality:** Patch cables, knobs, sliders = tactile interaction.
- **Formats:** 3U Eurorack, 5U (Moog), 4U (Buchla/Serge).

---

## Design & Architecture

The Neurorack integrates:
- A **Jetson Nano**: quad-core ARM + 128-core GPU, CUDA-enabled.
- A **modular interface**: CV/Gate inputs, audio output, OLED display, rotary encoder.
- A **real-time deep synthesis model**: descriptor-controlled Sinc-NSF.

![](/images/jetson.png)

![](/images/interface_neurorack.png)

It runs entirely standalone — no laptop required — and behaves like any Eurorack module, with signal and control integration via mini-jacks.

---

## Sound Generation

### Why Impact Sounds?
Impact sounds are notoriously hard to synthesize. They require rich transients, wide bandwidth, and organic textures. Traditional subtractive/FM synthesis falls short.

### Dataset
- 3,500 curated cinematic impacts from Splice.
- Preprocessed: silence trimmed, RMS normalized.
- Sampled at 44.1kHz, optimized for deep training.

### Descriptors
Sound is controlled via 7 interpretable descriptors:
- Loudness (RMS)
- Percussivity (ZCR)
- Noisiness (Spectral Flatness)
- Tone-like (Roll-off)
- Richness (Bandwidth)
- Brightness (Centroid)
- Pitch ($f_0$)

These are extracted from reference sounds and used to condition the model.

---

## Software System

The synthesis engine uses an adapted **Sinc-NSF model**, combining neural filtering with DSP-inspired sinusoidal and noise source separation. Key features:

- **One-pass generation** (non-autoregressive)
- **Descriptor-driven** conditioning
- **Spectral loss** for accurate timbral fidelity
- **Trained on GPU**, but runs inference on Jetson Nano in real-time

![](/images/steps.png)

### Real-Time Architecture
- Python multiprocessing for parallel CV/audio/screen handling.
- Jetson’s GPU leveraged with TensorRT/CUDA.
- Audio buffer tuning and model burn-in at startup for stable performance.

---

## Hardware Integration

The Neurorack faceplate follows Eurorack 3U/11hp standard and offers:

- OLED screen
- Rotary encoder + push button
- 2 Gate inputs:
  - Gate 1: triggers a sound
  - Gate 2: loops a buffer (granular-style)
- 4 CV inputs:
  - CV1: interpolate between two descriptor sets
  - CV2: scrub through descriptor buffer
  - CV3: shape transient sharpness (RMS, Bandwidth)
  - CV4: introduce stochastic variation

Output is a mono audio jack. All CV/gate signals conform to Eurorack voltage standards.

---

## Community & Recognition

### Presentations
- **IRCAM’s Manifest Festival** with Raster-Noton artists
- **Superbooth Berlin**: presented to >15k attendees
- **SynthFest France**: 5,000+ synth lovers in Nantes

### Media Coverage
- Featured in: NVIDIA blog, Synthtopia, Sonic State, Keyboards.de
- Track and video demos: [YouTube](https://www.youtube.com/watch?v=64VpQenCHVs)

---

## Limitations & Future Work

### Limitations
- Startup requires model burn-in (can delay interaction)
- Descriptor control not fully open to user customization
- Multiprocessing overhead causes rare audio glitches
- Current Jetson-based setup requires external PSU

### Ongoing Development
- Second prototype features FRAVE model integration
- Slimmer faceplate, tighter wiring, more robust layout
- Exploring Raspberry Pi 5 + Hailo-8 for power efficiency
- Adding a UI for custom descriptor curve design

![](/images/front_croped.jpg)

### Future Directions
- Interactive latent space navigation
- CV-to-descriptor calibration
- Latency reduction via optimized buffering
- Community-shared descriptor banks

---

## Listen

<audio controls>
  <source src="/audio/raster_demo.wav" type="audio/wav">
</audio>

---

## References

Full scientific paper: [EPFL Archive](https://infoscience.epfl.ch/record/291222)  
Original GitHub repo: [ACIDS @ IRCAM](https://github.com/acids-ircam/neurorack)  
NVIDIA article: [Jetson Project of the Month](https://developer.nvidia.com/blog/jetson-neurorack-deep-ai-synthesizer/)

---

## Credits

Developed by Ninon (IRCAAM/EPFL), Philippe Esling, Martin Vert, Corentin Vercoustre.

<style>
audio {
  width: 100%;
  margin: 1.5rem 0;
}

img {
  border-radius: 6px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.15);
  margin: 1.5rem auto;
  display: block;
  max-width: 100%;
  height: auto;
}

table {
  font-size: 0.95rem;
  border-collapse: collapse;
  margin: 1.5rem 0;
  width: 100%;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 0.75rem;
}

blockquote {
  font-style: italic;
  background: rgba(255,255,255,0.03);
  border-left: 4px solid #aaa;
  padding: 1rem;
  margin: 1.5rem 0;
}
</style>






