# Control Strategies for Smoothing and Blending Material Streams

Simulation code to replicate the results presented in:

> **Control Strategies for Smoothing and Blending Material Streams**  
> Bill Tubbs, Spartan Controls, Canada  
> CIM COM 2026, Paper 26312

## Abstract

One of the biggest challenges facing mineral processing plants is the high variability
in mined ore properties such as hardness, particle size, and composition. Technology to
measure these properties online is still limited. Even when imperfect measurements exist
(e.g. online particle size or grade analysers), not all operations have the flexibility to
mix, divert or blend ore streams to try to reduce the variations. However, when this is
the case, the question arises: what strategies exist to control and smooth variations in a
way that reduces the impact on the processing plant, and how should these be evaluated?

This paper highlights two fundamental methods of dealing with disturbances—buffer tanks
and ratio control—and draws attention to existing academic literature on these topics.
Using numerical simulations, it illustrates the main properties, benefits, and limitations
of each, including how system design, physical constraints, and measurement inaccuracy
limit the ability to reject or attenuate disturbances in ore properties.

**Keywords:** Ore Blending, Variability, Buffer Tanks, Ratio Control

## Contents

### [`buffer-tanks.ipynb`](buffer-tanks.ipynb) — Section 2: Buffer Tanks

Develops the theory and simulations for buffer (mixed) tanks used to smooth disturbances
in feed stream properties.

- **Model** — transfer function for a single buffer tank and tanks in series; frequency
  response analysis (§2.3)
- **Mixed Tank Example** — worked example of a single mixed tank
- **Smoothing Quality Disturbances** — smoothing composition variations using a buffer
  tank (§2.2)
- **Mixed Tank Simulation** — simulation with bounded random walk disturbances
- **Smoothing Flow Rate Disturbances** — surge tank model for smoothing flow rate
  variations (§2.1)
- **Surge Tank Simulation** — simulation with bounded random walk disturbances
- **Design and Sizing** — frequency response and sizing considerations (§2.4)
- **Demonstration: Simulating a First Order System in Discrete Time Intervals** —
  discrete-time simulation of a first-order system, illustrating buffer tank dynamics
  (§2.3)

### [`blending.ipynb`](blending.ipynb) — Section 3: Blending

Develops and simulates a ratio control strategy for blending two feed streams to maintain
a target outlet composition.

- **Generate Bounded Random Walk (BRW) Sequences** — generates stochastic feed
  concentration disturbances
- **Construct Mixer and Tank Dynamic System** — builds the CasADi state-space model of
  the mixer and downstream tank
- **Simulate with For Loop** — open-loop simulation showing uncontrolled composition
  variation
- **Ratio Control** — closed-loop PI ratio controller simulation illustrating disturbance
  rejection (§3)

## Setup

Requires Python 3.10 or later. To create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
```

Then select the `.venv` kernel in VS Code or Jupyter to run the notebooks.
