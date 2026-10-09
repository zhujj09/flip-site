---
title: "柱塞气举瞬态建模与智能诊断"
url: /research/plunger/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 3</p>

柱塞气举是治理气井积液的主流间歇采气工艺，但井下柱塞运动无法直接观测，开关井制度多凭经验，异常工况也靠人工看油套压曲线判断。课题组从瞬态建模、智能诊断和制度优化三方面开展研究。

**瞬态模型。** 在 OLGA 中建立井筒、柱塞、控制器与储层模型，用现场油压、套压拟合参数；并自研全周期柱塞动力学模型，耦合统一多相流模型与组分物性，描述关井、下落、开井、上行、续流全过程，主要运行参数与 OLGA 对比精度达 90%。以全周期模型为“数字井”，用 SPSA、贝叶斯优化等算法优化开关井制度，并比较多种算法的效率与稳定性。

{{< fig src="uploads/research/plunger-cycle.jpg" alt="柱塞举升装置与举升循环" caption="典型柱塞举升装置（左）与一个举升循环内的油压、套压和产量变化（右）" >}}

{{< fig src="uploads/research/plunger-olga-field.jpg" alt="柱塞井现场数据与 OLGA 模拟对比" caption="柱塞井现场油压、套压与 OLGA 瞬态模型的长周期对比" >}}

**智能工况诊断。** 针对柱塞井高频油套压数据，发展了二维 CNN＋迁移学习、无监督聚类、VAE 数据增强、GASF/GADF 图像化＋Vision Transformer、双向 LSTM 动态预测，以及改进 CLIP 的零样本工况分类；用瞬态模型模拟的油管破裂、电动阀卡死、储层出水等反常工况补充稀缺样本，显著提升诊断精度，并封装为在线诊断程序。

{{< fig src="uploads/research/ai-plunger-diagnosis.jpg" alt="迁移学习模型对新井数据的工况诊断" caption="迁移学习模型对未参与训练的 4 口柱塞井油套压数据的工况识别结果" >}}

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（10 篇）</h4>
  <ol>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, H Zhu. <a href="https://doi.org/10.2118/233751-pa" target="_blank" rel="noopener">Optimizing Plunger Lift Systems for Gas Well Deliquification: A Bayesian Approach with Comparative Algorithmic Analysis</a>. <i>SPE Journal, 1-15</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, R Zhong, H Zhu. <a href="https://doi.org/10.3390/pr14132045" target="_blank" rel="noopener">Enhancing Plunger Lift Anomaly Detection: A Vision Transformer-Based Approach Leveraging Pretrained Models and Graphic Data Augmentation</a>. <i>Processes 14 (13), 2045</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, M Chen, H Wang, Y Li, H Zhu. <a href="https://doi.org/10.1016/j.rineng.2026.110368" target="_blank" rel="noopener">Enhanced Zero-Shot Classification of Plunger Lift Operating Conditions Using a Modified Clip Architecture with Selective Data Sampling</a>. <i>Results in Engineering, 110368</i>, 2026.</li>
    <li>QX Liu, <b>JJ Zhu</b>, HB Wang, S Chen, HY Wang, N Li, RZ Zhong, YJ Liu 等. <a href="https://doi.org/10.1016/j.petsci.2025.08.017" target="_blank" rel="noopener">Deep Feature Learning for Anomaly Detection in Gas Well Deliquification using Plunger Lift: A Novel CNN-based Approach</a>. <i>Petroleum Science</i>, 2025.</li>
    <li>M Chen, <b>J Zhu</b>, G Cao, N Li, H Wang, H Zhu, M Jia, X Yang, D Guo. <a href="https://doi.org/10.2118/222161-ms" target="_blank" rel="noopener">Plunger Lift Working Cycle Optimization using a Dynamic Full-Cycle Model Coupled with Simultaneous Perturbation Stochastic Approximation (SPSA) Algorithm</a>. <i>Abu Dhabi International Petroleum Exhibition and Conference, D021S036R003</i>, 2024.</li>
    <li>Y Xie, S Ma, H Wang, N Li, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.geoen.2023.212305" target="_blank" rel="noopener">Unsupervised clustering for the anomaly diagnosis of plunger lift operations</a>. <i>Geoenergy Science and Engineering 231, 212305</i>, 2023.</li>
    <li>Q Zhao, <b>J Zhu</b>, G Cao, H Zhu, HQ Zhang. <a href="https://doi.org/10.2118/205386-PA" target="_blank" rel="noopener">Transient modeling of plunger lift for gas well deliquification</a>. <i>SPE Journal 26 (05), 2928-2947</i>, 2021.</li>
    <li><b>J Zhu</b>, H Jia, H Wang, G Cao, H Zhu. Modeling and applications of plunger lift for gas well deliquification via a transient multiphase simulator. <i>Petroleum Science Bulletin 6 (4), 626-637</i>, 2021.</li>
    <li><b>J Zhu</b>, G Cao, W Tian, Q Zhao, H Zhu, J Song, J Peng, Z Lin, HQ Zhang. <a href="https://doi.org/10.2118/196201-ms" target="_blank" rel="noopener">Improved data mining for production diagnosis of gas wells with plunger lift through dynamic simulations</a>. <i>SPE Annual Technical Conference and Exhibition, D021S030R001</i>, 2019.</li>
    <li><b>J Zhu</b>, H Zhu, Q Zhao, W Fu, Y Shi, HQ Zhang. <a href="https://doi.org/10.2523/IPTC-19211-MS" target="_blank" rel="noopener">A transient plunger lift model for liquid unloading from gas wells</a>. <i>International Petroleum Technology Conference, D021S047R002</i>, 2019.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><a href="{{< u "research/esp/" >}}">← 2. 电潜泵多相增压机理与工况诊断</a><a href="{{< u "research/" >}}">研究方向总览</a><a href="{{< u "research/jetpump/" >}}">4. 水力射流泵排水采气机理与优化 →</a></nav>
