---
title: "Scientific Papers"
layout: single
permalink: /research/papers/
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/musicsheet.jpeg
excerpt: "Publications sorted by date"
toc: true
toc_label: "Publications"
sidebar:
  nav: "research"
---

## Under Reviw
> Shahan Nercessian, Johannes Imort, Ninon Devis, Frederik Blang

<p align="center">
ISMIR - 2024 
</p>


## The ACIDS Research project

> Giovanni Bindi, Antoine Caillon, Axel Chemla--Romeu-Santos, Nils Demerlé, Ninon Devis, Constance Douwes, Philippe Esling, David Genova, Sarah Nabi.

<p align="center">
VDT Magazin - 2023 
</p>

Throughout history, music has been closely intertwined with technological advancements. The evolution of musical genres has been greatly influenced by the development of musical instruments and tools, which have been made possible by groundbreaking scientific discoveries. The study of organology, for instance, has shed light on the progression of musical instruments, allowing composers to explore new forms of expression. Significant technological breakthroughs, like the hammer mechanism of the piano in the 18th century, have enabled composers to create music with greater tonal expression and dynamic range. This has played a crucial role in the rise of the piano as a leading solo instrument in Western classical music. The advent of electronic synthesizers has further expanded the range of sounds available and has become ubiquitous in various musical genres, even giving rise to entirely new ones. In recent years, Artificial Intelligence (AI) has made significant strides, particularly in the field of deep machine learning (ML). Generative models, in particular, have seen impressive results in generating entirely new data, spanning computer vision, language processing, and audio synthesis. As a result, a plethora of models capable of generating high-quality images, audio, and text from user-written prompts have emerged, such as StableDiffusion from Stability AI, AudioLM from Google, and ChatGPT from OpenAI. The integration of ML into music creation is also gaining popularity, with dedicated tools such as DDSP or RAVE being developed for specific creative applications. However, this trend raises profound questions regarding the nature and place of these tools in the creative landscape. Are we witnessing a turning point in our relationship with creative mediums? What are the promises and dangers that may arise from these novel tools? This article seeks to illuminate the relationship between ML tools and musical creativity, by illustrating these questions with the work performed over the past decade by the ACIDS group at IRCAM.

[Paper only with VDT account]([https://arxiv.org/abs/2302.13542](https://tonmeister.org/de/magazin/2023/2/)){: .btn .btn--light-outline}

## Continuous descriptor-based control for deep audio synthesis

> Ninon Devis, Nils Demerlé, Sarah Nabi, David Genova, Philippe Esling

<p align="center">
ICASSP - 2023 
</p>

Despite significant advances in deep models for music generation, the use of these techniques remains restricted to expert users. Before being democratized among musicians, generative models must first provide expressive control over the generation, as this conditions the integration of deep generative models in creative workflows. In this paper, we tackle this issue by introducing a deep generative audio model providing expressive and continuous descriptor-based control, while remaining lightweight enough to be embedded in a hardware synthesizer. We enforce the controllability of real-time generation by explicitly removing salient musical features in the latent space using an adversarial confusion criterion. User-specified features are then reintroduced as additional conditioning information, allowing for continuous control of the generation, akin to a synthesizer knob. We assess the performance of our method on a wide variety of sounds including instrumental, percussive and speech recordings while providing both timbre and attributes transfer, allowing new ways of generating sounds.

[Companion Website]([https://arxiv.org/abs/2302.13542](https://neurorave.github.io/neurorave/)){: .btn .btn--light-outline}

[Paper](https://arxiv.org/abs/2302.13542){: .btn .btn--light-outline}


## Neurorack: deep audio learning in hardware synthesizers

> Ninon Devis, Philippe Esling

<p align="center">
EPFL - 2021 
</p>

Deep learning models have provided extremely successful methods in most application fields by enabling unprecedented accuracy in various tasks. For audio applications, although the massive complexity of generative models allows handling complex temporal structures, it often precludes their real-time use on resource-constrained hardware platforms, particularly pervasive in this field. The lack of adequate lightweight models is an impediment to the development of stand-alone instruments based on deep models, entailing a significant limitation for real-life creation by musicians and composers. Recently, we built the first deep learning-based music instrument by implementing a lightweight generative musical audio model on an adequate hardware platform that can handle its complexity. By embedding this deep model, we provide a controllable and flexible creative hardware interface. More precisely, we focused our work on the Eurorack synthesizers format, which offers Control Voltage (CV) and gate mechanisms allowing to interact with other classical Eurorack modules.

[Link](https://infoscience.epfl.ch/record/291222?ln=en){: .btn .btn--light-outline}

## L'avenir de la créativité sera-t-il artificiel ?

> Ninon Devis

<p align="center">
The Conversation - 2021 
</p>

Au sein de nos sociétés profondément impactées par les avancées technologiques, il semble que l’espace créatif tende également à se développer en harmonie avec ces progrès. Plus particulièrement, l’exploitation de l’intelligence artificielle s’intensifie et son utilisation s’immisce dans toutes les sphères artistiques. Et pourtant, bien que l’IA soit par définition un algorithme capable de résoudre des tâches relevant de l’intelligence humaine, le succès de son utilisation – quel que soit son domaine d’étude – repose sur une formalisation rigoureuse du problème traité ainsi qu’une définition claire des objectifs.

À ce titre, il semble légitime de se demander dans quelle mesure il est possible de conjuguer créativité et intelligence artificielle. Peut-on élaborer une forme de créativité artificielle ? Si oui, quelles en sont ses limites ? Face à l’automatisation massive qui n’épargne aucun domaine des arts, quelle place conserve l’originalité ? Dans le secteur de la musique, quels outils futurs reposant sur l’IA peut-on concevoir ? Quels pourraient alors être les instruments de demain ?

[Lien](https://theconversation.com/lavenir-de-la-creativite-musicale-sera-t-il-artificiel-157443){: .btn .btn--light-outline}

## Creativity in the era of artificial intelligence

> Philippe Esling, Ninon Devis

<p align="center">
2020 
</p>

Creativity is a deeply debated topic, as this concept is arguably quintessential to our humanity. Across different epochs, it has been infused with an extensive variety of meanings relevant to that era. Along these, the evolution of technology have provided a plurality of novel tools for creative purposes. Recently, the advent of Artificial Intelligence (AI), through deep learning approaches, have seen proficient successes across various applications. The use of such technologies for creativity appear in a natural continuity to the artistic trend of this century. However, the aura of a technological artefact labeled as intelligent has unleashed passionate and somewhat unhinged debates on its implication for creative endeavors. In this paper, we aim to provide a new perspective on the question of creativity at the era of AI, by blurring the frontier between social and computational sciences. To do so, we rely on reflections from social science studies of creativity to view how current AI would be considered through this lens. As creativity is a highly context-prone concept, we underline the limits and deficiencies of current AI, requiring to move towards artificial creativity. We argue that the objective of trying to purely mimic human creative traits towards a self-contained ex-nihilo generative machine would be highly counterproductive, putting us at risk of not harnessing the almost unlimited possibilities offered by the sheer computational power of artificial agents.

[Link](https://arxiv.org/pdf/2008.05959.pdf){: .btn .btn--light-outline}

## Diet deep generative audio models with structured lottery

> Philippe Esling, Ninon Devis, Adrien Bitton, Antoine Caillon, Axel Chemla--Romeu-Santos, Constance Douwes

<p align="center">
DAFx - 2020 
</p>

Deep learning models have provided extremely successful solutions in most audio application fields. However, the high accuracy of these models comes at the expense of a tremendous computation cost. This aspect is almost always overlooked in evaluating the quality of proposed models. However, models should not be evaluated without taking into account their complexity. This aspect is especially critical in audio applications, which heavily relies on specialized embedded hardware with real-time constraints. In this paper, we build on recent observations that deep models are highly overparameterized, by studying the lottery ticket hypothesis on deep generative audio models. This hypothesis states that extremely efficient small sub-networks exist in deep models and would provide higher accuracy than larger models if trained in isolation. However, lottery tickets are found by relying on unstructured masking, which means that resulting models do not provide any gain in either disk size or inference time. Instead, we develop here a method aimed at performing structured trimming. We show that this requires to rely on global selection and introduce a specific criterion based on mutual information. First, we confirm the surprising result that smaller models provide higher accuracy than their large counterparts. We further show that we can remove up to 95% of the model weights without significant degradation in accuracy. Hence, we can obtain very light models for generative audio across popular methods such as Wavenet, SING or DDSP, that are up to 100 times smaller with commensurate accuracy. We study the theoretical bounds for embedding these models on Raspberry Pi and Arduino, and show that we can obtain generative models on CPU with equivalent quality as large GPU models. Finally, we discuss the possibility of implementing deep generative audio models on embedded platforms.

[Link](https://arxiv.org/pdf/2007.16170.pdf){: .btn .btn--light-outline}

## Ultra-light deep MIR by trimming lottery tickets

> Philippe Esling, Theis Bazin, Adrien Bitton, Tristan Carsault, Ninon Devis

<p align="center">
ISMIR - 2020 
</p>

Current state-of-the-art results in Music Information Retrieval are largely dominated by deep learning approaches. These provide unprecedented accuracy across all tasks. However, the consistently overlooked downside of these models is their stunningly massive complexity, which seems concomitantly crucial to their success. In this paper, we address this issue by proposing a model pruning method based on the lottery ticket hypothesis. We modify the original approach to allow for explicitly removing parameters, through structured trimming of entire units, instead of simply masking individual weights. This leads to models which are effectively lighter in terms of size, memory and number of operations. We show that our proposal can remove up to 90% of the model parameters without loss of accuracy, leading to ultra-light deep MIR models. We confirm the surprising result that, at smaller compression ratios (removing up to 85% of a network), lighter models consistently outperform their heavier counterparts. We exhibit these results on a large array of MIR tasks including audio classification, pitch recognition, chord extraction, drum transcription and onset estimation. The resulting ultra-light deep learning models for MIR can run on CPU, and can even fit on embedded devices with minimal degradation of accuracy.

[Link](https://arxiv.org/pdf/2007.16187.pdf){: .btn .btn--light-outline}
