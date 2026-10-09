---
title: "Intelligent Defect Recognition in Pipeline MFL In-Line Inspection"
url: /en/research/mfl/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 5</p>

Magnetic flux leakage (MFL) in-line inspection is the main method for detecting corrosion and cracks in long-distance pipelines. One run produces massive signal data, while defect samples with excavation labels are scarce.

{{< fig src="uploads/research/mfl-cascade-framework.jpg" alt="Cascaded MFL defect detection framework" caption="Cascaded framework: MFL acquisition and augmentation, YOLOv5 localization, ViT classification" >}}

{{< fig src="uploads/research/mfl-pull-test.jpg" alt="MFL pull-test loop" caption="MFL pull-test loop used for labeled defect signals" >}}

With Prof. Jianli Wang's group at Southeast University, the group proposes cascaded deep learning: a pretrained YOLO network locates defects on MFL images, then a Vision Transformer or multi-input parallel CNN regresses defect length, width and depth. Diffusion models generate samples and reconstruct under-sampled signals.

<div class="flip-theme-pubs not-prose">
  <h4>Representative papers</h4>
  <ol>
    <li>J Xie, J Yang, K Fu, L Tai, X Wang, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100282" target="_blank" rel="noopener">Quantitative Assessment of Pipeline Defects Utilizing a Dual-Stage Deep Learning Framework: Integration of Pretrained YOLO Network and Multi-input Parallel Convolution …</a>. <i>Journal of Pipeline Science and Engineering, 100282</i>, 2025.</li>
    <li>J Yang, Y Zhang, C Su, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100382" target="_blank" rel="noopener">Multi-Priors Tensor Completion for Highly Under-sampled Magnetic Flux Leakage Signal Reconstruction</a>. <i>Journal of Pipeline Science and Engineering, 100382</i>, 2025.</li>
    <li>J Yang, J Xie, X Gao, K Fu, <b>J Zhu</b>, J Wang. <a href="https://doi.org/10.1016/j.jpse.2025.100363" target="_blank" rel="noopener">Synthetic Magnetic Flux Leakage Signal Generation Using Diffusion Models: A Novel Approach to Improve Pipeline Defect Detection Accuracy</a>. <i>Journal of Pipeline Science and Engineering, 100363</i>, 2025.</li>
    <li>X Chen, M Fu, X Liu, <b>J Zhu</b>. <a href="https://doi.org/10.1109/tim.2025.3602568" target="_blank" rel="noopener">Synthesizing Labeled Magnetic Flux Leakage Signals for Pipeline Integrity Assessment: A Generation and Evaluation Methodology</a>. <i>IEEE Transactions on Instrumentation and Measurement</i>, 2025.</li>
    <li>P Chen, R Li, K Fu, Z Zhong, J Xie, J Wang, <b>J Zhu</b>. <a href="https://doi.org/10.1016/j.ymssp.2023.110919" target="_blank" rel="noopener">A cascaded deep learning approach for detecting pipeline defects via pretrained YOLOv5 and ViT models based on MFL data</a>. <i>Mechanical Systems and Signal Processing 206, 110919</i>, 2024.</li>
  </ol>
</div>

<nav class="flip-theme-nav not-prose">
<a href="{{< u "en/research/jetpump/" >}}">← 4. Hydraulic Jet Pump</a>
<a href="{{< u "en/research/" >}}">Research overview</a>
<a href="{{< u "en/research/bigdata/" >}}">6. Big-Data Analytics →</a>
</nav>
