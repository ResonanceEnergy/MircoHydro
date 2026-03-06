"""
HYDRO MAPPER AGENT
Site identification, resource assessment, geographic analysis, feasibility scoring.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def map_water_resources(region):
    """Identify potential micro-hydro sites in a region"""
    
    prompt = f"""Identify and map potential micro-hydro sites in: {region}

**WATER RESOURCE MAPPING REPORT**

---

**REGION ANALYSIS: {region}**

---

**STEP 1: HYDROLOGICAL INVENTORY**

**River Systems:**

| River/Stream Name | Length (mi) | Avg Flow (CFS) | Gradient | Access | Priority |
|-------------------|-------------|----------------|----------|--------|----------|
| [River 1] | __ | __ | High/Med/Low | Good/Fair/Poor | High |
| [River 2] | __ | __ | High/Med/Low | Good/Fair/Poor | High |
| [River 3] | __ | __ | High/Med/Low | Good/Fair/Poor | Medium |

**Irrigation Canals:**
- Canal system 1: [Name, flow, drop]
- Canal system 2: [Name, flow, drop]
- Canal system 3: [Name, flow, drop]

**Water Treatment Facilities:**
- Facility 1: [Name, outflow volume, elevation change]
- Facility 2: [Name, outflow volume, elevation change]

**Industrial Water Systems:**
- Cooling water outflows
- Process water discharge
- Mine water pumping

---

**STEP 2: SITE IDENTIFICATION CRITERIA**

**Minimum Requirements:**
- ✅ Flow rate: 50+ GPM (0.11+ CFS) minimum
- ✅ Head (elevation drop): 10+ feet
- ✅ Year-round flow (not seasonal)
- ✅ Property access rights
- ✅ Grid connection within 1 mile
- ✅ No protected/endangered species habitat

**Ideal Characteristics:**
- 🌟 Flow rate: 200+ GPM
- 🌟 Head: 30+ feet
- 🌟 Existing infrastructure (old mill, dam)
- 🌟 Industrial/commercial property nearby
- 🌟 Supportive local regulations
- 🌟 Existing road access

---

**STEP 3: POTENTIAL SITES IDENTIFIED**

**SITE #1: [Site Name/Location]**

**Coordinates:** [Lat, Long]

**Resource Assessment:**
- **Flow Rate:** ___ GPM (___ CFS)
- **Head:** ___ feet
- **Estimated Power:** ___ kW
- **Flow Regime:** Perennial / Seasonal / Regulated

**Site Characteristics:**
- **Land Ownership:** Private / Public / Mixed
- **Current Use:** Agricultural / Industrial / Undeveloped
- **Access:** Road within ___ feet
- **Grid Distance:** ___ miles
- **Existing Infrastructure:** Dam / Weir / Canal / None

**Feasibility Score:** __/100
- Resource quality: __/30
- Site access: __/20
- Regulatory: __/20
- Economic: __/20
- Environmental: __/10

**Estimated System:**
- Capacity: ___ kW
- Annual generation: ___ MWh
- Capital cost: $___
- Annual revenue: $___
- Simple payback: ___ years

**Next Steps:**
1. Site visit and flow measurement
2. Property owner contact
3. Environmental screening
4. Preliminary engineering

**Priority:** 🔴 High / 🟡 Medium / 🟢 Low

---

**SITE #2: [Site Name/Location]**
[Repeat format...]

---

**SITE #3: [Site Name/Location]**
[Repeat format...]

---

[Continue for all identified sites...]

---

**STEP 4: GEOGRAPHIC ANALYSIS**

**Topography:**
- Mountainous regions (high gradient streams)
- Foothill areas (moderate gradient)
- Valley floors (low gradient, higher flow)
- Elevation range: ___ to ___ feet

**Geology:**
- Bedrock type (affects foundation design)
- Soil stability (landslide risk)
- Seismic activity (earthquake considerations)

**Climate:**
- Annual precipitation: ___ inches
- Seasonal patterns (wet/dry seasons)
- Temperature extremes
- Freeze risk (winterization needs)

**Land Use:**
- Agricultural: ___%
- Forest: ___%
- Urban/Suburban: ___%
- Industrial: ___%
- Protected lands: ___%

---

**STEP 5: INFRASTRUCTURE MAPPING**

**Electrical Grid:**
- Transmission lines: [Voltages, locations]
- Substations: [Locations, capacity]
- Distribution lines: [Coverage map]
- Grid interconnection points: [Identify nearest]

**Transportation:**
- Highways: [Major routes]
- Local roads: [Access to sites]
- Bridges: [Weight limits for equipment delivery]
- Distance to major cities: [For workforce, materials]

**Existing Dams/Weirs:**
- Historic sites (old mills, power stations)
- Irrigation infrastructure
- Flood control structures
- Potential for re-powering

---

**STEP 6: REGULATORY LANDSCAPE**

**Water Rights:**
- Prior appropriation states: [Filing required]
- Riparian rights states: [Existing rights]
- Permit requirements: [FERC, state agencies]

**Environmental Regulations:**
- Endangered Species Act (ESA) considerations
- Clean Water Act (Section 404 permits)
- State environmental review (NEPA/SEPA)
- Fish passage requirements

**Land Use/Zoning:**
- County zoning designations
- Conditional use permits needed
- Building permits
- Setback requirements

**Utility Regulations:**
- Net metering availability
- Interconnection standards (IEEE 1547)
- Power purchase agreements
- Renewable energy incentives

---

**STEP 7: COMPETITIVE ANALYSIS**

**Existing Renewable Energy:**
- Solar installations: [Map locations, capacity]
- Wind farms: [Locations]
- Other hydro: [Existing projects]
- Biomass/geothermal: [If applicable]

**Market Dynamics:**
- Electricity rates: $___ per kWh
- Rate trends (increasing/stable/decreasing)
- Demand growth projections
- Incentive programs available

**Competitive Advantages:**
- Areas with high electricity costs
- Limited solar potential (cloudy, forested)
- Strong water resources
- Supportive policies

---

**STEP 8: PRIORITIZATION MATRIX**

| Site | Resource (30) | Access (20) | Regulatory (20) | Economic (20) | Env (10) | Total | Rank |
|------|---------------|-------------|-----------------|---------------|----------|-------|------|
| Site 1 | __ | __ | __ | __ | __ | __ | 1 |
| Site 2 | __ | __ | __ | __ | __ | __ | 2 |
| Site 3 | __ | __ | __ | __ | __ | __ | 3 |

**Top 10 Priority Sites:**
1. [Site name] - Score __, Est. ___ kW
2. [Site name] - Score __, Est. ___ kW
3. [Site name] - Score __, Est. ___ kW
[...]

---

**STEP 9: MARKET POTENTIAL**

**Total Sites Identified:** ___
**High Priority (80+ score):** ___
**Medium Priority (60-79):** ___
**Low Priority (<60):** ___

**Aggregate Potential:**
- Total capacity: ___ MW
- Annual generation: ___ GWh
- Capital investment: $___ million
- Annual revenue: $___ million
- Jobs created: ___ (construction + operations)

**Market Penetration Strategy:**
1. Target top 10 sites (quick wins)
2. Develop 3-5 demonstration projects
3. Build regional reputation
4. Scale to medium-priority sites
5. Partnerships for low-priority sites

---

**STEP 10: EXECUTION ROADMAP**

**Phase 1 (Months 1-3): Site Validation**
- Conduct site visits (top 10)
- Flow measurements (30-day minimum)
- Property owner outreach
- Preliminary cost estimates

**Phase 2 (Months 4-6): Feasibility Studies**
- Detailed engineering (top 5)
- Environmental assessments
- Permitting strategy
- Financial modeling

**Phase 3 (Months 7-12): Project Development**
- Secure site control (leases/purchases)
- Complete permit applications
- Customer acquisition
- Financing arrangements

**Phase 4 (Year 2+): Construction & Operations**
- Build first 3-5 projects
- Prove concept and economics
- Refine processes
- Scale to additional sites

---

**DELIVERABLES:**

1. **GIS Map Package:**
   - Site locations (KML/Shapefile)
   - Hydrologic network
   - Infrastructure overlay
   - Protected areas
   - Ownership boundaries

2. **Site Summary Database:**
   - Spreadsheet with all sites
   - Key metrics and scores
   - Contact information
   - Status tracking

3. **Priority Site Profiles:**
   - 2-page summary per site
   - Photos (Google Earth/Street View)
   - Preliminary economics
   - Risk assessment

4. **Regional Strategy Document:**
   - Market opportunity
   - Competitive positioning
   - Go-to-market plan
   - Resource requirements

---

**DATA SOURCES:**

- **USGS National Hydrography Dataset (NHD)**
- **USGS StreamStats** (flow estimates)
- **State water resource agencies**
- **County GIS departments** (parcels, zoning)
- **Google Earth** (reconnaissance)
- **Utility interconnection maps**
- **FERC hydropower database** (existing projects)
- **State energy offices** (incentive programs)

---

**RECOMMENDATIONS:**

**Immediate Actions:**
1. Field reconnaissance of top 5 sites
2. Contact property owners (sites 1-3)
3. Request historical flow data from USGS
4. Meet with county planning departments
5. Engage environmental consultant for screening

**Resource Needs:**
- GIS analyst/software (QGIS or ArcGIS)
- Hydrologist (flow measurement and analysis)
- Engineer (preliminary design)
- Business development (property owner outreach)
- Legal (water rights review)

**Timeline:** 3-6 months for comprehensive regional assessment

**Budget:** $50k-100k (depending on region size and site count)

This is a data-driven, systematic approach to identifying the best micro-hydro opportunities."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def assess_site_potential(site_data):
    """Detailed site assessment and feasibility scoring"""
    
    prompt = f"""Conduct detailed assessment of micro-hydro site:

**Site Data:** {site_data}

**SITE FEASIBILITY ASSESSMENT**

---

**SITE IDENTIFICATION:**
- Site Name: [Name]
- Location: [Address/Coordinates]
- County/State: [Location]
- Parcel ID: [Tax parcel number]

---

**HYDROLOGIC ASSESSMENT:**

**Flow Characteristics:**
- **Average Flow:** ___ GPM (___ CFS)
- **Minimum Flow (90% exceedance):** ___ GPM
- **Maximum Flow (10% exceedance):** ___ GPM
- **Flow Regime:** Perennial / Seasonal / Regulated
- **Flow Measurement Method:** Gauged / Estimated / Modeled

**Flow Duration Curve:**
```
| Exceedance % | Flow (GPM) | Power (kW) | Hours/Year | Energy (MWh) |
|--------------|------------|------------|------------|--------------|
| 10% (high)   | ___        | ___        | 876        | ___          |
| 50% (median) | ___        | ___        | 4380       | ___          |
| 90% (low)    | ___        | ___        | 7884       | ___          |
```

**Head (Elevation Drop):**
- **Gross Head:** ___ feet (survey measurement)
- **Friction Losses:** ___ feet (pipe, intake, tailrace)
- **Net Head:** ___ feet (available for generation)
- **Head Measurement Method:** Topographic map / GPS / Survey

**Power Potential:**

Formula: P (kW) = (Q × H × η × 0.085)
- Q = Flow (CFS)
- H = Net Head (feet)
- η = Efficiency (0.70-0.85)

**At Design Flow:**
- Flow: ___ CFS
- Net Head: ___ feet
- Efficiency: 0.75 (estimate)
- **Power Output: ___ kW**

**Annual Energy Production:**
- Average generation: ___ kW
- Capacity factor: ___% (based on flow duration)
- **Annual Energy: ___ MWh**

---

**SITE CHARACTERISTICS:**

**Topography:**
- Slope: ___% (___ degrees)
- Terrain: Steep / Moderate / Gentle
- Vegetation: Forest / Grassland / Agricultural
- Soil Type: [From NRCS soil survey]

**Access:**
- Road Access: Paved / Gravel / 4WD only / None
- Distance from Public Road: ___ feet
- Bridge/Crossing Needed: Yes / No
- Equipment Access: Good / Fair / Poor
- **Access Score: __/20**

**Existing Infrastructure:**
- Dam/Weir: Present (condition: ___) / Absent
- Old Powerhouse: Yes / No (condition if present)
- Penstock Route: Existing / New required
- Tailrace: Existing / New required
- Transmission Line Distance: ___ miles
- **Infrastructure Score: __/20**

**Property Characteristics:**
- Land Ownership: Private / Public / Mixed
- Owner Contact: [Known / Research needed]
- Current Use: Agricultural / Forest / Industrial / Vacant
- Zoning: [Designation]
- Property Size: ___ acres
- **Property Score: __/15**

---

**TECHNICAL FEASIBILITY:**

**System Sizing:**
- **Turbine Type:** Pelton / Turgo / Crossflow / Francis
  - Selection based on head and flow characteristics
- **Generator:** Synchronous / Induction / Permanent magnet
- **Rated Capacity:** ___ kW
- **Design Flow:** ___ GPM
- **Design Head:** ___ feet

**Major Components:**

1. **Intake Structure:**
   - Type: Run-of-river / Small weir / Existing dam
   - Fish screen: Required / Not required
   - Sediment management: Settling basin / Self-cleaning screen
   - Estimated Cost: $___

2. **Penstock:**
   - Material: HDPE / Steel / PVC
   - Diameter: ___ inches
   - Length: ___ feet
   - Estimated Cost: $___

3. **Powerhouse:**
   - Size: ___ sq ft
   - Foundation: Concrete pad / Building
   - Access: [Description]
   - Estimated Cost: $___

4. **Turbine-Generator Unit:**
   - Manufacturer: [TBD based on specifications]
   - Efficiency: ___% at design point
   - Estimated Cost: $___

5. **Electrical/Controls:**
   - Switchgear, inverter (if needed), SCADA
   - Estimated Cost: $___

6. **Interconnection:**
   - Grid connection point: ___ feet
   - Transformer: Required / Existing
   - Estimated Cost: $___

**Total Capital Cost Estimate:**
- Equipment: $___
- Civil works: $___
- Electrical: $___
- Engineering (10-15%): $___
- Permitting (5-10%): $___
- Contingency (15-20%): $___
- **TOTAL: $___**

**Cost per kW:** $___ (benchmark: $3,000-8,000/kW)

**Technical Feasibility Score: __/25**

---

**REGULATORY FEASIBILITY:**

**Water Rights:**
- State System: Prior appropriation / Riparian / Hybrid
- Existing Rights: [Research status]
- New Permit Required: Yes / No
- Approval Timeline: ___ months
- **Score: __/20**

**Environmental Permits:**

Required Permits (typical):
- [ ] FERC License/Exemption (if navigable water)
- [ ] State water quality certification (§401)
- [ ] Army Corps wetlands permit (§404)
- [ ] State environmental review
- [ ] Endangered Species Act consultation
- [ ] State fish passage requirements

**Environmental Concerns:**
- Threatened/Endangered Species: [List if present]
- Critical Habitat: Yes / No
- Fish Passage: Required / Not required
- Minimum Instream Flow: ___ GPM required
- **Environmental Risk: Low / Medium / High**

**Permitting Timeline:** ___ months (typical: 12-36 months)

**Regulatory Feasibility Score: __/20**

---

**ECONOMIC FEASIBILITY:**

**Revenue Projections:**

**Option 1: Net Metering**
- Annual Energy: ___ MWh
- Avoided Cost: $___ per kWh (retail rate)
- **Annual Value: $___**

**Option 2: Wholesale/PPA**
- Annual Energy: ___ MWh
- Wholesale Rate: $___ per kWh
- **Annual Value: $___**

**Option 3: Behind-the-Meter**
- Customer Load: ___ kW
- Energy Offset: ___ MWh
- Rate: $___ per kWh
- **Annual Savings: $___**

**Operating Costs:**
- Maintenance (2x/year): $___ per year
- Insurance: $___ per year
- Administration: $___ per year
- Property lease (if applicable): $___ per year
- **Total Annual Costs: $___**

**Net Operating Income:** $___ per year

**Financial Metrics:**

**Simple Payback:** 
- Capital Cost / Annual Net Income = ___ years

**Discounted Cash Flow (25-year project life):**
- Discount Rate: 8%
- NPV: $___
- IRR: ___%
- Levelized Cost of Energy (LCOE): $___ per kWh

**Sensitivity Analysis:**

| Scenario | Capital Cost | Revenue | Payback |
|----------|--------------|---------|---------|
| Base Case | $___        | $___    | ___ yrs |
| Optimistic | -20%       | +20%    | ___ yrs |
| Pessimistic | +20%      | -20%    | ___ yrs |

**Economic Feasibility Score: __/20**

---

**RISK ASSESSMENT:**

**Technical Risks:**
- Flow variability (drought risk): Low / Med / High
- Sedimentation: Low / Med / High
- Flood damage: Low / Med / High
- Equipment failure: Low / Med / High
- **Mitigation:** [Strategies]

**Regulatory Risks:**
- Permit denial/delay: Low / Med / High
- Environmental opposition: Low / Med / High
- Water rights conflict: Low / Med / High
- **Mitigation:** [Strategies]

**Financial Risks:**
- Cost overruns: Low / Med / High
- Revenue shortfall: Low / Med / High
- Interest rate risk: Low / Med / High
- **Mitigation:** [Strategies]

**Property Risks:**
- Access denial: Low / Med / High
- Land lease termination: Low / Med / High
- Competing uses: Low / Med / High
- **Mitigation:** [Strategies]

**Overall Risk Level:** Low / Medium / High

---

**COMPOSITE FEASIBILITY SCORE:**

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Resource Quality | 25% | __/25 | __ |
| Technical | 20% | __/20 | __ |
| Regulatory | 20% | __/20 | __ |
| Economic | 20% | __/20 | __ |
| Access/Property | 15% | __/15 | __ |
| **TOTAL** | **100%** | **__/100** | **__** |

**Site Classification:**
- **90-100:** Excellent (proceed immediately)
- **75-89:** Good (high priority)
- **60-74:** Fair (medium priority)
- **<60:** Poor (defer or abandon)

---

**RECOMMENDATION:**

**Overall Assessment:** [Excellent / Good / Fair / Poor]

**Proceed with Development?** ✅ Yes / ⏸️ Maybe / ❌ No

**Rationale:**
[Explanation of recommendation based on scores and risks]

**Next Steps (if proceed):**
1. [Action item 1 with timeline]
2. [Action item 2 with timeline]
3. [Action item 3 with timeline]

**Resources Needed:**
- Personnel: [Roles needed]
- Budget: $___ for next phase
- Timeline: ___ months to [milestone]

**Critical Success Factors:**
- [Factor 1]
- [Factor 2]
- [Factor 3]

**Deal-Breakers (that would stop project):**
- [Condition 1]
- [Condition 2]

---

This assessment provides a comprehensive, objective evaluation to support go/no-go decisions."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def flow_analysis(location, method="estimate"):
    """Analyze water flow characteristics"""
    
    prompt = f"""Analyze water flow for potential micro-hydro site:

**Location:** {location}
**Analysis Method:** {method}

**FLOW ANALYSIS REPORT**

---

**OBJECTIVE:** Determine if water resource can support viable micro-hydro generation

---

**METHOD 1: USGS GAUGE DATA** (Most Accurate)

If USGS gauge exists on or near stream:

**Gauge Information:**
- Station ID: [Number]
- Station Name: [Name]
- Location: [Lat/Long]
- Period of Record: [Start - End]
- Drainage Area: ___ sq miles

**Historical Flow Statistics:**

| Statistic | Value (CFS) | Value (GPM) |
|-----------|-------------|-------------|
| Mean Annual | ___ | ___ |
| 10-percentile | ___ | ___ |
| 25-percentile | ___ | ___ |
| 50-percentile (median) | ___ | ___ |
| 75-percentile | ___ | ___ |
| 90-percentile | ___ | ___ |
| Record High | ___ | ___ |
| Record Low | ___ | ___ |

**Reliability:** High (measured data)

---

**METHOD 2: USGS STREAMSTATS** (Modeled Estimates)

If no gauge, use USGS StreamStats tool:

**Watershed Delineation:**
- Drainage Area: ___ sq miles
- Mean Annual Precipitation: ___ inches
- Basin Shape/Slope: [Description]

**Estimated Flow Statistics:**

**Mean Annual Flow:** ___ CFS (___ GPM)

**Regional Regression Equations:**
- Q90 (low flow): ___ CFS
- Q50 (median): ___ CFS
- Q10 (high flow): ___ CFS

**Flow Duration Curve:**
```
Exceedance %: Flow (CFS)
100% (min):   ___
90%:          ___
75%:          ___
50% (median): ___
25%:          ___
10%:          ___
0% (max):     ___
```

**Reliability:** Medium (modeled, not measured)

---

**METHOD 3: DRAINAGE AREA RATIO** (Quick Estimate)

If nearby gauge exists, extrapolate using drainage areas:

**Known Gauge:**
- Location: [Upstream/downstream]
- Drainage Area: ___ sq miles
- Mean Flow: ___ CFS

**Project Site:**
- Drainage Area: ___ sq miles (from GIS)

**Flow Estimate:**
Q_project = Q_gauge × (A_project / A_gauge)^0.8

**Estimated Flow:** ___ CFS (___ GPM)

**Reliability:** Low-Medium (rule of thumb)

---

**METHOD 4: FIELD MEASUREMENT** (Site-Specific)

**Velocity-Area Method:**

1. **Select Cross-Section:**
   - Width: ___ feet
   - Average Depth: ___ feet
   - Area: ___ sq ft

2. **Measure Velocity:**
   - Method: Float method / Flow meter / Acoustic
   - Surface velocity: ___ ft/sec
   - Average velocity: ___ × 0.85 = ___ ft/sec

3. **Calculate Flow:**
   Q = Area × Velocity
   Q = ___ sq ft × ___ ft/sec = ___ CFS (___ GPM)

**Measurement Date:** [Date]
**Conditions:** [Dry/Normal/Wet season]

**Reliability:** High (for conditions measured), but single point in time

**Recommendation:** Measure monthly for 12 months to capture seasonal variation

---

**METHOD 5: RATIONAL METHOD** (Conceptual Estimate)

For ungauged, small watersheds:

**Inputs:**
- Drainage Area: ___ sq miles
- Runoff Coefficient (C): ___ (0.2 forest, 0.5 urban)
- Rainfall Intensity: ___ inches/hour (design storm)

**Peak Flow Estimate:**
Q = C × I × A × 1.008

**Result:** ___ CFS (peak flow, not average)

**Reliability:** Low (for preliminary screening only)

---

**FLOW REGIME CHARACTERIZATION:**

**Seasonal Pattern:**

| Month | Est. Flow (CFS) | % of Annual Mean |
|-------|-----------------|------------------|
| Jan   | ___             | ___%             |
| Feb   | ___             | ___%             |
| Mar   | ___             | ___%             |
| Apr   | ___             | ___%             |
| May   | ___             | ___%             |
| Jun   | ___             | ___%             |
| Jul   | ___             | ___%             |
| Aug   | ___             | ___%             |
| Sep   | ___             | ___%             |
| Oct   | ___             | ___%             |
| Nov   | ___             | ___%             |
| Dec   | ___             | ___%             |

**Flow Classification:**

- **Perennial:** Flows year-round ✅ Good for hydro
- **Intermittent:** Dry in summer ⚠️ Seasonal generation
- **Ephemeral:** Only during storms ❌ Not suitable

**Flow Variability:**
- Coefficient of Variation (CV): ___ (std dev / mean)
  - Low CV (<0.5): Stable flow ✅
  - Med CV (0.5-1.0): Moderate variability ⚠️
  - High CV (>1.0): Highly variable ❌

**Regulation:**
- Upstream Dam: Yes / No
- Flow Control: Regulated / Natural
- Impact: Stabilizes flow / Reduces flow / No impact

---

**POWER POTENTIAL BY FLOW CONDITION:**

Assuming Net Head = __ feet, Efficiency = 75%:

| Flow Scenario | Flow (CFS) | Power (kW) | Hours/Year | Energy (MWh/yr) |
|---------------|------------|------------|------------|-----------------|
| 10% (high)    | ___        | ___        | 876        | ___             |
| 25%           | ___        | ___        | 2190       | ___             |
| 50% (median)  | ___        | ___        | 4380       | ___             |
| 75%           | ___        | ___        | 6570       | ___             |
| 90% (low)     | ___        | ___        | 7884       | ___             |

**Design Flow Selection:**

Most projects size to Q50-Q90 (median to low flow):
- Maximizes hours of operation
- Avoids oversizing for rare high flows
- Balances capital cost vs. generation

**Recommended Design Flow:** ___ CFS

**Capacity Factor:** ___% (actual generation / nameplate capacity)
- Typical: 70-90% for micro-hydro (excellent)
- Compare to: Solar 15-25%, Wind 25-40%

---

**ENVIRONMENTAL FLOW REQUIREMENTS:**

**Minimum Instream Flow:**
- Agency Requirement: ___ CFS (if specified)
- If not specified, estimate: 10-30% of mean annual flow
- **Bypass Flow:** ___ CFS

**Available Flow for Generation:**
- Total Flow - Bypass Flow = ___ CFS available

**Impact on Generation:**
- Loss: __% of potential generation
- Adjusted Annual Energy: ___ MWh

---

**DATA QUALITY ASSESSMENT:**

**Gauge Data (if used):**
- Period of Record: __ years (15+ years ideal)
- Data Completeness: __% (95%+ good)
- Recent Data: [Date of latest record]
- Quality: Excellent / Good / Fair / Poor

**Modeled Estimates (if used):**
- Model Type: [USGS StreamStats / Regional equation]
- Uncertainty Range: ±__%
- Validation: Compared to nearby gauges? Yes/No

**Field Measurements (if conducted):**
- Number of Measurements: __
- Season Represented: [Dry / Average / Wet]
- Measurement Quality: Excellent / Good / Fair / Poor

**Overall Data Confidence:** High / Medium / Low

---

**RECOMMENDATIONS:**

**For Project Development:**

**If Data Confidence is HIGH:**
✅ Proceed with preliminary design
- Use flow statistics for sizing
- Assume __% safety margin
- Plan for ___ kW system

**If Data Confidence is MEDIUM:**
⚠️ Conduct short-term monitoring
- Install flow gauge for 3-6 months
- Correlation with nearby USGS gauge
- Validate design assumptions

**If Data Confidence is LOW:**
🔴 Extensive monitoring required
- 12-month flow measurement minimum
- Consider multiple sites
- High uncertainty = high risk

**Monitoring Plan:**

**Equipment:**
- Pressure transducer (continuous level)
- Staff gauge (manual backup)
- Rating curve development (multiple measurements)

**Duration:** 12 months minimum (capture seasonal variation)

**Frequency:** 
- Automated: Hourly readings
- Manual: Monthly site visits

**Cost:** $5k-15k for equipment and installation

**Value:** Reduces risk, improves design, supports permitting

---

**FLOW MEASUREMENT PROTOCOL:**

**For Future Field Measurements:**

1. **Site Selection:**
   - Straight channel (50+ feet upstream/downstream)
   - Uniform cross-section
   - No obstructions

2. **Equipment:**
   - Measuring tape (width)
   - Wading rod (depth)
   - Flow meter or float
   - Safety gear (PFD, waders)

3. **Procedure:**
   - Divide width into 10-20 sections
   - Measure depth at each section
   - Measure velocity at 0.6 × depth
   - Calculate flow for each section
   - Sum to get total flow

4. **Repeat:**
   - Different flow conditions (low, med, high)
   - Build rating curve (stage-discharge relationship)

5. **Documentation:**
   - Photos of site
   - Sketch of cross-section
   - GPS coordinates
   - Date/time/weather

This systematic flow analysis provides foundation for design and permitting."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def site_comparison(sites_list):
    """Compare multiple sites and rank"""
    
    prompt = f"""Compare and rank multiple micro-hydro sites:

**Sites to Compare:** {sites_list}

**MULTI-SITE COMPARISON & RANKING**

---

**COMPARISON MATRIX:**

| Site | Flow (CFS) | Head (ft) | Power (kW) | Access | Regulatory | Economic | Total Score | Rank |
|------|------------|-----------|------------|--------|------------|----------|-------------|------|
| A    | ___        | ___       | ___        | __/20  | __/20      | __/20    | __/100      | __   |
| B    | ___        | ___       | ___        | __/20  | __/20      | __/20    | __/100      | __   |
| C    | ___        | ___       | ___        | __/20  | __/20      | __/20    | __/100      | __   |

---

**DETAILED SCORING:**

**SITE A: [Name/Location]**

**Resource (30 points):**
- Flow adequacy: __/10 (>200 GPM = 10, 100-200 = 7, 50-100 = 5)
- Flow reliability: __/10 (Perennial = 10, Regulated = 8, Seasonal = 5)
- Head: __/10 (>50ft = 10, 30-50 = 7, 10-30 = 5)
- **Subtotal: __/30**

**Technical (20 points):**
- Site access: __/5 (Paved road = 5, Gravel = 3, 4WD = 2)
- Existing infrastructure: __/5 (Major = 5, Some = 3, None = 0)
- Grid distance: __/5 (<0.5mi = 5, 0.5-1mi = 3, >1mi = 1)
- Constructability: __/5 (Easy = 5, Moderate = 3, Difficult = 1)
- **Subtotal: __/20**

**Regulatory (20 points):**
- Permitting complexity: __/10 (Simple = 10, Moderate = 6, Complex = 3)
- Environmental concerns: __/5 (None = 5, Minor = 3, Major = 0)
- Water rights: __/5 (Clear = 5, Obtainable = 3, Uncertain = 1)
- **Subtotal: __/20**

**Economic (20 points):**
- Capital efficiency: __/10 (Cost/kW: <$4k = 10, $4-6k = 6, >$6k = 3)
- Revenue potential: __/5 (High rates = 5, Medium = 3, Low = 2)
- Payback period: __/5 (<2yr = 5, 2-3yr = 3, >3yr = 1)
- **Subtotal: __/20**

**Property (10 points):**
- Ownership clarity: __/5 (Single owner = 5, Multiple = 3, Public = 2)
- Owner interest: __/5 (Eager = 5, Neutral = 3, Skeptical = 1)
- **Subtotal: __/10**

**SITE A TOTAL: __/100**

---

**[Repeat scoring for Sites B, C, etc.]**

---

**RANKING BY CATEGORY:**

**Best Resource:**
1. Site __ (__ CFS, __ ft head, __ kW potential)
2. Site __ 
3. Site __

**Best Economics:**
1. Site __ ($__/kW, __ year payback)
2. Site __
3. Site __

**Easiest Permitting:**
1. Site __ (__ month timeline)
2. Site __
3. Site __

**Best Access:**
1. Site __ (__ from road, __ grid)
2. Site __
3. Site __

---

**PORTFOLIO RECOMMENDATIONS:**

**Tier 1 (Develop First):**
- Site A: [Rationale - why this is best quick win]
- Site C: [Rationale]

**Tier 2 (Develop Next):**
- Site B: [Rationale - good but needs more work]
- Site E: [Rationale]

**Tier 3 (Future Opportunity):**
- Site D: [Rationale - viable but lower priority]
- Site F: [Rationale]

**Not Recommended:**
- Site G: [Rationale - fatal flaw or too challenging]

---

**PORTFOLIO STRATEGY:**

**Diversification:**
- Geographic spread (different watersheds)
- Size mix (small/medium/large)
- Customer types (industrial/commercial/utility)
- Risk profile (sure bets + higher-risk/higher-reward)

**Sequencing:**
- Start with 1-2 highest-scoring sites (prove concept)
- Build reputation and learn
- Scale to medium-tier sites
- Revisit low-tier as market matures

**Resource Allocation:**
- Focus 80% effort on top 20% of sites
- Don't spread too thin
- Walk away from marginal sites

---

**DECISION FRAMEWORK:**

**Green Light (Proceed):** Score 80+
- All systems go
- Move to feasibility study
- Engage property owner immediately

**Yellow Light (Conditional):** Score 60-79
- Good potential but needs work
- Address specific issues (permitting, access, etc.)
- Revisit after issue resolution

**Red Light (Stop):** Score <60
- Not viable with current information
- Archive for future consideration
- Focus resources elsewhere

Use this systematic comparison to make objective, defensible site selection decisions."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Hydro Mapper Agent initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: map, assess, flow, compare")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'map':
            region = sys.argv[2] if len(sys.argv) > 2 else 'Pacific Northwest'
            print(map_water_resources(region))
        elif cmd == 'assess':
            site = sys.argv[2] if len(sys.argv) > 2 else 'Sample site with 150 GPM flow, 40 ft head'
            print(assess_site_potential(site))
        elif cmd == 'flow':
            location = sys.argv[2] if len(sys.argv) > 2 else 'Small creek, mountainous region'
            print(flow_analysis(location))
        elif cmd == 'compare':
            sites = sys.argv[2] if len(sys.argv) > 2 else 'Site A (100 GPM, 50ft), Site B (200 GPM, 30ft), Site C (150 GPM, 40ft)'
            print(site_comparison(sites))
