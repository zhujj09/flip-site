---
title: "井筒多相流动建模与积液预测"
url: /research/wellbore/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 1</p>

油气井从井底到地面要经过直井段、斜井段、水平段和地面管线，气液两相在不同倾角下呈现分层流、段塞流、搅混流、环状流等流型，压降与持液率规律差别很大。井筒多相流模型是人工举升设计、积液判断和生产优化的共同基础，课题组同时发展稳态和瞬态两类模型。

**稳态：统一井筒多相流模型。** 以段塞单元为控制体，建立适用于多倾角、油气水三相流的统一模型：液膜区对应分层流、环雾状流，液塞区对应分散气泡流、泡状流，其余流型在求解中自然过渡。在此基础上集成和改进界面摩擦、乳化液流变、液塞持液率、平移速度等闭合关系，与文献流型数据和多种经典模型对比验证，并作为柱塞、电潜泵、射流泵工艺模型的井筒底座。

{{< fig src="uploads/research/mp-unified-model.jpg" alt="段塞单元控制体与流型边界验证" caption="统一模型：段塞单元控制体（左）与水平管流型边界计算结果对比（右）" >}}

**瞬态：水平气井漂移流模型。** 建立一维油、气、水三相漂移流模型，考虑油藏侧向质量流入，采用有限体积法、交错网格、全隐式迎风格式和牛顿迭代求解，并带自适应时间步长。与 OLGA 对比，1000–3000 m 井筒压力平均相对误差 0.36%–1.04%，5 类典型工况计算耗时 1.96–3.65 s，已形成「水平气井瞬态计算软件 V1.0」。针对水平井地形段塞，还研究了尾管设计对段塞的抑制作用。

{{< fig src="uploads/research/mp-transient-model.jpg" alt="漂移流模型交错网格离散与自研瞬态模型–OLGA 对比" caption="瞬态漂移流模型：交错网格离散（左，压力/体积分数存于质量控制体中心，速度存于界面）；自研瞬态三相流模型与 OLGA 的油气水表观流速、压力对比（右）" >}}

**物理信息神经网络（PINN）快速计算。** 把守恒方程嵌入神经网络损失函数，让 AI 模型“懂物理”：用 OLGA 多工况数据训练嵌入漂移流守恒方程残差的 PI-DeepONet，水平气井两相流平均相对误差 <1%，隐去 80% 观测数据误差仍在 5% 以内，单次推理约 0.1 s；进一步发展分时间块的 XPINN 框架，只用入口流量与出口压力等边界数据重构管内压力、含气率瞬态场，并比较多流型工况下的重构精度。

**气井积液判断。** 气体流速下降到不足以携液时，井底开始积液。课题组汇集液滴、液膜、夹带、动能四类 48 个临界携液模型，建立文献气井 620 口、现场数据 36000 余组的资料库，用无监督聚类寻找“相似井”并对模型评分排序，给出特定井况的推荐模型；进一步结合卷积神经网络直接预测积液起始。

{{< fig src="uploads/research/ll-droplet-film.jpg" alt="井筒内液滴与液膜受力示意" caption="两类临界携液机理：井筒内液滴受力（左）与液膜受力（右）" >}}

**泡排剂加注智能决策。** 与东南大学王建立教授团队合作，把气井泡排剂加注量优化从“拟合历史加注量”改写为以油套压差风险为反馈的短期动态决策问题：用现场日度生产数据训练动作条件的数据驱动世界模型，预测不同候选加注量下下一时刻的油套压差；在此基础上构建风险感知规划智能体（RAPA），高风险阶段自适应加注、低风险阶段抑制无效加注，并与 PPO、DDPG、SAC、TD3 等 Actor-Critic 类深度强化学习算法及贝叶斯优化系统对比，同时发展了 Actor-Critic 加注量推荐模型。单井测试中累计压差风险负担降低 46.96%，单步决策约 0.126 s；多井共享应用中降低 99.56%。相关论文在投。

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（7 篇）</h4>
  <ol>
    <li>Q Wang, H Zou, C Liang, S Zhang, H Jia, <b>J Zhu</b>. <a href="https://doi.org/10.1002/cjce.70389" target="_blank" rel="noopener">A combined approach for predicting liquid loading onset via clustering and convolutional neural networks</a>. <i>The Canadian Journal of Chemical Engineering</i>, 2026.</li>
    <li>J Yang, M Chen, H Wang, R Zheng, Z Li, H Zhou, <b>J Zhu</b>. <a href="https://doi.org/10.3390/pr13103363" target="_blank" rel="noopener">Fast Calculation Method of Two-Phase Flow in Horizontal Gas Wells Based on PI-DeepONet</a>. <i>Processes 13 (10), 3363</i>, 2025.</li>
    <li>H Zhu, Y Liu, D Tychus, D Zheng, SP Adiraju, TS Tatu, <b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.1016/j.geoen.2023.212598" target="_blank" rel="noopener">Sensitivity analysis on tailpipe design for mitigating terrain slug in horizontal wells</a>. <i>Geoenergy Science and Engineering 235, 212598</i>, 2024.</li>
    <li>Z Wang, W Fu, H Li, <b>J Zhu</b>. <a href="https://doi.org/10.3389/978-2-83251-686-7" target="_blank" rel="noopener">Multiphase flow behavior in the deep-stratum and deep-water wellbores</a>. <i>Frontiers Media SA</i>, 2023.</li>
    <li>H Wang, J Du, J Chen, G Cao, N Li, <b>J Zhu</b>, M Jia, X Yang. <a href="https://doi.org/10.2523/iptc-22730-ea" target="_blank" rel="noopener">A New Method to Calculate Loading Liquid Water of Gas Wells in Qinghai Oilfield</a>. <i>International Petroleum Technology Conference, D032S052R001</i>, 2023.</li>
    <li>H Jia, <b>J Zhu</b>, G Cao, Y Lu, B Lu, H Zhu. <a href="https://doi.org/10.2118/209578-PA" target="_blank" rel="noopener">A model ranking approach for liquid loading onset predictions</a>. <i>SPE Production &amp; Operations 37 (03), 370-382</i>, 2022.</li>
    <li>SY Nahri, Y Chen, W Williams, O Santos, L Thibodeaux, <b>J Zhu</b>. <a href="https://doi.org/10.1115/omae2019-96683" target="_blank" rel="noopener">Understanding the Phenomenon of Dissolved Gas Migration of Gas in Riser During Drilling Operations</a>. <i>International Conference on Offshore Mechanics and Arctic Engineering 58875 …</i>, 2019.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><span></span><a href="{{< u "research/" >}}">研究方向总览</a><a href="{{< u "research/esp/" >}}">2. 电潜泵多相增压机理与工况诊断 →</a></nav>
