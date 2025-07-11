---
title: 'Probabilistic Matrix Factorization with Non-random Missing Data'
collection: publications
permalink: /publications/mnar14
date: 2014-06-21
authors: 'José Miguel Hernández-Lobato, Neil Houlsby, Zoubin Ghahramani'
venue: 'International Conference on Machine Learning (ICML)'
paperurl: 'http://proceedings.mlr.press/v32/hernandez-lobatob14'
---

We propose a probabilistic matrix factorization model for collaborative filtering that learns from data that is missing not at random (MNAR). Matrix factorization models exhibit state-of-the-art predictive performance in collaborative filtering. However, these models usually assume that the data is missing at random (MAR), and this is rarely the case. For example, the data is not MAR if users rate items they like more than ones they dislike. When the MAR assumption is incorrect, inferences are biased and predictive performance can suffer. Therefore, we model both the generative process for the data and the missing data mechanism. By learning these two models jointly we obtain improved performance over state-of-the-art methods when predicting the ratings and when modeling the data observation process. We present the first viable MF model for MNAR data. Our results are promising and we expect that further research on NMAR models will yield large gains in collaborative filtering.

