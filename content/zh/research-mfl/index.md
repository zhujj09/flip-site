---
title: "管道漏磁内检测缺陷智能识别"
url: /research/mfl/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "research/" >}}">研究方向</a> / 方向 5</p>

漏磁（MFL）内检测是油气长输管道腐蚀、裂纹等缺陷检测的主要手段：检测器磁化管壁，缺陷处磁力线外泄，传感器阵列记录三轴漏磁信号。一次内检测产生海量信号，人工判读费时且依赖经验，而带真实开挖标签的缺陷样本又很少。

**缺陷识别与量化。** 与东南大学王建立教授合作，课题组提出级联深度学习方法：先用预训练 YOLO 网络在漏磁信号图上定位缺陷，再用 Vision Transformer 或多输入并行卷积网络回归缺陷长、宽、深，实现检测与量化一体化。

{{< fig src="uploads/research/mfl-cascade-framework.jpg" alt="YOLOv5 与 ViT 级联的漏磁缺陷检测框架" caption="级联深度学习框架：漏磁信号采集与扩增、YOLOv5 快速定位缺陷、ViT 精细分类" >}}

**样本生成与信号重建。** 针对标签样本稀缺，用扩散模型和生成模型合成带标签的漏磁缺陷信号，并建立合成信号质量评价方法，用合成数据提升缺陷检测精度；针对检测器高速运行或通道失效造成的欠采样，提出多先验张量补全方法重建漏磁信号。

{{< fig src="uploads/research/mfl-pull-test.jpg" alt="漏磁内检测牵拉试验管段与人工缺陷" caption="漏磁内检测牵拉试验：试验管段布置、人工缺陷与检测器" >}}

<div class="flip-theme-pubs not-prose">
  <h4>代表性论文（5 篇）</h4>
  <ol>
    <li>J Xie, J Yang, K Fu, L Tai, X Wang, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100282" target="_blank" rel="noopener">Quantitative Assessment of Pipeline Defects Utilizing a Dual-Stage Deep Learning Framework: Integration of Pretrained YOLO Network and Multi-input Parallel Convolution …</a>. <i>Journal of Pipeline Science and Engineering, 100282</i>, 2025.</li>
    <li>J Yang, Y Zhang, C Su, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100382" target="_blank" rel="noopener">Multi-Priors Tensor Completion for Highly Under-sampled Magnetic Flux Leakage Signal Reconstruction</a>. <i>Journal of Pipeline Science and Engineering, 100382</i>, 2025.</li>
    <li>J Yang, J Xie, X Gao, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100363" target="_blank" rel="noopener">Synthetic Magnetic Flux Leakage Signal Generation Using Diffusion Models: A Novel Approach to Improve Pipeline Defect Detection Accuracy</a>. <i>Journal of Pipeline Science and Engineering, 100363</i>, 2025.</li>
    <li>X Chen, M Fu, X Liu, <b>J Zhu</b>. <a href="https://doi.org/10.1109/tim.2025.3602568" target="_blank" rel="noopener">Synthesizing Labeled Magnetic Flux Leakage Signals for Pipeline Integrity Assessment: A Generation and Evaluation Methodology</a>. <i>IEEE Transactions on Instrumentation and Measurement</i>, 2025.</li>
    <li>P Chen, R Li, K Fu, Z Zhong, J Xie, J Wang, <b>J Zhu</b>. <a href="https://doi.org/10.1016/j.ymssp.2023.110919" target="_blank" rel="noopener">A cascaded deep learning approach for detecting pipeline defects via pretrained YOLOv5 and ViT models based on MFL data</a>. <i>Mechanical Systems and Signal Processing 206, 110919</i>, 2024.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose"><a href="{{< u "research/jetpump/" >}}">← 4. 水力射流泵排水采气机理与优化</a><a href="{{< u "research/" >}}">研究方向总览</a><a href="{{< u "research/bigdata/" >}}">6. 油气田大数据分析 →</a></nav>
