"""
DEAL TERMS ANALYST AGENT
Analyzes investment term sheets and negotiates favorable terms.
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

def analyze_term_sheet(investor_name):
    """
    Analyze investment term sheet and identify key terms to negotiate.
    """
    
    prompt = f"""You are a startup attorney and term sheet negotiation expert. Provide comprehensive analysis of a term sheet from {investor_name}.

**TERM SHEET ANALYSIS FRAMEWORK**

---

**CRITICAL TERMS** (these determine control and economics)

**1. VALUATION & ECONOMICS**

**Pre-Money Valuation**: $__M
- ✅ Market rate? Compare to similar companies
- ⚠️ Red flags: Significantly below expectations, round-down from last raise
- 💡 Negotiation: Use competing offers, demonstrate traction growth

**Investment Amount**: $__M
- ✅ Fully funded? Or dependent on other investors?
- ⚠️ Syndication risk: Lead investor committing vs. contingent on others

**Post-Money Valuation**: $__M
**Dilution**: __%
- ✅ Founder ownership after round: __%
- ⚠️ Watch for: Option pool increase before round (increases dilution)

**Option Pool**:
- Current: __%
- Post-round: __%
- ⚠️ Sneaky dilution: Pool expansion counted in pre-money valuation dilutes existing shareholders, not new investors

**Fully Diluted vs. As-Converted**:
- How is ownership calculated?
- Does it include all options, warrants, convertibles?

---

**2. LIQUIDATION PREFERENCE** (who gets paid first in exit)

**Structure**: __x liquidation preference, [participating / non-participating]

**Examples**:

**1x Non-Participating** (STANDARD - GOOD):
```
Investment: $2M at $8M pre-money
Exit scenario: $50M sale

Investor gets greater of:
a) 1x investment = $2M, OR
b) 20% of proceeds = $10M
Investor takes: $10M
Founders/employees: $40M
✅ This is fair and market standard
```

**1x Participating** (INVESTOR-FAVORABLE):
```
Investment: $2M at $8M pre-money
Exit scenario: $50M sale

Investor gets:
a) 1x investment = $2M, PLUS
b) 20% of remaining $48M = $9.6M
Investor takes: $11.6M
Founders/employees: $38.4M
⚠️ Double-dipping - pushback on this
```

**2x or 3x Non-Participating** (INVESTOR-FAVORABLE):
```
Investment: $2M at $8M pre-money
2x liquidation preference
Exit scenario: $50M sale

Investor gets greater of:
a) 2x investment = $4M, OR
b) 20% of proceeds = $10M
Investor takes: $10M
⚠️ High multiple protects downside but okay if non-participating
```

**What to Negotiate**:
- ✅ Push for 1x non-participating (industry standard)
- ❌ Resist participating preferred (except in dire circumstances)
- ❌ Resist > 1x multiple (except in down rounds)

---

**3. BOARD COMPOSITION** (who controls the company)

**Proposed Board Structure**:
- __ founder seats
- __ investor seats  
- __ independent seats
- Total: __ seats

**Analysis**:
- ✅ Good: Founders maintain majority or equal representation
- ⚠️ Caution: Investor majority (lose control)
- ✅ Good: Independent director mutually agreed upon
- ⚠️ Caution: Investor picks independent director

**Board Observers**:
- Who: [List]
- ⚠️ Watch: Too many observers slows decision-making

**Voting Thresholds**:
- Majority vote vs. supermajority vs. unanimous
- ⚠️ Watch: Supermajority/unanimous for routine decisions = gridlock

---

**4. PROTECTIVE PROVISIONS** (veto rights for investors)

Investor gets veto/approval rights over:

**STANDARD** (typical and acceptable):
- ✅ Sale of company
- ✅ Liquidation or dissolution
- ✅ Amendments to charter that affect investor rights
- ✅ Issuing stock senior to or on parity with preferred
- ✅ Redemption of shares
- ✅ Changes to board size or composition
- ✅ Related party transactions

**CONCERNING** (overreach - negotiate these):
- ⚠️ Operating budget approval (day-to-day control)
- ⚠️ Any employee hire/fire above $X salary
- ⚠️ Any contract over $X
- ⚠️ Raising additional capital
- ⚠️ Intellectual property decisions
- ⚠️ Office location changes

**Recommendation**: Protect investor downside (sale, liquidation, dilution) but preserve management's ability to operate company.

---

**5. ANTI-DILUTION PROTECTION**

**Type**: [Broad-based weighted average / Narrow-based / Full ratchet]

**Explanation**:

**No Anti-Dilution** (FOUNDER-FRIENDLY):
- If down round happens, investor ownership stays at original %
- They dilute just like everyone else

**Broad-Based Weighted Average** (STANDARD - FAIR):
- Adjusts conversion price based on price and amount of down round
- Protects investor partially, but not punitive to founders
- ✅ This is market standard - accept it

**Full Ratchet** (VERY INVESTOR-FAVORABLE):
- If down round at lower price, investor gets repriced to new lower price
- Massively dilutes founders
- ❌ Avoid this unless desperate

**Example**:
```
Investment: $2M at $10/share (200K shares, 20% ownership)
Down round: $5/share

No protection: Investor keeps 200K shares (20% ownership)
Weighted average: Investor gets ~250K shares (~22% ownership)
Full ratchet: Investor gets 400K shares (dilutes founders significantly)
```

**Recommendation**: Broad-based weighted average is standard. Push back on full ratchet strongly.

---

**6. DRAG-ALONG RIGHTS** (can investors force a sale?)

**Provision**: Investors holding __% can force all shareholders to approve sale

**Analysis**:
- ✅ Reasonable: 66-75% threshold (prevents minority blocking good exit)
- ⚠️ Concerning: < 50% threshold (investors alone can force sale)
- ✅ Good: Carve-outs for founders (minimum price thresholds, liquidity protections)

**Negotiate**:
- Minimum sale price (e.g., must be > $XM or >__x return for founders)
- Founder liquidity (founders get to sell pro-rata portion)
- Founders don't have personal liability exposure

---

**7. PAY-TO-PLAY** (penalty for not investing in future rounds)

**Provision**: If investor doesn't participate pro-rata in next round, their preferred converts to common (lose preferences)

**Analysis**:
- ✅ Good for founders: Incentivizes continued support
- ⚠️ Can backfire: If terms are bad, good investors get punished for not following on

**Negotiation**: Include in Series B+, not usually in Seed/Series A

---

**8. REDEMPTION RIGHTS** (can investors force you to buy them out?)

**Provision**: After __ years, investors can require company to redeem shares

**Analysis**:
- ⚠️ Concerning: Creates pressure for exit or raises
- ⚠️ Problematic: Most startups don't have cash to redeem
- Often present but rarely exercised (signaling mechanism)

**Negotiation**: 
- Push for longer timeframe (7-10 years, not 3-5)
- Make it contingent on company having available cash
- Include in late-stage rounds only

---

**9. CONVERSION RIGHTS**

**Provision**: Preferred stock converts to common at __:1 ratio

**Standard Terms**:
- Voluntary conversion at any time
- Automatic conversion upon IPO (> $X valuation, > $Y share price)
- Automatic conversion if __% of preferred holders vote to convert

**Analysis**:
- ✅ Standard: 1:1 conversion ratio (subject to anti-dilution adjustments)
- ✅ Standard: Auto-convert on qualified IPO
- ⚠️ Watch: Any provisions that allow investors to stay preferred in IPO (rare but problematic)

---

**10. VESTING** (for founders and employees)

**Founder Vesting**:
- ⚠️ Red flag: Investors requiring founder equity to re-vest
- Standard ask: 4-year vest, 1-year cliff, with credit for time served
- ✅ Negotiate: If been working for 2 years, start with 50% vested

**Employee Option Pool**:
- Size: __%  
- Pre-money or post-money?
- ⚠️ Watch: Large pool expansion counted pre-money (dilutes founders)

**Acceleration**:
- Single-trigger: Vesting accelerates on sale
- Double-trigger: Vesting accelerates on sale + termination
- ✅ Negotiate: Double-trigger for founders (50-100% acceleration)

---

**11. NO-SHOP / EXCLUSIVITY**

**Provision**: __ day exclusive negotiating period (can't talk to other investors)

**Analysis**:
- ✅ Reasonable: 30-45 days after term sheet signed
- ⚠️ Concerning: > 60 days or very restrictive terms
- ✅ Include: Break-up fee or expense reimbursement if investor backs out

**Strategy**: 
- Use competing term sheets to reduce exclusivity period
- Ensure all major issues resolved before signing (no surprises in docs)

---

**12. INFORMATION RIGHTS**

**Provision**: Company provides investors with:
- Monthly financial statements
- Annual audited financials
- Budget and operating plan
- Access to facilities and records

**Analysis**:
- ✅ Standard: Quarterly financials, annual budget, annual audits
- ⚠️ Burdensome: Monthly detailed reports (time sink for small companies)
- ✅ Reasonable: Rights expire when investor holds < __% (e.g., 5%)

---

**13. PRO-RATA RIGHTS** (right to invest in future rounds)

**Provision**: Investor can maintain ownership % in future rounds

**Analysis**:
- ✅ Good: Shows investor commitment to support company long-term
- ✅ Reasonable: Pro-rata participation in future rounds
- ⚠️ Generous: Super pro-rata (> their ownership %)

---

**14. REGISTRATION RIGHTS** (for IPO)

**Types**:
- Demand rights: Investor can force registration (IPO)
- Piggyback rights: Investor can join company-initiated registration

**Analysis**:
- ✅ Standard: Piggyback rights (low burden)
- ⚠️ Burdensome: Multiple demand rights early on
- ✅ Include: Cutoffs for small holders (< __%)

---

**15. NDAS, NON-COMPETES, IP ASSIGNMENT**

**Standard Provisions**:
- Founders sign NDAs
- Founders assign all IP to company
- Key employees sign offer letters with IP assignment
- Non-competes (where enforceable)

**Analysis**:
- ✅ Expected: Clean IP ownership by company
- ⚠️ Watch: Overly broad non-competes

---

**OVERALL TERM SHEET SCORECARD**

Rate each category (Founder-Friendly | Fair/Market | Investor-Favorable):

| Term | Rating | Comments |
|------|--------|----------|
| Valuation | [FF/Market/IF] | |
| Liquidation Preference | [FF/Market/IF] | |
| Board Composition | [FF/Market/IF] | |
| Protective Provisions | [FF/Market/IF] | |
| Anti-Dilution | [FF/Market/IF] | |
| Drag-Along | [FF/Market/IF] | |
| Redemption | [FF/Market/IF] | |
| Vesting | [FF/Market/IF] | |
| No-Shop | [FF/Market/IF] | |
| **OVERALL** | **[FF/Market/IF]** | |

---

**NEGOTIATION STRATEGY**

**Top 3 Issues to Negotiate**:
1. [Issue #1] - [Why and what to counter-propose]
2. [Issue #2] - [Why and what to counter-propose]
3. [Issue #3] - [Why and what to counter-propose]

**What to Accept** (pick your battles):
- [List 2-3 terms that are reasonable/market standard]

**What to Push Back On** (non-negotiable):
- [List 2-3 terms that are problematic]

**Alternatives if Can't Get Good Terms**:
- Walk away and find better investors
- Raise less money on better terms
- Consider convertible/SAFE to defer valuation discussion
- Build more traction before raising

---

**TERM SHEET COMPARISON** (if you have multiple offers)

Compare side-by-side:

| Term | Investor A | Investor B | Investor C | Winner |
|------|------------|------------|------------|--------|
| Valuation | $__M | $__M | $__M | |
| Liquidation Pref | 1x non-part | 1x participating | 2x non-part | |
| Board Control | 2F-2I-1Ind | 2F-3I | 3F-2I | |
| Anti-Dilution | Weighted avg | Weighted avg | Full ratchet | |
| Overall Rating | | | | |

**Beyond Terms - Investor Quality**:
- Value-add (connections, expertise, operational help)
- Reputation (references from portfolio companies)
- Support in tough times (will they fund bridge rounds?)
- Network (can they help recruit, sell, raise next round?)

**Best offer ≠ Highest valuation**

Sometimes better to take lower valuation from better investor.

---

**FINAL RECOMMENDATIONS**

**Should you sign this term sheet?**
- ✅ YES, if: [Conditions]
- ⚠️ YES, but negotiate: [Specific terms]
- ❌ NO, because: [Dealbreakers]

**Next Steps**:
1. [Action]
2. [Action]
3. [Action]

**Timeline**:
- Negotiate: __ days
- Legal docs: __ days
- Due diligence: __ days
- Close: __ days

**Cost Estimate**:
- Legal fees: $__k - $__k
- Due diligence support: $__k
- Total: $__k - $__k

Get a good startup attorney. The legal fees are worth it—bad terms can cost you millions."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def standard_terms():
    """
    Display standard/market terms for different funding stages.
    """
    
    prompt = """You are a startup attorney. Provide guide to market-standard terms for each funding stage.

**MARKET STANDARD TERMS BY STAGE**

---

**FRIENDS & FAMILY ROUND** ($25k - $500k)

**Typical Structure**: Convertible note or SAFE

**Standard Terms**:
- Valuation cap: $2M - $5M (depends on traction)
- Discount: 20%
- Interest rate (if note): 4-6%
- Maturity (if note): 18-24 months
- No board seats
- Minimal investor rights
- Light documentation (5-10 pages)

**Legal Costs**: $2k - $5k

**Timeline**: 2-4 weeks

---

**SEED ROUND** ($500k - $3M)

**Typical Structure**: SAFE or Priced Equity

**If SAFE**:
- Valuation cap: $5M - $15M
- Discount: 20%
- Most favored nation (MFN) clause
- Pro-rata rights for lead investor

**If Priced Equity**:
- Valuation: $5M - $15M pre-money
- Liquidation preference: 1x non-participating
- Anti-dilution: Broad-based weighted average
- Board: 1-2 founders, 1 investor, 0-1 independent
- Option pool: 10-15% post-money
- Protective provisions: Standard package
- Information rights: Quarterly financials
- Pro-rata rights: Yes for lead, sometimes for others

**Legal Costs**: $15k - $40k

**Timeline**: 6-12 weeks

---

**SERIES A** ($3M - $15M)

**Structure**: Priced Equity Round (Series A Preferred Stock)

**Standard Terms**:

**Valuation**: $15M - $60M pre-money

**Liquidation Preference**: 
- 1x non-participating (market standard)
- Senior to common, pari passu with other Series A

**Anti-Dilution**:
- Broad-based weighted average
- Adjusts on down rounds only

**Board Composition**:
- Total: 5 seats
- 2 founders
- 2 investors (1 from lead, 1 from previous investors or another Series A investor)
- 1 independent (mutually agreed)

**Protective Provisions** (require Series A majority approval):
- Sale or liquidation of company
- Amendment of charter
- Issuance of senior or pari passu securities
- Stock repurchases
- Dividends
- Changes to board size
- Related party transactions > $X

**Voting**:
- Series A votes with common on as-converted basis
- Except for protective provisions (class vote)

**Dividends**: 
- Non-cumulative, when/as declared by board
- Typically never declared

**Conversion**:
- Optional at any time (1:1 ratio, subject to anti-dilution)
- Automatic on qualified IPO ($50M+ valuation, $10+ share price)
- Automatic if majority of Series A votes to convert

**Redemption**: 
- Rare at Series A
- If included: After 5-7 years, can be triggered by majority of Series A
- Paid over 3 years
- Subject to available funds

**Vesting**:
- Founders: Typically already vested or accelerated schedule with credit
- New employees: 4 years, 1 year cliff
- Acceleration: Double-trigger for executives (50% or more)

**Option Pool**:
- Size: 15-20% post-money
- Expansion often negotiated as part of round

**Information Rights**:
- Quarterly unaudited financials (within 30 days)
- Annual audited financials (within 120 days)
- Annual operating budget (30 days before fiscal year)
- Monthly cap table updates

**Pro-Rata Rights**:
- Major investors (> 5% or > $1M invested): Yes
- Minor investors: Sometimes

**Registration Rights**:
- Piggyback rights: Yes
- Demand rights: 1-2 demands, exercisable after earlier of IPO or 5 years

**Drag-Along**:
- Holders of 66-75% of voting power can approve sale
- Must meet minimum price (e.g., > $XM or > 3x investor cost)

**No-Shop**:
- 45 days after term sheet signed
- Expense reimbursement if company breaches

**Legal Costs**: $40k - $100k

**Timeline**: 8-16 weeks (including due diligence)

---

**SERIES B** ($15M - $50M)

**Structure**: Series B Preferred Stock

**Standard Terms** (similar to Series A, with these differences):

**Valuation**: $50M - $200M pre-money

**Liquidation Preference**:
- 1x non-participating
- Senior to Series A and common
- Series A maintains their 1x preference

**Board Composition**:
- Total: 5-7 seats
- 2 founders
- 3 investors (1 Series B lead, 1-2 from Series A)
- 1-2 independent

**Protective Provisions**:
- Series B gets their own class vote
- Some provisions require majority of A + B together

**Pay-to-Play** (sometimes included):
- If existing investors don't participate pro-rata in Series B, their Series A preferred converts to common
- Ensures continued support from existing investors

**Other Terms**: Generally same as Series A

**Legal Costs**: $50k - $150k

**Timeline**: 10-20 weeks

---

**SERIES C+** ($50M+)

**Structure**: Series C Preferred Stock

**Valuation**: $200M+ pre-money

**Terms**: Generally similar to Series B

**Additional Considerations**:
- More complex cap table management
- Multiple liquidation preferences stacked
- More sophisticated investors with specific requirements
- May include:
  * Weighted average anti-dilution for all series
  * Cumulative dividends (rare but possible)
  * Stricter protective provisions
  * Management incentive plans

**Legal Costs**: $75k - $200k+

**Timeline**: 12-24 weeks

---

**TERM SHEET RED FLAGS** (regardless of stage)

❌ **Run away if you see**:
- Participating preferred (double dip on exits)
- Full ratchet anti-dilution
- > 1x liquidation preference (in normal market)
- Investor board control (more investor seats than founders)
- Personal guarantees or liability for founders
- Excessive protective provisions (operating control)
- Very short redemption rights (3 years)
- Founder equity re-vesting from zero
- Option pool tricks (huge expansion pre-money)
- "Pay-to-play" in Seed/Series A (too early)

⚠️ **Negotiate hard if you see**:
- < 30 days no-shop period
- Broad redemption rights
- Very low valuation compared to traction
- Narrow-based weighted average anti-dilution
- Super pro-rata rights (investor can buy more than pro-rata)
- Aggressive vesting (no credit for time served)

✅ **Green flags**:
- 1x non-participating liquidation preference
- Broad-based weighted average anti-dilution
- Balanced board (founders equal to or > investors)
- Standard protective provisions (downside protection only)
- Reasonable no-shop (30-45 days)
- Pro-rata rights for major investors
- Double-trigger acceleration
- Information rights with reasonable thresholds

---

**BENCHMARKING YOUR TERMS**

Compare your term sheet to these standards:

| Your Term | Your Terms | Market Standard | Assessment |
|-----------|------------|-----------------|------------|
| Stage | | | |
| Valuation | $__M | $__M - $__M | [Good/Market/Low] |
| Liq Pref | | 1x non-part | [Match/Worse] |
| Anti-Dilution | | Broad WA | [Match/Worse] |
| Board | | Balanced | [Match/Worse] |

If most terms are "Match" → Go ahead

If several "Worse" → Negotiate or walk

---

**NEGOTIATION PRIORITIES**

**Non-Negotiable** (walk away if can't fix):
1. Valuation significantly below market
2. Participating preferred or high multiples
3. Loss of board control
4. Excessive operational control (protective provisions)

**Important but Negotiable**:
1. Option pool size and timing
2. Vesting schedules
3. Information rights scope
4. Pro-rata rights
5. No-shop period length

**Nice to Have**:
1. Registration rights specifics
2. Drag-along thresholds
3. Minor protective provisions
4. Expense reimbursement terms

---

**FINAL ADVICE**

1. **Always get a lawyer** specializing in startups
   - Cost: $15k-50k for Series A
   - Savings: Potentially millions in bad terms

2. **Understand every term** - Don't sign what you don't understand

3. **Think long-term** - Terms affect every future round and exit

4. **Value matters more than valuation** - $5M from a great investor > $8M from a problematic one

5. **Create competition** - Multiple term sheets = better terms

6. **Benchmark** - Know what's market standard for your stage

7. **Talk to other founders** - Get references on investors

8. **Read between the lines** - Aggressive terms signal potential problems

Your cap table is permanent. Choose wisely."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def comparison_tool(num_offers=2):
    """
    Generate side-by-side comparison framework for multiple term sheets.
    """
    
    prompt = f"""You are analyzing {num_offers} competing term sheets. Create comprehensive comparison framework.

**TERM SHEET COMPARISON TOOL**

---

**EXECUTIVE SUMMARY**

| | Offer A | Offer B {' | Offer C' if num_offers >= 3 else ''} | Winner |
|-|---------|---------|---------|--------|
| **Investor** | [Name] | [Name] {' | [Name]' if num_offers >= 3 else ''} | |
| **Amount** | $__M | $__M {' | $__M' if num_offers >= 3 else ''} | |
| **Pre-Money** | $__M | $__M {' | $__M' if num_offers >= 3 else ''} | |
| **Dilution** | __% | __% {' | __%' if num_offers >= 3 else ''} | |
| **Lead?** | Yes/No | Yes/No {' | Yes/No' if num_offers >= 3 else ''} | |
| **Overall Score** | __/100 | __/100 {' | __/100' if num_offers >= 3 else ''} | |

---

**DETAILED COMPARISON**

**1. ECONOMICS** (40 points)

| Term | Offer A | Offer B | Offer C | Best | Points |
|------|---------|---------|---------|------|--------|
| **Valuation** | | | | | __/15 |
| Pre-money | $__M | $__M | $__M | | |
| Post-money | $__M | $__M | $__M | | |
| Price per share | $__ | $__ | $__ | | |
| Dilution to founders | __% | __% | __% | | |
| | | | | | |
| **Liquidation Pref** | | | | | __/15 |
| Multiple | __x | __x | __x | | |
| Participating? | Y/N | Y/N | Y/N | | |
| Seniority | [Structure] | [Structure] | [Structure] | | |
| | | | | | |
| **Exit Scenarios** | | | | | __/10 |
| $20M exit | $__M to investors | $__M | $__M | | |
| $50M exit | $__M to investors | $__M | $__M | | |
| $100M exit | $__M to investors | $__M | $__M | | |
| $200M exit | $__M to investors | $__M | $__M | | |
| | | | | | |
| **Economics Score** | **__/40** | **__/40** | **__/40** | | |

---

**2. CONTROL** (30 points)

| Term | Offer A | Offer B | Offer C | Best | Points |
|------|---------|---------|---------|------|--------|
| **Board** | | | | | __/15 |
| Founders | __ | __ | __ | | |
| Investors | __ | __ | __ | | |
| Independent | __ | __ | __ | | |
| Observer rights | [Who] | [Who] | [Who] | | |
| Founder control? | Y/N | Y/N | Y/N | | |
| | | | | | |
| **Protective Provisions** | | | | | __/10 |
| # of provisions | __ | __ | __ | | |
| Operational control? | Y/N | Y/N | Y/N | | |
| Reasonable scope? | Y/N | Y/N | Y/N | | |
| | | | | | |
| **Drag-Along** | | | | | __/5 |
| Threshold | __% | __% | __% | | |
| Minimum price | $__M | $__M | $__M | | |
| Founder protection | Y/N | Y/N | Y/N | | |
| | | | | | |
| **Control Score** | **__/30** | **__/30** | **__/30** | | |

---

**3. DOWNSIDE PROTECTION** (15 points)

| Term | Offer A | Offer B | Offer C | Best | Points |
|------|---------|---------|---------|------|--------|
| **Anti-Dilution** | | | | | __/8 |
| Type | [Type] | [Type] | [Type] | | |
| Founder-friendly? | Y/N | Y/N | Y/N | | |
| | | | | | |
| **Redemption** | | | | | __/4 |
| Years until trigger | __ | __ | __ | | |
| Conditions | [Terms] | [Terms] | [Terms] | | |
| | | | | | |
| **Vesting** | | | | | __/3 |
| Founder revest? | Y/N | Y/N | Y/N | | |
| Acceleration | [Terms] | [Terms] | [Terms] | | |
| | | | | | |
| **Downside Score** | **__/15** | **__/15** | **__/15** | | |

---

**4. TERMS & CONDITIONS** (15 points)

| Term | Offer A | Offer B | Offer C | Best | Points |
|------|---------|---------|---------|------|--------|
| **No-Shop** | | | | | __/3 |
| Period | __ days | __ days | __ days | | |
| Break fee | $__ | $__ | $__ | | |
| | | | | | |
| **Conditions** | | | | | __/5 |
| Due diligence | [Scope] | [Scope] | [Scope] | | |
| Syndication risk | High/Med/Low | H/M/L | H/M/L | | |
| Legal review | [Concerns] | [Concerns] | [Concerns] | | |
| | | | | | |
| **Rights** | | | | | __/4 |
| Pro-rata | Y/N | Y/N | Y/N | | |
| Info rights | [Level] | [Level] | [Level] | | |
| Registration | [Type] | [Type] | [Type] | | |
| | | | | | |
| **Option Pool** | | | | | __/3 |
| Size | __% | __% | __% | | |
| Pre or post? | [When] | [When] | [When] | | |
| | | | | | |
| **Terms Score** | **__/15** | **__/15** | **__/15** | | |

---

**TOTAL SCORE**: __/100, __/100, __/100

---

**BEYOND THE TERMS - QUALITATIVE FACTORS**

**Investor Quality** (not scored, but critical):

| Factor | Offer A | Offer B | Offer C | Winner |
|--------|---------|---------|---------|--------|
| **Reputation** | | | | |
| Industry standing | [Assessment] | [Assessment] | [Assessment] | |
| Portfolio success | __% exit rate | __% | __% | |
| Founder references | [Feedback] | [Feedback] | [Feedback] | |
| | | | | |
| **Value-Add** | | | | |
| Domain expertise | [Level] | [Level] | [Level] | |
| Operational help | [What] | [What] | [What] | |
| Recruiting network | [Strength] | [Strength] | [Strength] | |
| Customer intros | [Potential] | [Potential] | [Potential] | |
| Next round help | [Track record] | [Track record] | [Track record] | |
| | | | | |
| **Chemistry** | | | | |
| Founder-investor fit | [Assessment] | [Assessment] | [Assessment] | |
| Communication style | [Match?] | [Match?] | [Match?] | |
| Trust level | [Gut feel] | [Gut feel] | [Gut feel] | |
| | | | | |
| **Support in Tough Times** | | | | |
| Bridge round history | [Supportive?] | [Supportive?] | [Supportive?] | |
| Down round behavior | [Fair?] | [Fair?] | [Fair?] | |
| Portfolio company loyalty | [Examples] | [Examples] | [Examples] | |

---

**EXIT SCENARIO MODELING**

Model founder returns under different exit scenarios:

**$20M Exit** (early acquisition):
| | Offer A | Offer B | Offer C |
|-|---------|---------|---------|
| Investor payout | $__M | $__M | $__M |
| Founder payout | $__M | $__M | $__M |
| Founder % of exit | __% | __% | __% |

**$50M Exit** (decent outcome):
| | Offer A | Offer B | Offer C |
|-|---------|---------|---------|
| Investor payout | $__M | $__M | $__M |
| Founder payout | $__M | $__M | $__M |
| Founder % of exit | __% | __% | __% |

**$100M Exit** (good outcome):
| | Offer A | Offer B | Offer C |
|-|---------|---------|---------|
| Investor payout | $__M | $__M | $__M |
| Founder payout | $__M | $__M | $__M |
| Founder % of exit | __% | __% | __% |

**$200M+ Exit** (great outcome):
| | Offer A | Offer B | Offer C |
|-|---------|---------|---------|
| Investor payout | $__M | $__M | $__M |
| Founder payout | $__M | $__M | $__M |
| Founder % of exit | __% | __% | __% |

**Key Insight**: At what exit value do the term sheet differences stop mattering?

---

**RECOMMENDATION**

**Rank Order**:
1. **[Offer Name]** - Score: __/100
   - Pros: [Top 3 reasons]
   - Cons: [Top 2 concerns]
   - Negotiation targets: [What to improve]

2. **[Offer Name]** - Score: __/100
   - Pros: [Top 3 reasons]
   - Cons: [Top 2 concerns]
   - Why not #1: [Key differentiators]

3. **[Offer Name]** - Score: __/100
   - Pros: [Top 3 reasons]
   - Cons: [Top 2 concerns]
   - Why not #1: [Key differentiators]

---

**DECISION FRAMEWORK**

**Choose Offer A if**:
- [Conditions where this is best choice]

**Choose Offer B if**:
- [Conditions where this is best choice]

**Choose Offer C if**:
- [Conditions where this is best choice]

---

**NEGOTIATION STRATEGY**

**With Top Choice**:
1. Accept: [Terms you're comfortable with]
2. Negotiate: [Terms to improve]
3. Walk away if: [Dealbreakers]

**Leverage from Other Offers**:
- Use [Offer X]'s valuation to improve [Offer Y]
- Use [Offer X]'s terms to fix [Offer Y]'s problematic provisions
- Create competitive tension without burning bridges

**Timeline**:
- Week 1: Negotiate key terms
- Week 2: Legal review
- Week 3-4: Due diligence
- Week 5-6: Closing

---

**BOTTOM LINE**

**Best Offer**: [Offer Name]

**Why**: [2-3 sentence justification considering terms, investor quality, and strategic fit]

**Next Action**: [Specific next step]

Remember: 
- Best terms ≠ Highest valuation
- Best investor ≠ Best terms
- Optimize for long-term success, not short-term ego"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Deal Terms Analyst initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python deal_terms_analyst.py <command> [parameters]")
        print("\nCommands:")
        print("  analyze <investor_name>  - Analyze term sheet from specific investor")
        print("  standards                - Show market standard terms by stage")
        print("  compare <num_offers>     - Compare multiple term sheets (2-3)")
        print("\nExamples:")
        print("  python deal_terms_analyst.py analyze 'Andreessen Horowitz'")
        print("  python deal_terms_analyst.py standards")
        print("  python deal_terms_analyst.py compare 3")
    else:
        command = sys.argv[1].lower()
        
        if command == 'analyze':
            investor = sys.argv[2] if len(sys.argv) > 2 else 'Investor Name'
            print(f"⚖️ Analyzing term sheet from {investor}...\n")
            result = analyze_term_sheet(investor)
            print(result)
            
        elif command == 'standards':
            print("📋 Showing market standard terms by stage...\n")
            result = standard_terms()
            print(result)
            
        elif command == 'compare':
            num = int(sys.argv[2]) if len(sys.argv) > 2 else 2
            print(f"⚖️ Comparing {num} term sheets...\n")
            result = comparison_tool(num)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: analyze, standards, compare")
