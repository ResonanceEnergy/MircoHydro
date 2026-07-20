# CSA B51 / ABSA Compliance Memo — Air Chamber & Pressure Boundary (REQ-S1)

**Date:** 2026-07-19 · **Status:** engineering analysis for counsel/P.Eng review — NOT a legal opinion; thresholds below cite commonly applied B51/Alberta interpretations and **must be verified against the current CSA B51 edition and Alberta's Pressure Equipment Safety Regulation (AR 49/2006 as amended) + ABSA policy before reliance.** · **Closes:** dept-audit gap #1 path; PRD REQ-S1 acceptance = "stamped calc or documented exemption."

## Inventory of pressure boundaries in Machine B

| Component | Operating pressure | Fault-case pressure | Volume | B51 exposure analysis |
|---|---|---|---|---|
| **Air chamber (40 L class, F9)** | ~0.9–1.0 bar g (ride at delivery head) | ~4.7 bar g (blocked-delivery full Joukowsky, POWERTRAIN/PHYSICS_PROOF) | 40 L | **Primary strategy: stay under the small-vessel exemption class.** B51 practice exempts vessels below ~**42.5 L (1.5 ft³)** internal volume (and separately, small-diameter vessels ≤ ~152 mm ID are commonly treated as piping) — our F9 finding that 40 L suffices was chosen with exactly this line in view. **Alternate strategy: buy compliance** — a commodity pre-charged bladder/diaphragm expansion vessel with an existing **CRN** (Canadian Registration Number) registered for Alberta, rated PN10/10 bar ≫ 4.7 bar fault case. Either path avoids custom vessel engineering entirely. |
| **Egg headstock (D-8)** | **atmospheric** (vented, open collar) | atmospheric | ~4 m³ | **Out of B51 scope** — not a pressure vessel. The vent/overflow must be sized so no credible blockage pressurizes it (vent ≥ rise-pipe bore; overflow ≥ max delivery). Recorded as a design rule on the drawing. |
| Drive pipe (steel, 300 mm) | transient spikes ~1 bar; fault ~4.7 bar | — | — | **Piping, not vessel.** Sch 40 steel rated far beyond fault case; hoop stress a few MPa (infinite fatigue life, COMPONENT_TECH_SCAN §3). Falls under piping provisions; expansible-fluid piping thresholds to be checked, but water piping at <10 bar and ≤300 mm is routine. |
| Penstock (DN90 HDPE PE100-RC) | ~0.9 bar static | +surge (self-limiting, low wave speed) | — | Piping; PE100 PN10 class; deflector-first shutdown spec prevents fast-closure surge. |
| Rise pipe (DN100) | ~1 bar | ~4.7 bar fault | — | Piping; steel or PE PN10 both clear. |

## Recommended path (in order)

1. **Design-out (primary): spec the chamber at ≤40 L** (already the F9 recommendation — zero performance cost at the jet) **and document the exemption measurement** (internal volume calc on the drawing, witnessed). One page + one drawing note ends REQ-S1 for the chamber *if* the current B51 edition confirms the 42.5 L class — verification action V-1 below.
2. **Alternate (parallel-quote): CRN'd bladder vessel** (e.g., commodity 60 L PN10 expansion vessel with Alberta CRN). Cost ~$150–300; compliance is the manufacturer's CRN, not ours. Also solves the snifter-maintenance question (sealed pre-charge). Keep as the northern-package default where service intervals matter.
3. **Relief protection regardless of path:** a relief valve set ≤ chamber rating on the delivery side covers the blocked-delivery fault (4.7 bar) with margin; cost trivial; removes the fault case from every conversation with an inspector.
4. **Egg vessel:** add the "cannot pressurize" vent/overflow sizing rule to the D-8 drawing + a one-line scope statement in the install manual. No further action.

## Verification actions before reliance (founder/P.Eng)

- **V-1:** Confirm the small-vessel exemption volume + diameter figures against the **current CSA B51 edition** and ABSA's published interpretation (AB-506/pressure equipment exemption guidance). *(The 42.5 L / 1.5 ft³ and 152 mm figures are widely cited practice; editions move.)*
- **V-2:** Confirm CRN validity in Alberta for the chosen bladder vessel model (CRN must carry the Alberta suffix).
- **V-3:** One-hour consult with an ABSA-experienced P.Eng to bless the classification memo — this document is structured to make that consult cheap.

**Bottom line: the legal blocker dissolves into a volume choice we already made for performance reasons (F9), plus a $200 commodity alternative, plus one verification consult. REQ-S1 acceptance becomes a documentation task, not an engineering program.**
