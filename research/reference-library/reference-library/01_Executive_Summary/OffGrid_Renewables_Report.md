# Off‑Grid / Renewable / Cleantech Knowledge Report + Reference Library

**Generated:** 2026-01-22

> **Important scope note (read first):** No one can literally “scrape the entire internet” inside Word/Copilot in a single run. What I *can* do is compile a **deep, structured, evidence‑based research report** and a **curated reference library** anchored to authoritative sources (DOE, NREL, IRENA, EIA, etc.), plus practical design checklists. 

---

## 1) Executive Summary

Off‑grid power systems combine **generation** (PV/wind/hydro/biogas), **storage** (batteries, sometimes hydrogen), and **power conversion/controls** (charge controllers, inverters, protection). DOE’s overview of stand‑alone systems emphasizes that beyond the generation device you need “balance‑of‑system” equipment such as batteries, charge controllers, power conditioning, and safety equipment. (See DOE Energy Saver.) 

Well‑designed systems start with **load reduction** and accurate **load profiling**, then technology selection and sizing. DOE notes stand‑alone systems can be economical when line extension is expensive, and often use hybrids plus demand reduction. 

Cost trends matter. Recent global cost reporting shows renewables remain among the most cost‑competitive new generation options, while storage costs continue to decline in many segments. (See IRENA cost report and Lazard LCOE+.) 

Finally, “**free energy**” claims (perpetual motion/over‑unity) conflict with well‑established thermodynamics; treat such claims with strong skepticism and require reproducible third‑party validation.

---

## 2) Fundamentals: What an Off‑Grid System *Is*

### 2.1 Stand‑alone vs grid‑connected
- **Stand‑alone (off‑grid)**: operates without utility connection; requires storage or controllable generation to ride through resource gaps. DOE describes these as “stand‑alone systems” and highlights additional equipment beyond PV/wind/hydro: batteries, charge controller, power conditioning, safety equipment, metering. 
- **Grid‑connected**: uses the grid as a buffer; excess generation can be fed back; storage may be optional. DOE notes net metering arrangements and the need to meet utility interconnection requirements. 

### 2.2 Core building blocks
1. **Loads**: what you must power (kWh/day) and peak power (kW).
2. **Generation**: PV/wind/hydro/biogas, often hybridized.
3. **Storage**: batteries (dominant); sometimes thermal storage; hydrogen in niche cases.
4. **Conversion & control**: charge controllers (MPPT), inverters, DC/DC, protective devices.
5. **Distribution**: AC and/or DC buses, wiring, grounding, disconnects.
6. **Operations**: monitoring, maintenance, spares, seasonal plans.

NREL’s REopt training materials describe modeling and optimization for sizing and dispatch of PV and batteries for off‑grid microgrids (a formal way to choose least‑cost mixes subject to reliability constraints).

---

## 3) Technology Deep Dives (Practical)

### 3.1 Solar PV (off‑grid)
**Why it’s popular:** modular, low maintenance, predictable daily pattern. DOE’s stand‑alone systems page includes PV as a common option and stresses the need for BOS equipment (batteries, controllers, conditioning).

**Key design variables:**
- Insolation/seasonality (winter is usually the sizing driver in northern latitudes).
- Array size vs battery size trade‑off.
- DC‑coupled vs AC‑coupled architectures. (NREL REopt module discusses AC‑coupled assumptions in modeling.)

**Typical pitfalls:** undersized winter PV, inadequate surge capacity, poor wiring/protection, and battery temperature management.

### 3.2 Wind
Wind can complement solar seasonally and diurnally, but site quality is everything (tower height, turbulence). Hybrid systems are common for reliability (DOE encourages hybridization strategies for stand‑alone reliability).

### 3.3 Microhydro (continuous power when water is reliable)
Microhydro can deliver **24/7** energy where head/flow exist. NREL’s fact sheet defines microhydro as systems up to 100 kW and notes a 10 kW system can power a large home or small farm/resort. 
The DOE Microhydropower Handbook provides comprehensive engineering background on microhydro system design (penstocks, turbines, etc.).

**Back‑of‑envelope power:**

\[P ≈ ρ g Q H η\]

Where \(Q\)=flow (m³/s), \(H\)=head (m), \(η\)=overall efficiency. (Use handbook/fact sheet guidance for realistic \(η\) values and losses.)

### 3.4 Bioenergy / Biogas (anaerobic digestion)
Anaerobic digestion turns organic wastes into biogas (methane + CO₂) and digestate fertilizer. FAO describes AD as biological breakdown in the absence of oxygen producing methane and CO₂ and emphasizes waste handling and renewable energy potential. ATTRA provides a beginner guide for micro‑scale digesters and practical operation notes.

### 3.5 Hydrogen / Electrolysis (usually *not* best for small off‑grid unless specific needs)
DOE’s electrolysis page explains electrolyzers (PEM, alkaline, solid oxide) and notes operating temperature differences and process basics (splitting water into H₂ and O₂). Hydrogen can be useful for long‑duration/seasonal storage, but round‑trip efficiency and complexity often make batteries preferable at small scale.

---

## 4) System Architecture Patterns (How to put it together)

### 4.1 DC‑coupled solar + battery (common cabin pattern)
- PV -> MPPT controller -> battery -> inverter -> AC loads
- Pros: efficient for PV charging, simple
- Cons: inverter must handle surges; DC wiring can be heavy.

### 4.2 AC‑coupled hybrid microgrid
- PV inverter/wind/hydro feed an AC bus; battery inverter manages storage and grid‑forming
- NREL’s REopt off‑grid module discusses AC‑coupled modeling assumptions.
- Pros: flexible integration
- Cons: controls and curtailment logic more complex.

### 4.3 Hybrid with generator backup
DOE notes hybrid strategies can reduce inconvenience and improve reliability for stand‑alone systems (e.g., renewables + fossil generator).

---

## 5) Safety, Codes, and Standards (High‑level)

Even off‑grid systems must be built safely. For grid‑connected interconnection, standards like IEEE 1547 and UL 1741 are central; NREL’s “Grid Standards and Codes” page describes work on IEEE 1547 and related revisions and how standards streamline interconnection and reliability. (Always consult local electrical codes and qualified electricians for permitting and safety.)

---

## 6) Economics & Cost Trends

- IRENA’s 2024 renewable cost report (published 2025) summarizes that most newly commissioned utility‑scale renewables deliver electricity at lower cost than the cheapest new fossil alternative, and provides LCOE movements by technology and year.
- Lazard’s LCOE+ (June 2025) compiles ranges for generation and storage LCOE/LCOS and discusses competitive positioning.
- U.S. EIA’s AEO 2025 LCOE report provides modeled levelized costs and methodology for comparison across new generation resources in the U.S.

Use these for **order‑of‑magnitude benchmarking**—your off‑grid project economics depend heavily on site conditions, logistics, financing, and reliability requirements.

---

## 7) “Free Energy” / Over‑Unity: How to Evaluate Claims

Perpetual motion machines that produce work indefinitely without input energy violate the first and/or second laws of thermodynamics, and are considered impossible by mainstream physics. A general overview is summarized in the “Perpetual motion” reference.

**Practical evaluation checklist:**
1. **Define boundaries** (what counts as input: heat, RF, vibration, sunlight, ground currents, chemical reactions).
2. **Calibrated measurements** (true RMS power, phase, harmonics, hidden batteries).
3. **Independent replication** by competent labs.
4. **Energy balance** over long duration.
5. **Publication or transparent documentation** sufficient for replication.

If a device cannot pass these, treat it as unproven. Prefer investing time into proven renewables and efficiency.

---

## 8) Tools & Checklists (practical starting points)

### 8.1 Load audit template (quick)
- List appliances: watts, hours/day, duty cycle.
- Compute kWh/day and peak simultaneous load.
- Identify surge loads (pumps, compressors, power tools).

### 8.2 Battery sizing heuristic
- Choose autonomy days (e.g., 1–3 days for PV cabins, more for critical loads).
- Consider usable DoD, temperature derating, aging reserve.

### 8.3 Microhydro site screening
- Measure head (m) and flow (m³/s).
- Estimate power using \(P ≈ ρ g Q H η\).
- Check seasonal flow variability and water rights/permitting. (See NREL microhydro fact sheet and DOE handbook.)

---

## 9) Reference Index

See **09_Reference_Index/references.json** and **references.md** for a clickable list.
