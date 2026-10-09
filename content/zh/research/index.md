---
title: 研究方向
date: 2026-10-09
---

FLIP 课题组的研究围绕油气井从井底到地面的流动与举升展开，分为五个方向：井筒多相流动建模与积液预测、电潜泵多相增压机理与工况诊断、柱塞气举瞬态建模与智能诊断、水力射流泵排水采气机理与优化、管道漏磁内检测缺陷智能识别。研究手段是实验、数值模拟（CFD、OLGA）、机理建模与数据驱动方法相结合，相互校核。每个方向后列出支撑论文，完整列表见 [Google Scholar](https://scholar.google.com/citations?user=sfsM2TUAAAAJ&hl=en)。

<nav class="flip-research-toc not-prose"><a href="#wellbore">1. 井筒多相流动建模</a><a href="#esp">2. 电潜泵多相增压与诊断</a><a href="#plunger">3. 柱塞气举建模与诊断</a><a href="#jetpump">4. 水力射流泵排水采气</a><a href="#mfl">5. 管道漏磁缺陷识别</a></nav>

## 1. 井筒多相流动建模与积液预测 {#wellbore}

油气井从井底到地面要经过直井段、斜井段、水平段和地面管线，气液两相在不同倾角下呈现分层流、段塞流、搅混流、环状流等流型，压降与持液率规律差别很大。井筒多相流模型是人工举升设计、积液判断和生产优化的共同基础，课题组同时发展稳态和瞬态两类模型。

**稳态：统一井筒多相流模型。** 以段塞单元为控制体，建立适用于多倾角、油气水三相流的统一模型：液膜区对应分层流、环雾状流，液塞区对应分散气泡流、泡状流，其余流型在求解中自然过渡。在此基础上集成和改进界面摩擦、乳化液流变、液塞持液率、平移速度等闭合关系，与文献流型数据和多种经典模型对比验证，并作为柱塞、电潜泵、射流泵工艺模型的井筒底座。

{{< fig src="uploads/research/mp-unified-model.jpg" alt="段塞单元控制体与流型边界验证" caption="统一模型：段塞单元控制体（左）与水平管流型边界计算结果对比（右）" >}}

**瞬态：水平气井漂移流模型。** 建立一维油、气、水三相漂移流模型，考虑油藏侧向质量流入，采用有限体积法、交错网格、全隐式迎风格式和牛顿迭代求解，并带自适应时间步长。与 OLGA 对比，1000–3000 m 井筒压力平均相对误差 0.36%–1.04%，5 类典型工况计算耗时 1.96–3.65 s，已形成「水平气井瞬态计算软件 V1.0」。为进一步提速，用 OLGA 多工况数据库训练嵌入守恒方程残差的 PI-DeepONet，平均相对误差 <1%，单次推理约 0.1 s。针对水平井地形段塞，还研究了尾管设计对段塞的抑制作用。

{{< fig src="uploads/research/mp-transient-hwell.jpg" alt="水平井井筒与油藏耦合及压力时空分布" caption="水平气井井筒–油藏侧向流入示意（左）与井筒压力时空分布（右）" >}}

**气井积液判断。** 气体流速下降到不足以携液时，井底开始积液。课题组汇集液滴、液膜、夹带、动能四类 48 个临界携液模型，建立文献气井 620 口、现场数据 36000 余组的资料库，用无监督聚类寻找“相似井”并对模型评分排序，给出特定井况的推荐模型；进一步结合卷积神经网络直接预测积液起始。

{{< fig src="uploads/research/ll-droplet-film.jpg" alt="井筒内液滴与液膜受力示意" caption="两类临界携液机理：井筒内液滴受力（左）与液膜受力（右）" >}}

<div class="flip-theme-pubs not-prose">
  <h4>支撑论文（7 篇）</h4>
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

## 2. 电潜泵多相增压机理与工况诊断 {#esp}

油井进入中后期或产水气井排液时，泵入口游离气增加，电潜泵（ESP）扬程退化，进而发展为喘振直至气锁停机；传统设计多用均相流模型，只在含气率很低时适用。课题组的研究主线是：旋转叶轮高剪切流场中气泡破碎聚并 → 原位含气率 → 流型转化 → 增压退化，并扩展到高粘、油水乳化、含砂等复杂工况。

{{< fig src="uploads/research/esp-gas-degradation.jpg" alt="电潜泵含气工况增压退化示意" caption="含气工况下电潜泵增压退化：随入口含气率增加，叶轮内由离散泡状流向泡状流、分层流转变" >}}

**实验与机理模型。** 依托塔尔萨大学 TUALP 多级电潜泵两相环路（14 级 TE-2700 泵，逐级测压）和本校离心泵可视化实验台，用高速摄影观测叶轮内流型与喘振起始：入口含气率超过约 7% 时增压骤降，表面活性剂可推迟甚至消除喘振。据此建立旋转流场临界气泡直径、原位含气率和流型转化边界模型；提出“最佳匹配流量 Q<sub>BM</sub>”概念，构建单相、高粘、油水乳化和气液两相的统一增压模型，在三台不同类型电潜泵上验证，误差基本在 ±20% 以内、平均约 10%。

{{< fig src="uploads/research/esp-highspeed-patterns.jpg" alt="旋转叶轮内气液流型高速摄影" caption="旋转叶轮内气液流型高速摄影：随含气率增加，由离散泡状流、泡状流过渡到间歇流" >}}

**数值模拟。** 欧拉双流体 CFD 结合相间力模拟多级泵内气液流动与跨级流型演变，用动态模态分解（DMD）提取叶轮内流场主导模态；国家自然科学基金面上项目「深海电潜泵油气混输流动机理及瞬态多相流模型研究」进一步面向海上混流式电潜泵。

{{< fig src="uploads/research/esp-cfd-void-fraction.jpg" alt="电潜泵叶轮与导叶内含气率分布" caption="不同入口含气率下电潜泵叶轮与导叶内的含气率分布（CFD）" >}}

**工况诊断与管理。** 把机理增压模型与机器学习结合，研发电潜泵实时管理框架，覆盖工况识别、故障诊断、故障预警和剩余寿命预测，形成「智能电潜泵管理系统 V1.0」算法模块。

{{< fig src="uploads/research/esp-management-dashboard.jpg" alt="智能电潜泵管理系统总览界面" caption="智能电潜泵管理系统：井群总览、故障诊断、性能曲线与剩余寿命预测" >}}

<div class="flip-theme-pubs not-prose">
  <h4>支撑论文（21 篇）</h4>
  <ol>
    <li>C Zhang, Q Li, J Zhang, <b>J Zhu</b>, Y Wang. <a href="https://doi.org/10.1063/5.0350203" target="_blank" rel="noopener">Energy conversion mechanisms and flow boundaries of gas–liquid multiphase flow in a mixed-flow electrical submersible pump for offshore oilfields</a>. <i>Physics of Fluids 38 (9)</i>, 2026.</li>
    <li>C Zhang, H Jia, X Zhang, Q Li, Y Li, Y Zhang, H Zhu, <b>J Zhu</b>. <a href="https://doi.org/10.1115/1.4072097" target="_blank" rel="noopener">Flow Structure Analysis in a Rotating Centrifugal Impeller under Gassy Conditions Using Dynamic Mode Decomposition</a>. <i>Journal of Energy Resources Technology, Part B: Subsurface Energy and Carbon …</i>, 2026.</li>
    <li>L Peng, L Feng, Q Guang, <b>J Zhu</b>, H Liu, Z Nie, C Ma, C Di, Q Wu. <a href="https://doi.org/10.2118/226795-ms" target="_blank" rel="noopener">Real-Time ESP Management Framework Using Hybrid Physics-Based and ML Models</a>. <i>SPE Offshore Europe Conference and Exhibition, D021S009R008</i>, 2025.</li>
    <li><b>J ZHU</b>, Y JI, J PENG, H ZHU. A new mechanistic model on boosting pressure of Electrical Submersible Pumps (ESPs) under gas-liquid two-phase flow. <i>Petroleum Science Bulletin 9 (1), 130-147</i>, 2024.</li>
    <li>Y Li, <b>J Zhu</b>, H Zeng, Y Zhang, Y Lu, Y Fan, H Zhu. <a href="https://doi.org/10.2118/210604-pa" target="_blank" rel="noopener">An Indirect Approach for Flow Pattern Transition Identification Inside a Low-Specific-Speed Centrifugal Pump with Experimental Verification and Theoretical Modeling</a>. <i>SPE Journal 28 (01), 184-200</i>, 2023.</li>
    <li>H Zhu, <b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.1016/j.ces.2021.117288" target="_blank" rel="noopener">Mechanistic modeling of gas effect on Multi-stage Electrical submersible pump (ESP) performance with experimental validation</a>. <i>Chemical Engineering Science 252, 117288</i>, 2022.</li>
    <li>Y Shi, <b>J Zhu</b>, H Wang, H Zhu, J Zhang, HQ Zhang. <a href="https://doi.org/10.1177/09576509211014974" target="_blank" rel="noopener">Experiments and mechanistic modeling of viscosity effect on a multistage ESP performance under viscous fluid flow</a>. <i>Proceedings of the Institution of Mechanical Engineers, Part A: Journal of …</i>, 2021.</li>
    <li><b>J Zhu</b>, H Zhao, G Cao, H Banjar, H Zhu, J Peng, HQ Zhang. <a href="https://doi.org/10.2118/196155-pa" target="_blank" rel="noopener">A New Mechanistic Model for Emulsion Rheology and Boosting Pressure Prediction in Electrical Submersible Pumps (ESPs) under Oil-Water Two-Phase Flow</a>. <i>SPE Journal 26 (02), 667-684</i>, 2021.</li>
    <li>H Zhu, <b>J Zhu</b>, Z Lin, Q Zhao, R Rutter, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2021.108399" target="_blank" rel="noopener">Performance degradation and wearing of Electrical Submersible Pump (ESP) with gas-liquid-solid flow: Experiments and mechanistic modeling</a>. <i>Journal of Petroleum Science and Engineering 200, 108399</i>, 2021.</li>
    <li>H Zhu, <b>J Zhu</b>, R Rutter, HQ Zhang. <a href="https://doi.org/10.1115/1.4048863" target="_blank" rel="noopener">Experimental Study on Deteriorated Performance, Vibration, and Geometry Changes of an Electrical Submersible Pump Under Sand Water Flow Condition</a>. <i>Journal of Energy Resources Technology 143 (8), 082104</i>, 2021.</li>
    <li><b>J Zhu</b>, H Zhu, G Cao, J Zhang, J Peng, H Banjar, HQ Zhang. <a href="https://doi.org/10.2118/194384-PA" target="_blank" rel="noopener">A New Mechanistic Model To Predict Boosting Pressure of Electrical Submersible Pumps Under High-Viscosity Fluid Flow with Validations by Experimental Data</a>. <i>SPE Journal 25 (02), 744-758</i>, 2020.</li>
    <li>C Wang, Y Zhang, J Zhang, <b>J Zhu</b>. <a href="https://doi.org/10.1016/j.petrol.2020.107467" target="_blank" rel="noopener">Flow pattern recognition inside a rotodynamic multiphase pump via developed entropy production diagnostic model</a>. <i>Journal of Petroleum Science and Engineering 194, 107467</i>, 2020.</li>
    <li><b>J Zhu</b>, J Zhang, G Cao, Q Zhao, J Peng, H Zhu, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2019.05.059" target="_blank" rel="noopener">Modeling flow pattern transitions in electrical submersible pump under gassy flow conditions</a>. <i>Journal of Petroleum Science and Engineering 180, 471-484</i>, 2019.</li>
    <li>H Zhu, <b>J Zhu</b>, R Rutter, HQ Zhang. <a href="https://doi.org/10.1115/1.4044941" target="_blank" rel="noopener">A numerical study on erosion model selection and effect of pump type and sand characters in electrical submersible pumps by sandy flow</a>. <i>Journal of Energy Resources Technology 141 (12), 122004</i>, 2019.</li>
    <li><b>J Zhu</b>, H Zhu, J Zhang, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2018.10.038" target="_blank" rel="noopener">A numerical study on flow patterns inside an electrical submersible pump (ESP) and comparison with visualization experiments</a>. <i>Journal of Petroleum Science and Engineering 173, 339-350</i>, 2019.</li>
    <li><b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.3390/en11010180" target="_blank" rel="noopener">A review of experiments and modeling of gas-liquid flow in electrical submersible pumps</a>. <i>Energies 11 (1), 180</i>, 2018.</li>
    <li><b>J Zhu</b>, H Zhu, Z Wang, J Zhang, R Cuamatzi-Melendez, JAM Farfan 等. <a href="https://doi.org/10.1016/j.expthermflusci.2018.05.013" target="_blank" rel="noopener">Surfactant Effect on Air/Water Flow in a Multistage Electrical Submersible Pump (ESP)</a>. <i>Experimental Thermal and Fluid Science</i>, 2018.</li>
    <li><b>J Zhu</b>, X Guo, F Liang, HQ Zhang. <a href="https://doi.org/10.1016/j.jngse.2017.06.027" target="_blank" rel="noopener">Experimental study and mechanistic modeling of pressure surging in electrical submersible pump</a>. <i>Journal of Natural Gas Science and Engineering 45, 625-636</i>, 2017.</li>
    <li><b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.2118/170727-PA" target="_blank" rel="noopener">Numerical study on electrical-submersible-pump two-phase performance and bubble-size modeling</a>. <i>SPE Production &amp; Operations 32 (03), 267-278</i>, 2017.</li>
    <li><b>J Zhu</b>, HQ Zhang. <a href="https://doi.org/10.1016/j.jngse.2016.10.020" target="_blank" rel="noopener">Mechanistic modeling and numerical simulation of in-situ gas void fraction inside ESP impeller</a>. <i>Journal of Natural Gas Science and Engineering 36, 144-154</i>, 2016.</li>
    <li><b>J Zhu</b>, H Banjar, Z Xia, HQ Zhang. <a href="https://doi.org/10.1016/j.petrol.2016.07.033" target="_blank" rel="noopener">CFD simulation and experimental study of oil viscosity effect on multi-stage electrical submersible pump (ESP) performance</a>. <i>Journal of Petroleum Science and Engineering 146, 735-745</i>, 2016.</li>
  </ol>
</div>

## 3. 柱塞气举瞬态建模与智能诊断 {#plunger}

柱塞气举是治理气井积液的主流间歇采气工艺，但井下柱塞运动无法直接观测，开关井制度多凭经验，异常工况也靠人工看油套压曲线判断。课题组从瞬态建模、智能诊断和制度优化三方面开展研究。

**瞬态模型。** 在 OLGA 中建立井筒、柱塞、控制器与储层模型，用现场油压、套压拟合参数；并自研全周期柱塞动力学模型，耦合统一多相流模型与组分物性，描述关井、下落、开井、上行、续流全过程，主要运行参数与 OLGA 对比精度达 90%。以全周期模型为“数字井”，用 SPSA、贝叶斯优化等算法优化开关井制度，并比较多种算法的效率与稳定性。

{{< fig src="uploads/research/plunger-cycle.jpg" alt="柱塞举升装置与举升循环" caption="典型柱塞举升装置（左）与一个举升循环内的油压、套压和产量变化（右）" >}}

{{< fig src="uploads/research/plunger-olga-field.jpg" alt="柱塞井现场数据与 OLGA 模拟对比" caption="柱塞井现场油压、套压与 OLGA 瞬态模型的长周期对比" >}}

**智能工况诊断。** 针对柱塞井高频油套压数据，发展了二维 CNN＋迁移学习、无监督聚类、VAE 数据增强、GASF/GADF 图像化＋Vision Transformer、双向 LSTM 动态预测，以及改进 CLIP 的零样本工况分类；用瞬态模型模拟的油管破裂、电动阀卡死、储层出水等反常工况补充稀缺样本，显著提升诊断精度，并封装为在线诊断程序。

{{< fig src="uploads/research/ai-plunger-diagnosis.jpg" alt="迁移学习模型对新井数据的工况诊断" caption="迁移学习模型对未参与训练的 4 口柱塞井油套压数据的工况识别结果" >}}

<div class="flip-theme-pubs not-prose">
  <h4>支撑论文（12 篇）</h4>
  <ol>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, H Zhu. <a href="https://doi.org/10.2118/233751-pa" target="_blank" rel="noopener">Optimizing Plunger Lift Systems for Gas Well Deliquification: A Bayesian Approach with Comparative Algorithmic Analysis</a>. <i>SPE Journal, 1-15</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, H Wang, M Chen, N Li, G Cao, R Zhong, H Zhu. <a href="https://doi.org/10.3390/pr14132045" target="_blank" rel="noopener">Enhancing Plunger Lift Anomaly Detection: A Vision Transformer-Based Approach Leveraging Pretrained Models and Graphic Data Augmentation</a>. <i>Processes 14 (13), 2045</i>, 2026.</li>
    <li><b>J Zhu</b>, Y Liu, M Chen, H Wang, Y Li, H Zhu. <a href="https://doi.org/10.1016/j.rineng.2026.110368" target="_blank" rel="noopener">Enhanced Zero-Shot Classification of Plunger Lift Operating Conditions Using a Modified Clip Architecture with Selective Data Sampling</a>. <i>Results in Engineering, 110368</i>, 2026.</li>
    <li>QX Liu, <b>JJ Zhu</b>, HB Wang, S Chen, HY Wang, N Li, RZ Zhong, YJ Liu 等. <a href="https://doi.org/10.1016/j.petsci.2025.08.017" target="_blank" rel="noopener">Deep Feature Learning for Anomaly Detection in Gas Well Deliquification using Plunger Lift: A Novel CNN-based Approach</a>. <i>Petroleum Science</i>, 2025.</li>
    <li>M Chen, <b>J Zhu</b>, G Cao, N Li, H Wang, H Zhu, M Jia, X Yang, D Guo. <a href="https://doi.org/10.2118/222161-ms" target="_blank" rel="noopener">Plunger Lift Working Cycle Optimization using a Dynamic Full-Cycle Model Coupled with Simultaneous Perturbation Stochastic Approximation (SPSA) Algorithm</a>. <i>Abu Dhabi International Petroleum Exhibition and Conference, D021S036R003</i>, 2024.</li>
    <li>Z Xu, H Lin, Y Jia, J Du, J Mao, <b>J Zhu</b>, J Chen, F Li, N Li. <a href="https://doi.org/10.1109/icmsp64464.2024.10867109" target="_blank" rel="noopener">Data Augmentation and Recognition for Plunger Lift Based on Variational Autoencoders</a>. <i>2024 6th International Conference on Intelligent Control, Measurement and …</i>, 2024.</li>
    <li>Z Zhong, H Wang, N Li, H Zhu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1109/eebda60612.2024.10485764" target="_blank" rel="noopener">Prediction of Plunger Lift Dynamics Using a Bidirectional Long Short-Term Memory Neural Network with an Innovative Forecasting Strategy</a>. <i>2024 IEEE 3rd International Conference on Electrical Engineering, Big Data …</i>, 2024.</li>
    <li>Y Xie, S Ma, H Wang, N Li, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.geoen.2023.212305" target="_blank" rel="noopener">Unsupervised clustering for the anomaly diagnosis of plunger lift operations</a>. <i>Geoenergy Science and Engineering 231, 212305</i>, 2023.</li>
    <li>Q Zhao, <b>J Zhu</b>, G Cao, H Zhu, HQ Zhang. <a href="https://doi.org/10.2118/205386-PA" target="_blank" rel="noopener">Transient modeling of plunger lift for gas well deliquification</a>. <i>SPE Journal 26 (05), 2928-2947</i>, 2021.</li>
    <li><b>J Zhu</b>, H Jia, H Wang, G Cao, H Zhu. Modeling and applications of plunger lift for gas well deliquification via a transient multiphase simulator. <i>Petroleum Science Bulletin 6 (4), 626-637</i>, 2021.</li>
    <li><b>J Zhu</b>, G Cao, W Tian, Q Zhao, H Zhu, J Song, J Peng, Z Lin, HQ Zhang. <a href="https://doi.org/10.2118/196201-ms" target="_blank" rel="noopener">Improved data mining for production diagnosis of gas wells with plunger lift through dynamic simulations</a>. <i>SPE Annual Technical Conference and Exhibition, D021S030R001</i>, 2019.</li>
    <li><b>J Zhu</b>, H Zhu, Q Zhao, W Fu, Y Shi, HQ Zhang. <a href="https://doi.org/10.2523/IPTC-19211-MS" target="_blank" rel="noopener">A transient plunger lift model for liquid unloading from gas wells</a>. <i>International Petroleum Technology Conference, D021S047R002</i>, 2019.</li>
  </ol>
</div>

## 4. 水力射流泵排水采气机理与优化 {#jetpump}

水平气井和致密气井进入中后期，地层能量下降、携液能力变差，水力射流泵井下无运动部件、对出砂和气体适应性强，是排水采气的可选工艺。难点在于气液两相进入喉管后容易出现气阻，泵效骤降，喷嘴与喉管参数也缺乏针对气井的设计方法。

**机理模型与气阻边界。** 课题组研究同心双管水力射流泵排水采气工艺，建立射流泵两相、三相流动机理模型和气阻临界边界，CFD 与机理模型压差互验误差在 12% 以内，并耦合井筒管流模型完成工艺设计计算。

**参数优化与软件。** 用 CFD＋代理模型＋NSGA-II 多目标优化喷嘴、喉管等结构参数和工作参数，形成「射流泵智能化工况分析软件」，支持两相/三相计算、气阻校核和参数优选。

{{< fig src="uploads/research/jet-pump-surface-flow.jpg" alt="同心双管水力射流泵排水采气地面流程" caption="同心双管水力射流泵排水采气地面流程" >}}

{{< fig src="uploads/research/jet-pump-software.jpg" alt="射流泵软件两相流功能界面" caption="射流泵智能化工况分析软件：不同气液比下的流量比–效率曲线" >}}

<div class="flip-theme-pubs not-prose">
  <h4>支撑论文（1 篇）</h4>
  <ol>
    <li><b>J ZHU</b>, A LI, Y JI, J PENG, Y ZHANG, H ZHU. Optimization of gas-liquid two-phase flow characteristic parameters in a concentric dual-tube hydraulic jet pump. <i>The Chinese Journal of Process Engineering 26 (3), 233-244</i>, 2026.</li>
  </ol>
</div>

## 5. 管道漏磁内检测缺陷智能识别 {#mfl}

漏磁（MFL）内检测是油气长输管道腐蚀、裂纹等缺陷检测的主要手段：检测器磁化管壁，缺陷处磁力线外泄，传感器阵列记录三轴漏磁信号。一次内检测产生海量信号，人工判读费时且依赖经验，而带真实开挖标签的缺陷样本又很少。

**缺陷识别与量化。** 与东南大学王建立教授合作，课题组提出级联深度学习方法：先用预训练 YOLO 网络在漏磁信号图上定位缺陷，再用 Vision Transformer 或多输入并行卷积网络回归缺陷长、宽、深，实现检测与量化一体化。

**样本生成与信号重建。** 针对标签样本稀缺，用扩散模型和生成模型合成带标签的漏磁缺陷信号，并建立合成信号质量评价方法，用合成数据提升缺陷检测精度；针对检测器高速运行或通道失效造成的欠采样，提出多先验张量补全方法重建漏磁信号。

{{< fig src="uploads/research/mfl-workflow.jpg" alt="漏磁内检测数据分析流程示意" caption="漏磁内检测数据分析流程：信号采集 → 预处理与样本扩增 → 缺陷识别与量化" >}}

<div class="flip-theme-pubs not-prose">
  <h4>支撑论文（5 篇）</h4>
  <ol>
    <li>J Xie, J Yang, K Fu, L Tai, X Wang, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100282" target="_blank" rel="noopener">Quantitative Assessment of Pipeline Defects Utilizing a Dual-Stage Deep Learning Framework: Integration of Pretrained YOLO Network and Multi-input Parallel Convolution …</a>. <i>Journal of Pipeline Science and Engineering, 100282</i>, 2025.</li>
    <li>J Yang, Y Zhang, C Su, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100382" target="_blank" rel="noopener">Multi-Priors Tensor Completion for Highly Under-sampled Magnetic Flux Leakage Signal Reconstruction</a>. <i>Journal of Pipeline Science and Engineering, 100382</i>, 2025.</li>
    <li>J Yang, J Xie, X Gao, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100363" target="_blank" rel="noopener">Synthetic Magnetic Flux Leakage Signal Generation Using Diffusion Models: A Novel Approach to Improve Pipeline Defect Detection Accuracy</a>. <i>Journal of Pipeline Science and Engineering, 100363</i>, 2025.</li>
    <li>X Chen, M Fu, X Liu, <b>J Zhu</b>. <a href="https://doi.org/10.1109/tim.2025.3602568" target="_blank" rel="noopener">Synthesizing Labeled Magnetic Flux Leakage Signals for Pipeline Integrity Assessment: A Generation and Evaluation Methodology</a>. <i>IEEE Transactions on Instrumentation and Measurement</i>, 2025.</li>
    <li>P Chen, R Li, K Fu, Z Zhong, J Xie, J Wang, <b>J Zhu</b>. <a href="https://doi.org/10.1016/j.ymssp.2023.110919" target="_blank" rel="noopener">A cascaded deep learning approach for detecting pipeline defects via pretrained YOLOv5 and ViT models based on MFL data</a>. <i>Mechanical Systems and Signal Processing 206, 110919</i>, 2024.</li>
  </ol>
</div>
