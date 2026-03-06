"""
FINANCIAL MODELER AGENT
Creates financial models, projections, and scenario analysis for fundraising.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv(dotenv_path='../.env')

# Initialize Groq client
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

def build_model(business_type='hardware', time_horizon=5):
    """
    Generate comprehensive financial model framework.
    
    Types: hardware, saas, services, hybrid
    Horizon: 3, 5, or 10 years
    """
    
    prompt = f"""You are a financial modeling expert. Create a comprehensive {time_horizon}-year financial model for a {business_type} business.

**FINANCIAL MODEL FRAMEWORK**

---

**MODEL STRUCTURE**

Build model with these sheets/sections:
1. Assumptions (inputs)
2. Revenue Model
3. Cost of Goods Sold (COGS)
4. Operating Expenses (OpEx)
5. Headcount Plan
6. Capital Expenditures (CapEx)
7. Income Statement (P&L)
8. Cash Flow Statement
9. Balance Sheet
10. Key Metrics Dashboard
11. Scenario Analysis

---

**1. ASSUMPTIONS SHEET** (all inputs in one place)

**Revenue Assumptions**:
```
Units sold Year 1: [X]
Unit growth rate: Y% year-over-year
Average selling price (ASP): $Z
Price increase: W% annually
Revenue mix (if multiple products):
  - Product A: __% (Price: $___)
  - Product B: __% (Price: $___)
  - Service/recurring: __% (Price: $___)
```

**Customer Acquisition**:
```
Customer acquisition cost (CAC): $___
Marketing spend as % of revenue: ___%
Sales cycle length: ___ months
Sales team capacity: ___ deals per rep per year
```

**Cost Assumptions**:
```
COGS as % of revenue Year 1: ___%
COGS improvement: __% annually (economies of scale)
R&D as % of revenue: ___%
S&M as % of revenue: ___%
G&A as % of revenue: ___%
```

**Headcount Assumptions**:
```
Starting headcount: ___
Hiring plan:
  - Engineering: ___ Year 1, ___ Year 2, etc.
  - Sales: ___ Year 1, ___ Year 2, etc.
  - Operations: ___ Year 1, ___ Year 2, etc.
  - G&A: ___ Year 1, ___ Year 2, etc.
Average salaries:
  - Engineering: $___k
  - Sales: $___k + __% commission
  - Operations: $___k
  - G&A: $___k
Benefits/taxes: __% of salary
```

**Capital Requirements**:
```
Equipment/machinery: $___
Facilities: $___/year
Inventory: ___ months of COGS
Payment terms:
  - Customer payment: ___ days
  - Vendor payment: ___ days
```

---

**2. REVENUE MODEL**

Build bottoms-up revenue model:

**{business_type.upper()} REVENUE MODEL**:

| Year | Units | ASP | Product Revenue | Recurring Revenue | Total Revenue |
|------|-------|-----|-----------------|-------------------|---------------|
| 1 | __ | $__ | $__ | $__ | $__ |
| 2 | __ | $__ | $__ | $__ | $__ |
| 3 | __ | $__ | $__ | $__ | $__ |
| 4 | __ | $__ | $__ | $__ | $__ |
| 5 | __ | $__ | $__ | $__ | $__ |

**Revenue Build-Up** (Year 1 example):
```
Q1: ___ units × $___ ASP = $___
Q2: ___ units × $___ ASP = $___
Q3: ___ units × $___ ASP = $___
Q4: ___ units × $___ ASP = $___
Year 1 Total: $___

Growth drivers:
- Unit growth: __% (market expansion)
- Price growth: __% (value capture)
- Recurring revenue: __% (service attach rate)
```

**Sales Funnel** (supports unit projections):
```
Leads: ___
→ Qualified: ___ (___% conversion)
→ Proposals: ___ (___% conversion)
→ Customers: ___ (___% close rate)
→ Revenue: $___ (average deal size)
```

---

**3. COST OF GOODS SOLD (COGS)**

**Unit Economics**:
```
Direct materials: $___ per unit
Direct labor: $___ per unit
Manufacturing overhead: $___ per unit
Total COGS per unit: $___ 
Gross margin per unit: $___ (__%)
```

**COGS by Year**:

| Year | Units | COGS/Unit | Total COGS | % of Revenue | Gross Margin % |
|------|-------|-----------|------------|--------------|----------------|
| 1 | __ | $__ | $__ | __% | __% |
| 2 | __ | $__ | $__ | __% | __% |
| 3 | __ | $__ | __% | __% | __% |
| 4 | __ | $__ | $__ | __% | __% |
| 5 | __ | $__ | $__ | __% | __% |

**Margin Improvement Drivers**:
- Volume discounts from suppliers
- Manufacturing efficiency improvements
- Design for manufacturability (DFM)
- Automation investments

---

**4. OPERATING EXPENSES (OPEX)**

**R&D / Engineering**:
| Year | Headcount | Avg Salary | Total Comp | Other R&D | Total R&D | % Revenue |
|------|-----------|------------|------------|-----------|-----------|-----------|
| 1 | __ | $__k | $__ | $__ | $__ | __% |
| 2 | __ | $__k | $__ | $__ | $__ | __% |
| 3 | __ | $__k | $__ | $__ | $__ | __% |

**Sales & Marketing**:
| Year | Headcount | Total Comp | Marketing | Events | Total S&M | % Revenue |
|------|-----------|------------|-----------|--------|-----------|-----------|
| 1 | __ | $__ | $__ | $__ | $__ | __% |
| 2 | __ | $__ | $__ | $__ | $__ | __% |
| 3 | __ | $__ | $__ | $__ | $__ | __% |

**General & Administrative**:
| Year | Headcount | Total Comp | Facilities | Insurance | Other | Total G&A | % Revenue |
|------|-----------|------------|------------|-----------|-------|-----------|-----------|
| 1 | __ | $__ | $__ | $__ | $__ | $__ | __% |
| 2 | __ | $__ | $__ | $__ | $__ | $__ | __% |

---

**5. HEADCOUNT PLAN**

| Department | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
|------------|----|----|----|----|----|----|
| Engineering | __ | __ | __ | __ | __ | __ |
| Product | __ | __ | __ | __ | __ | __ |
| Sales | __ | __ | __ | __ | __ | __ |
| Marketing | __ | __ | __ | __ | __ | __ |
| Operations | __ | __ | __ | __ | __ | __ |
| Finance | __ | __ | __ | __ | __ | __ |
| Legal/HR | __ | __ | __ | __ | __ | __ |
| **Total** | **__** | **__** | **__** | **__** | **__** | **__** |

**Key Hires by Quarter**:
Year 1:
- Q1: [Roles]
- Q2: [Roles]
- Q3: [Roles]
- Q4: [Roles]

---

**6. INCOME STATEMENT (P&L)**

| Line Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|-----------|--------|--------|--------|--------|--------|
| **Revenue** | $__ | $__ | $__ | $__ | $__ |
| Product revenue | $__ | $__ | $__ | $__ | $__ |
| Recurring revenue | $__ | $__ | $__ | $__ | $__ |
| **COGS** | $__ | $__ | $__ | $__ | $__ |
| **Gross Profit** | **$__** | **$__** | **$__** | **$__** | **$__** |
| **Gross Margin %** | **__%** | **__%** | **__%** | **__%** | **__%** |
| | | | | | |
| **Operating Expenses** | | | | | |
| R&D | $__ | $__ | $__ | $__ | $__ |
| Sales & Marketing | $__ | $__ | $__ | $__ | $__ |
| G&A | $__ | $__ | $__ | $__ | $__ |
| **Total OpEx** | **$__** | **$__** | **$__** | **$__** | **$__** |
| **OpEx as % Revenue** | **__%** | **__%** | **__%** | **__%** | **__%** |
| | | | | | |
| **EBITDA** | **($__)** | **($__)** | **$__** | **$__** | **$__** |
| **EBITDA Margin %** | **(_%)** | **(_%)** | **__%** | **__%** | **__%** |
| | | | | | |
| Depreciation | $__ | $__ | $__ | $__ | $__ |
| Amortization | $__ | $__ | $__ | $__ | $__ |
| **EBIT** | **($__)** | **($__)** | **$__** | **$__** | **$__** |
| | | | | | |
| Interest expense | $__ | $__ | $__ | $__ | $__ |
| Interest income | $__ | $__ | $__ | $__ | $__ |
| **Pre-tax Income** | **($__)** | **($__)** | **$__** | **$__** | **$__** |
| | | | | | |
| Taxes (30%) | $__ | $__ | $__ | $__ | $__ |
| **Net Income** | **($__)** | **($__)** | **$__** | **$__** | **$__** |
| **Net Margin %** | **(_%)** | **(_%)** | **__%** | **__%** | **__%** |

**Key Inflection Points**:
- Gross margin positive: [Quarter/Year]
- EBITDA positive: [Quarter/Year]
- Net income positive: [Quarter/Year]
- Cash flow positive: [Quarter/Year]

---

**7. CASH FLOW STATEMENT**

| Line Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|-----------|--------|--------|--------|--------|--------|
| **Operating Activities** | | | | | |
| Net income | ($__) | ($__) | $__ | $__ | $__ |
| Add: Depreciation | $__ | $__ | $__ | $__ | $__ |
| Add: Amortization | $__ | $__ | $__ | $__ | $__ |
| Changes in working capital: | | | | | |
|   Accounts receivable | ($__) | ($__) | ($__) | ($__) | ($__) |
|   Inventory | ($__) | ($__) | ($__) | ($__) | ($__) |
|   Accounts payable | $__ | $__ | $__ | $__ | $__ |
| **Cash from Operations** | **($__)** | **($__)** | **$__** | **$__** | **$__** |
| | | | | | |
| **Investing Activities** | | | | | |
| Equipment purchases | ($__) | ($__) | ($__) | ($__) | ($__) |
| Facility improvements | ($__) | ($__) | ($__) | ($__) | ($__) |
| **Cash from Investing** | **($__)** | **($__)** | **($__)** | **($__)** | **($__)** |
| | | | | | |
| **Financing Activities** | | | | | |
| Equity raised | $__ | $__ | $__ | $__ | $__ |
| Debt raised | $__ | $__ | $__ | $__ | $__ |
| Debt repayment | ($__) | ($__) | ($__) | ($__) | ($__) |
| **Cash from Financing** | **$__** | **$__** | **$__** | **$__** | **$__** |
| | | | | | |
| **Net Change in Cash** | **$__** | **$__** | **$__** | **$__** | **$__** |
| Beginning cash | $__ | $__ | $__ | $__ | $__ |
| **Ending Cash** | **$__** | **$__** | **$__** | **$__** | **$__** |
| | | | | | |
| **Monthly Burn Rate** | $__ | $__ | $__ | $__ | $__ |
| **Runway (months)** | __ | __ | __ | __ | __ |

---

**8. KEY METRICS DASHBOARD**

**Growth Metrics**:
- Revenue growth (YoY): __%, __%, __%, __%, __%
- Unit growth (YoY): __%, __%, __%, __%, __%
- Customer growth: __%, __%, __%, __%, __%

**Profitability Metrics**:
- Gross margin: __%, __%, __%, __%, __%
- EBITDA margin: __%, __%, __%, __%, __%
- Net margin: __%, __%, __%, __%, __%

**Efficiency Metrics**:
- CAC: $__, $__, $__, $__, $__
- LTV: $__, $__, $__, $__, $__
- LTV:CAC ratio: __:1, __:1, __:1, __:1, __:1
- Payback period (months): __, __, __, __, __
- Magic number (ARR growth / S&M spend): __, __, __, __, __

**Unit Economics**:
- Revenue per unit: $__, $__, $__, $__, $__
- COGS per unit: $__, $__, $__, $__, $__
- Gross profit per unit: $__, $__, $__, $__, $__

**Capital Efficiency**:
- Burn multiple (Net burn / Net new ARR): __, __, __, __, __
- Revenue per employee: $__, $__, $__, $__, $__
- Capital raised to date: $__M
- Years to profitability: __ years
- Return on invested capital: __%, __%, __%, __%, __%

---

**9. SCENARIO ANALYSIS**

Build three scenarios:

**BASE CASE** (50% probability):
- Revenue growth: __% annually
- Gross margin: __% by Year 3
- Profitability: Year __
- Funding needed: $__M
- Valuation at exit (Year 5): $__M

**BEST CASE** (25% probability):
- Revenue growth: __% annually (50% higher)
- Gross margin: __% by Year 3
- Profitability: Year __ (1 year earlier)
- Funding needed: $__M (same or less)
- Valuation at exit (Year 5): $__M (2-3x higher)
- Drivers: [Faster customer adoption, higher pricing power, strategic partnership]

**WORST CASE** (25% probability):
- Revenue growth: __% annually (30% lower)
- Gross margin: __% by Year 3
- Profitability: Year __ (2 years later)
- Funding needed: $__M (50% more)
- Valuation at exit (Year 5): $__M (50% lower)
- Drivers: [Slower adoption, price pressure, higher costs]

**Sensitivity Analysis**:
What happens if we change key assumptions?

| Variable | -20% | Base | +20% | Impact on NPV |
|----------|------|------|------|---------------|
| Units sold | $__M | $__M | $__M | High |
| ASP | $__M | $__M | $__M | High |
| COGS % | $__M | $__M | $__M | Medium |
| CAC | $__M | $__M | $__M | Medium |
| Growth rate | $__M | $__M | $__M | High |

---

**10. FUNDRAISING IMPLICATIONS**

**Funding Requirements**:
- Seed round: $__M (get to [milestone])
- Series A: $__M (get to [milestone])
- Series B: $__M (get to [milestone])
- Total capital: $__M

**Dilution Schedule**:
| Round | Amount | Pre-money | Post-money | Dilution | Founder % |
|-------|--------|-----------|------------|----------|-----------|
| Seed | $__M | $__M | $__M | __% | __% |
| Series A | $__M | $__M | $__M | __% | __% |
| Series B | $__M | $__M | $__M | __% | __% |

**Investor Returns**:
Exit valuation: $__M (Year 5)
Investor IRR: __%
Investor MOIC: __x
Founder equity value: $__M

---

**MODEL BEST PRACTICES**:

1. **Build from first principles** (bottoms-up, not top-down)
2. **Separate assumptions from calculations** (easy to update)
3. **Use monthly detail for Year 1**, quarterly for Year 2-3, annually for Year 4-5
4. **Version control** (save iterations as you update)
5. **Sensitivity test** key assumptions
6. **Validate with comparables** (benchmarks from similar companies)
7. **Be conservative** on revenue, realistic on costs
8. **Show your work** (document assumptions and sources)
9. **Make it dynamic** (change inputs, see outputs update)
10. **Keep it simple** (complexity kills usability)

This model should be your strategic planning tool AND your fundraising tool."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def unit_economics(business_model):
    """
    Calculate and analyze unit economics.
    
    Models: saas, hardware, marketplace, services
    """
    
    prompt = f"""You are a unit economics specialist. Analyze and optimize unit economics for a {business_model} business.

**UNIT ECONOMICS ANALYSIS**

---

**1. CUSTOMER ACQUISITION COST (CAC)**

**Formula**: Total S&M spend / New customers acquired

**Build-up**:
```
Sales team:
- Sales reps: __ × $__k salary × ___% time on new biz = $__
- Sales management: $__
- Sales tools/enablement: $__
Subtotal sales: $__

Marketing:
- Digital marketing: $__
- Content marketing: $__
- Events/conferences: $__
- Brand/PR: $__
- Marketing team: $__
Subtotal marketing: $__

Total S&M for new customer acquisition: $__
New customers acquired: __
**CAC = $__**
```

**CAC by Channel** (which channels are most efficient?):
| Channel | Cost | Customers | CAC | Conversion Rate |
|---------|------|-----------|-----|-----------------|
| Inbound/SEO | $__ | __ | $__ | __% |
| Paid ads | $__ | __ | $__ | __% |
| Events | $__ | __ | $__ | __% |
| Referrals | $__ | __ | $__ | __% |
| Direct sales | $__ | __ | $__ | __% |
| Partners | $__ | __ | $__ | __% |

Insight: [Which channels to double down on vs. reduce]

---

**2. LIFETIME VALUE (LTV)**

**For {business_model}**:

**Formula**: Average revenue per customer × Gross margin % × Customer lifetime (years)

**Calculation**:
```
Average annual revenue per customer: $__
Gross margin: __%
Gross profit per customer per year: $__
Customer lifetime: __ years
**LTV = $__**
```

**Alternative Method (for recurring revenue)**:
```
Monthly recurring revenue (MRR): $__
Gross margin: __%
Churn rate (monthly): __%
LTV = (MRR × Gross margin) / Churn rate
**LTV = $__**
```

**LTV Drivers**:
1. Increase revenue per customer:
   - Upsells: +__% ($__)
   - Cross-sells: +__% ($__)
   - Price increases: +__% ($__)

2. Improve retention:
   - Current churn: __%
   - Target churn: __%
   - Impact: +__% LTV

3. Expand margin:
   - Current: __%
   - Target: __%
   - Impact: +__% LTV

---

**3. LTV:CAC RATIO**

**Current Ratio**: $__ LTV / $__ CAC = **__:1**

**Benchmark Standards**:
- < 1:1 = ❌ Unsustainable (losing money on every customer)
- 1:1 to 3:1 = ⚠️ Acceptable but challenging
- 3:1 to 5:1 = ✅ Healthy unit economics
- > 5:1 = 🚀 Excellent (may be under-investing in growth)

**Your Assessment**: [Evaluation]

**Path to 3:1** (if not there yet):
| Quarter | CAC | LTV | Ratio | Actions |
|---------|-----|-----|-------|---------|
| Current | $__ | $__ | __:1 | [Baseline] |
| Q1 | $__ | $__ | __:1 | [Reduce CAC via channel optimization] |
| Q2 | $__ | $__ | __:1 | [Improve conversion rates] |
| Q3 | $__ | $__ | __:1 | [Increase prices / reduce churn] |
| Q4 | $__ | $__ | __:1 | [Optimize gross margins] |

---

**4. PAYBACK PERIOD**

**Formula**: CAC / (Monthly revenue per customer × Gross margin %)

**Calculation**:
```
CAC: $__
Monthly revenue per customer: $__
Gross margin: __%
Monthly gross profit per customer: $__

**Payback period = __ months**
```

**Benchmark Standards**:
- < 12 months = ✅ Excellent
- 12-18 months = ✅ Good  
- 18-24 months = ⚠️ Acceptable
- > 24 months = ❌ Risky (too much capital tied up)

**Your Assessment**: [Evaluation]

**Accelerating Payback**:
- Increase initial contract size (annual vs. monthly)
- Add upfront implementation fees
- Improve gross margins
- Reduce CAC

---

**5. COHORT ANALYSIS**

Track unit economics by customer cohort:

| Cohort | Customers | CAC | Month 1 Rev | Month 6 Rev | Month 12 Rev | LTV | Payback |
|--------|-----------|-----|-------------|-------------|--------------|-----|---------|
| Jan '24 | __ | $__ | $__ | $__ | $__ | $__ | __ mo |
| Apr '24 | __ | $__ | $__ | $__ | $__ | $__ | __ mo |
| Jul '24 | __ | $__ | $__ | $__ | $__ | $__ | __ mo |
| Oct '24 | __ | $__ | $__ | $__ | $__ | $__ | __ mo |

**Cohort Insights**:
- Are newer cohorts improving? (Lower CAC, higher LTV)
- Which cohorts have best retention?
- What changed between cohorts?

---

**6. BENCHMARKING**

Compare your unit economics to industry standards:

**{business_model.upper()} BENCHMARKS**:
| Metric | Your Company | Industry P25 | Industry Median | Industry P75 |
|--------|--------------|--------------|-----------------|--------------|
| CAC | $__ | $__ | $__ | $__ |
| LTV | $__ | $__ | $__ | $__ |
| LTV:CAC | __:1 | 2.5:1 | 4:1 | 6:1 |
| Payback (mo) | __ | 18 | 12 | 8 |
| Gross margin | __% | 60% | 70% | 80% |
| Churn (annual) | __% | 20% | 12% | 5% |

**Gap Analysis**: Where do you need to improve?

---

**7. OPTIMIZATION ROADMAP**

**Priority 1 - Reduce CAC** (Target: -__% in __ months):
- [ ] Optimize ad spend (shift budget to highest ROI channels)
- [ ] Improve conversion rates (better landing pages, sales process)
- [ ] Increase referrals (referral program, customer advocacy)
- [ ] Build inbound engine (SEO, content marketing)
- Expected impact: CAC from $__ to $__

**Priority 2 - Increase LTV** (Target: +__% in __ months):
- [ ] Reduce churn (customer success program, product improvements)
- [ ] Expand revenue per customer (upsells, cross-sells)
- [ ] Increase prices (value-based pricing)
- [ ] Improve gross margins (reduce COGS)
- Expected impact: LTV from $__ to $__

**Priority 3 - Accelerate Payback** (Target: __ months):
- [ ] Annual contracts instead of monthly
- [ ] Upfront fees (implementation, onboarding)
- [ ] Faster sales cycles
- Expected impact: Payback from __ to __ months

**90-Day Action Plan**:
- Week 1-4: [Actions]
- Week 5-8: [Actions]
- Week 9-12: [Actions]

---

**8. FUNDRAISING IMPLICATIONS**

With current unit economics:
- Monthly gross profit per customer: $__
- Customers needed for break-even: __
- Capital required to reach break-even: $__M
- Time to break-even: __ months

With improved unit economics (post-optimization):
- Monthly gross profit per customer: $__
- Customers needed for break-even: __
- Capital required to reach break-even: $__M  
- Time to break-even: __ months

**This is why optimizing unit economics BEFORE scaling is critical.**

---

**KEY TAKEAWAYS**:

1. **Current State**: Your LTV:CAC is __:1 and payback is __ months
2. **Target State**: Get to 3:1+ ratio and <12 month payback
3. **Biggest Lever**: [CAC reduction / LTV increase / Margin improvement]
4. **Action Plan**: [Top 3 priorities]
5. **Expected Impact**: [Quantified improvement in 90 days]

Make unit economics your north star metric."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def valuation_analysis(stage, revenue, growth_rate):
    """
    Generate valuation analysis and comparables.
    """
    
    prompt = f"""You are a valuation expert. Analyze and justify valuation for a {stage} company with ${revenue} revenue growing at {growth_rate}% annually.

**VALUATION ANALYSIS**

---

**1. COMPARABLE COMPANY ANALYSIS**

Find 5-10 comparable companies at similar stage:

| Company | Stage | Revenue | Growth Rate | Last Valuation | Revenue Multiple | Notes |
|---------|-------|---------|-------------|----------------|------------------|-------|
| [Company A] | {stage} | $__M | __%| $__M | __x | [Similar tech/market] |
| [Company B] | {stage} | $__M | __% | $__M | __x | [Geographic focus] |
| [Company C] | {stage} | $__M | __% | $__M | __x | [Different model] |
| ... | | | | | | |

**Statistical Summary**:
- Median revenue multiple: __x
- Mean revenue multiple: __x
- Range: __x to __x
- Standard deviation: __x

**Factors Affecting Multiple**:
- Higher growth = Higher multiple (typically)
- Recurring revenue = Higher multiple
- Better margins = Higher multiple
- Larger market = Higher multiple
- Stronger team = Higher multiple

---

**2. YOUR VALUATION RANGE**

**Method 1: Revenue Multiple**

Base case (median comp multiple):
- Your revenue: $__M
- Median multiple: __x
- **Valuation: $__M**

Adjusted for growth:
- Your growth rate: {growth_rate}%
- Comparable avg growth: __%
- Growth premium: __% adjustment
- **Adjusted valuation: $__M**

**Method 2: Discounted Cash Flow (DCF)**

Assumptions:
- Year 1-5 revenue: $__M, $__M, $__M, $__M, $__M
- EBITDA margins: __%, __%, __%, __%, __%
- Terminal growth rate: __%
- Discount rate (WACC): __%

Calculation:
- PV of Year 1-5 cash flows: $__M
- Terminal value: $__M
- PV of terminal value: $__M
- **Enterprise value: $__M**
- Less: Net debt: $__M
- **Equity value: $__M**

**Method 3: Venture Capital Method**

Exit assumptions:
- Exit in Year __
- Exit valuation: $__M (based on revenue multiple at exit)
- Discount rate: __% (target IRR for {stage} investors)

Calculation:
- Terminal value: $__M
- Required return: (__%)^__ years = __x
- **Pre-money valuation: $__M**

---

**3. VALUATION RANGE SUMMARY**

| Method | Low | Base | High |
|--------|-----|------|------|
| Comparable companies | $__M | $__M | $__M |
| DCF | $__M | $__M | $__M |
| VC method | $__M | $__M | $__M |
| **VALUATION RANGE** | **$__M** | **$__M** | **$__M** |

**Recommended Range for Fundraising**: $__M - $__M

---

**4. NEGOTIATION STRATEGY**

**Your Position**:
- Floor (walk-away): $__M
- Target: $__M  
- Ceiling (if you can get it): $__M

**Justification for Target Valuation**:
1. **Strong Growth**: {growth_rate}% YoY (top quartile for stage)
2. **Market Opportunity**: $__B TAM, early mover advantage
3. **Unit Economics**: LTV:CAC of __:1, payback in __ months
4. **Traction**: [Key proof points]
5. **Team**: [Relevant experience / past success]
6. **Technology**: [IP / defensibility]

**Addressing Lower Valuations**:
If investors push for lower valuation:
- Demonstrate traction trajectory
- Show competitive tension (other interested investors)
- Offer milestone-based valuation step-ups
- Consider structure (convertible with cap vs. priced equity)

**Addressing Higher Valuations**:
If you can command premium:
- Leverage competitive process
- Demonstrate exceptional metrics vs. comps
- Show clear path to next milestone
- Quality of investors (value-add beyond capital)

---

**5. DEAL STRUCTURE OPTIONS**

**Option A: Priced Equity Round**
- Pre-money: $__M
- Investment: $__M
- Post-money: $__M
- Dilution: __%
- Pros: Price certainty, cleaner cap table
- Cons: More negotiation, legal costs

**Option B: SAFE (Simple Agreement for Future Equity)**
- Valuation cap: $__M
- Discount: __%
- Investment: $__M
- Pros: Fast, simple, delay valuation discussion
- Cons: Uncertain dilution, can stack up

**Option C: Convertible Note**
- Valuation cap: $__M
- Interest rate: __%
- Maturity: __ months
- Discount: __%
- Pros: Speed, flexibility
- Cons: Debt on books, can complicate next round

**Recommendation**: [Which structure and why for your situation]

---

**6. DILUTION ANALYSIS**

**Current Cap Table**:
| Shareholder | Shares | % |
|-------------|--------|---|
| Founders | __ | __% |
| Employees (option pool) | __ | __% |
| Previous investors | __ | __% |
| **Total** | **__** | **100%** |

**After This Round**:
| Shareholder | Shares | % | Change |
|-------------|--------|---|--------|
| Founders | __ | __% | -__% |
| Employees (option pool) | __ | __% | -__% |
| Previous investors | __ | __% | -__% |
| New investors | __ | __% | NEW |
| **Total** | **__** | **100%** | |

**Founder Equity Value**:
- Before round: __% × $__M = $__M
- After round: __% × $__M = $__M
- Absolute gain: $__M (even with dilution)

**This is the game**: Take dilution to increase pie size.

---

**7. COMPARABLE EXITS** (to justify exit potential)

Recent exits in your sector:

| Company | Exit Type | Exit Value | Revenue at Exit | Multiple | Acquirer | Year |
|---------|-----------|------------|-----------------|----------|----------|------|
| [Company A] | Acquisition | $__M | $__M | __x | [Acquirer] | 202X |
| [Company B] | IPO | $__M | $__M | __x | Public | 202X |
| [Company C] | Acquisition | $__M | $__M | __x | [Acquirer] | 202X |

**Median exit multiple**: __x revenue

**Your Potential Exit**:
- Year 5 revenue: $__M (projected)
- Exit multiple: __x (conservative)
- **Potential exit value: $__M**

**Investor Returns**:
- Investment: $__M at $__M valuation
- Ownership: __%
- Exit value: __% × $__M = $__M
- **Return: __x / __% IRR**

This math works for investors—that's why they'll invest.

---

**8. KEY MESSAGES FOR INVESTORS**

When discussing valuation:

✅ **DO**:
- Be confident but flexible
- Show your math (revenue multiples, DCF)
- Reference comparable valuations
- Demonstrate competitive tension
- Focus on potential, not just current state
- Emphasize value-add you want from investors

❌ **DON'T**:
- Pull numbers out of thin air
- Be arrogant or inflexible
- Over-optimize on valuation (wrong investors at high price is worse than right investors at fair price)
- Ignore market conditions
- Burn bridges over valuation disputes

---

**BOTTOM LINE**:

**Fair Valuation Range**: $__M - $__M

**Target for This Round**: $__M

**Raise Amount**: $__M

**Resulting Dilution**: __%

**Use This Analysis**:
- In pitch decks (valuation slide)
- In term sheet negotiations
- To educate co-founders/team
- To evaluate competing offers

Remember: Valuation is important, but finding the right investors who can help you succeed is MORE important."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Financial Modeler initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python financial_modeler.py <command> [parameters]")
        print("\nCommands:")
        print("  model <business_type> <years>     - Build financial model (hardware/saas/services/hybrid)")
        print("  economics <business_model>        - Analyze unit economics (saas/hardware/marketplace/services)")
        print("  valuation <stage> <revenue> <growth>  - Valuation analysis")
        print("\nExamples:")
        print("  python financial_modeler.py model hardware 5")
        print("  python financial_modeler.py economics hardware")
        print("  python financial_modeler.py valuation seed 500000 150")
    else:
        command = sys.argv[1].lower()
        
        if command == 'model':
            biz_type = sys.argv[2] if len(sys.argv) > 2 else 'hardware'
            years = int(sys.argv[3]) if len(sys.argv) > 3 else 5
            print(f"📊 Building {years}-year financial model for {biz_type} business...\n")
            result = build_model(biz_type, years)
            print(result)
            
        elif command == 'economics':
            model = sys.argv[2] if len(sys.argv) > 2 else 'hardware'
            print(f"💰 Analyzing unit economics for {model} business...\n")
            result = unit_economics(model)
            print(result)
            
        elif command == 'valuation':
            stage = sys.argv[2] if len(sys.argv) > 2 else 'seed'
            revenue = int(sys.argv[3]) if len(sys.argv) > 3 else 500000
            growth = int(sys.argv[4]) if len(sys.argv) > 4 else 150
            print(f"📈 Analyzing valuation for {stage} stage (${revenue:,} revenue, {growth}% growth)...\n")
            result = valuation_analysis(stage, revenue, growth)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: model, economics, valuation")
