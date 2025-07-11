---
title: 'Stochastic Inference for Scalable Probabilistic Modeling of Binary Matrices'
collection: publications
permalink: /publications/svi14
date: 2014-06-21
authors: 'José Miguel Hernández-Lobato, Neil Houlsby, Zoubin Ghahramani'
venue: 'International Conference on Machine Learning (ICML), 2021'
paperurl: 'http://proceedings.mlr.press/v32/hernandez-lobatoa14.html'
---

Fully observed large binary matrices appear in a wide variety of contexts. To model them, probabilistic matrix factorization (PMF) methods are an attractive solution. However, current batch algorithms for PMF can be inefficient because they need to analyze the entire data matrix before producing any parameter updates. We derive an efficient stochastic inference algorithm for PMF models of fully observed binary matrices. Our method exhibits faster convergence rates than more expensive batch approaches and has better predictive performance than scalable alternatives. The proposed method includes new data subsampling strategies which produce large gains over standard uniform subsampling. We also address the task of automatically selecting the size of the minibatches of data used by our method. For this, we derive an algorithm that adjusts this hyper-parameter online.

