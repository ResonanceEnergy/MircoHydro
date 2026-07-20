# Powertrain Audit — Wheel & Generator Physics Check (Founder Challenge)

**Date:** 2026-07-19 · **Trigger:** founder: "the physics and engineering don't add up for flywheel and generator." · **Method:** every number re-derived from first principles; visualization checked against the numbers; discrepancies classified real-engineering vs viz-error.

## 1. The numbers, re-derived end to end (all check out)

| Step | Relation | Value | Check |
|---|---|---|---|
| Delivery (sim) | q | 1.819 L/s continuous | MOC run, energy-audited |
| Net head at nozzle | Hd − penstock loss | 8.98 m | Darcy, 0.2% loss |
| Jet velocity | Vj = 0.97·√(2g·H) | 12.88 m/s | ✓ |
| Jet area needed | A = q/Vj | 141.2 mm² | ✓ |
| Twin nozzles | 2 × ⌀9.5 mm | 141.7 mm² | **consistent to 0.4%** |
| PCD/d ratio | 150/9.5 | 15.8 | Turgo practice ≥6.5 — conservative ✓ |
| Wheel speed | u = 0.46·Vj → N = 60u/(πD) | 5.92 m/s → **754 rpm** | Turgo speed ratio 0.44–0.48 ✓ |
| Shaft torque | τ = P/ω | 113 W / 78.95 rad/s = **1.43 N·m** | ✓ |
| Jet force (Euler) | ΣF = ρq(Vj−u)(1−cos β₂), β₂=165° | 24.9 N → τ = 1.87 N·m ideal | ideal transfer 147 W vs 151 W jet power — 97% Euler ceiling; canon 0.75 incl. all losses is comfortably below ✓ |
| Electric | 151 × 0.75 × 0.85 × 0.92 | **88 W** | chain values canon; Bristol's measured 91% runner says 0.75 is conservative |

**Energy conservation holds at every stage.** No step creates or loses unaccounted power.

## 2. "Flywheel" — why this machine doesn't need one (founder question answered with numbers)

A flywheel smooths torque pulsation. Our torque is **steady by architecture**: the ram's ~0.9 Hz pulses are absorbed by the air chamber and then fully decoupled by the headstock (Finding 9 — minutes of residence time). The penstock feeds the nozzles at constant head, so jet force is constant, so wheel torque is constant (τ ripple ≈ 0, unlike diesel/single-piston prime movers). The runner's own inertia (~0.002 kg·m² for a 150 mm steel wheel) is irrelevant to power quality — the electrical side (MPPT + battery) handles the load side. **A flywheel would add cost and bearing load and buy nothing. The headstock IS the energy buffer — hydraulic, not rotational.** (A direct-coupled variant without headstock WOULD need one — Roberts 2019's 0.3–1.7% time-averaged direct conversion is what un-buffered pulsation costs.)

## 3. The genuine engineering gap the audit found: generator speed matching (NEW → PRD)

754 rpm is **below the 1,200–2,400 rpm band** the benchmark PMGs (Motenergy hydro line) are wound for. At 754 rpm an off-the-shelf ME-series may produce too little voltage to reach a 48 V MPPT window. Three honest options, decision needed at BOM freeze:

1. **Smaller wheel**: PCD 100 mm → 1,131 rpm (in-band). Costs PCD/d = 10.5 — still fine for Turgo. Cheapest fix.
2. **Winding/kV selection**: specify generator kV such that V_oc at 754 rpm lands in the MPPT input window (SRNE 250 V class gives wide headroom). Custom or selected axial-flux (their 50–300 rpm low-speed windings actually fit better — but partial-load curves unpublished; dyno first per COMPONENT_TECH_SCAN).
3. **Belt step-up** (2:1): adds losses (~3–5%) and a service item — against the appliance thesis; last resort.

**Action logged: REQ-P9 (PRD) — generator/wheel speed-match analysis at BOM freeze; default direction option 1 or 2, decided by dyno data.**

## 4. Visualization errors found by this audit (the render lied; the sim didn't)

1. **Jet geometry WRONG in the v3 powerhouse scene: jets approached the runner along its AXIS** (perpendicular to the plane of rotation — striking the disc face). A wheel fed axially receives ~zero tangential force and would not turn. Real Turgo jets enter close to the runner plane, aimed tangentially at the pitch circle with ~20° axial inclination. **Fixed: nozzles relocated beside the rim, jets re-aimed tangential-with-20°, impact point and spray moved to the pitch circle, exit water thrown to the tailrace side.**
2. **Wheel scale undisclosed**: model runner ≈370 mm vs the labeled 150 mm PCD. **Fixed: plate now reads "wheel model 2.5:1 for visibility."**
3. **Cup speed vs jet speed**: cups shown at 1/5–1/10 real speed next to full-speed jets — visually violates u ≈ 0.46·Vj. **Mitigation: label states the slow-motion factor; motion blur set so the speed *relationship* reads correctly at the chosen scale.** (Rendering the true 12.6 rev/s turns the runner into an unreadable blur disc — the label is the honest compromise.)

*The MOC sim data and all published numbers were never wrong — the 3D artist (me) was. Per canon: the render is an illustration of the numbers; where they disagreed, the numbers win and the render gets fixed.*

*Cross-refs: PHYSICS_PROOF_FULL_SYSTEM (chain numbers), Finding 9 (headstock smoothing), COMPONENT_TECH_SCAN §4 (PMG benchmarks, axial-flux caveat), PRD REQ-P9 (new).* 
