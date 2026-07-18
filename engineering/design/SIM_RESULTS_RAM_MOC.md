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

## Status of the retired fit

η(r) = 0.85 − 0.03r is retired per D-5. At the operating point it happens to agree with the sim (0.67 vs 0.667) — the fit was right where it mattered and wrong in shape elsewhere, which is exactly why it needed replacing.

## Queue (in order)

1. ~~Drive-pipe length sweep~~ **DONE 2026-07-18 → Findings 4 & 5.** (Answer: appetite does NOT recover with length — it's a weight-knob variable at constant delivery; optimum L/D 100–250; per-ram power cap confirmed.)
2. Valve tuning map at the new operating points (weight × stroke) → the field commissioning card — now reframed as the site-water-budget card (Finding 5). Include the WPT pressure-matrix convolute (expired US9518595B2) as a short-site variant per COMPONENT_TECH_SCAN.
3. Chamber + rise-pipe sizing for T-001 jet quality (Gen 0 metric as design requirement).
4. Model v2: reopen-leakage; re-anchor; then solver ingestion and full SKU re-statement.
5. Physical bench correlation when hardware exists (±10% model-vs-prototype gate, VALIDATION req 8).
