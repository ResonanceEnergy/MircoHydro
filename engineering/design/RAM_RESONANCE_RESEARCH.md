# Ram Resonance, φ Coherence & Efficiency Maximization — Full Research Synthesis

**Date:** 2026-07-18 · Three research sweeps: (1) published ram-optimization science, (2) Keely + Tesla patents and record, (3) φ/coherence evidence in fluid machinery. Everything graded measured / theory / lore. Feeds: `SIM_RESULTS_RAM_MOC.md` queue, PROTOCOL_001, IP disclosures.

---

## 1. Proper dimensions — what measured data actually supports

| Parameter | Data-backed optimum | Source |
|---|---|---|
| Drive pipe L/D | **150–1000 window; target ≈500** (Watt: "L/D 500 or L = 4×supply head, whichever smaller"). L/D is the governing dimensionless group (confirmed by dimensional analysis + experiment, Fatahi-Alkouhi 2019); the field rule L = 3–7×fall is a siting convenience | [Watt/ITDG manual](https://archive.org/details/AManualOnTheHydraulicRamForPumpingWaterS.B.Watt), [Calvert via builditsolar](https://www.builditsolar.com/Projects/WaterPumping/Ram%20Pump/ram.htm), [Scientia Iranica 2019](https://scientiairanica.sharif.edu/article_4597.html) |
| Drive pipe material | **Steel, thick-wall — mandatory.** Pulse pressure falls as D/t rises; low wave speed (PVC) directly degrades pumping | Watt's charts; matches our MOC wave-speed physics |
| Waste valve stroke × weight | **Joint optimum; sharp.** Best modern lab: **η = 70.45% at 1 kg / 10 mm stroke** (3" ram); efficiency peaks at 5–10 mm stroke, collapses past ~15 mm; each weight has its own optimal stroke | [Johanis et al.](https://pdfs.semanticscholar.org/f878/1c90d730822128ad183a19027e34efd9d53e.pdf), [Rahman 2025](https://sciresol.s3.us-east-2.amazonaws.com/IJST/Articles/2025/Issue-18/IJST-2025-394.pdf) |
| Beat frequency | Scale-dependent: 1" lab rams optimize at 200–285 bpm; 2–4" rams at 40–100 bpm; higher beat → higher η but lower absolute flow | [Asvapoositkul 2019](https://onlinelibrary.wiley.com/doi/10.1155/2019/9702183), [Lansford & Dugan 1941](https://www.ideals.illinois.edu/items/5169) |
| Valve kinematics | Opening ∝ t^1.5, closure ∝ t^0.2 (measured); delivery-valve flutter degrades output; **valve elasticity/bounce needed in models** (Lansford could only match data with it) | [Li 2022](https://journals.sagepub.com/doi/10.1177/09576509221075870) |
| Air chamber | **Insensitive above a minimum** (precharge 1–3 bar: no difference; volume sweeps: no effect on delivery). Inferred practice ≈50–100× per-cycle delivery volume. Too small → violent cycling/waterlog | [Asvapoositkul](https://onlinelibrary.wiley.com/doi/10.1155/2019/9702183), [Ngolle & Hong 2019](https://koreascience.or.kr/article/JAKO201921957010654.page) |
| Snifter | **0.5–1.0 mm; check-valve type best** (plain holes leak spike energy; larger holes measurably cut η) | [Suarda 2019](https://iopscience.iop.org/article/10.1088/1757-899X/539/1/012007/pdf) |
| Delivery pipe | ½ drive-pipe diameter (century-old convention, unchallenged) | Watt/Blake tables |
| Body geometry | "Back-enlargement" body beats front-enlargement (CFD-optimized, field-proven 50–70% η) | [Guo 2018](https://journals.sagepub.com/doi/abs/10.1177/0957650918756761) |

**Efficiency ceiling, measured:** 65–70% Rankine (best-instrumented classic, 4" ram), 70.45% modern lab peak, 60–65% commercial (Blake/Rife rate at 0.6). η falls universally as lift ratio exceeds ~15–20. Note for our sim reporting: **distinguish D'Aubuisson vs Rankine** (Rankine is stricter; they diverge several points at low lift ratios). Our calibration (0.667 D'Aubuisson at r=6) sits exactly in the credible band.

## 2. Resonance — the real physics, and the one published tuning condition

- **The ram is legitimately a resonance machine.** Joukowsky: ΔP = ρ·a·Δv — the water column's kinetic energy converts to a pressure spike of **25–70× the supply head** (measured: ~10⁶ Pa from 1–2 m falls; Blake lifts 105–150 m from a few metres). This is the honest "force multiplier": a **pressure transformer**, never an energy amplifier — every measured machine obeys η ≤ ~0.70.
- **Young's zero-recoil condition (1995/96) is the published resonance tuning:** optimal operation occurs when the waste valve *reopens exactly as the reflected wave brings drive-pipe flow to zero* — the valve cycle phase-locked to the pipe's 2L/a reflection schedule. This is the closest thing in a century of literature to "tuned resonant operation," and it's real, calculable engineering. ([Young 1995](https://journals.sagepub.com/doi/10.1243/PIME_PROC_1995_209_010_01), [1996](https://journals.sagepub.com/doi/10.1243/PIME_PROC_1996_210_048_02))
- **The open research niche is wide:** no peer-reviewed work exists on deliberately period-matched multi-pulse rams, and the wave-energy-utilization metric (Ep/Em, [Fatahi-Alkouhi 2019](https://www.sciencedirect.com/science/article/pii/S2090447919300814)) has never been optimized in a product. Our MOC simulator is built for exactly this hunt. The validated-model benchmark to match: [Lungudi et al., JHR 2024](https://www.tandfonline.com/doi/full/10.1080/00221686.2024.2401899).

### ★ The standout product idea this research produced: the self-tuning ram

Young's condition was published as a *design-time* calculation because 1990s rams had no brains. But zero-recoil is a **control target**: one $3 pressure sensor reads the wave timing, one microcontroller adjusts valve preload (solenoid or moving weight), and the machine *holds itself at resonance* through seasonal head/flow changes — the tuning that today takes a skilled installer hours and drifts out of optimum forever after. **Active phase-locked valve timing on a hydraulic ram appears in zero publications and zero products.** It is precisely "capturing waste energy with upgraded technology that prohibited it in the past" — the blockers were sensors and control, both now trivial. Candidate invention disclosure #2 (after the coupled-solver method). Expected honest gain: recovering the 5–15 efficiency points between field-typical (50–60%) and lab-tuned (65–70%) operation — *permanently, automatically*.

## 3. φ / coherence — the evidence, graded

- **The one commercial golden-spiral fluid machine:** PAX Scientific's **Lily impeller** ([case study](http://toolbox.biomimicry.org/wp-content/uploads/2015/01/Outreach-Toolkit-PAX-Scientific-Case-Study.pdf), [MoMA](https://www.moma.org/collection/works/110215)) — logarithmic-spiral geometry, genuinely shipped in municipal **tank mixers** (PAX Water/UGSI) with company-claimed large energy savings for low-shear bulk mixing. Grade: real product, real niche (mixing, not turbines), company-sourced numbers, no independent peer-reviewed efficiency comparison found.
- **The legitimate core of "Fibonacci blades":** standard turbomachinery practice selects **coprime blade counts** between rotating and stationary rows to prevent simultaneous excitation and resonance ([Concepts NREC](https://www.conceptsnrec.com/blog/vibration-and-resonance-issues-in-turbomachines), [ScienceDirect](https://www.sciencedirect.com/topics/engineering/blade-vibration)). A 21-blade runner (vs 20) has a *defensible vibration-engineering rationale* — 21 shares no factors with common strut/vane counts — entirely independent of mysticism. This reframes PROTOCOL_001 honestly: the A/B test isn't testing magic, it's testing whether the coprime/odd count buys smoothness or efficiency at our scale.
- **No peer-reviewed evidence anywhere** that φ proportions per se increase turbine or pump efficiency. The founding gate stands: PROTOCOL_001 measures it; claims wait.
- **Coherence, made operational:** your T-002 PSD-peakiness metric is now the quantitative definition of cycle coherence in the sim — and zero-recoil tuning should *maximize* it. Prediction worth testing: **the coherence peak and the efficiency peak coincide.** If they do, the founding intuition ("coherence = performance") earns a measured, publishable form.

## 4. Keely — see the neutral evidence file

The earlier verdict-first paragraph is superseded per founder directive. The full, both-sides record — sympathetic witnesses (Leidy, Willcox, Lascelles-Scott), the adversarial 1899 investigation and Clarence Moore's documented financial conflict, Kinraide's ambiguous silence, the real patent record (one 1871 grant, one abandoned 1872 application), modern replication attempts, physics adjacencies, open questions, and the tests that would settle them — lives in **`research/KEELY_EVIDENCE_FILE.md`**. The company-relevant constant survives unchanged from either reading: instruments and disclosure are what separate a claim from a story, and our telemetry/open-dashboard commitments are the structural answer.

## 5. Tesla — the usable inheritance, with patent numbers

| Artifact | Patent | Measured reality | Use for us |
|---|---|---|---|
| Polyphase AC generation | [US 381,968](https://patents.google.com/patent/US381968A/en) (1888) + family; Niagara 1895 | foundation of all AC hydro | our PMA/generator lineage — cite proudly |
| **Tesla valve (valvular conduit)** | [US 1,329,559](https://patents.google.com/patent/US1329559A/en) (1920) | diodicity ≈ 2 steady flow ([Nat. Comm. 2021](https://www.nature.com/articles/s41467-021-23009-y)); **performs best in pulsed/oscillating flow** (up to 2.5× quasi-steady); ships in microfluidics + phone cooling; NASA studied it for water-hammer mitigation | **NOT the impulse valve** (can't slam). Genuine candidates: **check-valve snifter duty, delivery-line transient damping** — a ram is a ~1 Hz AC flow source, the valve's home regime. **Zero published ram+Tesla-valve studies — open niche, bench A/B slot added** |
| Disc pump (boundary layer) | [US 1,061,142](https://patents.google.com/patent/US1061142A/en) | ~30–37% η measured; commercially proven for **abrasive/sediment/shear-sensitive fluids** (Discflo, 40+ yrs) | option for silty-intake auxiliary duty; a deliberate clog-immunity trade |
| Tesla turbine | [US 1,061,206](https://patents.google.com/patent/US1061206A/en) | claimed 80–97%; **measured 10–36%** across seven decades of tests | lore for power duty — stays excluded (already gated) |
| Resonance discipline | tuned circuits [US 645,576](https://patents.google.com/patent/US645576A/en); oscillator [US 514,169](https://patents.google.com/patent/US514169A/en) | radio tuning's legal/technical foundation; earthquake machine: busted (MythBusters ep. 60) | the transferable principle — drive at natural frequency, match impedance — is exactly zero-recoil tuning in hydraulic form |

## 6. Work orders fired by this research

**Simulator (in queue order):** (1) valve kinematics upgrade — t^1.5/t^0.2 laws + elasticity/bounce; (2) dual η reporting (D'Aubuisson + Rankine); (3) **zero-recoil hunt** — sweep valve preload/timing against the 2L/a schedule, map η and T-002 coherence together (test the coincidence prediction); (4) L/D sweep 150→1000 at fixed site (our current 150 is at the window's bottom edge); (5) validate traces vs Evangelista's 1 kHz data + Lungudi's model.
**Product:** check-valve snifter 1.0 mm spec'd; delivery = ½ drive diameter; steel drive pipe locked; stroke 5–15 mm tunable with paired-weight commissioning card; Tesla-valve snifter + delivery-damping added to bench A/B roster (alongside fluting, vortex nozzle, 21-blade runner).
**IP disclosures to draft:** (1) coupled ram-bank→headstock→jet sizing method; (2) **self-tuning phase-locked ram** (sensor + controller holding Young's zero-recoil condition); (3) Tesla-valve auxiliary functions in ram service (search shows the combination unpublished).
**Docs:** founding-inspiration pages gain the Keely anti-pattern paragraph and Tesla patent citations (X2 rewrite pass).
