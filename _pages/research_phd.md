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

## Abstract

Recent advancements in deep learning have opened new pathways for embedding these technologies in real-time audio applications, particularly in the realm of musical creativity. The primary goal of this research is to develop a new kind of musical instrument, harnessing the power and versatility of deep learning for sound generation. This innovative approach aims to address the fundamental question of how cutting-edge technology can be transformed into a creative tool that not only enhances but also empowers the artistic process.

To achieve this, the research first examines the notion of creativity itself and its implications, as well as the creative process, to highlight how these new technologies can be leveraged to foster an environment where artists can explore and expand their creative potential. Our main hypothesis centers on the crucial importance of the medium—the instrument—and its associated controls, as well as on the real-time nature of the sound generation.

We then propose a new model designed to enhance the control and expressiveness of audio generation, focusing on the manipulation of timbre through perceptual features. This model integrates techniques from Fader Networks and the recent RAVE model to allow for continuous descriptor-based control in real-time deep audio synthesis. By orthogonalizing the continuous time-varying attributes from the latent representation, our approach provides independent priors which enable separate operations such as timbre transfer and attribute transfer, opening up new avenues for creative exploration. This allows users to select a set of descriptors to condition the generation process, thereby creating a vast array of sounds.

A significant achievement of this research is the development of the 'Neurorack', a pioneering stand-alone synthesizer in the Eurorack format whose audio generation is driven by deep learning. The Neurorack is not just a theoretical construct but a tangible, functional instrument that demonstrates the practical application of the discussed concepts. It offers musicians a novel tool for live performance, equipped with real-time control over sound characteristics that were previously hard to manipulate, such as timbral texture and dynamic response. This instrument is designed to be intuitive, allowing seamless integration into existing musical setups and providing artists with immediate feedback and control, thereby enriching the live music creation experience.

Furthermore, the research speculates on the future of creative processes influenced by rapid technological advancements. We consider how emerging technologies might not only redefine traditional practices but also pave the way for novel forms of artistic expression. As deep learning continues to evolve, its integration into creative tools could lead to significant transformations in how music is composed, performed, and experienced. However, there are inherent risks in this evolution; the potential for these technologies to dominate and standardize creative outputs is a concerning possibility. This could potentially stifle individual creativity and homogenize art forms, overshadowing traditional techniques and skills that have defined artistic expression for centuries. Moreover, the increasing reliance on language models raises significant challenges in ensuring these tools contribute creatively in a meaningful way. The challenge lies not just in their technical development but also in defining and implementing frameworks that encourage genuine innovation without diluting the creative process, ensuring that these models enhance rather than replace the nuanced human touch in artistic creation.

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
