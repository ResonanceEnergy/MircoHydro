# Digital Bench Results — Ram MOC Simulator v1

**Date:** 2026-07-18 · **Tool:** `tools/design/ram_moc_sim.py` (method of characteristics, dynamic valves, air chamber, fixed-head headstock delivery per ratified architecture) · **Resolves:** decision D-5 (supersedes the fitted η curve) · **Runs:** D-4's Gen 0 metrics (T-001 jet variation, T-002 PSD peakiness) computed on every run.

## Model & calibration (stated plainly)

Physics from first principles: elastic water-hammer in the steel drive pipe (computed wave speed 1,173 m/s), entrance loss, waste-valve disc dynamics (weight vs flow-drag), check valve, polytropic air cushion, rise-pipe delivery to the fixed headstock head. **One calibration constant** — a junction dissipation lump `Kj` (valve-slam + unsteady friction) — anchored to the repo's own USAID commercial datum: **η = 0.667 at r = 6 with Kj = 125** (calibrated 2026-07-18). Everything else is geometry and physics.

## Results at the reference configuration (F = 1.5 m, 300 mm × 45 m steel drive pipe, headstock +9 m)

| Quantity | Simulated |
|---|---|
| Cycle frequency | 0.50 Hz |
| Drive flow swallowed | **17.6 L/s** |
| Delivery to headstock | 1.95 L/s |
| D'Aubuisson efficiency | 0.667 (anchored) |
| Chamber pressure ripple | ~12% |

## Finding 1 — the big design correction: one ram does NOT swallow 100 L/s

The fitted-era Machine B numbers assumed the site's 100 L/s drive flow passes through one ram. The transient model shows the pipe-and-valve dynamics of a 300 mm ram at 1.5 m fall swallow **~18 L/s** — consistent with real manufacturer tables for 12"-class rams (Blake/Rife: roughly 7–15 L/s). Column acceleration under 1.5 m of head over a 45 m pipe simply takes ~2 s per cycle; duty cycle caps the appetite.

**Consequences (honest restatement):**
- **Per-ram output at B-Standard conditions: ~172 W hydraulic at the jet → ≈ 100–120 W electric** — not 556 W.
- The 556 W-class site output requires a **ram bank: 5–6 parallel 300 mm rams** on a manifold (the "B-Max dual-ram" concept generalizes to banking as the standard scaling method). Modularity was already the plan; the sim says it starts earlier than we priced.
- Cost per watt worsens accordingly at small falls; SKU economics must be re-run with per-ram banking (queued: solver update to ingest sim-derived per-ram curves).
- A drive-pipe **length study is now open**: the L/D ≥ 150 rule forces long pipes → slow cycles → low appetite. Literature also supports L ≈ 5–10× fall (much shorter). The sim can sweep this trade directly — potentially several× more flow per ram. **This is the highest-value next simulation.**

## Finding 2 — the η(r) curve: anchored at the operating point, flat at high r (known limitation)

Sweep (Kj = 125): η_sim ≈ 0.62–0.70 across r = 4–20, versus published field behavior declining to ~0.3 by r = 20. The v1 model under-represents high-r losses (mechanism identified: waste-valve reopen leakage during recoil — the reflected wave's energy is recovered elastically in the model but partially dumped in real rams). **Design ruling:** the conservative envelope applies — **η_design(r) = min(η_sim, published-decline curve)**; since every ratified SKU operates at r ≤ 9 (B-Standard r = 6), the divergence barely touches the product envelope, and the sim is anchored exactly where we operate. Model v2 backlog: valve-reopen leakage term; then re-calibrate against the physical bench (the ±10% gate remains supreme).

## Finding 3 — Gen 0 metrics live again (D-4 delivered)

Every run now outputs **T-002 PSD peakiness** (0.2–20 Hz band, delivery pressure) and **T-001 jet-variation** (coefficient of variation of delivery flow). First data: the 60 L air chamber leaves delivery strongly pulsed between strokes (T-001 CoV > 1 at low chamber margin) — **the chamber and rise-pipe conductance need sizing up for jet-quality duty**; the founder's original coherence metric is now the design driver for exactly that sizing. The January 2026 test program is, at last, producing numbers.

## Finding 4 — drive-pipe length sweep (sim queue #1, run 2026-07-18): the L/D window reproduced, and the optimum is SHORTER than the literature target

Sweep L/D = 50…1000 at both scales (data: `engineering/data/sweep_drive_pipe_LD.csv`; grid held at dx ≈ 2–3 m, convergence verified n = 16→64 at both scales, η stable to <1%).

- **L/D = 50 kills the ram at both scales** — the machine cannot sustain a limit cycle on a short pipe. The literature's lower window edge (~100–150) falls out of our transient physics independently; nothing was tuned to make this happen.
- **The pico surprise: at 100 mm × L/D 150 (the TWO_MODEL site), the DEFAULT valve never establishes a cycle at all** (one stroke, then flutter — η ≈ 0.12 residual). The tuned valve (8 mm stroke, matched weight) runs fine there (η = 0.636, matching the two-model result). **Valve tuning and pipe length interact: the self-sustaining (weight × stroke) window NARROWS as L/D drops.** At L/D 250 the same default-ish settings work and the window is wide. Field translation: short-pipe installs are commissioning-critical; longer pipe is forgiving. This is a second, independent value case for the self-tuning module — it doesn't just hold peak, it keeps marginal installs alive.
- **Tuned optimum sits at L/D ≈ 100–250, NOT the literature's ~500.** Best tuned points: η = 0.754 (300 mm, L/D 100), 0.761 (L/D 250), 0.780 (100 mm, L/D 250) — vs 0.715 at L/D 500 where 150 m of wall friction eats the gain and delivery drops (q 1.67→1.41 L/s). Caveat stated: Kj was calibrated at one point (L = 45 m, untuned, η = 0.667); the *trend* is the deliverable; absolutes carry extra uncertainty away from the anchor until model v2 re-anchors. But the practical implication is large either way: **30–75 m of steel drive pipe beats 150 m — better AND much cheaper.** BOM effect: drive pipe is a top-3 cost item; the spec shortens.

## Finding 5 — the valve weight is a WATER-APPETITE knob at nearly constant delivery

Weight sweep at fixed site (300 mm, r = 6, L/D 100–250):

| Wf | η | Q swallowed | q delivered |
|---|---|---|---|
| 0.5 | 0.75–0.76 | 13–14 L/s | 1.7–1.8 L/s |
| 1.0 | 0.61–0.67 | 16–19 L/s | 1.8–1.96 L/s |
| 1.5 | 0.49–0.51 | 23 L/s | 1.9 L/s |
| 2.0 | 0.27–0.35 | 28–30 L/s | 1.4–1.6 L/s |

Delivered water stays in a narrow band (~1.4–2.0 L/s) while drive-water consumption varies **2.3×** and η varies **2.8×**. The weight knob doesn't primarily buy output — it buys *water efficiency*. Consequences:

- **Per-ram delivered power is hard-capped ≈ 170 W hydraulic (~2 L/s to +9 m) at this site across the entire tuning map.** Finding 1's ram-bank conclusion is now robust to tuning — banks are THE scaling route, full stop.
- Heavy tune approaches Kesharwani's measured 40–50 L/s large-ram field ceiling from below — the model sits consistently inside measured reality.
- Site logic: water-limited sites tune light (η 0.75+); water-rich sites gain nothing per-ram by tuning heavy — they just waste less-scarce water. The commissioning card (queue #2) becomes a *site-water-budget* card.
- The untuned flat-η ≈ 0.667 envelope of Finding 2 was a mid-window artifact; the tuned machine reaches the high end of the measured lab band (0.70-class) in-model. Public numbers remain frozen until model v2 + bench correlation per canon.

## Finding 6 — zero-recoil hunt (sim queue #3, run 2026-07-18): both predictions failed as stated, and what survived is more useful

New instrument: `recoil_mismatch` = |water-column flow at valve-reopen| / mean drive flow (0 = Young's zero-recoil condition, measured mid-pipe). Grid: 7 weights × 3 strokes at B300, L/D 100 (data: `engineering/data/tuning_map_zero_recoil.csv`; 17/21 points sustain cycling).

**P1 (Young: η peak coincides with zero recoil) — REFUTED as a global correlation** (Spearman +0.19, predicted strongly negative). The η peak (0.797 at the lightest working valve) carries recoil 0.249; the min-recoil point (0.034) sits at η = 0.747. Mechanism visible in the data: an ever-lighter valve keeps raising η by wasting less water per cycle — but it *starves* the machine (Q 8.2 L/s, delivery collapses to 1.09 L/s). Efficiency alone rewards starvation; Young's condition doesn't chase it.

**What survived is better than the prediction:**
1. **The min-recoil point lands at the knee of the trade-off** — η = 0.747 (94% of peak) at essentially full delivery (1.83 vs max 2.04 L/s → 161 W vs the η-peak's 96 W). Ranked by delivered power at high efficiency, min-recoil is arguably the best *operating* point on the grid.
2. **Recoil separates alive from dead sharply**: every non-cycling flutter state shows recoil > 1.4; every live state < 0.25. It's a binary health signal plus a continuous tuning signal in one number.
3. **And it is sensor-measurable per cycle** (one pressure/flow transducer), unlike η (needs calibrated flow measurement on two legs). **A controller that servos to minimum recoil lands within ~6% of peak η at full delivery, detects stall instantly, and needs one cheap sensor.** This upgrades the self-tuning module from "holds a mapped setpoint" to "closed-loop on a physically meaningful target" — the strongest technical exhibit yet for IP Disclosure 2 (which claims exactly this loop).

**P2 (founder: coherence peak coincides with η peak) — INCONCLUSIVE, metric's fault.** T-002 as implemented (single DFT peak/median) scatters over two orders of magnitude across neighboring grid points — too fragile to answer the question. Not refuted, not confirmed. Fix queued: Welch-averaged PSD over per-cycle windows, then re-ask.

**Tuning-map deliverables also banked** (same grid): stroke-weight pairing reproduced (light weights need short strokes — 15/25 mm strokes die under light weights, exactly the literature's "each weight has its own optimal stroke"); the site-water-budget card now has its data table (appetite 8→24 L/s vs η 0.80→0.48 at near-constant ~2 L/s delivery).

## Finding 7 — T-002 v2 (Welch) answers P2: coherence is a HEALTH signal, not an optimizer

The reworked metric (Hann-windowed, 50%-overlap Welch-averaged PSD, peak/median in dB) is stable where v1 scattered over two orders of magnitude. Verdict on the founding prediction ("coherence peak coincides with efficiency peak"): **in-model, there is no coherence peak to coincide with.** Every live operating point sits in a tight 39–43 dB band regardless of tuning (η 0.48–0.80 across those same points); every dead/flutter state sits at 28–33 dB. Delivery-pressure coherence saturates as soon as the machine cycles regularly — it cleanly separates *running* from *stalled* but carries almost no tuning information. The founding intuition survives in modified form: **coherence = alive** (a genuinely useful, cheap fleet-telemetry health metric — a 5 dB drop is a dispatch alarm), while **recoil = tuned** (the continuous signal near the knee). Both computed from one pressure sensor. Physical-bench confirmation pending as always.

## Finding 8 — the self-tuning module's control law, found the honest way (three failures on the record)

Digital prototype of the self-tuning ram (`tools/design/servo_min_recoil.py`), developed adversarially against our own model:

- **v1 failed**: naive extremum-seeking on raw |recoil| climbed into a *fake* low-recoil basin created by valve-bounce chatter (the model's reopen events included micro-bounces) and lost 4× output. Lesson: debounce (closure ≥ 50 ms defines a real reopen).
- **v2 failed differently**: debounced, the chatter basin vanished but a REAL second attractor at heavy tune remains — |recoil| is multi-modal in valve weight. Blind descent from an arbitrary mistune converges to whichever basin is downhill. A signed-flow phase detector was also tested and refuted (all reopens occur during backflow at every weight; sign carries no direction information in-model).
- **v3 works — sweep-then-track** (the same architecture solar MPPT adopted for the same multi-modal problem): a ~44 s commissioning sweep maps recoil across the weight range, jumps to the global minimum, then tracks with small steps + best-point memory + auto-re-sweep on 2.5× degradation.

**Result (mistuned start Wf = 1.4; supply fall drops 1.5 → 1.2 m mid-run):**

| Window | Fixed valve | Servo v3 | |
|---|---|---|---|
| pre-drift η | 0.566 | **0.729** | +29% rel. |
| post-drift η | 0.456 | **0.646** | +42% rel. |
| post-drift recoil | 0.212 | 0.020 | tracker followed the drift with no re-sweep needed |

The sweep found Wf* = 0.70 on its own — the static grid's knee (0.65–0.70) rediscovered by the controller with no map given. Stated fairly: the servo holds the *water-efficiency knee*, so it delivers slightly less water than a heavy fixed valve on a water-rich site (1.28 vs 1.42 L/s post-drift) while consuming 36% less drive water — on the water-limited sites where rams matter most, the servo's operating point is the one that survives. **Hardware implied: one pressure sensor, one preload actuator, firmware a $3 MCU runs. This is IP Disclosure 2's reduction-to-practice narrative, now with its failure modes documented — which is what makes it credible.**

## Finding 9 — chamber sizing (sim queue #3): the architecture makes the small, legal chamber sufficient

Grid: gas volume 15–120 L × rise-pipe conductance, tuned B300 knee point (data: `engineering/data/sweep_chamber_sizing.csv`).

- **η is insensitive to chamber size** (0.67–0.76 across an 8× volume range) — the literature's "insensitive above a minimum" (Asvapoositkul) reproduced by our transient physics.
- **Smoothing scales with volume as expected**: rise-pipe delivery CoV 1.34 (15 L) → 0.82 (30 L) → 0.45 (60 L) → 0.23 (120 L) at the gentlest rise-pipe setting; a more restrictive rise pipe also filters, at ~no η cost.
- **The architectural point that decides REQ-S1: in the ratified design the JET is fed from the HEADSTOCK, not the chamber.** The open headstock (minutes of residence time) smooths delivery essentially completely before the penstock — so chamber size affects rise-pipe pulsation only, not jet quality. T-001 at the nozzle is governed by penstock/manifold/nozzle design (D-6 study), not by chamber volume. A direct-coupled machine (no headstock) would need the big chamber; ours does not — **another engineering payoff of the founder's headstock, on the record.**
- **REQ-S1 consequence:** a chamber in the ~40 L class (CSA B51 small-vessel exemption territory — **threshold to be verified against current B51/ABSA Pressure Equipment Safety Regulation before reliance**) costs ~2% relative η vs 120 L and nothing at the jet. Design direction: (a) primary — exemption-class chamber, exit vessel scope entirely; (b) alternate — commodity **CRN-registered pre-charged bladder vessel** (COMPONENT_TECH_SCAN §3), compliance bought off the shelf. The legacy 150 L PN10 spec is superseded pending the verification memo.

## Status of the retired fit

η(r) = 0.85 − 0.03r is retired per D-5. At the operating point it happens to agree with the sim (0.67 vs 0.667) — the fit was right where it mattered and wrong in shape elsewhere, which is exactly why it needed replacing.

## Queue (in order)

1. ~~Drive-pipe length sweep~~ **DONE 2026-07-18 → Findings 4 & 5.** (Answer: appetite does NOT recover with length — it's a weight-knob variable at constant delivery; optimum L/D 100–250; per-ram power cap confirmed.)
2. ~~Valve tuning map~~ **DONE 2026-07-18 → Finding 6** (site-water-budget card data banked; WPT pressure-matrix short-site variant still pending).
2b. ~~T-002 metric rework~~ **DONE 2026-07-18 → Finding 7** (coherence = health signal; P2 answered in-model).
2c. ~~Min-recoil servo simulation~~ **DONE 2026-07-18 → Finding 8** (sweep-then-track v3; v1/v2 failures on the record).
3. ~~Chamber + rise-pipe sizing~~ **DONE 2026-07-18 → Finding 9** (small legal chamber sufficient; headstock does the jet smoothing; REQ-S1 exemption memo queued).
4. Model v2: reopen-leakage; re-anchor; then solver ingestion and full SKU re-statement (incl. WPT pressure-matrix short-site variant).
5. Physical bench correlation when hardware exists (±10% model-vs-prototype gate, VALIDATION req 8).

**Toolchain status (P0-1 DONE 2026-07-18):** 25 unit tests now guard the solvers (`tools/tests/test_solvers.py` — physics invariants, input validation, calibration-anchor regression envelope, energy-conservation bound, Welch-metric sanity, solver smoke tests) and run in GitHub Actions CI on every push (`.github/workflows/ci.yml`). Input validation added to `RamSim.__init__`. The ram_pelton solver's doc drift (headstock-less architecture text) corrected + D-5 supersession note added inline.
