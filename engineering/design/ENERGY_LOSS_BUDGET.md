# Energy Loss Budget — Every Loss Point, Quantified, With What's Recoverable

**Date:** 2026-07-19 · **Founder directive:** "jet entry, angle, wheel design all critical — find ALL energy loss points or places we can conserve for max output." · **Baseline:** tuned knee operating point (Finding 6), 218 W of river water entering one 300 mm ram. All ram-side numbers from fresh sim runs today; downstream from audited chain arithmetic.

## The waterfall — where every watt goes (per ram, r = 6 site)

| Stage | In → Out | Lost | % of stage | Mechanism | Recoverable? |
|---|---|---|---|---|---|
| River → ram (drive water) | 218 W → 160.5 W | **57.5 W** | 26% | valve slam + junction dissipation (dominant), waste-flow exit KE, pipe friction (minor) | partially — see levers 1, 8 |
| Rise pipe → headstock | 160.5 → 160.5 | ~1 W in throttle margin | 0.6% | linear throttling h_ch−Hd | +1.1 W with DN100 rise pipe (sim-verified today) |
| Penstock | 160.5 → 160.2 | 0.3 W | 0.2% | Darcy friction | already optimal — **smooth wall wins; a fluted bore multiplies this ×1.6–2.7 (D-6 test decides on jet-quality grounds, not friction — friction says smooth)** |
| Nozzle | 160.2 → 150.8 | **9.5 W** | 5.9% | Cv = 0.97 (contraction, wall friction) | lever 3: ~3–5 W |
| **Jet → runner** | 150.8 → 113.1 | **37.7 W** | **25%** | cup hydraulic loss, exit whirl, windage, splash-back | **lever 2 — the single biggest recoverable block: 15–24 W** |
| Shaft (direct drive) | 113.1 → 113.1 | ~0 | 0% | no belt, no gearbox | design already right — protect it (REQ-P9 option 3 would break this) |
| Generator (PMA 0.85) | 113.1 → 96.1 | **17.0 W** | 15% | copper + iron + mismatch | lever 4: ~6–8 W |
| MPPT/electronics (0.92) | 96.1 → 88.4 | **7.7 W** | 8% | conversion | lever 5: ~5–6 W |
| **Electric out** | **88.4 W** | | | | |

**Checksum:** 218 = 88.4 + 57.5 + 1 + 0.3 + 9.5 + 37.7 + 17.0 + 7.7 (−0.7 rounding). Books close.

## The levers, ranked by watts per dollar

1. **Runner quality (0.75 → 0.85 measured-grade, 0.91 ceiling): +15 to +24 W.** The biggest block on the table. Bristol measured 91% jet-to-mechanical on exactly our class of low-head Turgo — our canon 0.75 is the *cheap-wheel* number. What buys it: cup geometry fidelity (cast or high-res printed, not bent sheet), surface finish inside the cups, correct cup count/angle, minimal exit whirl. This is a make/buy decision, not physics risk.
2. **Speed-ratio discipline (u/Vj = 0.46 held by MPPT): protects lever 1.** Error is quadratic: 10% off-speed costs ~1–2%, 25% off costs ~9%. The MPPT's load curve must be programmed to hold the wheel at 0.46·Vj across seasonal head — this is firmware, nearly free, and REQ-P9's kV matching is its prerequisite.
3. **Nozzle Cv (0.97 → 0.98–0.985): +3 to +5 W.** Polished convergent taper, straight approach run ≥3×bore (already adopted from tech scan), honeycomb conditioning (D-6 arm). Cheap machining.
4. **Generator matching (REQ-P9): +6 to +8 W.** A quality PMG at its *matched* operating point runs 0.90+; an off-band one runs 0.80 or worse. kV selection or 100 mm PCD — decided by dyno.
5. **Modern MPPT (0.92 → 0.96–0.97): +5 to +6 W.** Current-generation converters bench at 97%+; our 0.92 is a conservative legacy number. Component selection, no design work.
6. **Rise pipe DN100: +1.1 W** (sim-verified). Bigger than DN100 BREAKS the cycle (sim: DN125-class conductance collapses delivery 34% — the throttle is part of the machine's dynamics). Small, cheap, bounded.
7. **Ram valve tuning within the water budget: up to +6%** system-wide (η 0.736 → 0.78 at lighter valve where site water allows — Finding 5/6 trade), and **the self-tuning servo holding the knee against seasonal drift is worth more than every hardware lever above in field terms** (Finding 8: drifted fixed valve = −30%).
8. **Valve-event dissipation (inside the 57.5 W ram block): research, not retrofit.** The slam/bounce loss is the ram's working principle doing its job, but the Finding-8 chatter observation says some of it is *bounce*, not work. Valve bounce control (elastomer seat, damped stem) is a model-v2 + bench question. Flagged, unpromised.

## Negative findings — money NOT to spend (sim-verified today)

- **Bellmouth intake: +0.4 W.** Not worth a casting. Standard entrance is fine.
- **Smoother drive pipe (f 0.022→0.016): +0.3 W.** Ordinary steel is fine; the pipe is not where the ram loses.
- **Oversized rise pipe: NEGATIVE.** DN125-class conductance collapses output 34% — the delivery throttle is load-matching the chamber; leave it engineered, not maximized.
- **Fluting for friction: negative on this table** (×1.6–2.7 on an admittedly tiny 0.3 W). D-6's jet-quality question remains open and is the only way the flute earns its place — the CoV test decides.

## Jet entry & wheel geometry — why the founder is right that it's critical

Misalignment loss goes as ~cos²(error): 5° costs 0.8% (1.2 W), 10° costs 3% (4.5 W), and **axial entry (what the render wrongly showed) costs ~100% — the wheel doesn't turn.** The design's requirements, now written as spec: jets enter in the runner plane ±20–25° axial inclination, tangent to the pitch circle, twin jets separated ≥25° circumferentially (ours: 23°→ widened to 25° in the corrected scene), housing clearance sized so discharged water exits without re-striking cups (splash-back/windage costs 2–5% in bad housings — REQ addition for the housing drawing), discharge path falls clear to the tailrace.

**Manifold approach spec (founder catch — the render's "hook" was a violation):** the penstock-to-nozzle run makes **ONE wide-radius sweep** (bend radius ≥5× bore), then a **dead-straight header aligned with the jet axis, ≥3× bore (built: ~8×) before N1**; N2 takes off at a **shallow-angle wye (≤30°), never a right-angle tee**, with its own straight run before its nozzle; the isolation valve sits on the N2 branch, upstream of that straight run (a part-open valve directly before a nozzle is a jet-quality killer). Every elbow within a few diameters of a nozzle disturbs the velocity profile the nozzle is supposed to perfect — this is the same physics as the D-6 straight-run/honeycomb rule. Hydraulic cost of a bad hook: 2–4 minor-loss coefficients (~0.5–1 W here) plus an unquantified-but-larger jet CoV penalty at the wheel.

## The honest max-output stack (same water, same site)

| Build | Chain | Electric out |
|---|---|---|
| Today's baseline | 160.5 × 0.998 × 0.941 × 0.75 × 0.85 × 0.92 | **88 W** |
| **Buildable now** (levers 3,4,5,6: Cv .98, runner .85, PMG .90, MPPT .965) | 161.6 × 0.998 × 0.960 × 0.85 × 0.90 × 0.965 | **≈114 W (+29%)** |
| Stretch (runner .91, Cv .985, MPPT .98) | | **≈125 W (+41%)** |
| + ram tuned to 0.78 where water allows | | **≈133 W (+50%)** |

Per 6-ram bank: baseline 530 W → buildable ≈ **685 W** → stretch ≈ **750–800 W**. All numbers remain sim-anchored and carry the calibration caveat until bench; the *ratios* are the deliverable per canon.

*Cross-refs: POWERTRAIN_AUDIT (chain verification), SIM_RESULTS Findings 5–9, COMPONENT_TECH_SCAN §4 (runner/PMG/MPPT benchmarks), PRD REQ-P9 + housing-clearance addition, D-6 (flute decided by CoV, not friction).* 
