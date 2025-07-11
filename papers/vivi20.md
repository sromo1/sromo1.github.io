---
title: 'Self-Supervised Learning of Video-Induced Visual Invariances'
collection: publications
permalink: /publications/vivi20
date: 2019-12-05
authors: 'Michael Tschannen, Josip Djolonga, Marvin Ritter, Aravindh Mahendran, Xiaohua Zhai, Neil Houlsby, Sylvain Gelly, Mario Lucic'
venue: 'Computer Vision and Pattern Recognition (CVPR), 2020'
# paperurl: 'https://openaccess.thecvf.com/content_CVPR_2020/html/Tschannen_Self-Supervised_Learning_of_Video-Induced_Visual_Invariances_CVPR_2020_paper.html'
paperurl: 'https://arxiv.org/abs/1912.02783'
---

We propose a general framework for self-supervised learning of transferable visual representations based on Video-Induced Visual Invariances (VIVI). We consider the implicit hierarchy present in the videos and make use of (i) frame-level invariances (e.g. stability to color and contrast perturbations), (ii) shot/clip-level invariances (e.g. robustness to changes in object orientation and lighting conditions), and (iii) video-level invariances (semantic relationships of scenes across shots/clips), to define a holistic self-supervised loss. Training models using different variants of the proposed framework on videos from the YouTube-8M (YT8M) data set, we obtain state-of-the-art self-supervised transfer learning results on the 19 diverse downstream tasks of the Visual Task Adaptation Benchmark (VTAB), using only 1000 labels per task. We then show how to co-train our models jointly with labeled images, outperforming an ImageNet-pretrained ResNet-50 by 0.8 points with 10x fewer labeled images, as well as the previous best supervised model by 3.7 points using the full ImageNet data set.

