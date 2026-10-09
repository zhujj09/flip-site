---
title: "Plunger Lift Transient Modeling and Intelligent Diagnosis"
url: /en/research/plunger/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 3</p>

Plunger lift is the main intermittent deliquification method for gas wells, but plunger motion cannot be observed downhole and schedules are often set by experience.

{{< fig src="uploads/research/plunger-cycle.jpg" alt="Typical plunger-lift installation (left) and tubing pressure, casing pressure and rate over one lift cycle (right)" caption="Typical plunger-lift installation (left) and tubing pressure, casing pressure and rate over one lift cycle (right)" >}}

**Transient models.** OLGA well–plunger–controller–reservoir models are history-matched with field pressures, and an in-house full-cycle plunger dynamics model coupled with the unified multiphase flow model matches OLGA on the main operating parameters with about 90% accuracy. Using it as a digital well, open/shut-in schedules are optimized with SPSA and Bayesian optimization.

**Intelligent diagnosis.** CNN, ViT, VAE-based data augmentation and zero-shot CLIP-style models identify abnormal plunger-well conditions from tubing/casing pressure curves.

Representative publications are listed on the [Chinese page]({{< u "research/plunger/" >}}) and in [Outputs]({{< u "en/outputs/" >}}); see also [Google Scholar](https://scholar.google.com/citations?user=sfsM2TUAAAAJ&hl=en).
