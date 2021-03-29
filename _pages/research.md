---
title: "Research"
layout: splash
permalink: /research
header:
  overlay_color: "#000"
  overlay_filter: "0.7"
  overlay_image: /images/research_header.jpg
excerpt: "All the educational material and project statements available here."
PhD:
  - image_path: /images/phd.jpg
    alt: "PhD"
    title: "PhD Subject"
    excerpt: '> ### Lightweight deep learning on real-time embedded architectures.

Deep learning models have provided extremely successful methods in most application fields, by enabling unprecedented accuracy in various tasks. However, the consistently overlooked downside of deep models is their massive complexity and tremendous computation cost. Besides the challenge of understanding such models, the energy and computational costs of such architectures are raising crucial issues of environmental sustainability. 

In audio applications, deep generative models are able to synthesize waveform data with unprecedented quality. However, this task remains challenging as the generation of high-quality waveform requires to handle complex temporal structures. In this context, model reduction becomes eminently important to provide these systems to users in real-time settings and on dedicated lightweight embedded hardware, which are particularly pervasive in the audio generation domain. The lack of work on model reduction is a significant limitation for the real-life use of deep models on this resource-constrained hardware.'
    url: "research/phd"
    btn_label: "Read More"
    btn_class: "btn--primary"
conferences:
  - image_path: /images/conference.jpeg
    alt: "Conferences"
    title: "Conferences and Seminars"
    excerpt: 'Links to the **descriptions and videos** of various speaking intervention'
    url: "research/conferences"
    btn_label: "Read More"
    btn_class: "btn--primary"
papers:
  - image_path: /images/papers.jpeg
    alt: "Papers"
    title: "Scientific Papers"
    excerpt: 'List of the publications'
    url: "research/papers"
    btn_label: "Read More"
    btn_class: "btn--primary"
---

{% include feature_row id="PhD" type="left" %}

{% include feature_row id="conferences" type="right" %}

{% include feature_row id="papers" type="left" %}
