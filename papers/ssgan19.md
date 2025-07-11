---
title: 'Self-Supervised GANs via Auxiliary Rotation Loss'
collection: publications
permalink: /publications/ssgan19
date: 2018-11-27
authors: 'Ting Chen, Xiaohua Zhai, Marvin Ritter, Mario Lucic, Neil Houlsby'
venue: 'Computer Vision and Pattern Recognition (CVPR), 2019'
# paperurl: 'http://openaccess.thecvf.com/content_CVPR_2019/papers/Chen_Self-Supervised_GANs_via_Auxiliary_Rotation_Loss_CVPR_2019_paper.pdf'
paperurl: 'https://arxiv.org/abs/1811.11212'
---

Conditional GANs are at the forefront of natural image
synthesis. The main drawback of such models is the necessity for labeled data. In this work we exploit two popular
unsupervised learning techniques, adversarial training and
self-supervision, and take a step towards bridging the gap
between conditional and unconditional GANs. In particular,
we allow the networks to collaborate on the task of representation learning, while being adversarial with respect to
the classic GAN game. The role of self-supervision is to
encourage the discriminator to learn meaningful feature representations which are not forgotten during training. We test
empirically both the quality of the learned image representations, and the quality of the synthesized images. Under
the same conditions, the self-supervised GAN attains a similar performance to state-of-the-art conditional counterparts.
Finally, we show that this approach to fully unsupervised
learning can be scaled to attain an FID of 23.4 on unconditional ImageNet generation.
