---
aliases:
  - /platforms/
title: "Facilities"
date: 2026-10-09
---

The group's experiments rely on the in-house centrifugal-pump gas–liquid visualization rig at China University of Petroleum (Beijing) and on the TUALP multistage ESP loop used by the PI at The University of Tulsa. A multistage pump visualization platform is being planned and built. Numerical simulation and model training run on the group's two high-performance computing servers.

## Computing resources {#computing}

The group operates two servers of its own, used for full-scale 3-D transient CFD of ESPs, wellbore multiphase-flow computation, and training of deep neural networks such as PINNs.

| | Dual EPYC 9965 CPU–GPU server (2025) | Dual EPYC 7742 compute server |
|---|---|---|
| CPU | 2 × AMD EPYC 9965, 384 physical cores in total | 2 × AMD EPYC 7742, 128 cores / 256 threads |
| Memory | 1 TB DDR5 (16 × 64 GB) | 256 GB |
| GPU | 2 × NVIDIA RTX 5090 (32 GB) | 2 × NVIDIA RTX 4090 (24 GB), added in 2023 |
| Storage | about 20 TB | — |
| Main use | Large-scale parallel CFD, multiphysics coupling, PINN training | CFD simulation, deep-learning model training |

The dual EPYC 9965 server was accepted in June 2025 and is installed in Room B914 of the Main Building. It uses a Gigabyte MZ73-LM2 motherboard with liquid-cooled CPUs, and together with two RTX 5090 cards forms a CPU–GPU heterogeneous computing environment.

<div class="flip-figs flip-figs--computing">
{{< fig src="uploads/platforms/server-epyc9965-inside.jpg" alt="Dual EPYC 9965 server internals" caption="Internals: liquid-cooled dual EPYC CPUs, 16 DIMMs and RTX 5090 GPU" >}}
{{< fig src="uploads/platforms/server-epyc9965-chassis.jpg" alt="Dual EPYC 9965 server, closed chassis" caption="Dual EPYC 9965 CPU–GPU server (closed chassis)" >}}
</div>

## Centrifugal pump gas–liquid visualization rig (CUP) {#cup-rig}

Rebuilt from a centrifugal-pump hydraulic test bench (supported by NSFC Young Scientists Fund 52004304), the rig is used to test the boosting performance of ultra-low specific-speed centrifugal pumps at high water cut and high gas–liquid ratio, and to film the full flow passage of the rotating impeller at high speed. Main instruments include a PHANTOM V1212 high-speed motion analysis system, 8530B-200 high-frequency pressure transducers, 8530C-50 high-frequency differential-pressure transducers and a multichannel data acquisition system. Visualization has identified dispersed-bubble, bubbly, gas-pocket and segregated flow inside the impeller. Since 2025 the rig has been upgraded under an NSFC General Program grant: temperature control from 0 to 60 °C (±0.5 °C) and 5000 fps high-speed imaging.

{{< fig src="uploads/platforms/cup-esp-gas-rig.jpg" alt="Centrifugal pump test rig for high water cut and high gas–liquid ratio" caption="Centrifugal pump test rig for high water cut and high gas–liquid ratio: flow loop, layout and main instruments, with boosting curves at different gas fractions" >}}

{{< fig src="uploads/platforms/cup-impeller-visual.jpg" alt="Visualization equipment for the rotating impeller passage" caption="Visualization of the rotating impeller passage: high-speed camera, sensors and key specifications, with dispersed-bubble, bubbly and intermittent flow in the impeller" >}}

## Labyrinth pump tests under high viscosity and gas entrainment {#labyrinth}

A labyrinth screw pump test rig is used to measure labyrinth pump performance with viscous and gassy fluids. The system includes a gas tank, a two-phase separator, a torque sensor, a variable-frequency drive and a data acquisition system; head–flow curves have been measured at different speeds and viscosities.

{{< fig src="uploads/platforms/cup-labyrinth-pump.jpg" alt="Labyrinth pump tests under high viscosity and gas entrainment" caption="Labyrinth pump tests under high viscosity and gas entrainment: rotor and stator, test-rig flow loop, and head–flow curves at different speeds and viscosities" >}}

## TUALP multistage ESP two-phase loop (The University of Tulsa) {#tualp}

<span class="flip-tag flip-tag--ext">University of Tulsa facility</span>

This loop belongs to Tulsa University Artificial Lift Projects (TUALP) and is **not** a facility of this group. The PI, Jianjun Zhu, used it for ESP gas–liquid experiments during his Ph.D. study and work as a research associate at The University of Tulsa (2012–2019).

Main specifications: a 14-stage radial TE-2700 ESP (538 series) with stage-by-stage pressure taps; a 7.62 cm closed two-phase loop with a 24 m³ separator at 345/689/1034 kPa; speed 1800–3500 rpm; tap water and compressed air as working fluids, with optional IPA surfactant injection. The loop supports two-phase, high-viscosity, emulsion and sand-laden tests.

<div class="flip-figs">
{{< fig src="uploads/platforms/tualp-esp-loop-schematic.jpg" alt="TUALP two-phase ESP loop schematic" caption="TUALP two-phase ESP loop schematic" >}}
{{< fig src="uploads/platforms/tualp-esp-loop-photos.jpg" alt="TUALP ESP test piping and test pump" caption="TUALP test piping, 14-stage test pump and stage-by-stage pressure taps" >}}
</div>

## Multistage pump impeller/diffuser multiphase visualization platform {#multistage}

<span class="flip-tag flip-tag--plan">Under construction / planned</span>

This platform is at the planning and construction stage and **has not been built yet**. It is led by Jianjun Zhu, with a construction period from October 2025 to September 2028. The figures below are design targets from the feasibility report, not measured performance.

- Three-stage impeller–diffuser train, switchable between 1 and 3 stages, with diffuser outlet angle adjustable by ±5°; transparent passages and quartz-glass windows.
- 4K high-speed imaging (1000 fps at full frame) and PIV to measure transient velocity fields and identify vortex structures.
- Gas–liquid and solid–liquid transport: gas fraction ≤15%, particle size ≤1 mm, solid concentration ≤5%.
- 16-channel synchronized acquisition at 10 kHz; interlocked shutdown within 0.1 s when vibration or displacement exceeds limits.
- Permanent-magnet synchronous motor with vector frequency control, 0–6000 rpm; flow 0–30 m³/h, pressure 0.6–3.0 MPa.

{{< fig src="uploads/platforms/multistage-pump-visual-planned.jpg" alt="Multistage pump visualization platform (planned)" caption="Platform concept (planned design, not a photo of built equipment)" >}}
