# PROTOCOL 001: φ-TURBINE DESKTOP TEST
**Status:** Ready to Execute  
**Lead:** Research Agent + Human  
**Budget:** $130-355  
**Timeline:** Week 1-3 (Jan 26 - Feb 16, 2026)  
**Deliverable:** Provisional Patent #1 Filed

---

## 🎯 OBJECTIVE

Validate hypothesis: **21-blade Fibonacci runner with golden angle spacing (137.5°) achieves 6-12% higher efficiency than 20-blade uniform runner (18° spacing).**

**Success Criteria:**
- Statistical significance (p < 0.05)
- Efficiency improvement: 6-12% range
- Test data suitable for patent evidence
- Lab report published within 24 hours of test completion

---

## 📊 HYPOTHESIS

**H₀ (Null):** There is no significant difference in efficiency between φ-optimized runner (21-blade) and control runner (20-blade).

**H₁ (Alternative):** The φ-optimized runner achieves 6-12% higher efficiency than control runner.

**Significance Level:** α = 0.05  
**Statistical Test:** Two-sample t-test (independent samples)

---

## 🛒 MATERIALS & EQUIPMENT

### Order Today (Amazon Prime 2-day)

| Item | Specification | Example Product | Est. Price | Priority |
|------|---------------|-----------------|-----------|----------|
| **PLA Filament** | 1kg, any color | OVERTURE PLA 1.75mm | $20-30 | 🔴 CRITICAL |
| **Submersible Pump** | 350-1200 GPH (22-76 L/min) | VIVOSUN 800GPH | $50-80 | 🔴 CRITICAL |
| **Vinyl Tubing** | 1/2" or 3/4" ID, 10ft | Clear PVC | $15-25 | 🔴 CRITICAL |
| **Multimeter** | DC voltage/current | AstroAI Digital | $20-40 | 🔴 CRITICAL |
| **Bucket/Tote** | 5-10 gallon | Storage container | $10-20 | 🔴 CRITICAL |
| **Digital Flow Meter** | 1-30 L/min range | SeaMetrics S100 | $80-150 | 🟡 HIGH |
| **Pressure Gauge** | 0-30 PSI | Glycerin-filled | $15-30 | 🟡 HIGH |
| **Tachometer** | Non-contact, RPM | Digital laser tach | $20-40 | 🟢 MEDIUM |

**Total (Essential):** $115-205  
**Total (With all sensors):** $245-395

**Amazon Cart Links:**
```
PLA Filament: search "OVERTURE PLA 1.75mm"
Pump: search "VIVOSUN 800GPH submersible pump"
Tubing: search "clear vinyl tubing 1/2 inch"
Multimeter: search "AstroAI digital multimeter"
Flow meter: search "water flow meter sensor 1-30 L/min"
```

### Already Have (Verify)
- [ ] 3D printer (operational, calibrated)
- [ ] Computer with CAD software (FreeCAD, Fusion 360, Shapr3D)
- [ ] Ruler/calipers (for measuring dimensions)
- [ ] Notebook (lab notebook for manual logs)
- [ ] Camera/phone (for documentation photos/video)

---

## 🔧 EXPERIMENTAL SETUP

### Phase 1: CAD Design (Day 1-2)

**Runner A: 21-Blade Fibonacci (φ-optimized)**
```
Blade count: 21 (Fibonacci number)
Angular spacing: 137.5° (golden angle = 360°/φ²)
Blade chord progression: φ-ratio (each blade 1.618× previous)
Outer diameter: 100mm (desktop scale)
Inner diameter: 30mm (hub)
Blade thickness: 3mm (3D printable)
Blade height: 40mm
Blade angle: 25-30° (tangent to flow)
```

**Runner B: 20-Blade Uniform (Control)**
```
Blade count: 20 (conventional)
Angular spacing: 18° (uniform = 360°/20)
Blade chord: Uniform width (not φ-scaled)
Outer diameter: 100mm (same as Runner A)
Inner diameter: 30mm (same as Runner A)
Blade thickness: 3mm
Blade height: 40mm
Blade angle: 25-30° (match Runner A)
```

**Runner C: 25-Blade Uniform (Negative Control)**
```
Blade count: 25 (test "more is better" hypothesis)
Angular spacing: 14.4° (uniform = 360°/25)
All other dimensions match Runners A & B
```

**CAD Software:**
- FreeCAD (free, open-source)
- Fusion 360 (free for hobbyists)
- Shapr3D (free tier available)

**Export Format:** STL (for 3D printing)

---

### Phase 2: 3D Printing (Day 3-5)

**Print Settings:**
- Material: PLA (easier to print than ABS)
- Layer height: 0.2mm (balance speed vs quality)
- Wall thickness: 1.2mm (4 perimeters at 0.3mm nozzle)
- Infill: 20% (sufficient strength)
- Print speed: 50mm/s (quality over speed)
- Supports: Yes (for blade overhangs)
- Bed adhesion: Brim or raft

**Print Time Estimate:**
- Runner A: 24-36 hours
- Runner B: 24-36 hours
- Runner C: 24-36 hours
- **Total: 72-108 hours (3-4.5 days)**

**Strategy:** Print Runner A first (critical path), then B and C in parallel if multiple printers or while testing A.

**Post-Processing:**
- Remove supports carefully
- Sand rough edges if needed
- Verify dimensions (calipers)
- Check for warping (should spin freely on shaft)

---

### Phase 3: Test Rig Assembly (Day 5-6)

**Components:**
1. **Reservoir:** 5-10 gallon bucket/tote (recirculating system)
2. **Pump:** Submersible, mounted in reservoir
3. **Supply Line:** Vinyl tubing from pump to runner inlet
4. **Runner Mount:** Vertical or horizontal (shaft with bearings)
5. **Generator/Load:** Small DC motor as generator, resistor bank as load
6. **Return:** Gravity drain back to reservoir

**Assembly Steps:**
1. Mount pump in bottom of reservoir
2. Connect tubing to pump outlet
3. Route tubing to runner inlet (1m head if vertical)
4. Mount runner on shaft with bearings (minimize friction)
5. Couple generator to runner shaft (direct or belt)
6. Connect multimeter in series with load resistor
7. Install flow meter in supply line (if available)
8. Install pressure gauge at runner inlet (if available)
9. Fill reservoir with water (8-10 liters)
10. Test for leaks (run pump, check all connections)

**Safety:**
- Electrical: Keep multimeter/wiring away from water
- Mechanical: Guard on rotating parts (no loose clothing)
- Spills: Towels ready, work on waterproof surface

**Photo Documentation:**
- Overall test rig (3 angles)
- Close-up of runner in position
- Sensor connections
- Flow path diagram

---

## 📋 TEST PROCEDURE

### Pre-Test Checklist
- [ ] Runner installed and spins freely
- [ ] All connections leak-free
- [ ] Multimeter calibrated and zeroed
- [ ] Data collection sheet ready
- [ ] Camera ready for video recording
- [ ] Lab notebook open for notes
- [ ] Safety check complete

---

### Test Matrix (20 tests per runner, 60 total)

| Test # | Runner | Flow Rate (L/min) | Head (m) | Load (Ω) | RPM Target | Notes |
|--------|--------|-------------------|----------|----------|------------|-------|
| 1-4    | A      | 5, 10, 15, 20    | 1.0      | 10Ω      | Variable   | Low flow |
| 5-8    | A      | 5, 10, 15, 20    | 1.0      | 5Ω       | Variable   | Medium load |
| 9-12   | A      | 5, 10, 15, 20    | 1.0      | 2.5Ω     | Variable   | High load |
| 13-16  | A      | 10, 15, 20, 25   | 1.5      | 5Ω       | Variable   | Higher head |
| 17-20  | A      | 10, 15, 20, 25   | 0.5      | 5Ω       | Variable   | Lower head |
| 21-40  | B      | (Same as A)      | ...      | ...      | ...        | Control |
| 41-60  | C      | (Same as A)      | ...      | ...      | ...        | Negative |

**Variables:**
- **Independent:** Blade configuration (A/B/C), flow rate, head, electrical load
- **Dependent:** RPM, voltage, current, efficiency
- **Control:** Water temperature (20±2°C), runner diameter, test rig configuration

---

### Individual Test Procedure (15-20 minutes per test)

**Step 1: Setup (2 min)**
1. Install runner (A, B, or C)
2. Set flow rate (adjust pump voltage or valve)
3. Set head (adjust elevation or pump pressure)
4. Set load resistor (2.5Ω, 5Ω, or 10Ω)
5. Let system stabilize (30 seconds)

**Step 2: Baseline Measurement (1 min)**
1. Measure water temperature
2. Verify flow rate (flow meter or timed collection)
3. Verify head (pressure gauge or ruler)
4. Record ambient conditions

**Step 3: Data Collection (5 min)**
1. Start video recording (optional, for review)
2. Measure RPM (tachometer or count rotations)
3. Measure voltage across load (multimeter)
4. Measure current through load (multimeter)
5. Repeat 3 times (calculate average)
6. Observe: vibration, noise, spray pattern

**Step 4: Record Data (2 min)**
1. Write in lab notebook (ink, dated, signed)
2. Enter in spreadsheet:
   - Timestamp
   - Runner type (A/B/C)
   - Flow rate (L/min or L/s)
   - Head (m)
   - Load resistance (Ω)
   - RPM
   - Voltage (V)
   - Current (A)
   - Water temp (°C)
   - Notes/observations

**Step 5: Calculate Efficiency (2 min)**
```
Hydraulic Power (W):
P_hydro = ρ × g × Q × H
where:
  ρ = 1000 kg/m³ (water density)
  g = 9.81 m/s² (gravity)
  Q = flow rate (m³/s)
  H = head (m)

Electrical Power (W):
P_elec = V × I
where:
  V = voltage (V)
  I = current (A)

Efficiency (%):
η = (P_elec / P_hydro) × 100%
```

**Step 6: Next Test (5 min)**
1. Change variable (flow, load, or runner)
2. If changing runner: stop, remove, install new, resume
3. If same runner: adjust flow/load only

---

## 📊 DATA ANALYSIS

### Statistical Analysis (Research Agent + Data Analysis Agent)

**Descriptive Statistics:**
- Mean efficiency per runner: μ_A, μ_B, μ_C
- Standard deviation: σ_A, σ_B, σ_C
- Sample size: n = 20 per runner
- Efficiency range: min, max, median
- Operating range: flow rates where η > 50%

**Inferential Statistics:**
```python
from scipy import stats

# Two-sample t-test (Runner A vs B)
t_statistic, p_value = stats.ttest_ind(efficiency_A, efficiency_B)

# Hypothesis decision:
if p_value < 0.05:
    print("Reject H₀: Significant difference exists")
else:
    print("Fail to reject H₀: No significant difference")

# Effect size (Cohen's d):
pooled_std = sqrt(((n_A-1)*std_A^2 + (n_B-1)*std_B^2) / (n_A + n_B - 2))
cohens_d = (mean_A - mean_B) / pooled_std
# d > 0.8 = large effect, 0.5-0.8 = medium, < 0.5 = small
```

**Visualizations:**
1. **Efficiency vs Flow Rate** (line plot, all 3 runners)
2. **Box Plot** (compare efficiency distributions A, B, C)
3. **Bar Chart** (mean efficiency with error bars)
4. **Scatter Plot** (efficiency vs RPM, colored by runner)
5. **Histogram** (efficiency distribution, overlay all runners)

---

### Expected Results

**Hypothesis Validation Criteria:**
- ✅ **Pass:** μ_A - μ_B = 6-12%, p < 0.05
- ⚠️ **Marginal:** μ_A - μ_B = 3-6%, p < 0.10
- ❌ **Fail:** μ_A - μ_B < 3%, or p > 0.10

**Secondary Observations:**
- Vibration amplitude (Runner A should be lower)
- Acoustic signature (Runner A should be quieter)
- Operating range (Runner A should have wider high-efficiency band)

**Baseline Expectations:**
- Runner A: 58-68% efficiency (φ-optimized)
- Runner B: 52-60% efficiency (conventional)
- Runner C: 48-58% efficiency (too many blades = friction)

---

## 📝 DOCUMENTATION

### Lab Report (Research Documentation Agent)

**Generate within 24 hours of test completion**

**Structure:**
1. **Executive Summary** (100 words)
   - Hypothesis tested
   - Key result (% improvement, p-value)
   - Conclusion (validated or rejected)

2. **Introduction** (200 words)
   - Background (φ-optimization theory)
   - Prior art (what exists)
   - Research question

3. **Methods** (300 words)
   - Test rig description
   - Measurement procedure
   - Variables and controls
   - Statistical methods

4. **Results** (400 words + figures)
   - Data tables
   - Statistical tests
   - Visualizations
   - Observations

5. **Discussion** (300 words)
   - Interpretation
   - Comparison to theory
   - Limitations
   - Future work

6. **Conclusions** (100 words)
   - Hypothesis validation
   - Patent implications
   - Recommendations

7. **References** (10-15)
   - Prior art patents
   - Academic papers
   - Standards cited

8. **Appendices**
   - Raw data (CSV)
   - Photos/videos
   - Calculations
   - Equipment specs

---

### Patent Evidence Package

**Compile for provisional patent filing:**

1. **Test Data** (CSV file, all 60 tests)
2. **Statistical Analysis** (efficiency comparison, p-values)
3. **Visualizations** (high-res PNG, 300 DPI):
   - Efficiency curves
   - Box plots
   - Bar charts
4. **CAD Drawings** (PDF):
   - Runner A (21-blade φ)
   - Runner B (20-blade control)
   - Runner C (25-blade)
   - Dimensions and annotations
5. **Photos** (JPG, high-res):
   - Test rig overview
   - Runners side-by-side
   - Close-ups of blade geometry
6. **Video** (MP4, edited):
   - Test rig operation
   - Runner A vs B comparison
   - Vibration comparison
7. **Lab Report** (PDF, complete)

**File Naming Convention:**
```
GroupA_PhiTurbine_TestData_20260214.csv
GroupA_PhiTurbine_EfficiencyCurves_20260214.png
GroupA_PhiTurbine_RunnerA_CAD_20260214.pdf
GroupA_PhiTurbine_TestRig_Photo01.jpg
GroupA_PhiTurbine_LabReport_20260214.pdf
```

---

## ⚠️ QUALITY ASSURANCE

### Calibration & Validation
- [ ] Multimeter: Verify with known voltage source (battery)
- [ ] Flow meter: Cross-check with timed collection method
- [ ] Pressure gauge: Zero at atmospheric pressure
- [ ] Tachometer: Verify with strobe or count method
- [ ] Scale: Zero with empty container

### Data Quality Checks
- [ ] No missing values
- [ ] No obvious outliers (>3σ from mean)
- [ ] Measurements within expected physical limits:
  - Efficiency: 0-100% (should be 30-85%)
  - RPM: 0-3000 (should be 200-1500)
  - Power: >0 (should be 5-100W)
- [ ] Consistency: Repeat tests should be within 5%

### Error Sources & Mitigation
| Error Source | Impact | Mitigation |
|--------------|--------|------------|
| Temperature drift | Low | Test in climate-controlled space |
| Flow rate variation | Medium | Use flow meter, verify with bucket |
| Bearing friction | Medium | Use good bearings, lubricate |
| Electrical contact | High | Secure all connections, check resistance |
| Measurement error | Medium | Take 3 readings, average |
| Human error | High | Double-check data entry, peer review |

---

## 📅 TIMELINE

### Week 1 (Jan 26 - Feb 1)
- **Day 1 (Mon):** Order components, start CAD design
- **Day 2 (Tue):** Complete CAD, start printing Runner A
- **Day 3 (Wed):** Components arrive, continue printing
- **Day 4 (Thu):** Printing completes, start Runner B
- **Day 5 (Fri):** Assemble test rig, first test run
- **Day 6-7 (Weekend):** Troubleshoot, calibrate

### Week 2 (Feb 2 - 8)
- **Day 8-9 (Mon-Tue):** Test Runner A (20 tests)
- **Day 10-11 (Wed-Thu):** Test Runner B (20 tests)
- **Day 12 (Fri):** Test Runner C (20 tests)
- **Day 13-14 (Weekend):** Data analysis

### Week 3 (Feb 9 - 16)
- **Day 15 (Mon):** Lab report complete
- **Day 16-17 (Tue-Wed):** Patent specification draft
- **Day 18 (Thu):** Attorney review
- **Day 19 (Fri):** Revisions
- **Day 20-21 (Weekend):** **FILE PROVISIONAL PATENT #1** 🎯

---

## ✅ SUCCESS METRICS

### Week 1 Success
- [ ] Test rig operational
- [ ] All components working
- [ ] Runner A printed and tested
- [ ] Data logging working

### Week 2 Success
- [ ] 60 tests completed
- [ ] Data quality verified
- [ ] Statistical significance achieved (p < 0.05)
- [ ] Efficiency improvement: 6-12%

### Week 3 Success
- [ ] Lab report published
- [ ] Patent evidence compiled
- [ ] Provisional patent filed
- [ ] Application number received

---

## 🚨 CONTINGENCY PLANS

**Problem:** 3D printer fails  
**Solution:** Order runners from 3D Hubs, Shapeways, or local maker space

**Problem:** Pump too weak/strong  
**Solution:** Use voltage regulator to control pump speed

**Problem:** Data too noisy  
**Solution:** More tests (n=30 per runner), better sensors, reduce vibration

**Problem:** No significant difference  
**Solution:** Retest with improved setup, or pivot hypothesis (focus on vibration reduction)

**Problem:** Components delayed  
**Solution:** Start with simulation (CFD), order backups from multiple vendors

---

## 📞 SUPPORT

**Technical Questions:** Research Agent  
**Data Analysis:** Data Analysis Agent  
**Documentation:** Research Documentation Agent  
**Project Status:** Chief Engineering Agent

**Human Escalation:** If agents can't resolve in 24 hours

---

**PROTOCOL STATUS:** ✅ READY TO EXECUTE  
**NEXT ACTION:** Order components TODAY (Amazon cart ready)  
**DEADLINE:** Provisional patent filing by Feb 16, 2026

🚀 **LET'S VALIDATE THE HYPOTHESIS AND FILE PATENT #1!**
