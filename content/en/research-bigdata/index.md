---
title: "Oil and Gas Field Big-Data Analytics"
url: /en/research/bigdata/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 6</p>

Wellhead pressure, rate and chemical-injection data accumulate continuously as gas fields mature, but field decisions still rely largely on rules of thumb. The group uses data-driven modeling, risk-aware decision-making and deep anomaly diagnosis to move from post-hoc review to online recommendation.

{{< fig src="uploads/research/bigdata-framework.jpg" alt="Overall big-data analytics framework" caption="Overall framework: field data → sample library → world model → planning agent → recommended dosage, in closed loop" >}}

{{< fig src="uploads/research/bigdata-world-model.jpg" alt="Action-conditioned world model" caption="Action-conditioned world model for next-step tubing–casing pressure-difference prediction" >}}

{{< fig src="uploads/research/bigdata-rapa.jpg" alt="Risk-aware planning agent" caption="Risk-aware planning agent (RAPA) with layered risk rewards" >}}

{{< fig src="uploads/research/bigdata-injection-actions.jpg" alt="Dynamic injection actions comparison" caption="Dynamic foaming-agent injection actions: RAPA vs. SAC, PSO, XGBoost and field baseline" >}}

**Foam-assisted deliquification.** With Prof. Jianli Wang's group, foaming-agent dosage optimization is reformulated as a short-term decision problem driven by tubing–casing pressure-difference risk. An action-conditioned world model predicts the next pressure difference for candidate dosages, and a risk-aware planning agent (RAPA) selects actions with layered risk rewards.

<div class="flip-theme-pubs not-prose">
  <h4>Representative papers</h4>
  <ol>
    <li>Y Zhang, H Wang, M Chen, N Li, <b>J Zhu</b>, J Wang. A data-driven world-model-based planning agent for risk-aware foam-lifting agent injection optimization in gas wells. <i>Geoenergy Science and Engineering</i>, manuscript submitted (GEOEN-S-26-02523), 2026.</li>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, R Zhong, H Zhu. <a href="https://doi.org/10.3390/pr14132045" target="_blank" rel="noopener">Enhancing Plunger Lift Anomaly Detection: A Vision Transformer-Based Approach Leveraging Pretrained Models and Graphic Data Augmentation</a>. <i>Processes 14 (13), 2045</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, M Chen, H Wang, Y Li, H Zhu. <a href="https://doi.org/10.1016/j.rineng.2026.110368" target="_blank" rel="noopener">Enhanced Zero-Shot Classification of Plunger Lift Operating Conditions Using a Modified Clip Architecture with Selective Data Sampling</a>. <i>Results in Engineering, 110368</i>, 2026.</li>
    <li>Q Wang, H Zou, C Liang, S Zhang, H Jia, <b>J Zhu</b>. <a href="https://doi.org/10.1002/cjce.70389" target="_blank" rel="noopener">A combined approach for predicting liquid loading onset via clustering and convolutional neural networks</a>. <i>The Canadian Journal of Chemical Engineering</i>, 2026.</li>
    <li>QX Liu, <b>JJ Zhu</b>, HB Wang, S Chen, HY Wang, N Li, RZ Zhong, YJ Liu et al. <a href="https://doi.org/10.1016/j.petsci.2025.08.017" target="_blank" rel="noopener">Deep Feature Learning for Anomaly Detection in Gas Well Deliquification using Plunger Lift: A Novel CNN-based Approach</a>. <i>Petroleum Science</i>, 2025.</li>
    <li>L Peng, L Feng, Q Guang, <b>J Zhu</b>, H Liu, Z Nie, C Ma, C Di, Q Wu. <a href="https://doi.org/10.2118/226795-ms" target="_blank" rel="noopener">Real-Time ESP Management Framework Using Hybrid Physics-Based and ML Models</a>. <i>SPE Offshore Europe Conference and Exhibition, D021S009R008</i>, 2025.</li>
    <li>Z Zhong, H Wang, N Li, H Zhu, <b>J Zhu</b>, J Wang. Prediction of Plunger Lift Dynamics Using a Bidirectional Long Short-Term Memory Neural Network with an Innovative Forecasting Strategy. <i>2024 IEEE 3rd International Conference on Electrical Engineering, Big Data and Algorithms (EEBDA)</i>, 2024.</li>
    <li>Z Xu, H Lin, Y Jia, J Du, J Mao, <b>J Zhu</b>, J Chen, F Li, N Li. Data Augmentation and Recognition for Plunger Lift Based on Variational Autoencoders. <i>2024 6th International Conference on Intelligent Control, Measurement and Signal Processing (ICMSP)</i>, 2024.</li>
    <li>Y Xie, S Ma, H Wang, N Li, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.geoen.2023.212305" target="_blank" rel="noopener">Unsupervised clustering for the anomaly diagnosis of plunger lift operations</a>. <i>Geoenergy Science and Engineering 231, 212305</i>, 2023.</li>
    <li><b>J Zhu</b>, G Cao, W Tian, Q Zhao, H Zhu, J Song, J Peng, Z Lin, HQ Zhang. <a href="https://doi.org/10.2118/196201-ms" target="_blank" rel="noopener">Improved data mining for production diagnosis of gas wells with plunger lift through dynamic simulations</a>. <i>SPE Annual Technical Conference and Exhibition, D021S030R001</i>, 2019.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose">
<a href="{{< u "en/research/mfl/" >}}">← 5. Pipeline MFL Inspection</a>
<a href="{{< u "en/research/" >}}">Research overview</a>
</nav>
