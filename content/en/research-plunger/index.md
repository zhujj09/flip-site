---
title: "Plunger Lift Transient Modeling and Intelligent Diagnosis"
url: /en/research/plunger/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 3</p>

Plunger lift is the main intermittent deliquification method for gas wells, but plunger motion cannot be observed downhole and schedules are often set by experience.

{{< fig src="uploads/research/plunger-cycle.jpg" alt="Plunger-lift installation and one lift cycle" caption="Typical plunger-lift installation (left) and tubing/casing pressure and rate over one lift cycle (right)" >}}

**Transient models.** OLGA well–plunger–controller–reservoir models are history-matched with field pressures, and an in-house full-cycle plunger dynamics model coupled with the unified multiphase flow model matches OLGA on the main operating parameters with about 90% accuracy. Using it as a digital well, open/shut-in schedules are optimized with SPSA and Bayesian optimization.

**Intelligent diagnosis.** CNN, ViT, VAE-based data augmentation and zero-shot CLIP-style models identify abnormal plunger-well conditions from tubing/casing pressure curves.

<div class="flip-theme-pubs not-prose">
  <h4>Representative papers</h4>
  <ol>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, H Zhu. <a href="https://doi.org/10.2118/233751-pa" target="_blank" rel="noopener">Optimizing Plunger Lift Systems for Gas Well Deliquification: A Bayesian Approach with Comparative Algorithmic Analysis</a>. <i>SPE Journal, 1-15</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, R Zhong, H Zhu. <a href="https://doi.org/10.3390/pr14132045" target="_blank" rel="noopener">Enhancing Plunger Lift Anomaly Detection: A Vision Transformer-Based Approach Leveraging Pretrained Models and Graphic Data Augmentation</a>. <i>Processes 14 (13), 2045</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, M Chen, H Wang, Y Li, H Zhu. <a href="https://doi.org/10.1016/j.rineng.2026.110368" target="_blank" rel="noopener">Enhanced Zero-Shot Classification of Plunger Lift Operating Conditions Using a Modified Clip Architecture with Selective Data Sampling</a>. <i>Results in Engineering, 110368</i>, 2026.</li>
    <li>QX Liu, <b>JJ Zhu</b>, HB Wang, S Chen, HY Wang, N Li, RZ Zhong, YJ Liu et al. <a href="https://doi.org/10.1016/j.petsci.2025.08.017" target="_blank" rel="noopener">Deep Feature Learning for Anomaly Detection in Gas Well Deliquification using Plunger Lift: A Novel CNN-based Approach</a>. <i>Petroleum Science</i>, 2025.</li>
    <li>M Chen, <b>J Zhu</b>, G Cao, N Li, H Wang, H Zhu, M Jia, X Yang, D Guo. <a href="https://doi.org/10.2118/222161-ms" target="_blank" rel="noopener">Plunger Lift Working Cycle Optimization using a Dynamic Full-Cycle Model Coupled with Simultaneous Perturbation Stochastic Approximation (SPSA) Algorithm</a>. <i>Abu Dhabi International Petroleum Exhibition and Conference, D021S036R003</i>, 2024.</li>
    <li>Y Xie, S Ma, H Wang, N Li, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.geoen.2023.212305" target="_blank" rel="noopener">Unsupervised clustering for the anomaly diagnosis of plunger lift operations</a>. <i>Geoenergy Science and Engineering 231, 212305</i>, 2023.</li>
    <li>Q Zhao, <b>J Zhu</b>, G Cao, H Zhu, HQ Zhang. <a href="https://doi.org/10.2118/205386-PA" target="_blank" rel="noopener">Transient modeling of plunger lift for gas well deliquification</a>. <i>SPE Journal 26 (05), 2928-2947</i>, 2021.</li>
    <li><b>J Zhu</b>, H Jia, H Wang, G Cao, H Zhu. Modeling and applications of plunger lift for gas well deliquification via a transient multiphase simulator. <i>Petroleum Science Bulletin 6 (4), 626-637</i>, 2021.</li>
    <li><b>J Zhu</b>, G Cao, W Tian, Q Zhao, H Zhu, J Song, J Peng, Z Lin, HQ Zhang. <a href="https://doi.org/10.2118/196201-ms" target="_blank" rel="noopener">Improved data mining for production diagnosis of gas wells with plunger lift through dynamic simulations</a>. <i>SPE Annual Technical Conference and Exhibition, D021S030R001</i>, 2019.</li>
    <li><b>J Zhu</b>, H Zhu, Q Zhao, W Fu, Y Shi, HQ Zhang. <a href="https://doi.org/10.2523/IPTC-19211-MS" target="_blank" rel="noopener">A transient plunger lift model for liquid unloading from gas wells</a>. <i>International Petroleum Technology Conference, D021S047R002</i>, 2019.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose">
<a href="{{< u "en/research/esp/" >}}">← 2. ESP Multiphase Boosting</a>
<a href="{{< u "en/research/" >}}">Research overview</a>
<a href="{{< u "en/research/jetpump/" >}}">4. Hydraulic Jet Pump →</a>
</nav>
