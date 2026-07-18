# IP Disclosure Frame — Post-Tech-Scan Reframe (Ratified)

**Date:** 2026-07-18 · **Authority:** Founder ratification ("yes") following COMPONENT_TECH_SCAN prior-art findings. Supersedes the three-item disclosure list in RAM_RESONANCE_RESEARCH §6 where they conflict.

## Prior art that constrains us (the honest map)

| Prior art | What it covers | Status | Effect on us |
|---|---|---|---|
| [CN107228042B](https://patents.google.com/patent/CN107228042B/en) (IWHR 2017) | waves→rams→elevated tank→turbine→generator, incl. rams-per-output formula | **EXPIRED 2024** | blocks broad claims on the base ram→tank→turbine architecture; **grants us freedom to operate** |
| [CN116802400A](https://patents.google.com/patent/CN116802400A/en) (HydroHammer, priority 2020-12) | stepper-driven variable valve aperture, magnetic valve sensing, EM opening assist, remote start/stop/throttle | **PENDING** | forecloses generic "electronically controlled ram" claims; does NOT claim cycle-timing control |
| [CN212675388U](https://patents.google.com/patent/CN212675388U/en) (Jianghan U. 2020) | IoT-monitored ram (sensors, cloud, health diagnosis) | **EXPIRED** | monitoring-only claims foreclosed AND free to use |
| [US6206041](https://patents.google.com/patent/US6206041) (Papa/Selwyn) | springless elastomer venturi waste valve | **EXPIRED** | free design element |
| [US9518595B2](https://patents.google.com/patent/US9518595B2/en) (WPT) | convolute "pressure matrix" virtually extending drive-pipe length | **EXPIRED** | free design element — drive-pipe sweep variant |
| EP2722575B1 (WPT) | gas-spring accumulator replacing air chamber | granted | avoid; commodity CRN bladder vessel sidesteps it |
| Zenodo [10.5281/zenodo.18318909](https://doi.org/10.5281/zenodo.18318909) (2026 preprint) | "resonance-tuned" ram framing, passive self-locking | unreviewed | read before filing; date-stamps our independent work now |

## The three disclosures we draft (narrowed to verified-open ground)

**Disclosure 1 — Coupled ram-bank→headstock→jet operating-point method.** The sizing/coupling mathematics (MOC transient model + junction solve + fixed-head delivery + bank scaling) as a *method* for designing generation systems. The expired IWHR patent covered the plumbing, not the solver. Status: method exists and runs (`ram_moc_sim.py`); needs dating and witnessing.

**Disclosure 2 — Self-tuning phase-locked ram (NARROWED).** Claims restricted to what search verified as unoccupied: (a) **per-cycle closure-timing control holding Young's zero-recoil condition** — valve cycle phase-locked to the pipe's 2L/a reflection schedule via pressure-wave sensing (HydroHammer throttles aperture; nobody times the cycle); (b) **multi-ram phase coordination** — anti-synchronized banks smoothing headstock inflow (zero publications); (c) **generation-optimized control** — tuning target driven by turbine/electrical demand rather than water delivery (zero publications). The magnetic-repulsion valve return (Chen 2025, published) is prior art as a *component* but its use as the *actuator of a phase-locked controller* is not.

**Disclosure 3 — Tesla-valve auxiliary functions in ram service.** Unchanged (combination still unpublished): check-valve snifter duty and delivery-line transient damping in a ~1 Hz pulsed-flow machine.

## Standing rules

- Zero-recoil sim evidence (the sweep hunting the phase-lock point) is the technical exhibit for Disclosure 2 — the sim run IS the reduction-to-practice narrative until the physical rig exists.
- Nothing is filed on extrapolation: each disclosure waits for its sim/bench evidence per canon.
- Freedom-to-operate note: expired CN107228042B is our shield on the architecture itself; keep a dated copy in the repo record.

*Cross-refs: RAM_RESONANCE_RESEARCH §2/§6, COMPONENT_TECH_SCAN §1/§5, PRD P1-10 (disclosure task), D-6/D-7 (CoV instrumentation shared with evidence program).*
