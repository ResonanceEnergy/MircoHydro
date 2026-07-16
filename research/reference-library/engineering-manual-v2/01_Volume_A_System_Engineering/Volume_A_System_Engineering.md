# Volume A — System Engineering for Off‑Grid Power

Generated: 2026-01-22

## A1. Requirements & Load Modeling

### A1.1 Start with loads
Define: daily energy (kWh/day), peak power (kW), surge loads, and critical loads. A stand‑alone system must supply loads without a grid buffer, so load profiling is the first design driver.

DOE notes stand‑alone systems typically require balance‑of‑system equipment (batteries, charge controllers, power conditioning, safety equipment) in addition to the generator, and reliability is achieved through a combination of system sizing and reducing required electricity. citeturn1search31

### A1.2 Reliability targets
- Autonomy days (e.g., 1–3+ days)
- Loss of load probability (LOLP) or practical equivalent (hours/year of unmet load)
- Power quality requirements (frequency/voltage limits)

NREL’s REopt off‑grid training explains that optimization tools can size and dispatch PV and batteries for off‑grid microgrids under reliability constraints. citeturn1search28

## A2. Architecture Patterns

### A2.1 DC‑coupled (PV → MPPT → battery → inverter)
Typical for cabins/homes due to simplicity and efficient charging. See DOE’s BOS concept for the required controllers/inverters/safety equipment. citeturn1search31

### A2.2 AC‑coupled hybrid microgrid
Multiple sources feed an AC bus; a grid‑forming inverter controls frequency/voltage and charges storage. REopt training discusses AC‑coupled assumptions in modeling off‑grid systems. citeturn1search28

## A3. Sizing Workflow (repeatable)
1) Reduce loads
2) Build hourly (or at least seasonal) load profile
3) Quantify resource (solar/wind/hydro/biomass)
4) Choose architecture
5) Size generation, storage, inverter, and protection
6) Validate with simulation (REopt / SAM / spreadsheet)
7) Design for safety & maintainability

## A4. Commissioning & O&M
Document: operating modes, spares, monitoring plan, seasonal procedures. Microgrid guidance emphasizes resilience planning, requirements definition and lessons learned from real deployments. citeturn2search68
