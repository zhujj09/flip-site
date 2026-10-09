---
title: "油气田大数据分析"
url: /research/bigdata/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 6</p>

气田进入中后期后，井口压力、产量、药剂加注等生产数据持续累积，但现场决策仍大量依赖经验规则和人工看曲线。课题组把油气田大数据分析作为独立方向：以泡排剂加注、柱塞举升、积液判断等生产时序数据为主，用数据驱动建模、风险感知决策和深度异常诊断，把“事后复盘”推进到“在线推荐”。

**泡排数据驱动的世界模型与风险感知决策。** 与东南大学王建立教授团队合作，面向气井泡排剂加注优化：不以历史加注量直接回归为目标，而把油套压差及其变化作为井筒载荷与积液风险表征，将加注量优化改写为基于压差风险反馈的短期动态决策问题。先用现场日度生产数据构造状态—动作—压差变化样本，训练动作条件的数据驱动世界模型，预测不同候选加注量下下一时刻的油套压差；再在该世界模型上构建风险感知规划智能体（RAPA），按安全、预警、危险、强危险分层生成候选动作，并结合短时滚动评估与风险分层奖励，在高风险阶段增强加注、在低风险阶段抑制无效加注。单井测试中累计压差风险负担降低 46.96%，单步决策约 0.126 s；多井共享场景中累计压差风险负担降低 99.56%。相关工作已投稿 *Geoenergy Science and Engineering*。

{{< fig src="uploads/research/bigdata-framework.jpg" alt="泡排剂加注优化系统总体框架" caption="泡排剂加注优化总体框架：现场数据 → 历史样本库 → 数据驱动世界模型 → 规划智能体 → 推荐加注执行，形成闭环反馈" >}}

{{< fig src="uploads/research/bigdata-rapa.jpg" alt="风险感知规划智能体 RAPA 结构" caption="风险感知规划智能体（RAPA）：风险状态编码、候选动作生成、一步筛选、短时序列评估与最终动作选择" >}}

{{< fig src="uploads/research/bigdata-world-model.jpg" alt="世界模型对油套压差变化的短期预测" caption="动作条件世界模型的短期预测：预测油套压差变化与实测值对比（测试集 MAE≈0.26 MPa，R²≈0.88）" >}}

{{< fig src="uploads/research/bigdata-injection-actions.jpg" alt="不同方法的动态加注动作对比" caption="单井测试序列上的动态加注动作：RAPA 在高风险阶段显著加大加注，在安全阶段保持克制，并与 SAC、PSO、XGBoost 及现场基准策略对比" >}}

**生产时序异常诊断与工况识别。** 同一套数据分析思路也用于柱塞气举高频油套压曲线和电潜泵工况管理：二维 CNN／迁移学习、VAE 样本增强、GASF 图像化＋Vision Transformer、改进 CLIP 零样本分类，以及 Actor-Critic 类强化学习对泡排剂加注量的推荐，把稀缺异常样本和弱标签现场数据转化为可部署的诊断与决策模型。相关结果已形成柱塞井在线诊断程序，并与电潜泵实时管理框架相互衔接。

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（10 篇）</h4>
  <ol>
    <li>Y Zhang, H Wang, M Chen, N Li, <b>J Zhu</b>, J Wang. A data-driven world-model-based planning agent for risk-aware foam-lifting agent injection optimization in gas wells. <i>Geoenergy Science and Engineering</i>, manuscript submitted (GEOEN-S-26-02523), 2026.</li>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, R Zhong, H Zhu. <a href="https://doi.org/10.3390/pr14132045" target="_blank" rel="noopener">Enhancing Plunger Lift Anomaly Detection: A Vision Transformer-Based Approach Leveraging Pretrained Models and Graphic Data Augmentation</a>. <i>Processes 14 (13), 2045</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, M Chen, H Wang, Y Li, H Zhu. <a href="https://doi.org/10.1016/j.rineng.2026.110368" target="_blank" rel="noopener">Enhanced Zero-Shot Classification of Plunger Lift Operating Conditions Using a Modified Clip Architecture with Selective Data Sampling</a>. <i>Results in Engineering, 110368</i>, 2026.</li>
    <li>Q Wang, H Zou, C Liang, S Zhang, H Jia, <b>J Zhu</b>. <a href="https://doi.org/10.1002/cjce.70389" target="_blank" rel="noopener">A combined approach for predicting liquid loading onset via clustering and convolutional neural networks</a>. <i>The Canadian Journal of Chemical Engineering</i>, 2026.</li>
    <li>QX Liu, <b>JJ Zhu</b>, HB Wang, S Chen, HY Wang, N Li, RZ Zhong, YJ Liu 等. <a href="https://doi.org/10.1016/j.petsci.2025.08.017" target="_blank" rel="noopener">Deep Feature Learning for Anomaly Detection in Gas Well Deliquification using Plunger Lift: A Novel CNN-based Approach</a>. <i>Petroleum Science</i>, 2025.</li>
    <li>L Peng, L Feng, Q Guang, <b>J Zhu</b>, H Liu, Z Nie, C Ma, C Di, Q Wu. <a href="https://doi.org/10.2118/226795-ms" target="_blank" rel="noopener">Real-Time ESP Management Framework Using Hybrid Physics-Based and ML Models</a>. <i>SPE Offshore Europe Conference and Exhibition, D021S009R008</i>, 2025.</li>
    <li>Z Zhong, H Wang, N Li, H Zhu, <b>J Zhu</b>, J Wang. Prediction of Plunger Lift Dynamics Using a Bidirectional Long Short-Term Memory Neural Network with an Innovative Forecasting Strategy. <i>2024 IEEE 3rd International Conference on Electrical Engineering, Big Data and Algorithms (EEBDA)</i>, 2024.</li>
    <li>Z Xu, H Lin, Y Jia, J Du, J Mao, <b>J Zhu</b>, J Chen, F Li, N Li. Data Augmentation and Recognition for Plunger Lift Based on Variational Autoencoders. <i>2024 6th International Conference on Intelligent Control, Measurement and Signal Processing (ICMSP)</i>, 2024.</li>
    <li>Y Xie, S Ma, H Wang, N Li, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.geoen.2023.212305" target="_blank" rel="noopener">Unsupervised clustering for the anomaly diagnosis of plunger lift operations</a>. <i>Geoenergy Science and Engineering 231, 212305</i>, 2023.</li>
    <li><b>J Zhu</b>, G Cao, W Tian, Q Zhao, H Zhu, J Song, J Peng, Z Lin, HQ Zhang. <a href="https://doi.org/10.2118/196201-ms" target="_blank" rel="noopener">Improved data mining for production diagnosis of gas wells with plunger lift through dynamic simulations</a>. <i>SPE Annual Technical Conference and Exhibition, D021S030R001</i>, 2019.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><a href="{{< u "research/mfl/" >}}">← 5. 管道漏磁内检测缺陷智能识别</a><a href="{{< u "research/" >}}">研究方向总览</a><span></span></nav>
