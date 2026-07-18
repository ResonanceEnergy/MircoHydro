# Decisions: D-1..D-5 Design Ratification · Canon (X1–X9) · Company Name

**Date:** 2026-07-18 · **Decided by:** Founder (NATRIX), directive: "build the water-hammer simulator with the D-1–D-5 design decisions, the canon ratification, Resonance Energy Systems" · **Status:** RATIFIED
**Resolves:** decision queue from `docs/strategy/DESIGN_HISTORY_AUDIT.md` §5 and canon table from `docs/strategy/FOUNDING_PRINCIPLES_AUDIT.md` X1–X9.

## Design decisions

**D-1 — Machine B wheel type: head-dependent selection rule.** Pelton for synthesized jet head ≥ 8 m; **Turgo for 4–8 m** (tolerates larger jet/wheel ratio, relaxes the jet-head floor that crushed 0.5 m-fall sites); the solver picks per site. HB-01 crossflow-first doctrine is amended with the head-synthesis exception (crossflow remains first choice for natural-head machines; impulse wheels govern the ram's synthesized-head branch).

**D-2 — Nozzles: fixed primary (N1) + valved boost (N2) confirmed.** Gen 1's four servo valves retired: flow is constant by design, so adjustability adds cost and failure modes without function. Reversible if field data shows part-load need.

**D-3 — Vortex nozzle: out of all baselines; preserved as a bench A/B candidate** alongside the fluted-penstock test. Jet physics case stands (impulse wheels require coherent jets); the founder's original hypothesis gets its measured day in court rather than silent deletion.

**D-4 — Gen 0 experimental program: REVIVED, digitally first.** The founder's original locked metrics — **T-001 jet coherence and T-002 PSD peakiness (0.2–20 Hz)** — are incorporated into the water-hammer simulator as computed outputs (delivery-pressure PSD peakiness; jet-velocity variation coefficient). The January 2026 test program runs at last — on the digital bench, physical later.

**D-5 — η_ram fit: superseded by simulation.** The Claude-fitted curve η(r) = 0.85 − 0.03r is demoted to "initial estimate"; the MOC simulator's derived curve becomes the design basis. All Machine B published numbers regenerate from simulator output. (This document accompanies the simulator build — `tools/design/ram_moc_sim.py`.)

## Canon ratification (X1–X9)

| # | Canonical answer (now binding) |
|---|---|
| X1 | Efficiency canon: **turbine component ≥70–75%; Machine A system 45–53%; Machine B system per simulator** (supersedes 29–42% fitted range). All other figures (55/62/65/75/81/95%) retired from every future document |
| X2 | PFK + FlowCube marketing + BRAND_IDENTITY to be rewritten from canon (queued work item) |
| X3 | **Three founding inspirations** (Schauberger, Tesla, Winter-exploratory); RWR = gated product hypothesis, not a founder. Corpus count stated once: 160 visionaries / 1,600 insights |
| X4 | **25-year design life; 30+ with service program.** "Infinite" banned |
| X5 | Community give-back: 2% revenue AND co-op equity both remain options; board-ratify at entity formation |
| X6 | Product ladder: **B-line 0.2–1.4 kW · A-line 2.5–4 kW · A-uprated 10–15 kW (site-gated)** |
| X7 | Penstock loss standard: **≤10%, ≤5% stretch** (HB-03 prevails) |
| X8 | $1,500–2,500/kW restated as Year-5+ volume target with staged milestones |
| X9 | Engineering handbook DISCLAIMER is supreme; visionary board charter amended to **inspiration panel** (no design authority) |

## Company name

**Resonance Energy Systems** — ratified as the operating name for the venture (Alberta incorporation per `docs/strategy/ALBERTA_LAUNCH_PLAN.md` Phase 0). Brand documents to be updated in the X2 rewrite pass. The name honors the founding inspiration layer while the canon keeps every claim physics-first.

## Follow-on work items opened by these decisions

1. Simulator build + Machine B number regeneration (this commit).
2. Solver update: Turgo branch for 4–8 m jet heads (relaxed floor HD_MIN 6→4 m with Turgo constraints).
3. HB-01 doctrine amendment paragraph.
4. X2 rewrite pass (PFK, FlowCube marketing, BRAND_IDENTITY → Resonance Energy Systems + canon numbers).
5. Blender functioning-unit model now unblocked (wheel type decided) — queued.
