---
title: 'On Self Modulation for Generative Adversarial Networks'
collection: publications
permalink: /publications/selfmod19
date: 2018-10-02
authors: 'Ting Chen, Mario Lucic, Neil Houlsby, Sylvain Gelly'
venue: 'International Conference on Learning Representations (ICLR), 2019'
# paperurl: 'https://openreview.net/forum?id=Hkl5aoR5tm'
paperurl: 'https://arxiv.org/abs/1810.01365'
---

Training Generative Adversarial Networks (GANs) is notoriously challenging. We propose and study an architectural modification, self-modulation, which improves GAN performance across different data sets, architectures, losses, regularizers, and hyperparameter settings. Intuitively, self-modulation allows the intermediate feature maps of a generator to change as a function of the input noise vector. While reminiscent of other conditioning techniques, it requires no labeled data. In a large-scale empirical study we observe a relative decrease of 5%-35% in FID. Furthermore, all else being equal, adding this modification to the generator leads to improved performance in 124/144 (86%) of the studied settings. Self-modulation is a simple architectural change that requires no additional parameter tuning, which suggests that it can be applied readily to any GAN.
