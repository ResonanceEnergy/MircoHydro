# Whole-Design Physics & Energy Audit — Gap Analysis

**Date:** 2026-07-16 · **Method:** every quantitative claim in `specs/HYBRID_SYSTEM_MASTER_SPEC.md`, `specs/technology/TECH_SPEC.md`, and `specs/EFFICIENCY_OPTIMIZATION_PLAN_65PCT.md` recomputed from first principles (conservation of energy, Bernoulli, Darcy-Weisbach, D'Aubuisson). All computations reproducible via `../tools/scripts/physics_audit.py`.

**Verdict in one line:** the deep engineering analysis buried in the master spec is largely sound — but the design's headline numbers (output, efficiency, cost/kW, LCOE, annual energy) don't survive its own physics, and several architecture features (spiral penstock, vortex nozzle, ram-pump boost, submerged turbine) contradict either energy conservation or crossflow-turbine practice.

---

## 1. The core energy-balance gap: the site can't make the power

| Quantity | Claim | Physics | Gap |
|---|---|---|---|
| Gross hydraulic power @ design point (150 L/s, 5 m) | — | **7.36 kW** (ρgQH) | this is the ceiling before any losses |
| Net electrical @ spec's own honest cascade (33%) | "10–15 kW peak, 7–10 kW avg" | **2.4 kW** | **4–6× shortfall** |
| Net @ best realistic optimized (53%) | — | **3.9 kW** | still 3× short |

To honestly deliver 12 kW net at 45% efficiency requires **Q·H ≈ 2.7 m⁴/s** — e.g. ~270 L/s @ 10 m. **Fix: either re-target the product at 2.5–4 kW class, or spec sites with 5–7× more flow×head.** No optimization closes this gap; it is set by conservation of energy at the intake.

## 2. Five different efficiencies in one document family

81% (TECH_SPEC front matter) · 70%+ (North Star) · 62% ("current claim") · 55–62% (Units 100+) · 48.5% (quick wins) · 45–50% ("realistic") · **33% (the only one derived from a full loss cascade)**.

The 81% figure commits two errors at once: it *adds* percentage losses instead of multiplying stage efficiencies, and it omits the three biggest stages entirely (intake 0.82, penstock 0.79, turbine 0.65). The referenced `efficiency_calculator.py` ("200+ validated equations") does not exist in the repo.

Re-derived corrections to the honest numbers themselves:

- **Penstock arithmetic is internally inconsistent:** the spec uses ID 0.273 m for friction but 0.300 m for velocity. At the real DN300 ID, hf ≈ **1.10 m (22% of head)**, not 0.69 m (14%).
- **Quick-win double counting:** upsizing to DN350 recovers **+2.9 system points** (32.6→35.5%), not the claimed +7. Summing all five "quick wins" as claimed (+15.5 pts) double-counts; a proper multiplicative re-cascade gives **~40–43%**, not 48.5%.

**Fix: one parametric model (spreadsheet or Python), stage efficiencies multiplied, one source of truth.** Everything else quotes it.

## 3. Ram-pump branch: energetically ~neutral, capitally terrible

The architecture diagram routes "20%" of the stream to a ram pump feeding a 55 m head tank (4 L/s claimed). Recomputed:

- Delivering 4 L/s to 55 m from a 5 m fall at η=0.66 requires **~67 L/s of drive flow** — 45% of the stream, not 20%.
- Energy through the ram→tank→Pelton path: **1.34 kW**. Same 67 L/s through the main turbine chain: **1.07 kW**. Net gain: **+0.27 kW** — and near-zero once the main chain gets its quick wins.
- Capital for that gain (ram, 55 m of pipe, tank, second turbine, controls): $8–15k → **$30–55k per added kW**, ~20× worse than just buying more PV.

The master spec's own "Option C" (head tank as water supply — irrigation, fire reserve, potable backup — **not** turbine feed) is the physically and economically correct choice. The pressure-mixing problem the spec flags (55 m and 5 m sources cannot share a pipe) is real; sequential/Option A resolves the physics but not the economics. **Fix: adopt Option C; sell the ram as the water-supply product it is** (see `../research/reference-library/.../Volume_G` §G4, which already contains the correct "not free energy" guardrail).

## 4. Hybrid arithmetic: average and peak both overstated

- **Average:** PV 5 kW at Alberta capacity factor (~16%) → 0.8 kW; small wind 2 kW (~15%, generous at low hub height) → 0.3 kW; hydro 2.4 kW → **~3.5 kW system average** on a year-round stream — vs "7–10 kW average" claimed. On an **irrigation canal (water ~5.5 months/yr) it's ~2.2 kW**.
- **Peak:** 15 kW claimed, but the single 10 kW inverter caps deliverable AC power at 10 kW. Simultaneous source peak is 9.4–10.9 kW anyway.
- **Annual energy:** the spec's 26–29 MWh/yr assumes the turbine runs at design point 8,760 h/yr — a 100% capacity factor. No flow-duration curve exists anywhere in the repo. Real run-of-river CF is 40–70%; an irrigation canal is ~0% from November to April (drained — which also moots half the winter-icing analysis for canal sites).

**Fix: hydrology first.** One season of measured (or WSC gauge-derived) flow-duration data per candidate site, then energy = ∫P(Q)dt. This is the single largest unmodeled variable in the whole design.

## 5. Economics: an order of magnitude apart

- **$/kW:** $110–135k installed over 2.4 kW honest net = **$46–56k/kW** ($28–35k/kW even fully optimized) vs the stated $1,500–2,500/kW target and the GIGA blueprint's $17k pilot install. These describe different products; no cost-down curve bridges 20×.
- **LCOE:** at $120k capex, 5%/25yr, $2k/yr O&M: **$0.38/kWh** year-round stream, **$0.83/kWh** canal — vs claims of $0.05–0.12. To reach $0.10/kWh at real capacity factors, installed cost must fall to ~$25–35k **or** site Q·H must rise ~4×. That trade should drive both product sizing and site selection.

## 6. Features that subtract performance (physics says remove)

1. **"Schauberger spiral/rifled penstock":** the spec's own numbers concede rifling raises the friction factor 0.015→0.018 (+20% loss) for an unquantified "self-cleaning benefit." Swirl increases wetted path and wall shear; there is no mechanism for the claimed +5%. **Baseline: plain smooth HDPE.** If desired, test rifled-vs-smooth on the bench rig later — it's a cheap A/B.
2. **"Vortex nozzle" ahead of a crossflow runner:** a crossflow turbine requires a flat rectangular sheet jet at a controlled angle across the runner width. Deliberately swirling the jet destroys the inlet angle and drops turbine efficiency; every point in the 65% turbine estimate depends on *not* doing this.
3. **"Turbine inlet ≥3 m below surface" (TECH_SPEC cavitation fix):** wrong machine class. A crossflow runner operates at (near-)atmospheric pressure and must discharge freely to air (optionally via a draft tube with an air-admission valve); submerging it 3 m drowns the runner. The master spec's NPSH section is more careful (and correctly derates Alberta atmospheric pressure to ~85 kPa) but still imports reaction-turbine methodology. **Fix: set runner above tailwater with air gap; cavitation analysis applies to the nozzle, not a suction head.**
4. **φ-geometry efficiency multipliers (η_φ = 1.12) and Schumann-resonance RPM tuning** (quarantined in `../speculative/`): no physical mechanism; the 21-blade question is answerable for ~$300 via PROTOCOL_001 before it earns any place in a spec.

## 7. Real gaps the spec itself flags but the BOM ignores

These are correct findings in the master spec's deep section that never made it into cost or design baselines:

- **Battery winter heating** — LiFePO₄ cannot charge below 0°C; Alberta needs the insulated + heated enclosure (~$4,500) that the spec marks "CRITICAL, NOT IN BOM". Also reconcile 15 kWh (front matter) vs 23 kWh (winter section); 15 kWh gives roughly one winter night of autonomy at 1 kW with no margin.
- **Winter hardening package** (+$16,700: heated/underwater intake, penstock burial below 2.5 m frost line, blade heaters) — quantified in the spec, absent from the $110–135k total.
- **Fish screen sizing:** 150 L/s at 0.3 m/s needs ≥0.5 m² net open area — ≥1 m² allowing 50% fouling; frazil ice remains the dominant unpriced winter risk on stream sites.
- **IEEE 1547-2018 specifics** (anti-islanding method, ride-through curves, THD limits) — correctly enumerated, no certified inverter selected. Choosing a UL-1741-SA-certified 10 kW hybrid inverter closes most of this section at catalog-selection cost.

## 8. What's solid and should anchor everything

The loss-cascade methodology (§1.1), the head-tank pressure-mixing catch, the Alberta-atmosphere NPSH correction, the winter-performance analysis, the fish-safe intake criterion, and the "don't promise 62% on day 1" honesty doctrine. The bones of a good engineering culture are already in this document — the gaps are where the marketing layer overrode it.

---

## Priority fix list

1. **Re-baseline the product truthfully:** 2.5–4 kW hydro class at the current design point, or re-spec sites at ~270 L/s @ 10 m for a 12 kW class. Update every headline number from the single parametric model.
2. **Build the parametric model** (one afternoon): stages multiplied, penstock ID consistent, capacity factor input, LCOE output. Retire all five competing efficiency figures.
3. **Hydrology:** flow-duration curves for the first 3 candidate Alberta sites (WSC gauges + irrigation district schedules). This decides canal-vs-stream and the real annual energy.
4. **Delete spiral penstock and vortex nozzle from the baseline;** keep as bench A/B candidates.
5. **Reclassify the ram pump as the water-supply product line** (Option C). It's genuinely excellent at that job.
6. **Fix the crossflow installation geometry** (runner above tailwater, free discharge).
7. **Add winter package + battery heating to the BOM** and republish the honest install cost.
8. **Select the certified inverter** (UL 1741 SA / IEEE 1547-2018) and cap peak claims at its rating.
9. **Run PROTOCOL_001** — first measured efficiency point; it also settles the Fibonacci-blade question.
10. **Reconcile the two products in the repo:** the $17k GIGA pilot and the $110–135k hybrid station are different machines; name them, cost them, and market them separately.
