"""
ENVIRONMENTAL ASSESSOR AGENT  
Impact studies, fish passage, ecological analysis, mitigation planning.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def environmental_impact(project_info):
    """Comprehensive environmental impact assessment"""
    
    prompt = f"""Environmental impact assessment for micro-hydro:

**Project:** {project_info}

**ENVIRONMENTAL IMPACT ASSESSMENT (EIA)**

---

**EXECUTIVE SUMMARY:**

Project: [Name, location, capacity]
Impact Level: Negligible / Minor / Moderate / Major
Recommendation: Proceed / Proceed with mitigation / Redesign / Abandon

---

**SECTION 1: PROJECT DESCRIPTION**

**Physical Components:**
- Intake structure (location, dimensions)
- Penstock (route, length, diameter)
- Powerhouse (footprint, height)
- Tailrace (discharge point)
- Access roads (new/improved)
- Transmission line (route, voltage)

**Construction:**
- Duration: __ months
- Workforce: __ people
- Equipment: [List]
- Material delivery: __ truck trips
- In-water work: __ days (timing)

**Operation:**
- Design flow: __ CFS (__ GPM)
- Bypass flow: __ CFS
- Dewatered reach: __ feet
- Operational mode: Run-of-river / Peaking
- Attended: Yes / No (remote SCADA)

---

**SECTION 2: AFFECTED ENVIRONMENT (BASELINE)**

**2.1 Aquatic Resources:**

**Stream Characteristics:**
- Stream order: [1st, 2nd, 3rd order]
- Gradient: __% 
- Width: __ feet (wetted at base flow)
- Depth: __ inches average
- Substrate: Boulder / Cobble / Gravel / Sand / Silt
- Habitat type: Pool / Riffle / Run / Cascade

**Fish Species Present:**

| Species | Status | Life Stage | Abundance | Habitat Use |
|---------|--------|------------|-----------|-------------|
| [Species 1] | T&E/Common | All/Spawning | High/Med/Low | [Description] |
| [Species 2] | ... | ... | ... | ... |

**Threatened/Endangered Species:**
- [List any ESA-listed species]
- Critical habitat: Yes / No
- Essential Fish Habitat (EFH): Yes / No

**Fish Passage:**
- Current conditions: Free passage / Partial barrier / Complete barrier
- Existing barriers: [Natural falls, dam, etc.]
- Migration timing: [Spring, fall]

**Spawning Areas:**
- Location: [Relative to project]
- Substrate: Gravel size (__-__ mm)
- Timing: [Months]
- Importance: High / Medium / Low

**Rearing Habitat:**
- Juvenile density: __ fish/sq meter
- Quality: High / Medium / Low
- Limiting factors: [Temperature, cover, food]

**Aquatic Invertebrates:**
- Macroinvertebrate survey results
- Biotic index: __ (Excellent/Good/Fair/Poor)
- Sensitive species present: Yes / No

**Water Quality:**

| Parameter | Existing | Standard | Meets? |
|-----------|----------|----------|--------|
| Temperature (°C) | __ | <18 (salmon) | Yes/No |
| Dissolved Oxygen (mg/L) | __ | >6 | Yes/No |
| pH | __ | 6.5-8.5 | Yes/No |
| Turbidity (NTU) | __ | <50 | Yes/No |
| Conductivity | __ | __ | Yes/No |

**2.2 Terrestrial Resources:**

**Vegetation:**
- Community type: Coniferous forest / Riparian / Shrub-steppe
- Dominant species: [List]
- Threatened/Endangered plants: [List or None]
- Invasive species: [List]
- Wetlands: __ acres (Type: Riverine, PEM, PSS, PFO)

**Wildlife:**
- Mammals: [Species observed or likely]
- Birds: [Raptors, songbirds, waterfowl]
- Amphibians: [Frogs, salamanders]
- Reptiles: [Snakes, lizards]

**Threatened/Endangered Species:**

| Species | Status | Habitat | Likelihood on-site | Impact potential |
|---------|--------|---------|--------------------|--------------------|
| [Species] | Listed/Candidate | [Description] | High/Med/Low | High/Med/Low |

**Critical Habitat:**
- Designated: Yes / No
- Species: [If yes]
- Habitat features: [PCEs - Primary Constituent Elements]

**2.3 Physical Environment:**

**Geology:**
- Bedrock: [Type]
- Soils: [NRCS series]
- Stability: Stable / Moderate / Unstable (landslide risk)
- Seismic: [Seismic zone]

**Hydrology:**
- Drainage area: __ sq miles
- Mean annual flow: __ CFS
- Flow regime: Snowmelt / Rainfall / Regulated
- Flood frequency: 10-year = __ CFS, 100-year = __ CFS

**Climate:**
- Annual precip: __ inches
- Temperature range: __°F to __°F
- Growing season: __ days

**2.4 Cultural Resources:**

- Historic properties: [Old mill, etc.]
- Archaeological sites: [Known or potential]
- Tribal: Traditional use / Treaty fishing / Sacred sites
- Recreation: Fishing / Kayaking / Hiking

---

**SECTION 3: ENVIRONMENTAL IMPACTS**

**3.1 Construction Phase Impacts:**

**Water Quality (Temporary):**

**Sediment/Turbidity:**
- **Impact:** Excavation and in-water work mobilize sediment
- **Magnitude:** __ NTU increase (monitored)
- **Duration:** __ weeks
- **Significance:** Minor (if BMPs implemented)
- **Species Affected:** Fish (gill damage, avoidance)

**Minimization:**
- Silt fences, sediment basins
- Isolate work area (coffer dams)
- Work during low-flow period (summer)
- Turbidity monitoring (real-time)
- Stop-work trigger (>10 NTU increase)

**Residual Impact:** Negligible

---

**Petroleum Spills:**
- **Risk:** Equipment refueling, hydraulic leaks
- **Magnitude:** 1-100 gallons potential
- **Significance:** Moderate if occurs
- **Minimization:** Spill kits, fueling away from stream, containment

---

**Vegetation Clearing:**
- **Impact:** __ acres cleared (access, staging, facilities)
- **Type:** Forest / Riparian / Upland
- **Significance:** Minor to Moderate
- **Minimization:** Limit clearing to minimum needed, retain mature trees, replant

---

**Wildlife Disturbance:**
- **Impact:** Noise, human presence
- **Species:** Nesting birds, denning mammals
- **Timing:** Avoid sensitive periods (Apr-Jul for birds)
- **Minimization:** Pre-construction surveys, timing restrictions, setbacks

---

**3.2 Operational Phase Impacts:**

**Hydrologic Alteration:**

**Dewatered Reach:**
- **Length:** __ feet (intake to tailrace)
- **Existing Flow:** __ CFS
- **Bypass Flow:** __ CFS (__% of mean)
- **Reduction:** __ CFS (__% reduction)
- **Impact:** Reduced wetted width, depth, habitat availability

**Significance Assessment:**
- **Negligible:** <10% flow reduction, high bypass flow
- **Minor:** 10-30% reduction, wetted perimeter maintained
- **Moderate:** 30-50% reduction, some habitat loss
- **Major:** >50% reduction, extensive dewatering

**This Project:** [Significance level] because [rationale]

---

**Mitigation:**
- **Increased bypass flow:** __ CFS (adaptive management)
- **Minimize reach length:** Design intake/tailrace close together
- **Habitat enhancement:** Add large woody debris, spawning gravel
- **Monitoring:** Annual fish surveys, photo points

---

**Flow Regime:**
- **Natural:** Seasonal variation (high spring, low summer)
- **With Project:** Similar pattern (run-of-river maintains regime)
- **Impact:** Negligible (no storage, no peaking)

---

**Temperature:**
- **Existing:** __°C (summer max)
- **Standard:** <18°C for salmon
- **Concern:** Dewatered reach could warm if low flow + sunny
- **Modeling:** Increase of __°C predicted (shade study)
- **Significance:** Minor / Moderate
- **Mitigation:** Adequate bypass flow, riparian shade preservation/enhancement

---

**Fish Entrainment/Impingement:**

**Entrainment (fish drawn into intake):**
- **Species at risk:** Juveniles, fry
- **Life stages:** [Months when present]
- **Magnitude:** __ fish/year estimated (T&E model)
- **Significance:** Moderate if ESA species

**Mitigation:**
- **Fish screens:** 1-2 mm mesh (excludes fry)
- **Approach velocity:** <0.5 ft/sec (fish can escape)
- **Screen type:** Rotating drum / Traveling / Fixed with airburst cleaning
- **Bypass:** Route screened fish back to stream
- **Cost:** $50k-150k

**Residual Impact:** Negligible to Minor

---

**Fish Passage:**

**Upstream:**
- **Existing:** Free passage
- **With Project:** Intake creates barrier (if not designed for passage)
- **Impact:** Blocks spawning migration = Major Impact

**Mitigation Options:**
1. **Fish Ladder:** $100k-500k, proven effective
2. **Nature-like fishway:** $200k-1M, mimics natural stream
3. **No passage needed:** If existing barrier upstream OR non-migratory species

**Recommendation:** [Ladder / Not needed / Design basis]

---

**Downstream:**
- **Risk:** Juveniles passing through turbine
- **Mortality:** __% (depends on turbine type, speed)
  - Francis turbine: 10-30% mortality
  - Kaplan: 5-15%
  - Pelton/Crossflow: <5% (low risk)

**Mitigation:**
- **Turbine selection:** Pelton (high head) = low mortality
- **Downstream bypass:** Surface collector, sluice gate
- **Seasonal shutdown:** During smolt outmigration (if needed)

---

**Habitat Fragmentation:**
- **Impact:** Population isolated above/below project
- **Significance:** Major (if no passage)
- **Significance:** Negligible (if fish ladder installed)

---

**Predation:**
- **Issue:** Fish congregate at barriers (easy prey for birds, otters)
- **Significance:** Minor
- **Mitigation:** Minimize attraction flows, provide cover

---

**Terrestrial Impacts:**

**Habitat Loss (Permanent):**
- **Footprint:** __ acres (powerhouse, access road)
- **Type:** Forest / Wetland / Riparian
- **Significance:** Minor (small footprint)
- **Mitigation:** Off-site restoration (__:__ ratio)

**Noise:**
- **Source:** Turbine operation (__ dB at __ feet)
- **Receptors:** Wildlife, residences (if nearby)
- **Significance:** Negligible (low noise, remote)

**Visual:**
- **Change:** Powerhouse building, transmission line
- **Viewers:** Hikers, kayakers
- **Significance:** Minor (small structure, landscaping)

---

**3.3 Cumulative Impacts:**

**Concept:** Combined effects of this + other past, present, future projects

**Other Projects in Watershed:**
- Existing dams: [List]
- Proposed hydro: [List]
- Logging/mining: [Activities]
- Water withdrawals: [Agriculture, municipal]

**Cumulative Hydrologic Alteration:**
- Total flow reduction: __% of watershed
- Significance: Minor / Moderate / Major

**Cumulative Habitat Loss:**
- This project: __ acres
- Other projects: __ acres
- Total: __ acres = __% of available habitat
- Significance: [Assessment]

**Assessment:** Cumulative impacts are [Negligible / Minor / Moderate / Major]

---

**SECTION 4: MITIGATION HIERARCHY**

**Step 1: AVOIDANCE (Best Option)**
- Site selection (avoid sensitive streams)
- Design (run-of-river, no storage)
- Timing (work outside spawning/nesting)

**Step 2: MINIMIZATION**
- High bypass flows (30-50% mean flow)
- Short dewatered reach (<500 feet)
- Fish-friendly design (screens, passage)
- Construction BMPs

**Step 3: MITIGATION (Compensate for unavoidable impacts)**
- Habitat restoration elsewhere in watershed
- Barrier removal (net benefit to fish passage)
- Riparian planting (shade, bank stability)
- Large woody debris placement

**Mitigation Ratio:** __:__ (restore __ acres for __ acres impacted)

**Mitigation Cost:** $__

---

**SECTION 5: MONITORING & ADAPTIVE MANAGEMENT**

**Pre-Construction (Baseline):**
- Fish surveys (Year -2, Year -1)
- Water quality (continuous temperature loggers)
- Habitat mapping (photo points, transects)

**Construction:**
- Turbidity (real-time, stop-work trigger)
- Compliance inspections (weekly)
- Wildlife monitoring (active nests)

**Post-Construction (Years 1-10):**

**Fish Population:**
- **Method:** Electrofishing, snorkel surveys
- **Timing:** Summer (low flow)
- **Metrics:** Density (fish/sq meter), size distribution, species composition
- **Frequency:** Annual (Years 1-5), Biennial (Years 6-10)
- **Compare to:** Baseline, reference stream

**Fish Passage:**
- **Method:** PIT tags, video monitoring
- **Metrics:** Passage efficiency (%), passage time
- **Frequency:** Annual (Years 1-3)
- **Threshold:** <80% efficiency = investigate/modify

**Water Quality:**
- **Temperature:** Continuous (15-min intervals)
- **Dissolved Oxygen:** Quarterly spot checks
- **Threshold:** >18°C or <6 mg/L = adaptive management

**Bypass Flow Compliance:**
- **Continuous monitoring:** USGS gauge or pressure transducer
- **Reporting:** Annual to state water agency
- **Threshold:** <90% compliance = violation, corrective action

**Adaptive Management Triggers:**

| Indicator | Threshold | Action |
|-----------|-----------|--------|
| Fish population decline | >20% vs. baseline | Increase bypass flow 10% |
| Passage efficiency | <80% | Modify ladder, add attraction flow |
| Temperature exceedance | >18°C for >7 days | Increase bypass, add shade |
| Entrainment | >__ fish/year (T&E) | Modify screens, seasonal shutdown |

**Reporting:**
- Annual monitoring report to agencies
- Photo documentation (standardized locations)
- Recommendations for adaptive management

**Duration:** Years 1-10 (intensive), then reduced monitoring as specified by permits

**Cost:** $30k-60k per year (Years 1-5), $10k-20k per year (Years 6-10)

---

**SECTION 6: ALTERNATIVES ANALYSIS**

**Alternative 1: No Action**
- Description: Do not build project
- Environmental: No impacts (but also no clean energy)
- Economic: Lost opportunity

**Alternative 2: Proposed Action**
- Description: [As described above]
- Environmental: [Impact summary]
- Economic: [Cost-benefit]

**Alternative 3: Different Site**
- Description: Site B (different location)
- Environmental: [Comparison - may have fewer species]
- Economic: [Cost difference]

**Alternative 4: Smaller Capacity**
- Description: 50 kW vs. 100 kW (lower diversion)
- Environmental: Reduced impacts (less flow diverted)
- Economic: Lower revenue

**Alternative 5: Different Technology**
- Description: Solar PV array instead
- Environmental: No aquatic impacts, land use
- Economic: [LCOE comparison]

**Preferred Alternative:** [Selection and rationale]

---

**SECTION 7: REGULATORY COMPLIANCE**

**Endangered Species Act:**
- Section 7 consultation required: Yes / No
- Species: [List]
- Conclusion: No Effect / NLAA / LAA
- Mitigation: [Summary]

**Clean Water Act:**
- Section 404 permit: Required
- Wetland impacts: __ acres
- Section 401 certification: Required
- Conditions: [Bypass flow, monitoring]

**National Environmental Policy Act:**
- NEPA document: EA / EIS
- Finding: FONSI / Significant Impact

**State Environmental Review:**
- Document: SEPA/CEQA checklist
- Determination: DNS / DS / EIS

**Fish & Wildlife Coordination Act:**
- Consultation: USFWS, state fish & wildlife
- Recommendations: [Bypass flow, passage]

**State Endangered Species Act:**
- Species: [If different from federal]
- Requirements: [Permits, mitigation]

---

**SECTION 8: CONCLUSIONS & RECOMMENDATIONS**

**Impact Summary:**

| Resource | Construction Impact | Operational Impact | Mitigation | Residual Impact |
|----------|---------------------|---------------------|------------|-----------------|
| Water Quality | Minor (temp) | Negligible | BMPs | Negligible |
| Fish Habitat | Minor | Moderate | High bypass, monitoring | Minor |
| Fish Passage | None | Major (if no ladder) | Fish ladder | Negligible |
| Terrestrial | Minor | Negligible | Restoration | Negligible |

**Overall Environmental Acceptability:** 

✅ **ACCEPTABLE** if mitigation measures implemented:
- High bypass flow (≥30% mean annual flow)
- Fish screens (1-2 mm mesh, low approach velocity)
- Fish passage (upstream ladder if needed)
- Habitat restoration (2:1 ratio)
- Long-term monitoring and adaptive management

⚠️ **CONDITIONAL** if:
- ESA-listed species present (requires full Section 7)
- Critical habitat (may need RPA)
- Outstanding fishery (stakeholder opposition likely)

❌ **NOT ACCEPTABLE** if:
- Jeopardy finding under ESA
- Unable to maintain water quality standards
- State opposes due to fish impacts

**Recommendation:** 

**Proceed with project** subject to:
1. Obtain all required permits (FERC, Corps, state)
2. Implement all mitigation measures as designed
3. Conduct 10-year monitoring program
4. Commit to adaptive management (increase bypass if needed)
5. Budget $300k-800k for environmental compliance (fish passage, mitigation, monitoring)

**Environmental Viability:** Medium-High (manageable impacts with proper design and mitigation)

This assessment provides agency-quality analysis for permitting."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def fish_passage_design(species_requirements):
    """Design fish passage facilities"""
    
    prompt = f"""Design fish passage system:

**Species:** {species_requirements}

Provide complete fish passage design including:
- Upstream passage (fish ladder type selection)
- Downstream passage (bypass or turbine screening)
- Hydraulic design criteria
- Attraction flow requirements
- Cost estimates
- Operation and maintenance plan

Include species-specific requirements (salmon vs. trout vs. resident fish)."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

def mitigation_plan(impact_summary):
    """Develop compensatory mitigation plan"""
    
    prompt = f"""Create mitigation plan for impacts:

**Impacts:** {impact_summary}

**COMPENSATORY MITIGATION PLAN**

Develop comprehensive plan including:

**On-Site Mitigation:**
- Habitat enhancement in dewatered reach
- Riparian planting (species, spacing, maintenance)
- Large woody debris placement
- Spawning gravel addition

**Off-Site Mitigation:**
- Barrier removal elsewhere (opens __ miles)
- Stream restoration (increase habitat by __ acres)
- Conservation easements
- Hatchery supplementation (if appropriate)

**Mitigation Ratios:**
- Wetland: 2:1 (restore 2 acres for 1 acre impacted)
- Fish habitat: 3:1 (conservative for functional lift)

**Implementation Schedule:**
- Year 1 (construction): [Actions]
- Year 2-3: [Establishment]
- Year 4-10: [Monitoring, maintenance]

**Success Criteria:**
- Vegetation survival (80% after 5 years)
- Fish use (present in mitigation area)
- Function (equivalent or better than baseline)

**Monitoring & Reporting:**
- Annual monitoring reports
- Photo documentation
- Adaptive management if not meeting criteria

**Cost:** $__ (implementation) + $__ (monitoring)

Provide agency-ready mitigation plan."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def environmental_monitoring_protocol(project_details):
    """Create monitoring program for compliance"""
    
    prompt = f"""Design environmental monitoring program:

**Project:** {project_details}

**ENVIRONMENTAL MONITORING PROTOCOL**

**Pre-Construction Baseline (2 years):**

**Fish Surveys:**
- Method: Electrofishing, snorkel surveys
- Season: Summer (July-August low flow)
- Frequency: 2 passes per year
- Metrics: Species, density, size distribution
- Location: Project reach + reference reach
- Cost: $15k per year

**Water Quality:**
- Temperature: Continuous loggers (15-min intervals), 4 locations
- DO, pH, turbidity: Monthly spot checks
- Lab analysis: Quarterly (nutrients, metals)
- Cost: $10k per year

**Habitat:**
- Cross-section surveys (10 transects)
- Substrate pebble counts
- Photo points (standardized)
- Large woody debris inventory
- Cost: $8k per year

---

**Construction Monitoring (Real-Time):**

**Turbidity:**
- Continuous monitors upstream and downstream
- Alarmed at >10 NTU increase
- Stop-work protocol if exceeded
- Daily logs
- Cost: $5k equipment + $2k per month

**Wildlife:**
- Nest surveys (if active nests nearby)
- Daily logs of wildlife observations
- Stop-work buffers (300 ft for eagles, 100 ft for songbirds)
- Cost: $5k

**Compliance:**
- Weekly inspections (environmental monitor)
- BMP effectiveness (silt fences, etc.)
- Photo documentation
- Agency reporting (if required)
- Cost: $3k per month

---

**Post-Construction (Operational - Years 1-10):**

**Year 1-3 (Intensive):**

**Fish Population:**
- Annual surveys (same methods as baseline)
- Passage effectiveness (PIT tags, video)
- Entrainment/mortality (netting at tailrace)
- Compare to baseline and reference
- Report to agencies
- Cost: $40k per year

**Water Quality:**
- Temperature: Continuous
- DO: Monthly
- Annual summary and comparison to baseline
- Cost: $12k per year

**Bypass Flow:**
- Continuous monitoring (flow meter or stage)
- Verify compliance with permit (__ CFS minimum)
- Annual report
- Cost: $5k per year (included in SCADA)

**Habitat:**
- Photo points (annual)
- Cross-sections (Year 1, Year 3)
- Qualitative assessment
- Cost: $5k per year

**Year 4-10 (Reduced):**

- Fish surveys: Every 2 years
- Water quality: Continuous temp, quarterly DO
- Photo points: Annual
- Cost: $15k per year

**Year 10+:**
- Long-term compliance monitoring per permit requirements
- Typically reduced to temperature and flow only
- Cost: $5k per year

---

**Adaptive Management:**

**Triggers and Responses:**

| Indicator | Trigger | Action | Cost |
|-----------|---------|--------|------|
| Fish population | >20% decline | Increase bypass 10% | Lost revenue $__/yr |
| Temperature | >18°C for 7+ days | Increase bypass, add shade | $__ |
| Passage | <80% efficiency | Modify ladder, add flow | $50k-150k |
| Entrainment | >__ T&E fish/yr | Screen upgrade, shutdown | $30k-100k |

**Decision Process:**
1. Exceedance detected (monitoring data)
2. Report to agencies within 30 days
3. Investigate cause (consultation with biologist)
4. Propose corrective action
5. Implement (if approved)
6. Continue monitoring (verify effectiveness)

---

**Reporting:**

**Annual Monitoring Report (to agencies):**
- Cover letter (summary of compliance)
- Fish survey results (tables, graphs)
- Water quality summary (exceedances noted)
- Flow compliance (% of time at required bypass)
- Photos (site conditions)
- Adaptive management actions (if any)
- Recommendations (continue monitoring, modifications)
- Due date: [Typically March 31 for prior calendar year]

**Cost:** $8k per report (technical writing, graphics)

---

**Total Monitoring Costs:**

**Pre-Construction (Years -2 to -1):** $33k × 2 = $66k
**Construction (6 months):** $15k
**Post-Construction:**
- Years 1-3: $65k × 3 = $195k
- Years 4-10: $15k × 7 = $105k
- Years 11+: $5k × 15 = $75k (assumes 25-year project)

**25-Year Total:** $456k

**NPV @ 8% discount:** $__

**As % of Project CAPEX:** __% (typically 5-15% for well-designed projects)

---

**Data Management:**

**Database:**
- Excel or Access (small projects)
- Specialized software (large projects)
- Backup protocol (cloud storage)

**Quality Assurance:**
- Field data sheets (standardized)
- Data entry verification (double-check)
- Chain of custody (water samples)
- Calibration logs (equipment)

**Archiving:**
- Retain all data for project life + 10 years
- Provide to agencies upon request
- Include in project asset files (for sale/transfer)

This protocol ensures regulatory compliance and project success."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Environmental Assessor initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: impact, fish_passage, mitigation, monitoring")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'impact':
            info = sys.argv[2] if len(sys.argv) > 2 else '100 kW project, salmon stream, 500ft dewatered reach'
            print(environmental_impact(info))
        elif cmd == 'fish_passage':
            species = sys.argv[2] if len(sys.argv) > 2 else 'Chinook salmon, Coho salmon, Steelhead'
            print(fish_passage_design(species))
        elif cmd == 'mitigation':
            summary = sys.argv[2] if len(sys.argv) > 2 else '0.5 acre wetland impact, 500ft dewatered reach'
            print(mitigation_plan(summary))
        elif cmd == 'monitoring':
            details = sys.argv[2] if len(sys.argv) > 2 else '75 kW, ESA consultation required'
            print(environmental_monitoring_protocol(details))
