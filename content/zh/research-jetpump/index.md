---
title: "水力射流泵排水采气机理与优化"
url: /research/jetpump/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 4</p>

致密气井、水平气井进入中后期后地层能量下降、携液能力不足，井筒积液使产量快速递减。水力射流泵井下无运动部件，靠地面高压动力液驱动，对出砂、高气液比和深井适应性强，是排水采气的重要工艺；但气液两相进入喉管后易发生空化和气阻，泵效普遍偏低，喷嘴、喉管等结构参数也缺少面向气井的设计方法。

{{< fig src="uploads/research/jetpump-geometry.jpg" alt="同心双管水力射流泵三维模型与工作原理" caption="同心双管水力射流泵：泵体三维模型与内部剖面（左）；喷嘴–吸入室–喉管–扩散管结构及沿程压力分布（右）" >}}

**机理模型与气阻边界。** 课题组围绕同心双管水力射流泵排水采气工艺，基于喷嘴、喉管、扩散管各段能量方程，建立计入喷嘴损失和喉管–扩散管损失的单相、气液两相及气–水–油三相性能模型，分析面积比、动力液/井液密度比、气水比对压力恢复比和泵效的影响；引入空化比与临界速度比，给出不同动力液压力、吸入压力下的空化与声速临界边界，确定“未空化区”内的最佳流量比区间，并据此给出喷嘴–喉管面积比的优选、次选和不推荐范围，用于防气阻排采制度设计。

{{< fig src="uploads/research/jetpump-performance.jpg" alt="射流泵气液两相性能曲线与空化临界预测" caption="气液两相射流泵性能：不同气水比下压力恢复比与效率随流量比的变化（左）；特定工况下效率、空化比与临界速度比预测，箭头指向未空化区（右）" >}}

**数值模拟与参数优化。** 依据现场井况建立射流泵三维流体域，采用 VOF 气液两相模型计算泵内压力、速度和含气率分布，与实验数据对比误差在 7.5% 以内，与机理模型压差互验误差在 12% 以内；以 CFD 样本训练 SVM（PSO、贝叶斯调参）代理模型，结合 NSGA-II 对面积比、喉嘴距、喉管长度、扩散角及动力液压力、吸入含气率协同优化：排液量由 42.05 m³/d 提升至 55.24 m³/d（+31.4%），泵效由 26.5% 提升至 30.5%。

{{< fig src="uploads/research/jetpump-cfd.jpg" alt="优化前后射流泵压力与速度云图" caption="优化前后射流泵内压力云图（左两幅）与速度云图（右两幅）：优化后喉管入口负压更低、射流核心速度更高，气液卷吸与混合增强" >}}

**工程应用。** 上述模型与优化方法已用于青海峁平 1 井等气井的射流泵排液工艺设计，并形成射流泵工况分析与参数优选计算程序，支持两相/三相计算、气阻校核和喷喉组合优选。

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（1 篇）</h4>
  <ol>
    <li><b>J Zhu</b>, A Li, Y Ji, J Peng, Y Zhang, H Zhu. <a href="https://doi.org/10.12034/j.issn.1009-606X.225156" target="_blank" rel="noopener">Optimization of gas-liquid two-phase flow characteristic parameters in a concentric dual-tube hydraulic jet pump</a>（同心双管水力射流泵气液两相流特征参数优化）. <i>The Chinese Journal of Process Engineering（过程工程学报）26 (3), 233-244</i>, 2026.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><a href="{{< u "research/plunger/" >}}">← 3. 柱塞气举瞬态建模与智能诊断</a><a href="{{< u "research/" >}}">研究方向总览</a><a href="{{< u "research/mfl/" >}}">5. 管道漏磁内检测缺陷智能识别 →</a></nav>
