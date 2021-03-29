---
title: "PhD Subject"
layout: single
permalink: /research/phd/
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/modular.jpeg
  actions:
    - label: "Download"
      url: "https://puredata.info/downloads"
excerpt: "First, get your Pure Data"
toc: true
---

## Subject

Deep learning have provided extremely successful solutions in almost all application fields, enabling unprecedented accuracy in both discriminative and generative tasks. However, the consistently overlooked downside of these models is their stunningly massive complexity, incurring tremendous computation costs and extensive inference time. This aspect is almost always underestimated in evaluating the quality of proposed models, overshadowed by the never-ending quest for accuracy. However, this complexity hampers the challenge of understanding the behavior of such models. Furthermore, the energy and computational costs are raising crucial issues of environmental sustainability. As a showering example, MegatronLM is a massive transformer model with 8.3 billion parameters, where training this  model took 512 V100 GPUs running continuously for 9.2 days. Hence, many prospects are still unattainable, specifically these huge memory footprint and humongous data processing are a major impediment to relying on these models on real-time embedded and constrained hardware. 

Specifically in audio applications, novel deep generative models are able to synthesize waveform data matching the acoustic properties of a given dataset with unprecedented quality. However, this task remains challenging as the generation of high-quality waveform requires to handle complex temporal structures at multiple scales. In this setup, reducing the size and memory footprints become eminently important as the audio generation domain is built around real-time settings and on dedicated lightweight embedded hardware. At the time being, the lack of work on lightweight and sparse deep models is a significant limitation for potential deployment on embedded platforms such as _Raspberry Pi_ or _Arduino_, which are particularly pervasive. Subsequently, none of the current deep generative audio models can fit real-life use with these computational constraints and memory limitations.

Recently, the _lottery ticket hypothesis_ suggested that randomly-initialized neural networks already contain powerful sub-networks that could have higher accuracy than the larger ones if they were trained in isolation. Finding these sub-networks allow a drastic pruning of large networks, while keeping the same level of accuracy. This implies that the same problem could be solved in a very lightweight, memory and energy-efficient way. The main goal of this PhD is to develop and enhance these recent hypotheses in order to enable a larger use, a simpler control and a highly lighter computation of deep generative models. This thesis will lead to the development of new creative tools through the implementation of generative models on hardware embedded into next-generation augmented musical instruments, making it possible to learn on-the-fly user behaviors and to provide unheard mixed reality experience (_creative instruments_).

### Research Design and Methodology

It has been repeatedly observed that deep architectures are profoundly over-parameterized. This implies that a large majority of the parameters in deep models could potentially be removed without significant loss in performance. However, this over-parameterization appears to be required for correctly training deep models, as it allows the optimization process to search for solutions in a simpler landscape. The idea of reducing models in order to improve the storage and computational costs of inference is well-established from the development of the widely used pruning technique. Removing unnecessary structure from neural networks and designing smaller topology is thus manageable through pruning that can reduce the number of parameters. Unfortunately those methods are rather unstable to train and provide only small compression ratios in order to save the accuracy \cite{liu2018rethinking}.

In this PhD, we will rely on the recently exposed _lottery ticket hypothesis_, which conjectures the existence of extremely sparse sub-networks, capable of reaching complete and even better accuracy  when trained in isolation. Studying the applicability of this approach to generative models will allow to obtain extremely lightweight solutions without damaging the efficiency of the model. Several studies have analyzed different properties of this theory, as it raises exciting prospects to obtain much smaller networks while still providing accuracy similar to larger state-of-art models. Unfortunately, this method relies on masking the weights, thus maintaining both the size and inference costs of large models. This hypothesis still opens up the path to lighter models, with efficient memory and energy footprints, and the prospect of embedded deep learning systems.

Hence, the goal of this PhD is first to implement and compare existing techniques of model reduction on deep generative audio models. Then, we will develop specifically tailored methods to enhance the memory and computation, while accounting for the peculiarities of generative models. This study will include the analysis of topological and information-theoretic properties of various generative models with a particular consideration for the relationships between compression, accuracy and stability. In a second step, this research will attempt to tackle interdisciplinary applications, by targeting the construction of an end-to-end solution that can be easily used and exploited for creative and artistic endeavors. This aspect will entail the implementation of a toolbox allowing the use of lightweight models on dedicated constrained hardware such as _creative instruments_. The final part of this research will focus on the creation of new modules for modular synthesizer systems, embedded systems for augmented instruments and, more generally, initiating a new approaches for creating and designing music. All along the research, special attention will be given to the viability and usability of the reduced models, by working in close relationship with composers and musicians already strongly involved in the work of the laboratory.

The proposed PhD is deeply linked with current researches conducted within the IRCAM STMS laboratory and its network of technological startup companies, and it will fully leverage the current momentum generated by both thesis directors, through the SSHRC ACTOR Network and ERC REACH projects, and under the supervision of Gerard Assayag and Philippe Esling.

### Objectives

The aims of this PhD will be attained by 
    - Establishing an analysis framework for complexity of deep models
    -  Implementing and comparing the state-of-art model reduction techniques
    -  Analyzing the topology of deep models in order to enhance the reduction techniques
    - Implementing selected generative models and applying compression techniques on these approaches
    - Developing specifically-tailored methods accounting for the peculiarities of generative models
    - Implementing a toolbox for lightweight deep learning on embedded platforms
    - Investigating the user-interactions and musical usability of the models
    - Developing new creative devices and enhanced instruments

## Bibliographie

The goal of this assignment is to compose an entire track _**only using Pure Data**_. It must last less than 15 minutes and has no restriction regarding the genre.

You must provide a .wav or .mp3 of your creation alongside with all the patches and samples you used to make it. You can attach a README.txt if necessary.

No post-processing, mixing or mastering are allowed unless you attach a README.txt explaining your method and why you felt the need to do that. A raw track must be provided as well.

No Max MSP allowed but any creative experiment will be valued.

> You can find the complete subject here:  

## Examples

Here are examples of tracks made by my students in accordance with the subject.
