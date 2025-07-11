---
title: 'Ask the Right Questions: Active Question Reformulation with Reinforcement Learning'
collection: publications
permalink: /publications/aqa18.md
date: 2017-05-22
authors: 'Christian Buck, Jannis Bulian, Massimiliano Ciaramita, Wojciech Gajewski, Andrea Gesmundo, Neil Houlsby, Wei Wang'
venue: 'International Conference on Learning Representations (ICLR), 2018 [Oral]'
# paperurl: 'https://openreview.net/forum?id=S1CChZ-CZ&noteId=S1CChZ-CZ'
paperurl: 'https://arxiv.org/abs/1705.07830'
---

We frame Question Answering (QA) as a Reinforcement Learning task, an approach that we call Active Question Answering. 
We propose an agent that sits between the user and a black box QA system and learns to reformulate questions to elicit the best possible answers. The agent probes the system with, potentially many, natural language reformulations of an initial question and aggregates the returned evidence to yield the best answer. 
The reformulation system is trained end-to-end to maximize answer quality using policy gradient. We evaluate on SearchQA, a dataset of complex questions extracted from Jeopardy!. The agent outperforms a state-of-the-art base model, playing the role of the environment, and other benchmarks.
We also analyze the language that the agent has learned while interacting with the question answering system. We find that successful question reformulations look quite different from natural language paraphrases. The agent is able to discover non-trivial reformulation strategies that resemble classic information retrieval techniques such as term re-weighting (tf-idf) and stemming.
