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

In audio applications, deep generative models are able to synthesize waveform data with unprecedented quality. However, this task remains challenging as the generation of high-quality waveform requires to handle complex temporal structures. In this context, model reduction becomes eminently important to provide these systems to users in real-time settings and on dedicated lightweight embedded hardware, which are particularly pervasive in the audio generation domain. The lack of work on model reduction is a significant limitation for the real-life use of deep models on this resource-constrained hardware. 

The goal of this PhD is to explore the very recently defined lottery ticket hypothesis, which states that randomly-initialized neural networks already contain extremely sparse sub-networks that could have higher accuracy than their larger counterparts if they were trained in isolation. Hence, finding these sub-networks implies that the same problem could be solved in a lightweight, memory and energy-efficient way. This PhD first extend and analyze these methods in generative frameworks. The main goal of this PhD is to develop specifically-tailored approaches that could allow to enable a larger use, a simpler control and a extremely lighter computational and memory footprint of deep generative models. This will lead to the development of lightweight deep learning models, creative tools and enhanced approaches that would allow to democratize deep models on lightweight and resource-constrained embedded hardware.'
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
