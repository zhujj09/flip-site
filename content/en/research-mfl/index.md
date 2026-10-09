---
title: "Intelligent Defect Recognition in Pipeline MFL In-Line Inspection"
url: /en/research/mfl/
date: 2026-10-09
---

<p class="flip-crumb not-prose"><a href="{{< u "en/research/" >}}">Research</a> / Area 5</p>

Magnetic flux leakage (MFL) in-line inspection is the main method for detecting corrosion and cracks in long-distance pipelines. One run produces massive signal data, while defect samples with excavation labels are scarce.

{{< fig src="uploads/research/mfl-cascade-framework.jpg" alt="Cascaded framework: MFL signal acquisition and augmentation, YOLOv5 localization, ViT classification" caption="Cascaded framework: MFL signal acquisition and augmentation, YOLOv5 localization, ViT classification" >}}

With Prof. Jianli Wang's group at Southeast University, the group proposes cascaded deep learning: a pretrained YOLO network locates defects on MFL images, then a Vision Transformer or multi-input parallel CNN regresses defect length, width and depth. Diffusion models are used to generate samples and reconstruct under-sampled signals.

Representative publications are listed on the [Chinese page]({{< u "research/mfl/" >}}) and in [Outputs]({{< u "en/outputs/" >}}); see also [Google Scholar](https://scholar.google.com/citations?user=sfsM2TUAAAAJ&hl=en).
