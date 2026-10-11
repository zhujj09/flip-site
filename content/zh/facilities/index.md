---
aliases:
  - /platforms/
title: 实验平台
date: 2026-10-09
---

课题组的实验工作依托本校离心泵气液两相可视化实验台，以及负责人在塔尔萨大学期间使用的 TUALP 多级电潜泵环路。多级离心泵可视化综合测试平台正在论证建设中。数值模拟与模型训练依托课题组自有的两台高性能计算服务器。

## 本校离心泵气液两相可视化实验台 {#cup-rig}

改造自离心泵水力性能台（国家自然科学基金青年项目 52004304 支持），用于超低比转速离心泵在高含水、高气液比工况下的增压性能测试，以及旋转叶轮全流道高速摄像观测。主要设备包括 PHANTOM V1212 高速运动分析系统、8530B-200 高频压力传感器、8530C-50 高频压差传感器和多通道数据采集系统。通过可视化观测，识别出叶轮内分散气泡流、泡状流、气囊流和分层流等流型。2025 年起在面上项目支持下升级：温控 0–60 ℃（±0.5 ℃），5000 fps 高速摄像。

{{< fig src="uploads/platforms/cup-esp-gas-rig.jpg" alt="离心泵高含水、高气液比工况测试台" caption="离心泵高含水、高气液比工况测试台：系统流程、现场布置与主要仪表，以及不同含气率下的增压曲线" >}}

{{< fig src="uploads/platforms/cup-impeller-visual.jpg" alt="旋转叶轮内流道可视化设备" caption="旋转叶轮内流道可视化设备：高速摄像、传感器与主要技术参数，以及叶轮内的分散气泡流、泡状流与间歇流" >}}

## 迷宫泵高粘、含气工况测试 {#labyrinth}

迷宫螺旋泵性能测试实验台，用于迷宫泵在高粘、含气工况下的性能测试。系统包括储气罐、两相分离器、扭矩传感器、变频器和数据采集系统，测试了不同转速与粘度下的扬程–流量曲线。

{{< fig src="uploads/platforms/cup-labyrinth-pump.jpg" alt="迷宫泵高粘、含气工况测试" caption="迷宫泵高粘、含气工况测试：转子与定子、实验台流程，以及不同转速、粘度下的扬程–流量曲线" >}}

## TUALP 多级电潜泵两相实验环路（塔尔萨大学） {#tualp}

<span class="flip-tag flip-tag--ext">塔尔萨大学平台</span>

该环路属于美国塔尔萨大学人工举升项目组（TUALP，Tulsa University Artificial Lift Projects），**不是本课题组的平台**。负责人朱建军在塔尔萨大学攻读博士学位及任助理研究员期间（2012–2019）使用该环路开展电潜泵气液两相实验。

环路主要参数：14 级径向式 TE-2700 电潜泵（538 系列）逐级测压；7.62 cm 两相闭式环路，24 m³ 分离器，分离器压力 345/689/1034 kPa；转速 1800–3500 rpm；介质为自来水和压缩空气，可注入 IPA 表面活性剂。可做两相、高粘、乳化、含砂等工况测试。

<div class="flip-figs">
{{< fig src="uploads/platforms/tualp-esp-loop-schematic.jpg" alt="TUALP 两相电潜泵环路示意" caption="TUALP 两相电潜泵环路示意" >}}
{{< fig src="uploads/platforms/tualp-esp-loop-photos.jpg" alt="TUALP 电潜泵实验管路与测试泵" caption="TUALP 实验管路、14 级测试泵结构与逐级测压点" >}}
</div>

## 多级离心泵叶轮及导叶多相流场可视化综合测试平台 {#multistage}

<span class="flip-tag flip-tag--plan">在建 / 规划中</span>

本平台处于论证建设阶段，**尚未建成**。负责人为朱建军，建设期限为 2025 年 10 月至 2028 年 9 月。以下指标为论证报告中的设计指标，不是实测性能。

- 三级叶轮–导叶串级结构，1–3 级快速切换，导叶出口角 ±5° 可调；透明流道与石英玻璃观察窗。
- 4K 高速成像（1000 fps 全幅）与 PIV 测速，测量瞬态速度场并识别涡结构。
- 气液、固液两相输送：含气率 ≤15%，固相粒径 ≤1 mm、浓度 ≤5%。
- 16 通道 10 kHz 同步采集；振动或位移超限时 0.1 s 内联动停机。
- 永磁同步电机加矢量变频调速，0–6000 rpm；流量 0–30 m³/h，压力 0.6–3.0 MPa。

{{< fig src="uploads/platforms/multistage-pump-visual-planned.jpg" alt="多级离心泵可视化综合测试平台示意图（规划）" caption="平台示意图（规划方案，非实物）" >}}

## 计算资源 {#computing}

课题组现有两台自有计算服务器，用于电潜泵全尺寸三维瞬态 CFD 模拟、井筒多相流数值计算，以及 PINN 等深度神经网络模型训练。

| | 双路 EPYC 9965 CPU–GPU 服务器（2025） | 双路 EPYC 7742 计算服务器 |
|---|---|---|
| 处理器 | 2 × AMD EPYC 9965，共 384 物理核 | 2 × AMD EPYC 7742，共 128 核 256 线程 |
| 内存 | 1 TB DDR5（16 × 64 GB） | 256 GB |
| GPU | 2 × NVIDIA RTX 5090（32 GB） | 2 × NVIDIA RTX 4090（24 GB），2023 年升级 |
| 存储 | 约 20 TB | 约 10 TB |
| 主要用途 | 大规模并行 CFD、多物理场耦合计算、PINN 训练 | CFD 模拟、深度学习模型训练 |

双路 EPYC 9965 服务器配备两块 RTX 5090，构成 CPU–GPU 异构协同计算环境。

<div class="flip-figs flip-figs--computing">
{{< fig src="uploads/platforms/server-epyc9965-cpu.jpg" alt="水冷双路 EPYC CPU 与内存" caption="水冷双路 EPYC CPU 与 16 条内存" >}}
{{< fig src="uploads/platforms/server-epyc9965-gpu.jpg" alt="RTX 5090 显卡" caption="RTX 5090 显卡与液冷管路" >}}
{{< fig src="uploads/platforms/server-epyc9965-chassis-v2.jpg" alt="双路 EPYC 9965 服务器整机" caption="整机（闭合机箱）" >}}
</div>

