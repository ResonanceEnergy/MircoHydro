"""
ECONOMIC ANALYST AGENT
Financial modeling, ROI analysis, cost-benefit, investment scenarios.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def project_economics(project_specs):
    """Comprehensive financial analysis of micro-hydro project"""
    
    prompt = f"""Analyze project economics for micro-hydro:

**Project Specifications:** {project_specs}

**MICRO-HYDRO FINANCIAL ANALYSIS**

---

**PROJECT PARAMETERS:**

**Physical:**
- Capacity: __ kW
- Average Generation: __ kW (capacity factor __%)
- Annual Energy: __ MWh
- Design Flow: __ CFS
- Net Head: __ feet

**Site:**
- Location: [State/Region]
- Grid Connection: ____ miles
- Property: Owned / Leased ($__/year)
- Access: [Quality]

---

**CAPITAL COSTS (CAPEX):**

**1. Hydro Equipment**

| Component | Specification | Unit Cost | Quantity | Total |
|-----------|---------------|-----------|----------|-------|
| Turbine | [Type, kW rating] | $__/kW | __ kW | $__ |
| Generator | [Type, kW] | $__/kW | __ kW | $__ |
| Governor | Electronic/Mechanical | $__ | 1 | $__ |
| Control System | SCADA/PLC | $__ | 1 | $__ |
| **Subtotal Turbine-Gen Unit** | | | | **$__** |

**Typical Equipment Costs:**
- Pelton turbine (high head): $1,500-2,500/kW
- Crossflow turbine (med head): $2,000-3,000/kW
- Kaplan turbine (low head): $2,500-3,500/kW
- Generator: $300-500/kW
- Controls: $10k-30k flat cost

**2. Civil Works**

| Item | Description | Cost |
|------|-------------|------|
| Intake Structure | Concrete, trash rack, screens | $__ |
| Penstock | [Material, diameter, length] | $__/ft × __ ft = $__ |
| Powerhouse | Building/enclosure __ sq ft | $__/sq ft = $__ |
| Tailrace | Channel/pipe to return flow | $__ |
| Foundation | Turbine mounting, equipment pads | $__ |
| Site Work | Excavation, grading, drainage | $__ |
| Access Road | Improvements for construction | $__ |
| **Subtotal Civil** | | **$__** |

**Civil Work Benchmarks:**
- Intake: $30k-100k (simple concrete structure)
- Penstock (HDPE): $50-150/ft installed
- Penstock (Steel): $100-300/ft installed
- Powerhouse: $150-300/sq ft (500-1000 sq ft typical)
- Tailrace: $20k-60k

**3. Electrical**

| Item | Description | Cost |
|------|-------------|------|
| Switchgear | Main breaker, protection | $__ |
| Transformer | Step-up (if needed) | $__ |
| Interconnection | Line extension, meter | $__/mile × __ = $__ |
| Inverter | If AC-DC-AC conversion | $__ |
| Wiring | From powerhouse to grid | $__ |
| **Subtotal Electrical** | | **$__** |

**Electrical Benchmarks:**
- Switchgear: $10k-30k
- Transformer: $5k-20k (depending on kVA)
- Line extension: $50k-150k per mile
- Inverter (if needed): $200-400/kW

**4. Soft Costs**

| Item | % of Hard Costs | Cost |
|------|-----------------|------|
| Engineering (Design) | 10-15% | $__ |
| Permitting | 5-10% | $__ |
| Environmental Studies | Variable | $__ |
| Legal | 2-5% | $__ |
| Project Management | 5-8% | $__ |
| Contingency | 15-20% | $__ |
| **Subtotal Soft Costs** | **40-58%** | **$__** |

**Soft Cost Ranges:**
- Small project (<100 kW): 50-80% of hard costs
- Medium project (100-500 kW): 40-60%
- Large project (>500 kW): 30-50%

**5. Other Costs**

| Item | Description | Cost |
|------|-------------|------|
| Land Acquisition | Purchase or easement | $__ |
| Land Lease | Prepayment or deposit | $__ |
| Financing Costs | Loan origination, appraisal | $__ |
| Insurance (construction) | Builder's risk | $__ |
| Start-up & Commissioning | Testing, adjustments | $__ |
| Initial Inventory | Spare parts | $__ |
| **Subtotal Other** | | **$__** |

---

**TOTAL CAPITAL COST SUMMARY:**

| Category | Amount | % of Total |
|----------|--------|------------|
| Equipment | $__ | __% |
| Civil Works | $__ | __% |
| Electrical | $__ | __% |
| Soft Costs | $__ | __% |
| Other | $__ | __% |
| **TOTAL CAPEX** | **$__** | **100%** |

**Cost per kW:** $__ per kW installed

**Benchmarks:**
- Excellent: $3,000-4,000/kW (simple site, existing infrastructure)
- Good: $4,000-6,000/kW (typical greenfield small hydro)
- Fair: $6,000-8,000/kW (challenging site, extensive permitting)
- Poor: >$8,000/kW (remote, complex environmental, low head)

**Assessment:** This project is [Excellent/Good/Fair/Poor] from capital efficiency perspective

---

**OPERATING COSTS (OPEX):**

**Annual Fixed Costs:**

| Item | Annual Cost | Notes |
|------|-------------|-------|
| Property Lease | $__ | If leased land |
| Insurance | $__ | $5-10/kW typical |
| Administrative | $__ | Accounting, reporting |
| Utility Fees | $__ | Standby charges (if any) |
| Water Rights | $__ | Annual fees (some states) |
| **Subtotal Fixed** | **$__/year** | |

**Annual Variable Costs:**

| Item | Annual Cost | Notes |
|------|-------------|-------|
| Routine Maintenance | $__ | 2-4x per year inspections |
| Repairs | $__ | 1-2% of CAPEX typical |
| Parts/Consumables | $__ | Seals, lubricants, screens |
| Labor | $__ | If not owner-operator |
| Utilities | $__ | Minimal for micro-hydro |
| **Subtotal Variable** | **$__/year** | |

**Total Annual OPEX:** $__/year

**As % of Revenue:** __% (benchmark: 15-25% for well-run small hydro)

**As $/kW-year:** $__/kW (benchmark: $100-300/kW-year)

---

**REVENUE ANALYSIS:**

**Energy Production:**
- Annual Energy: __ MWh
- Capacity Factor: __% (hours at full capacity / 8760)
- Availability: 95-98% (downtime for maintenance)
- Net Generation: __ MWh (after availability losses)

**Revenue Scenario 1: NET METERING / BEHIND-THE-METER**

**Assumptions:**
- Retail electricity rate: $___ per kWh
- Annual escalation: __% (inflation, fuel costs)
- All generation offsets customer load

**Annual Revenue:**
__ MWh × $__/kWh = $__ per year

**Advantages:**
- ✅ Highest $/kWh (retail rates vs. wholesale)
- ✅ No transmission charges
- ✅ Simple settlement (net meter)

**Disadvantages:**
- ⚠️ Need customer with sufficient load
- ⚠️ May have net metering caps (e.g., 110% of load)
- ⚠️ Depends on maintaining customer relationship

---

**Revenue Scenario 2: WHOLESALE / POWER PURCHASE AGREEMENT (PPA)**

**Assumptions:**
- PPA rate: $___ per kWh (fixed or escalating)
- Contract term: __ years
- Utility buyer: [Name]

**Annual Revenue:**
__ MWh × $__/kWh = $__ per year

**PPA Rate Benchmarks:**
- Low: $0.03-0.05/kWh (wholesale market, no REC value)
- Medium: $0.06-0.09/kWh (avoided cost, standard PPA)
- High: $0.10-0.15/kWh (premium for renewable, long-term contract)

**Advantages:**
- ✅ Long-term revenue certainty (15-25 year contracts)
- ✅ Bankable (lenders like fixed PPA)
- ✅ No customer acquisition needed

**Disadvantages:**
- ⚠️ Lower $/kWh than retail
- ⚠️ Negotiation required
- ⚠️ Utility may not be interested (small project)

---

**Revenue Scenario 3: COMMUNITY SOLAR / GREEN TARIFF**

**Assumptions:**
- Subscription rate: $___ per kWh
- Subscribers: __ customers
- % of generation subscribed: __%

**Annual Revenue:**
__ MWh × $__/kWh = $__ per year

**Advantages:**
- ✅ Retail or near-retail rates
- ✅ Diversified revenue (multiple customers)
- ✅ Marketing as "local, clean energy"

**Disadvantages:**
- ⚠️ Requires program/legislation support
- ⚠️ Customer acquisition and billing costs
- ⚠️ Subscriber churn risk

---

**RENEWABLE ENERGY CREDITS (RECs):**

**Value:**
- RECs generated: __ MWh = __ RECs (1 REC per MWh)
- REC price: $__ per REC (market varies widely)
- Annual REC revenue: __ × $__ = $__

**REC Market Benchmarks:**
- Voluntary market: $0.50-5 per REC
- Compliance market (RPS states): $10-50 per REC
- Micro-hydro: Sometimes excluded from RPS (check state rules)

**Total Annual Revenue (Scenario 1 + RECs):** $__ + $__ = $__

---

**TAX BENEFITS & INCENTIVES:**

**Federal:**

**Investment Tax Credit (ITC):**
- Rate: __% (check current law - varies by year)
- Eligible basis: $__ (CAPEX minus grants)
- Credit amount: $__
- Reduces tax liability (or creates refund)

**Production Tax Credit (PTC):**
- Rate: $___ per kWh (indexed for inflation)
- Duration: 10 years from commercial operation
- Annual benefit: __ MWh × $__/kWh = $__/year
- Total 10-year benefit: $__ × 10 = $__

**Depreciation (MACRS):**
- Hydro = 5-year property (accelerated depreciation)
- Year 1: 20% × $__ = $__ deduction
- Year 2: 32% × $__ = $__ deduction
- (etc.)
- Tax savings: __ × marginal rate (__%) = $__

**State Incentives:**

- **State Tax Credits:** __ (varies by state)
- **Grants:** $__ (DSIRE database for programs)
- **Property Tax Exemption:** Saves $__ per year
- **Sales Tax Exemption:** Saves __% on equipment

**Utility Incentives:**

- **Renewable Energy Rebate:** $__/kW installed
- **Performance Payment:** $__/kWh for __ years

**Total Incentive Value (20-year project):** $__

**As % of CAPEX:** __% (can be 30-50% with good incentives)

---

**FINANCIAL METRICS:**

**Simple Payback:**

Formula: Total CAPEX / Annual Net Income

Annual Net Income = Revenue - OPEX = $__ - $__ = $__

Payback Period = $__ / $__ = __ years

**Benchmarks:**
- Excellent: <5 years
- Good: 5-8 years
- Fair: 8-12 years
- Poor: >12 years (may not be viable)

---

**DISCOUNTED CASH FLOW (DCF) ANALYSIS:**

**Assumptions:**
- Project Life: __ years (25-30 typical for hydro)
- Discount Rate: __% (WACC or required return)
- Annual Revenue Escalation: __%
- Annual OPEX Escalation: __%
- Residual Value: $__ (end of life)

**Year-by-Year Cash Flows:**

| Year | Revenue | OPEX | Net CF | PV Factor | PV of CF |
|------|---------|------|--------|-----------|----------|
| 1    | $__     | $__  | $__    | 0.926     | $__      |
| 2    | $__     | $__  | $__    | 0.857     | $__      |
| 3    | $__     | $__  | $__    | 0.794     | $__      |
| ...  | ...     | ...  | ...    | ...       | ...      |
| 25   | $__     | $__  | $__    | 0.146     | $__      |

**Sum of PV Cash Flows:** $__

**Less Initial Investment:** -$__

**Net Present Value (NPV):** $__

**Decision Rule:**
- NPV > 0: Project adds value, proceed ✅
- NPV = 0: Break-even, marginal
- NPV < 0: Destroys value, reject ❌

**Internal Rate of Return (IRR):**

IRR = __% (the discount rate that makes NPV = 0)

**Benchmarks:**
- Excellent: IRR > 15%
- Good: IRR 10-15%
- Fair: IRR 7-10%
- Poor: IRR < 7% (below many project hurdle rates)

---

**LEVELIZED COST OF ENERGY (LCOE):**

Formula: LCOE = (Sum of PV Costs) / (Sum of PV Energy)

**Calculation:**
- PV of CAPEX: $__
- PV of OPEX (25 years): $__
- Total PV Costs: $__
- PV of Energy (25 years, __ MWh/yr): __ MWh
- **LCOE: $__/MWh** or **$__/kWh**

**Benchmarks (2024):**
- Solar PV: $30-50/MWh
- Wind: $30-60/MWh
- Natural gas: $40-70/MWh
- **Micro-hydro: $50-150/MWh** (varies widely by site)

**Competitiveness:** This project's LCOE is [Competitive/Marginal/Not competitive]

---

**SENSITIVITY ANALYSIS:**

**Variable 1: Electricity Rate**

| Rate (¢/kWh) | Annual Revenue | NPV | IRR |
|--------------|----------------|-----|-----|
| 8 (low)      | $__            | $__ | __% |
| 10 (base)    | $__            | $__ | __% |
| 12 (high)    | $__            | $__ | __% |

**Sensitivity:** Each 1¢/kWh change = $__ change in NPV

---

**Variable 2: Capital Cost**

| CAPEX | $/kW | NPV | IRR | Payback |
|-------|------|-----|-----|---------|
| -20% (low) | $__ | $__ | __% | __ yrs |
| Base | $__ | $__ | __% | __ yrs |
| +20% (high) | $__ | $__ | __% | __ yrs |

**Sensitivity:** Each 10% CAPEX increase reduces IRR by __ percentage points

---

**Variable 3: Capacity Factor**

| Cap Factor | Annual MWh | NPV | IRR |
|------------|------------|-----|-----|
| 60% (low)  | __         | $__ | __% |
| 75% (base) | __         | $__ | __% |
| 85% (high) | __         | $__ | __% |

**Sensitivity:** Capacity factor heavily impacts economics (reliable flow is critical)

---

**SCENARIO ANALYSIS:**

**Best Case:**
- High electricity rates (+20%)
- Low CAPEX (-15% due to existing infrastructure)
- High capacity factor (85%)
- Full incentives received
- **Result: NPV = $__, IRR = __%** 🌟

**Base Case:**
- Expected rates
- Typical CAPEX
- 75% capacity factor
- Some incentives
- **Result: NPV = $__, IRR = __%** ✅

**Worst Case:**
- Low rates (-20%)
- Cost overruns (+25%)
- Low capacity factor (60% due to drought)
- No incentives
- **Result: NPV = $__, IRR = __%** ⚠️

**Probability Assessment:**
- Best: 15% probability
- Base: 65% probability
- Worst: 20% probability

**Expected NPV:** (0.15 × $best) + (0.65 × $base) + (0.20 × $worst) = $__

---

**FINANCING STRUCTURE:**

**Option 1: All Equity (100% owner-financed)**

**Pros:**
- No interest payments
- Full ownership and control
- Simple structure

**Cons:**
- High upfront cash requirement
- No leverage (lower ROE)
- Opportunity cost

**Returns:**
- Cash-on-cash: __% (Year 1 cash flow / equity invested)
- Equity IRR: __% (same as project IRR if 100% equity)

---

**Option 2: Debt Financing (70% debt, 30% equity)**

**Debt Terms:**
- Loan amount: $__ (70% of CAPEX)
- Interest rate: __%
- Term: __ years
- Annual payment: $__ (P&I)

**Equity Required:** $__ (30% of CAPEX)

**Returns:**
- Cash-on-cash: __% (after debt service)
- Equity IRR: __% (leveraged returns)

**Debt Service Coverage Ratio (DSCR):**
DSCR = Net Operating Income / Debt Service = $__ / $__ = __

**Benchmarks:**
- DSCR > 1.25: Bankable
- DSCR 1.0-1.25: Marginal
- DSCR < 1.0: Can't service debt, not financeable

---

**Option 3: Tax Equity Partnership**

**Structure:**
- Tax equity investor provides 70% of capital
- Receives 99% of tax benefits (ITC, MACRS)
- Developer contributes 30%, receives majority of cash flows
- Flip at Year 6 (typical)

**Pros:**
- Monetize tax credits efficiently
- Leverage for developer

**Cons:**
- Complex structure
- High transaction costs (only viable for projects >$5M)

---

**BREAK-EVEN ANALYSIS:**

**Required Electricity Rate for Break-Even (NPV = 0):**

Solving for rate: $__ per kWh

**Current rate is $__ per kWh**
- If current rate > break-even: Project viable ✅
- If current rate < break-even: Not viable at current assumptions ❌

**Required Capacity Factor for Break-Even:**

Solving for capacity factor: __%

**Expected capacity factor is __%**
- If expected > break-even: Adequate resource ✅
- If expected < break-even: Insufficient resource ❌

---

**RISK ANALYSIS:**

**Technical Risks:**
- Flow variability (drought): Medium impact, Medium likelihood
  - Mitigation: Conservative capacity factor assumptions
- Equipment failure: Medium impact, Low likelihood
  - Mitigation: Quality equipment, maintenance program, insurance
- Sedimentation: Low impact, Medium likelihood
  - Mitigation: Design for sediment management

**Financial Risks:**
- Electricity rate decrease: High impact, Low-Medium likelihood
  - Mitigation: Long-term PPA, diversified revenue (RECs)
- Cost overruns: High impact, Medium likelihood
  - Mitigation: Contingency (20%), fixed-price contracts
- Financing unavailable: High impact, Low likelihood
  - Mitigation: Pre-qualify lenders, have backup equity

**Regulatory Risks:**
- Permit denial/delay: High impact, Low-Medium likelihood
  - Mitigation: Early agency coordination, experienced consultants
- New environmental requirements: Medium impact, Low likelihood
  - Mitigation: Adaptive management, conservative design

**Property Risks:**
- Lease termination: High impact, Low likelihood
  - Mitigation: Long-term lease (30+ years), purchase option
- Access disputes: Medium impact, Low likelihood
  - Mitigation: Recorded easements, good neighbor relations

**Overall Risk Profile:** Low-Medium (hydro is relatively low-risk if well-sited)

---

**INVESTMENT DECISION:**

**Quantitative Score: __/100**

| Metric | Target | Actual | Score (0-25) |
|--------|--------|--------|--------------|
| Payback | <8 yrs | __ yrs | __ |
| IRR | >10% | __% | __ |
| DSCR | >1.25 | __ | __ |
| LCOE | <$100/MWh | $__/MWh | __ |

**Qualitative Factors:**

✅ Excellent resource (high flow, head)
✅ Simple permitting (non-ESA stream)
✅ Low OPEX (run-of-river, minimal maintenance)
✅ Long asset life (50+ years for civil works)
✅ Stable, predictable revenue (hydro vs. solar/wind)

⚠️ High upfront cost (capital intensive)
⚠️ Permitting timeline (18-36 months)
⚠️ Grid interconnection challenges (remote)

**RECOMMENDATION:**

**Proceed:** Yes / No / Conditional

**Rationale:** [Based on NPV, IRR, strategic fit, risk tolerance]

**Conditions (if any):**
- Secure PPA at ≥$__ per kWh
- Obtain ITC/PTC incentives
- Keep CAPEX below $__ per kW
- Achieve FERC exemption (not full license)

This analysis provides a comprehensive financial foundation for the investment decision."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def cost_estimate(system_specs):
    """Detailed cost breakdown"""
    
    prompt = f"""Create detailed cost estimate:

**System:** {system_specs}

Generate itemized cost breakdown with:
- Equipment costs (turbine, generator, controls)
- Civil works (intake, penstock, powerhouse)
- Electrical (switchgear, interconnection)
- Soft costs (engineering, permits, legal)
- Contingency (15-20%)

Provide low/mid/high estimates and cost-per-kW benchmark.

Include procurement recommendations and cost reduction strategies."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def roi_scenarios(financial_assumptions):
    """ROI analysis with multiple scenarios"""
    
    prompt = f"""Calculate ROI scenarios:

**Assumptions:** {financial_assumptions}

Provide complete ROI analysis:

**SCENARIO ANALYSIS**

**Best Case (optimistic):**
- Higher electricity rates
- Lower costs
- High capacity factor
- Full incentives
- NPV, IRR, Payback calculation

**Base Case (expected):**
- Current rates
- Expected costs
- Typical capacity factor
- Some incentives
- NPV, IRR, Payback calculation

**Worst Case (conservative):**
- Rate decreases
- Cost overruns
- Lower generation
- No incentives
- NPV, IRR, Payback calculation

Include sensitivity analysis showing impact of:
- ±20% electricity rate changes
- ±20% capital cost changes
- ±15% generation changes

Provide tornado chart ranking of most impactful variables.

Calculate break-even electricity rate and minimum capacity factor.

Include financing comparison (100% equity vs. 70% debt)."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

def incentive_analysis(location, project_size):
    """Research available incentives and tax credits"""
    
    prompt = f"""Research renewable energy incentives:

**Location:** {location}
**Project Size:** {project_size}

**INCENTIVE CATALOG**

**Federal Incentives:**

**1. Investment Tax Credit (ITC)**
- Current rate: __% (check year)
- Eligible projects: [Micro-hydro qualification]
- Timing: Claimed in year of commercial operation
- Value for this project: $__

**2. Production Tax Credit (PTC)**
- Rate: $___ per kWh (indexed)
- Duration: 10 years
- Eligibility: New construction
- Total 10-year value: $__

**ITC vs. PTC:**
- Comparison table
- Recommendation: [Which is better for this project]

**3. MACRS Depreciation**
- 5-year accelerated depreciation
- Year 1-5 schedule
- Tax savings: $__ over 5 years

**4. USDA REAP Grant**
- Rural Energy for America Program
- Up to 25% of project costs
- Eligibility: Rural areas, agricultural
- Application process
- Estimated grant: $__

**5. Other Federal Programs**
- DOE grants (if R&D component)
- EPA brownfield remediation (if applicable)
- Economic development grants

---

**State Incentives: [{location}]**

**1. State Tax Credits**
- [State-specific programs]
- Rate: __%
- Cap: $__
- Value: $__

**2. State Grants**
- Clean Energy Fund
- Renewable Development
- Amount: $__

**3. Property Tax Exemption**
- Renewable energy systems exempt
- Saves: $__ per year × 25 years = $__

**4. Sales Tax Exemption**
- Equipment purchases exempt
- Saves: __% on $__ = $__

**5. Renewable Energy Certificates (RECs)**
- State RPS (Renewable Portfolio Standard)
- Solar/hydro tier pricing
- Value: $__ per REC × __ RECs/year = $__/year

---

**Utility Incentives:**

**1. Interconnection Rebates**
- $__ per kW installed
- Value: $__

**2. Performance Incentives**
- $__ per kWh for __ years
- Annual value: $__

**3. Preferential Rates**
- Higher than standard avoided cost
- PPA at $__ per kWh

---

**Local Incentives:**

**County/Municipal:**
- Economic development grants
- Green building incentives
- Utility fee waivers

---

**Total Incentive Value:**

| Incentive Type | Amount | Timing |
|----------------|--------|--------|
| Federal ITC/PTC | $__ | Year 1 |
| MACRS (PV) | $__ | Years 1-5 |
| USDA REAP | $__ | Construction |
| State Tax Credit | $__ | Year 1 |
| State Grant | $__ | Construction |
| Property Tax Exemption | $__ | Years 1-25 |
| RECs | $__ | Annual |
| **TOTAL NPV** | **$__** | |

**As % of Project CAPEX:** __%

**Incentive Strategy:**
- Which to pursue (prioritized list)
- Application timeline
- Coordination requirements
- Professional assistance needed

This maximizes financial viability through available incentives."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Economic Analyst initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: economics, cost, roi, incentives")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'economics':
            specs = sys.argv[2] if len(sys.argv) > 2 else '100 kW, 75% capacity factor, $0.10/kWh rate'
            print(project_economics(specs))
        elif cmd == 'cost':
            specs = sys.argv[2] if len(sys.argv) > 2 else '75 kW Pelton turbine system'
            print(cost_estimate(specs))
        elif cmd == 'roi':
            assumptions = sys.argv[2] if len(sys.argv) > 2 else '$500k CAPEX, $50k annual revenue, 8% discount'
            print(roi_scenarios(assumptions))
        elif cmd == 'incentives':
            location = sys.argv[2] if len(sys.argv) > 2 else 'Oregon'
            size = sys.argv[3] if len(sys.argv) > 3 else '100 kW'
            print(incentive_analysis(location, size))
