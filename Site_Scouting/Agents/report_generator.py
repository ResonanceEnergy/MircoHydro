"""
REPORT GENERATOR AGENT
Comprehensive site reports, presentations, executive summaries.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def site_assessment_report(site_data):
    """Generate comprehensive site assessment report"""
    
    prompt = f"""Generate comprehensive site assessment report:

**Site Data:** {site_data}

**MICRO-HYDRO SITE ASSESSMENT REPORT**

---

**EXECUTIVE SUMMARY**

**Site:** [Name / Location]
**Date:** [Assessment date]
**Assessed By:** [Team]

**Key Findings:**
- **Feasibility:** ✅ Viable / ⚠️ Conditional / ❌ Not Viable
- **Estimated Capacity:** __ kW
- **Capital Cost:** $__ ($__/kW)
- **Annual Revenue:** $__
- **Simple Payback:** __ years
- **Major Risks:** [Top 3]

**Recommendation:** Proceed / Proceed with Conditions / Further Study / Abandon

---

**1. SITE DESCRIPTION**

**1.1 Location**
- Address: [Street address if applicable]
- Coordinates: [Latitude, Longitude]
- County: [Name]
- State: [State]
- USGS Quad: [Map name]
- Access: [Description of road access]

**1.2 Stream Characteristics**
- Stream Name: [Official name]
- Drainage Area: __ sq miles
- Stream Order: [1st, 2nd, 3rd]
- Gradient: __% in project reach
- Elevation: __ ft (intake) to __ ft (tailrace)

**1.3 Surroundings**
- Land Use: Forest / Agricultural / Rural residential
- Population: Remote / Low density / Moderate
- Nearest Town: [Name], __ miles
- Infrastructure: [Roads, utilities nearby]

---

**2. HYDROLOGIC ASSESSMENT**

**2.1 Flow Data**

**Source:** USGS Gauge [Station ID] / StreamStats / Field Measurement

**Flow Statistics:**

| Statistic | Flow (CFS) | Flow (GPM) |
|-----------|------------|------------|
| Mean Annual | __ | __ |
| Q10 (high) | __ | __ |
| Q50 (median) | __ | __ |
| Q90 (low) | __ | __ |
| Record Min | __ | __ |

**Flow Duration Curve:**
[Describe shape - stable baseflow vs. flashy]

**Seasonal Pattern:**
- High flow: [Months] (snowmelt / rainy season)
- Low flow: [Months] (summer / drought)
- Reliability: Perennial / Seasonal / Regulated

**Data Confidence:** High (gauge) / Medium (model) / Low (estimate)

**2.2 Design Flow Selection**

**Recommended Design Flow:** __ CFS

**Rationale:**
- Q50-Q70 range (balances capacity vs. utilization)
- Ensures high capacity factor (70-85%)
- Avoids oversizing for rare high flows

**Bypass Flow Requirement:** __ CFS (30% of mean, typical)

**Available Flow for Generation:** __ CFS

---

**3. SITE INFRASTRUCTURE**

**3.1 Head (Elevation Drop)**

**Measurement Method:** Topographic map / GPS / Survey

**Gross Head:** __ feet (intake elevation - tailrace elevation)

**Head Losses:**
- Intake screen: __ ft (minor)
- Penstock friction: __ ft (Hazen-Williams calculation)
- Tailrace: __ ft (minor)
- **Total Losses:** __ ft

**Net Head:** __ feet (available for generation)

**3.2 Intake Location**

**Coordinates:** [Lat, Long]
**Description:** [Natural pool, behind small weir, etc.]
**Type:** Run-of-river / Low diversion / Existing structure
**Fish Screen Required:** Yes / No
**Sedimentation:** Low / Medium / High (management needed?)

**3.3 Penstock Route**

**Length:** __ feet
**Route Description:** [Follow contour, cross valley, etc.]
**Slope:** __% average
**Obstacles:** Stream crossings (__ locations), road crossing, trees
**Recommended Material:** HDPE / Steel (based on pressure, cost)
**Diameter:** __ inches (hydraulic calculation)
**Pressure Rating:** __ PSI

**3.4 Powerhouse Site**

**Location:** [Description relative to landmarks]
**Footprint:** __ sq ft required
**Foundation:** Rock / Soil (stable? excavation needed?)
**Access:** [Distance from road, slope]
**Flood Risk:** Above 100-year flood? Yes / No

**3.5 Tailrace**

**Discharge Point:** [Coordinates, description]
**Length:** __ feet (powerhouse to stream)
**Type:** Open channel / Pipe
**Erosion Protection:** Needed / Not needed

---

**4. POWER GENERATION POTENTIAL**

**4.1 Calculation**

**Formula:** P (kW) = Q (CFS) × H (ft) × η × 0.085

**Inputs:**
- Design Flow (Q): __ CFS
- Net Head (H): __ feet
- Efficiency (η): 0.75 (typical for micro-hydro)

**Rated Capacity:** __ kW

**4.2 Annual Energy Production**

**Capacity Factor:** __% (based on flow duration)
- Hours per year: 8,760
- Hours at full capacity: __ (based on Q exceeding design flow)
- Average generation: __ kW

**Annual Energy:** __ MWh

**4.3 Turbine Selection**

**Recommended Type:** Pelton / Turgo / Crossflow / Francis / Kaplan

**Selection Criteria:**
- Head range: [Match turbine to head]
- Flow range: [Match to flow variability]
- Efficiency: [Peak efficiency at design point]

**Manufacturer Options:** [List 2-3 suitable suppliers]

---

**5. ECONOMIC ANALYSIS**

**5.1 Capital Costs**

| Category | Cost Estimate |
|----------|---------------|
| Equipment (turbine, generator, controls) | $__ |
| Civil Works (intake, penstock, powerhouse) | $__ |
| Electrical (switchgear, interconnection) | $__ |
| Engineering & Design (10-15%) | $__ |
| Permitting & Environmental (5-15%) | $__ |
| Legal & Administrative | $__ |
| Contingency (15-20%) | $__ |
| **TOTAL CAPEX** | **$__** |

**Cost per kW:** $__/kW

**Benchmark:** $3-8k/kW typical (this project is [Excellent/Good/Fair/Poor])

**5.2 Operating Costs**

| Item | Annual Cost |
|------|-------------|
| Maintenance (labor, parts) | $__ |
| Insurance | $__ |
| Property Lease/Taxes | $__ |
| Administrative | $__ |
| **Total Annual OPEX** | **$__** |

**As % of Revenue:** __%

**5.3 Revenue**

**Energy Sales:**
- Rate: $__ per kWh (net metering / PPA / wholesale)
- Annual Energy: __ MWh
- **Annual Revenue:** $__

**RECs (if applicable):**
- RECs: __ per year
- Price: $__ per REC
- **REC Revenue:** $__

**Total Annual Revenue:** $__

**5.4 Financial Metrics**

**Simple Payback:** $__ CAPEX / $__ Net Income = __ years

**NPV (25 years, 8% discount):** $__

**IRR:** __%

**LCOE:** $__/MWh ($__/kWh)

**Assessment:** [Excellent / Good / Fair / Poor economics]

---

**6. REGULATORY & ENVIRONMENTAL**

**6.1 Permits Required**

- [ ] FERC: Exemption / License / Not Required
- [ ] Corps 404: Required / Not Required
- [ ] State Water Right: Required (timeline: __ months)
- [ ] State Environmental Review: SEPA/CEQA (timeline: __ months)
- [ ] ESA Consultation: Required / Not Required
- [ ] Local: Building, grading permits

**Estimated Permitting Timeline:** __ months

**Estimated Permitting Cost:** $__

**6.2 Environmental Concerns**

**Threatened/Endangered Species:**
- Present: [List] / None
- Critical Habitat: Yes / No
- Impact: Major / Moderate / Minor / Negligible

**Fish Passage:**
- Required: Yes / No
- Cost: $__ (if required)

**Wetlands:**
- Impacted: __ acres
- Mitigation: Required / Not Required

**Water Quality:**
- Concern: Temperature, sediment
- Mitigation: Bypass flow, BMPs

**Overall Environmental Risk:** Low / Medium / High

---

**7. PROPERTY & ACCESS**

**7.1 Ownership**

| Component | Parcel(s) | Owner | Rights Needed |
|-----------|-----------|-------|---------------|
| Intake | [ID] | [Name] | Easement / Purchase |
| Penstock | [ID] | [Name] | Easement |
| Powerhouse | [ID] | [Name] | Lease / Purchase |

**Total Parcels:** __
**Ownership Complexity:** Simple (1 owner) / Moderate (2-3) / Complex (4+)

**7.2 Access**

**Road:** Paved / Gravel / Dirt / No road

**Improvements Needed:**
- Widening: $__
- Surface: $__
- Drainage: $__
- **Total:** $__

**7.3 Acquisition Strategy**

**Recommended Approach:** Purchase / Lease / Easement

**Estimated Cost:** $__

**Landowner Relations:** Favorable / Neutral / Challenging

---

**8. GRID INTERCONNECTION**

**8.1 Utility**

**Serving Utility:** [Name]
**Type:** IOU / Muni / Coop

**8.2 Connection Point**

**Nearest Line:** __ miles (voltage: __ kV)
**Line Capacity:** Adequate / Marginal / Insufficient

**8.3 Interconnection Costs**

| Item | Cost Estimate |
|------|---------------|
| Application & Studies | $__ |
| Line Extension (if needed) | $__ |
| Transformer | $__ |
| Protective Relays | $__ |
| Metering | $__ |
| **Total Interconnection** | **$__** |

**8.4 Revenue Strategy**

**Preferred:** Net Metering / PPA / Wholesale

**Estimated Rate:** $__ per kWh

---

**9. RISK ASSESSMENT**

**9.1 Technical Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Flow variability | Medium | High | Conservative design flow, bypass |
| Cost overrun | Medium | Medium | Contingency, fixed-price contracts |
| Equipment failure | Low | Medium | Quality equipment, maintenance |

**9.2 Regulatory Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Permit delay | Medium | Medium | Early agency coordination |
| ESA consultation | Low | High | Avoid sensitive species sites |
| Water rights denial | Low | High | Non-consumptive use argument |

**9.3 Financial Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Rate decrease | Low | High | Long-term PPA |
| Financing unavailable | Low | High | Pre-qualify lenders |
| Revenue shortfall | Low | Medium | Conservative capacity factor |

**Overall Risk Profile:** Low / Medium / High

---

**10. RECOMMENDATIONS**

**10.1 Feasibility Conclusion**

**✅ VIABLE** / **⚠️ CONDITIONAL** / **❌ NOT VIABLE**

**Rationale:**
[Explain conclusion based on resource, economics, regulatory, etc.]

**10.2 Next Steps**

**If Proceed:**

**Phase 1 (Months 1-3):**
1. Flow monitoring (install gauge for 12 months)
2. Property negotiations (initiate contact with landowners)
3. Pre-application meetings (FERC, Corps, state agencies)
4. Preliminary engineering (30% design)

**Phase 2 (Months 4-12):**
1. Environmental surveys (fish, wildlife, wetlands)
2. Permit applications (water right, 404, FERC)
3. Utility interconnection application
4. Finalize property agreements

**Phase 3 (Months 13-24):**
1. Permit approvals
2. Final design (100%)
3. Financing secured
4. Contractor selection

**Phase 4 (Months 25-36):**
1. Construction
2. Commissioning
3. Commercial operation

**Total Timeline to Operation:** __ months

**10.3 Budget for Next Phase**

- Flow monitoring: $__
- Surveys: $__
- Engineering: $__
- Permitting: $__
- Legal: $__
- **Total:** $__

**10.4 Decision Point**

**Proceed if:**
- Flow monitoring confirms adequate resource
- Property agreements achievable at <$__ cost
- Permitting path clear (no major red flags)
- Financing available at <__% interest

---

**11. APPENDICES**

**Appendix A:** Maps
- Location map (regional)
- Site plan (detailed)
- Penstock route
- Property boundaries
- Hydrologic network

**Appendix B:** Hydrologic Data
- Flow statistics (full table)
- Flow duration curve (graph)
- USGS gauge records (if used)

**Appendix C:** Calculations
- Head loss (detailed)
- Power (formula with inputs)
- Energy production (capacity factor derivation)

**Appendix D:** Cost Estimate Backup
- Equipment quotes (if available)
- Construction unit costs

**Appendix E:** Agency Correspondence
- Pre-app meeting notes
- Email exchanges

**Appendix F:** Photos
- Site photos (numbered, dated)
- Google Earth imagery

---

**REPORT PREPARED BY:**

[Name]
[Title/Credentials]
[Company]
[Date]

---

This comprehensive report supports development decision-making and investor presentations."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def executive_summary(detailed_assessment):
    """Create concise executive summary for stakeholders"""
    
    prompt = f"""Create executive summary from assessment:

**Assessment:** {detailed_assessment}

Generate 2-3 page executive summary suitable for investors/executives:

**FORMAT:**

**1. Opportunity (1 paragraph)**
- Site name, location, capacity
- Unique selling points
- Strategic fit

**2. Key Metrics (bullet points)**
- Capacity: __ kW
- Annual Energy: __ MWh
- CAPEX: $__ ($__/kW)
- Revenue: $__/year
- Payback: __ years
- IRR: __%

**3. Resource (1 paragraph)**
- Flow and head summary
- Data confidence
- Reliability

**4. Economics (1 paragraph)**
- Cost breakdown (high level)
- Revenue strategy
- Financial returns

**5. Risks & Mitigation (bullet points)**
- Top 3 risks with mitigation

**6. Timeline (bullet points)**
- Permits: __ months
- Construction: __ months
- Operation: [Year]

**7. Recommendation (1 paragraph)**
- Go/No-Go with rationale
- Investment required for next phase

Make it compelling but honest. Use clear language, avoid jargon."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=2000
    )
    
    return response.choices[0].message.content

def investor_presentation(project_summary):
    """Generate investor pitch deck content"""
    
    prompt = f"""Generate investor presentation content:

**Project:** {project_summary}

**INVESTOR PITCH DECK (Slide-by-Slide Content)**

**SLIDE 1: TITLE**
- Project Name
- Location
- Capacity (kW)
- Presenter name, date

**SLIDE 2: THE OPPORTUNITY**
- Clean, reliable baseload power
- Proven technology (100+ year track record)
- Excellent site characteristics
- Attractive returns

**SLIDE 3: SITE OVERVIEW**
- Map showing location
- Key stats: Flow, Head, Capacity
- Photos (intake, penstock route, powerhouse site)

**SLIDE 4: RESOURCE**
- Flow duration curve (graph)
- 75% capacity factor (vs. 15-25% solar, 30-40% wind)
- Baseload generation profile (24/7 power)

**SLIDE 5: ECONOMICS**
Table:
- CAPEX: $__
- Annual Revenue: $__
- Annual OPEX: $__
- Net Income: $__
- Payback: __ years
- 25-year NPV: $__
- IRR: __%

**SLIDE 6: REVENUE MODEL**
- Net metering / PPA at $__/kWh
- Renewable Energy Credits: $__/year
- Total: $__/year
- Escalation: __% per year

**SLIDE 7: COST BREAKDOWN (Pie Chart)**
- Equipment: __%
- Civil: __%
- Electrical: __%
- Soft Costs: __%
- Contingency: __%

**SLIDE 8: PROJECT TIMELINE**
Gantt chart:
- Permits: Months 1-18
- Design: Months 6-18
- Construction: Months 19-30
- Operation: Month 31

**SLIDE 9: PERMITS & APPROVALS**
- List of permits (FERC, Corps, State)
- Status: Pre-app complete / Application ready
- Risk level: Low-Medium
- Professional team engaged (law firm, engineering, environmental)

**SLIDE 10: RISK MITIGATION**
Table:
- Risk → Mitigation
- Flow variability → Conservative design, bypass
- Permitting → Early agency coordination
- Construction → Fixed-price contract
- Revenue → Long-term PPA

**SLIDE 11: TEAM**
- Developer: [Experience]
- Engineer: [Firm, hydro projects completed]
- Legal: [Firm]
- Environmental: [Consultant]

**SLIDE 12: COMPARABLE PROJECTS**
- Similar projects (size, location, economics)
- Proven track record

**SLIDE 13: INVESTMENT STRUCTURE**
- Total Capital Needed: $__
- Equity: $__ (__%)
- Debt: $__ (__%)
- Uses: [Breakdown]
- Sources: [Investor equity, bank loan, grants]

**SLIDE 14: RETURNS TO INVESTORS**
- Equity IRR: __%
- Cash-on-cash (Year 1): __% 
- Payback: __ years
- Exit strategy: [Operate 25+ years, sell after 5-7 years, dividend stream]

**SLIDE 15: ESG IMPACT**
- Clean energy: __ MWh/year
- CO2 avoided: __ tons/year
- Jobs created: __ (construction), __ (permanent)
- Community benefit: [Local power, tax base]

**SLIDE 16: NEXT STEPS**
- Seeking: $__ equity investment
- Use of Funds: [Permitting, design, construction]
- Timeline: Close investment by [Date], operation by [Date]
- Contact: [Name, email, phone]

**APPENDIX SLIDES:**
- Detailed financials (pro forma)
- Site maps
- Letters of support (community, landowners)
- Term sheet (investment terms)

Make it visual, compelling, professional. Focus on why this is an excellent investment."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def comparative_analysis(multiple_sites):
    """Compare multiple sites and rank"""
    
    prompt = f"""Compare sites and generate ranking report:

**Sites:** {multiple_sites}

**MULTI-SITE COMPARATIVE ANALYSIS**

Generate comprehensive comparison:

**COMPARISON MATRIX:**

| Site | Capacity (kW) | CAPEX ($k) | $/kW | Revenue ($k/yr) | IRR | Payback | Score |
|------|---------------|------------|------|-----------------|-----|---------|-------|
| A    | __            | __         | __   | __              | __%  | __ yrs  | __/100 |
| B    | __            | __         | __   | __              | __%  | __ yrs  | __/100 |
| C    | __            | __         | __   | __              | __%  | __ yrs  | __/100 |

**DETAILED SCORING:**

**Resource Quality (30 points):**
- Flow adequacy and reliability
- Head
- Capacity factor

**Economics (25 points):**
- IRR
- Payback
- Cost per kW

**Regulatory (20 points):**
- Permitting complexity
- Environmental issues
- Timeline

**Infrastructure (15 points):**
- Site access
- Grid connection
- Existing facilities

**Property (10 points):**
- Ownership complexity
- Landowner relations

**SITE-BY-SITE ANALYSIS:**
[Detailed narrative for each site with strengths/weaknesses]

**RECOMMENDATIONS:**

**Tier 1 (Develop Immediately):**
- Site A: [Rationale]
- Score 80+, excellent economics, low risk

**Tier 2 (Develop Next):**
- Site B: [Rationale]
- Score 60-79, good but some challenges

**Tier 3 (Future Consideration):**
- Site C: [Rationale]
- Score <60, marginal economics or high risk

**PORTFOLIO STRATEGY:**
- Start with Tier 1 (prove concept)
- Scale to Tier 2 (leverage experience)
- Revisit Tier 3 (if market improves)

This supports data-driven site selection."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Report Generator initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: full_report, executive, investor, compare")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'full_report':
            data = sys.argv[2] if len(sys.argv) > 2 else '100 kW site, good flow, moderate costs'
            print(site_assessment_report(data))
        elif cmd == 'executive':
            assessment = sys.argv[2] if len(sys.argv) > 2 else 'Detailed assessment data'
            print(executive_summary(assessment))
        elif cmd == 'investor':
            summary = sys.argv[2] if len(sys.argv) > 2 else '75 kW, 15% IRR, $500k CAPEX'
            print(investor_presentation(summary))
        elif cmd == 'compare':
            sites = sys.argv[2] if len(sys.argv) > 2 else 'Site A (100kW, $600k), Site B (75kW, $400k)'
            print(comparative_analysis(sites))
