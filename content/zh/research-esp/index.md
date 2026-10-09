---
title: "电潜泵多相增压机理与工况诊断"
url: /research/esp/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 2</p>

油井进入中后期或产水气井排液时，泵入口游离气增加，电潜泵（ESP）扬程退化，进而发展为喘振直至气锁停机；传统设计多用均相流模型，只在含气率很低时适用。课题组的研究主线是：旋转叶轮高剪切流场中气泡破碎聚并 → 原位含气率 → 流型转化 → 增压退化，并扩展到高粘、油水乳化、含砂等复杂工况。

{{< fig src="uploads/research/esp-surging-curves.jpg" alt="含气工况电潜泵增压–流量曲线与喘振" caption="含气工况下电潜泵增压退化与喘振：随进气量增加，增压–流量曲线出现喘振拐点并大幅下降（左）；气液两相增压机理模型与实验对比（右）" >}}

**实验与机理模型。** 依托塔尔萨大学 TUALP 多级电潜泵两相环路（14 级 TE-2700 泵，逐级测压）和本校离心泵可视化实验台，用高速摄影观测叶轮内流型与喘振起始：入口含气率超过约 7% 时增压骤降，表面活性剂可推迟甚至消除喘振。据此建立旋转流场临界气泡直径、原位含气率和流型转化边界模型；提出“最佳匹配流量 Q<sub>BM</sub>”概念，构建单相、高粘、油水乳化和气液两相的统一增压模型，在三台不同类型电潜泵上验证，误差基本在 ±20% 以内、平均约 10%。

{{< fig src="uploads/research/esp-tualp-loop.jpg" alt="TUALP 多级电潜泵气液两相实验环路" caption="TUALP 多级电潜泵气液两相实验环路：流程（左）与 14 级 TE-2700 泵逐级测压段（右）" >}}

{{< fig src="uploads/research/esp-impeller-highspeed.jpg" alt="旋转叶轮流道内气液两相流高速摄影" caption="旋转叶轮流道内气液两相流高速摄影：气泡沿流道迁移、回流，并在叶片附近聚集成气团（Gas Pocket）" >}}

**数值模拟。** 欧拉双流体 CFD 结合相间力模拟多级泵内气液流动与跨级流型演变，用动态模态分解（DMD）提取叶轮内流场主导模态；国家自然科学基金面上项目「深海电潜泵油气混输流动机理及瞬态多相流模型研究」进一步面向海上混流式电潜泵。

{{< fig src="uploads/research/esp-cfd-gas-isosurface.jpg" alt="电潜泵叶轮内原位含气率等值面" caption="多级电潜泵第二级叶轮内原位含气率 α<sub>G</sub> = 5% 等值面（CFD）：不同工况下气相在叶轮进口聚集成环状气团并沿叶片延伸" >}}

**海上宽幅电潜泵叶导轮水力设计与 CFD 自动优化。** 海上油田进入中后期后排量波动大、含气高，传统单点设计电潜泵高效区窄，偏离设计点效率骤降。课题组面向 400、538 系列宽流道混流式电潜泵开展叶轮/导轮水力设计：以成熟泵型为基础，经相似定律尺度换算、欧拉方程扬程修正和比转速校核构建基础模型；再用 Python 串联 CFturbo 参数化几何、Workbench 网格更新与 PyFluent 批量求解，形成“几何批处理—网格更新—批量求解—代理模型寻优”的全流程自动优化闭环，以拉丁超立方采样和高斯过程代理模型搜索设计空间，并用已知泵型的实测曲线标定计入泄漏的 CFD 修正。首轮 62 组有效样本的 Spearman 敏感性分析表明，叶轮出口宽度 b<sub>2</sub> 对最佳效率点位置影响最大（ρ≈0.74），据此将设计变量由 10 维压缩到 5 维，显著提高寻优效率。

{{< fig src="uploads/research/esp-wide-impeller-opt.jpg" alt="宽幅电潜泵叶轮导轮参数化模型与 CFD 全流程自动优化流程" caption="宽幅电潜泵叶轮（左上）与导轮（左下）参数化三维模型；Python 驱动 Workbench（CFturbo / Mesh / Fluent）的 CFD 全流程自动优化流程（右）" >}}

{{< fig src="uploads/research/esp-wide-sensitivity.jpg" alt="叶轮几何参数敏感性分析" caption="首轮自动优化样本的几何参数敏感性分析（Spearman 秩相关）：叶轮出口宽度 b<sub>2</sub> 对目标函数、最佳效率点和大流量扬程的影响最显著" >}}

**工况诊断与管理。** 把机理增压模型与机器学习结合，研发电潜泵实时管理框架，覆盖工况识别、故障诊断、故障预警和剩余寿命预测，形成「智能电潜泵管理系统 V1.0」算法模块。

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（10 篇）</h4>
  <ol>
    <li>L Peng, L Feng, Q Guang, <b>J Zhu</b>, H Liu, Z Nie, C Ma, C Di, Q Wu. <a href="https://doi.org/10.2118/226795-ms" target="_blank" rel="noopener">Real-Time ESP Management Framework Using Hybrid Physics-Based and ML Models</a>. <i>SPE Offshore Europe Conference and Exhibition, D021S009R008</i>, 2025.</li>
    <li>Y Li, <b>J Zhu</b>, H Zeng, Y Zhang, Y Lu, Y Fan, H Zhu. <a href="https://doi.org/10.2118/210604-pa" target="_blank" rel="noopener">An Indirect Approach for Flow Pattern Transition Identification Inside a Low-Specific-Speed Centrifugal Pump with Experimental Verification and Theoretical Modeling</a>. <i>SPE Journal 28 (01), 184-200</i>, 2023.</li>
    <li>H Zhu, <b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.1016/j.ces.2021.117288" target="_blank" rel="noopener">Mechanistic modeling of gas effect on Multi-stage Electrical submersible pump (ESP) performance with experimental validation</a>. <i>Chemical Engineering Science 252, 117288</i>, 2022.</li>
    <li><b>J Zhu</b>, H Zhao, G Cao, H Banjar, H Zhu, J Peng, HQ Zhang. <a href="https://doi.org/10.2118/196155-pa" target="_blank" rel="noopener">A New Mechanistic Model for Emulsion Rheology and Boosting Pressure Prediction in Electrical Submersible Pumps (ESPs) under Oil-Water Two-Phase Flow</a>. <i>SPE Journal 26 (02), 667-684</i>, 2021.</li>
    <li><b>J Zhu</b>, H Zhu, G Cao, J Zhang, J Peng, H Banjar, HQ Zhang. <a href="https://doi.org/10.2118/194384-PA" target="_blank" rel="noopener">A New Mechanistic Model To Predict Boosting Pressure of Electrical Submersible Pumps Under High-Viscosity Fluid Flow with Validations by Experimental Data</a>. <i>SPE Journal 25 (02), 744-758</i>, 2020.</li>
    <li><b>J Zhu</b>, J Zhang, G Cao, Q Zhao, J Peng, H Zhu, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2019.05.059" target="_blank" rel="noopener">Modeling flow pattern transitions in electrical submersible pump under gassy flow conditions</a>. <i>Journal of Petroleum Science and Engineering 180, 471-484</i>, 2019.</li>
    <li><b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.3390/en11010180" target="_blank" rel="noopener">A review of experiments and modeling of gas-liquid flow in electrical submersible pumps</a>. <i>Energies 11 (1), 180</i>, 2018.</li>
    <li><b>J Zhu</b>, X Guo, F Liang, HQ Zhang. <a href="https://doi.org/10.1016/j.jngse.2017.06.027" target="_blank" rel="noopener">Experimental study and mechanistic modeling of pressure surging in electrical submersible pump</a>. <i>Journal of Natural Gas Science and Engineering 45, 625-636</i>, 2017.</li>
    <li><b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.1016/j.jngse.2016.10.020" target="_blank" rel="noopener">Mechanistic modeling and numerical simulation of in-situ gas void fraction inside ESP impeller</a>. <i>Journal of Natural Gas Science and Engineering 36, 144-154</i>, 2016.</li>
    <li><b>J Zhu</b>, H Banjar, Z Xia, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2016.07.033" target="_blank" rel="noopener">CFD simulation and experimental study of oil viscosity effect on multi-stage electrical submersible pump (ESP) performance</a>. <i>Journal of Petroleum Science and Engineering 146, 735-745</i>, 2016.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><a href="{{< u "research/wellbore/" >}}">← 1. 井筒多相流动建模与积液预测</a><a href="{{< u "research/" >}}">研究方向总览</a><a href="{{< u "research/plunger/" >}}">3. 柱塞气举瞬态建模与智能诊断 →</a></nav>
