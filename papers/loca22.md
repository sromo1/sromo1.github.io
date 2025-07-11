---
title: 'Location-Aware Self-Supervised Transformers for Semantic Segmentation'
collection: publications
permalink: /publications/loca22
date: 2022-12-05
authors: 'Mathilde Caron, Neil Houlsby, Cordelia Schmid'
venue: 'IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2023 [oral]'
paperurl: 'https://arxiv.org/abs/2212.02400'
---

Pixel-level labels are particularly expensive to acquire. Hence, pretraining is a critical step to improve models on a task like semantic segmentation. However, prominent algorithms for pretraining neural networks use image-level objectives, e.g. image classification, image-text alignment a la CLIP, or self-supervised contrastive learning. These objectives do not model spatial information, which might be sub-optimal when finetuning on downstream tasks with spatial reasoning. In this work, we pretrain network with a location-aware (LOCA) self-supervised method which fosters the emergence of strong dense features. Specifically, we use both a patch-level clustering scheme to mine dense pseudo-labels and a relative location prediction task to encourage learning about object parts and their spatial arrangements. Our experiments show that LOCA pretraining leads to representations that transfer competitively to challenging and diverse semantic segmentation datasets.
