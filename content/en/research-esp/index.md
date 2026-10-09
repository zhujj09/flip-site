---
title: "ESP Multiphase Boosting Mechanisms and Condition Diagnosis"
url: /en/research/esp/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 2</p>

When free gas enters an electrical submersible pump (ESP), boosting pressure degrades, then surges, and may end in gas lock. Traditional homogeneous-flow design applies only at very low gas fractions. The group studies the chain from bubble breakup and coalescence in the rotating impeller to in-situ gas void fraction, flow-pattern transition and boosting degradation, extending to high-viscosity, emulsion and sand-laden conditions.

{{< fig src="uploads/research/esp-surging-curves.jpg" alt="Boosting degradation and surging of an ESP under gassy conditions" caption="Boosting degradation and surging under gassy conditions: experiment vs. mechanistic model" >}}

**Experiments and mechanistic models.** On the TUALP multistage two-phase ESP loop (14-stage TE-2700 with stage-by-stage taps) and the CUP centrifugal-pump visualization rig, high-speed imaging captures impeller flow patterns and surge onset. Critical bubble diameter, in-situ gas fraction and flow-pattern boundaries are modeled; a “best-matching rate” concept supports unified boosting models for single-phase, viscous, emulsified and gas–liquid conditions, validated on three ESP types (typical error within ±20%, average ~10%).

{{< fig src="uploads/research/esp-tualp-loop.jpg" alt="TUALP multistage two-phase ESP loop" caption="TUALP multistage two-phase ESP loop: schematic and stage-by-stage pressure taps" >}}

{{< fig src="uploads/research/esp-impeller-highspeed.jpg" alt="High-speed imaging inside a rotating impeller" caption="High-speed imaging of gas–liquid flow in a rotating impeller: bubble migration and gas-pocket formation" >}}

**CFD.** Eulerian two-fluid CFD with interfacial forces captures multistage gas–liquid flow and cross-stage pattern evolution; dynamic mode decomposition extracts dominant impeller modes. An NSFC General Program project addresses deep-sea mixed-flow ESPs.

{{< fig src="uploads/research/esp-cfd-gas-isosurface.jpg" alt="In-situ gas void fraction isosurface in an ESP impeller" caption="CFD isosurface of in-situ gas fraction in a multistage ESP impeller" >}}

**Wide-range offshore ESP hydraulic design and automated CFD optimization.** For mid-to-late-life offshore wells with large rate swings and high gas fractions, the group designs wide-passage mixed-flow ESP impellers/diffusers (400/538 series): similarity scaling, Euler-head correction and specific-speed checks seed the base model; Python drives CFturbo–Workbench–PyFluent for geometry batching, mesh update, batch solve and surrogate-model search (Latin hypercube + Gaussian process). First-round sensitivity (Spearman) shows impeller exit width b₂ dominates BEP location (ρ≈0.74), cutting the design space from 10-D to 5-D.

{{< fig src="uploads/research/esp-wide-impeller-opt.jpg" alt="Wide-range ESP impeller/diffuser parametric model and CFD automation" caption="Parametric impeller/diffuser models and automated CFD optimization workflow" >}}

{{< fig src="uploads/research/esp-wide-sensitivity.jpg" alt="Impeller geometry sensitivity analysis" caption="Spearman sensitivity of impeller geometry on BEP and high-rate head" >}}

**Condition diagnosis.** Mechanistic boosting models are fused with machine learning into a real-time ESP management framework (condition recognition, fault diagnosis/early warning, remaining life), delivered as the “Intelligent ESP Management System V1.0” algorithm module.

<div class="flip-theme-pubs not-prose">
  <h4>Representative papers</h4>
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

<nav class="flip-theme-nav not-prose">
<a href="{{< u "en/research/wellbore/" >}}">← 1. Wellbore Multiphase Flow</a>
<a href="{{< u "en/research/" >}}">Research overview</a>
<a href="{{< u "en/research/plunger/" >}}">3. Plunger Lift →</a>
</nav>
