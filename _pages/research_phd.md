---
title: "PhD Subject"
layout: single
permalink: /research/phd/
author_profile: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/phd2.webp
  actions:
    - label: "Team Work"
      url: "https://acids.ircam.fr/"
excerpt: "Lightweight deep learning on real-time embedded architectures"
toc: true
toc_label: "Table of Contents"
sidebar:
  nav: "research"
---

[Activity Report Here](/documents/PhD_Report.pdf){: .btn .btn--light-outline}

## Subject

### Introduction

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

- Alexandre Défossez, Neil Zeghidour, Nicolas Usunier, Léon Bottou, and Francis Bach.  Sing:Symbol-to-instrument neural generator.  InAdvances in Neural Information Processing Systems,pages 9041–9051, 2018.
- Chris Donahue, Julian McAuley, and Miller Puckette.  Adversarial audio synthesis.Interna-tional Conference on Learning Representations, 2019.
- Jesse Engel, Kumar Krishna Agrawal, Shuo Chen, Ishaan Gulrajani, Chris Donahue, andAdam Roberts. Gansynth: Adversarial neural audio synthesis.arXiv preprint arXiv:1902.08710,2019.
- Jesse Engel, Lamtharn Hantrakul, Chenjie Gu, and Adam Roberts.   Ddsp:  Differentiabledigital signal processing.International Conference on Learning Representations, 2020.
- Jesse Engel, Cinjon Resnick, Adam Roberts, Sander Dieleman, Douglas Eck, Karen Si-monyan, and Mohammad Norouzi.   Neural audio synthesis of musical notes with wavenetautoencoders.International Conference on Machine Learning, 70:1068–1077, 2017.
- Philippe Esling, Axel Chemla-Romeu-Santos, and Adrien Bitton.  Generative timbre spaceswith variational audio synthesis.  InProceedings of the International Conference on DigitalAudio Effects (DAFx), 2018.
- Soroush Mehri, Kundan Kumar, Ishaan Gulrajani, Rithesh Kumar, Shubham Jain, Jose Sotelo,Aaron Courville, and Yoshua Bengio.  Samplernn: An unconditional end-to-end neural audiogeneration model.  InInternational Conference on Learning Representations, 2017.
- A.  van  den  Oord,  Yazhe  Li,  Igor  Babuschkin,  Karen  Simonyan,  Oriol  Vinyals,  KorayKavukcuoglu, George Driessche, Edward Lockhart, Luis Cobo, Florian Stimberg, NormanCasagrande, Dominik Grewe, Seb Noury, Sander Dieleman, Erich Elsen, Nal Kalchbrenner,Heiga Zen, Alex Graves, Helen King, Tom Walters, Dan Belov, and Demis Hassabis.  Parallelwavenet: Fast high-fidelity speech synthesis.International Conference on Machine Learning,80:3918–3926, 2018.
- Aäron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, AlexGraves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu.  Wavenet: A generativemodel for raw audio.  In9th ISCA Speech Synthesis Workshop, pages 125–125, 2016.
- Xin Wang, Shinji Takaki, and Junichi Yamagishi.  Neural source-filter waveform models forstatistical parametric speech synthesis.IEEE Transactions on Audio, Speech, and LanguageProcessing, 28:402–415, 2019.Lottery Ticket Hypothesis.
- Utku Evci, Trevor Gale, Jacob Menick, Pablo Samuel Castro, and Erich Elsen.  Rigging thelottery: Making all tickets winners.arXiv preprint arXiv:1911.11134, 2019.
- Jonathan Frankle and Michael Carbin.    The lottery ticket hypothesis:  Finding sparse,trainable neural networks.  InInternational Conference on Learning Representations, 2019.
- Jonathan Frankle, Gintare Karolina Dziugaite, Daniel M Roy, and Michael Carbin.  Linearmode connectivity and the lottery ticket hypothesis.arXiv preprint arXiv:1912.05671, 2019.
- Jonathan Frankle, Gintare Karolina Dziugaite, Daniel M Roy, and Michael Carbin.  Stabi-lizing the lottery ticket hypothesis.arXiv preprint arXiv:1903.01611, 2019.
- Jonathan Frankle, David J. Schwab, and Ari S. Morcos.  The early phase of neural networktraining.  InInternational Conference on Learning Representations, 2020.
- Chaoqi Wang, Guodong Zhang, and Roger Grosse.  Picking winning tickets before trainingby preserving gradient flow.arXiv preprint arXiv:2002.07376, 2020.
- Haoran You, Chaojian Li, Pengfei Xu, Yonggan Fu, Yue Wang, Xiaohan Chen, YingyanLin, Zhangyang Wang, and Richard G Baraniuk.  Drawing early-bird tickets: Towards moreefficient training of deep networks.arXiv preprint arXiv:1909.11957, 2019.2
Pruning.
- Song Han, Jeff Pool, John Tran, and William Dally.  Learning both weights and connectionsfor efficient neural network.   InAdvances in neural information processing systems, pages1135–1143, 2015.
- Yihui He, Xiangyu Zhang, and Jian Sun.  Channel pruning for accelerating very deep neuralnetworks.  InProceedings of the IEEE International Conference on Computer Vision, pages1389–1397, 2017.
- Zehao Huang and Naiyan Wang.    Data-driven sparse structure selection for deep neuralnetworks.   InProceedings of the European conference on computer vision (ECCV), pages304–320, 2018.
- Yann LeCun, John S Denker, and Sara A Solla.  Optimal brain damage.  InAdvances in neuralinformation processing systems, pages 598–605, 1990.
- Namhoon Lee, Thalaiyasingam Ajanthan, and Philip HS Torr.   Snip:  Single-shot networkpruning based on connection sensitivity.arXiv preprint arXiv:1810.02340, 2018.
- Hao Li, Asim Kadav, Igor Durdanovic, Hanan Samet, and Hans Peter Graf.  Pruning filters forefficient convnets.arXiv preprint arXiv:1608.08710, 2016.[P24]Zhuang Liu, Jianguo Li, Zhiqiang Shen, Gao Huang, Shoumeng Yan, and Changshui Zhang.Learning efficient convolutional networks through network slimming.  InProceedings of theIEEE International Conference on Computer Vision, pages 2736–2744, 2017.
- Zhuang Liu, Mingjie Sun, Tinghui Zhou, Gao Huang, and Trevor Darrell.  Rethinking thevalue of network pruning.arXiv preprint arXiv:1810.05270, 2018.
- Jian-Hao Luo, Jianxin Wu, and Weiyao Lin.  Thinet: A filter level pruning method for deepneural network compression.  InProceedings of the IEEE international conference on computervision, pages 5058–5066, 2017.
- Dmitry Molchanov, Arsenii Ashukha, and Dmitry Vetrov.   Variational dropout sparsifiesdeep neural networks.InProceedings of the 34th International Conference on MachineLearning-Volume 70, pages 2498–2507. JMLR. org, 2017.General audio ML.
- Sercan Ö Arık, Heewoo Jun, and Gregory Diamos.  Fast spectrogram inversion usingmulti-head convolutional neural networks.IEEE Signal Processing Letters, 26(1):94–98, 2019.Optimization.
- Sercan Ö Arık, Heewoo Jun, and Gregory Diamos.  Fast spectrogram inversion using multi-head convolutional neural networks.IEEE Signal Processing Letters, 26(1):94–98, 2019
