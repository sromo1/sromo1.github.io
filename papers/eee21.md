---
title: 'Sparse MoEs meet Efficient Ensembles'
collection: publications
permalink: /publications/eee21.md
date: 2021-10-07
authors: 'James Urquhart Allingham, Florian Wenzel, Zelda E Mariet, Basil Mustafa, Joan Puigcerver, Neil Houlsby, Ghassen Jerfel, Vincent Fortuin, Balaji Lakshminarayanan, Jasper Snoek, Dustin Tran, Carlos Riquelme Ruiz, Rodolphe Jenatton'
venue: 'Transactions on Machine Learning Research (TMLR)'
paperurl: 'https://arxiv.org/abs/2110.03360'
---

Machine learning models based on the aggregated outputs of submodels, either at the activation or prediction levels, often exhibit strong performance compared to individual models. We study the interplay of two popular classes of such models: ensembles of neural networks and sparse mixture of experts (sparse MoEs). First, we show that the two approaches have complementary features whose combination is beneficial. This includes a comprehensive evaluation of sparse MoEs in uncertainty related benchmarks. Then, we present Efficient Ensemble of Experts (E^3), a scalable and simple ensemble of sparse MoEs that takes the best of both classes of models, while using up to 45% fewer FLOPs than a deep ensemble. Extensive experiments demonstrate the accuracy, log-likelihood, few-shot learning, robustness, and uncertainty improvements of E^3 over several challenging vision Transformer-based baselines. E^3 not only preserves its efficiency while scaling to models with up to 2.7B parameters, but also provides better predictive performance and uncertainty estimates for larger models.