---
title: 'Frozen Feature Augmentation for Few-Shot Image Classification'
collection: publications
permalink: /publications/frofa24
date: 2024-03-15
authors: 'Andreas Bär, Neil Houlsby, Mostafa Dehghani, Manoj Kumar'
venue: 'Computer Vision and Pattern Recognition (CVPR), 2024'
paperurl: 'https://arxiv.org/abs/2403.10519'
---

Training a linear classifier or lightweight model on top of pretrained vision model outputs, so-called 'frozen features', leads to impressive performance on a number of downstream few-shot tasks. Currently, frozen features are not modified during training. On the other hand, when networks are trained directly on images, data augmentation is a standard recipe that improves performance with no substantial overhead. In this paper, we conduct an extensive pilot study on few-shot image classification that explores applying data augmentations in the frozen feature space, dubbed 'frozen feature augmentation (FroFA)', covering twenty augmentations in total. Our study demonstrates that adopting a deceptively simple pointwise FroFA, such as brightness, can improve few-shot performance consistently across three network architectures, three large pretraining datasets, and eight transfer datasets.
