"""
Licensing Strategist - Negotiate deals and structure agreements
Division: IP & Patent Strategy  
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path='../.env')

class LicensingStrategist:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Licensing Strategist initialized (Groq - FREE)")
    
    def target_licensees(self, technology_description):
        """Identify ideal licensing targets"""
        prompt = f"""
You are a licensing strategist identifying target licensees.

TECHNOLOGY TO LICENSE:
{technology_description}

Identify licensing targets:

## TIER 1 TARGETS (Top 10 Priority)

### Company 1: [Name]
- **Industry:** [Sector]
- **Why Good Fit:** [Strategic rationale]
- **Revenue Potential:** $X-Y annually
- **Decision Maker:** [Title/department]
- **Approach Strategy:** [How to reach them]
- **Expected Terms:** [Royalty rate, structure]

### Company 2: [Name]
[etc. for top 10]

## TIER 2 TARGETS (Secondary Opportunities)

By industry segment:
- **Micro-hydro manufacturers:** [5-10 companies]
- **Hydropower engineering firms:** [5-10 companies]
- **Renewable energy developers:** [5-10 companies]
- **Equipment distributors:** [5-10 companies]

## GEOGRAPHIC MARKETS

### North America
- Key players
- Market size
- Regulatory environment

### Europe
[etc.]

### Asia-Pacific
[etc.]

## LICENSING REVENUE MODEL

### Scenario Analysis
| Scenario | # Licensees | Avg Royalty | Annual Revenue |
|----------|-------------|-------------|----------------|
| Conservative | 2-3 | 2% | $X |
| Base Case | 5-7 | 3% | $Y |
| Optimistic | 10-15 | 4% | $Z |

## OUTREACH STRATEGY

### Phase 1 (Month 1-2): Top 3 Targets
- Contact approach
- Meeting prep
- Pitch materials needed

### Phase 2 (Month 3-4): Next 7 Targets
[etc.]

### Phase 3 (Month 5-6): Tier 2 Expansion
[etc.]

Generate comprehensive licensee targeting strategy.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=4000
        )
        return completion.choices[0].message.content
    
    def deal_structure(self, licensee_profile):
        """Design optimal licensing deal structure"""
        prompt = f"""
Design licensing deal structure for:

LICENSEE PROFILE:
{licensee_profile}

Create deal structure options:

## OPTION 1: EXCLUSIVE LICENSE

### Financial Terms
- **Upfront Payment:** $X (patent acquisition cost + premium)
- **Royalty Rate:** 4-6% of net sales
- **Minimum Annual Royalty:** $Y (ensures revenue floor)
- **Milestone Payments:** 
  - First commercial sale: $Z
  - $1M in sales: $Z
  - Patent improvements: Negotiable

### Non-Financial Terms
- **Exclusivity:** Geographic (North America) or Field-of-Use (residential systems)
- **Term:** 5-10 years with renewal options
- **Sublicensing:** Permitted with 50% revenue share
- **Development Milestones:** Commercial product within 18 months or revert to non-exclusive
- **Improvement Sharing:** Yes, cross-license improvements

### Pros & Cons
✅ Higher royalty rate, strategic partnership, focused development
❌ Limited market penetration, single counterparty risk

## OPTION 2: NON-EXCLUSIVE LICENSE

### Financial Terms
- **Upfront Payment:** $A (lower than exclusive)
- **Royalty Rate:** 2-3% of net sales
- **Minimum Annual Royalty:** $B
- **No milestone payments**

### Non-Financial Terms
- **Exclusivity:** None (license to multiple companies)
- **Term:** 3-5 years with auto-renewal
- **Sublicensing:** Not permitted
- **Field-of-Use:** Any hydro application
- **Improvement Sharing:** Optional

### Pros & Cons
✅ Broader market penetration, multiple revenue streams, faster adoption
❌ Lower per-licensee revenue, potential market conflicts

## OPTION 3: TIERED/HYBRID LICENSE

### Structure
- **Tier 1 (Exclusive):** Premium partner for specific vertical (e.g., large commercial)
  - Upfront: $X, Royalty: 5%, MFN clause
- **Tier 2 (Semi-Exclusive):** 2-3 partners for residential market
  - Upfront: $Y, Royalty: 3%
- **Tier 3 (Non-Exclusive):** Open licensing for developing markets
  - Upfront: $Z, Royalty: 2%

### Market Segmentation
- By product size (residential vs commercial vs utility-scale)
- By geography (North America vs Europe vs Asia)
- By application (grid-connected vs off-grid)

## DEAL TERMS COMPARISON

| Term | Exclusive | Non-Exclusive | Tiered |
|------|-----------|---------------|--------|
| Upfront | $200k | $50k | $100k avg |
| Royalty | 5% | 2.5% | 3-5% |
| Min Annual | $50k | $10k | $25k |
| # Licensees | 1 | 5-10 | 3-5 |
| Year 1 Revenue | $250k | $150k | $275k |
| Year 5 Revenue | $500k | $750k | $1.2M |

## NEGOTIATION RANGES

For each term, set:
- **Target:** What we want
- **Floor:** Minimum acceptable
- **Ceiling:** Maximum to offer

Example:
- Royalty Rate: Target 4%, Floor 2%, Ceiling 6%

## RISK MITIGATION

- **Performance Clauses:** Revert rights if no commercialization
- **Quality Control:** Approval rights on products
- **Audit Rights:** Annual royalty audits
- **Termination Rights:** Material breach, bankruptcy, non-payment

## RECOMMENDATION
[Which deal structure for this specific licensee? Why?]

Generate comprehensive deal structure options.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=4000
        )
        return completion.choices[0].message.content
    
    def negotiation_playbook(self, company_name):
        """Create negotiation strategy for specific licensee"""
        prompt = f"""
Create licensing negotiation playbook for: {company_name}

## PRE-NEGOTIATION RESEARCH

### Company Intelligence
- Revenue and profitability
- Current product line
- Strategic priorities
- M&A history
- Licensing history (deal structures they prefer)

### Decision Maker Profiling
- Name and title of licensing contact
- Background and priorities
- Negotiation style (data-driven, relationship-focused, etc.)
- Authority level (can they sign or must escalate?)

### Competitive Context
- Do they have alternative solutions?
- How urgently do they need this technology?
- Are competitors also being approached?

## NEGOTIATION STRATEGY

### Our BATNA (Best Alternative To Negotiated Agreement)
- License to their competitor
- Develop product ourselves
- Sell patent outright
- Our walk-away point

### Their BATNA
- Develop in-house
- License alternative technology
- Acquire different patent
- Their walk-away point

### Power Dynamics
Who has more leverage and why?

## OPENING POSITION

### Financial Terms (First Offer)
- Upfront: $X
- Royalty: Y%
- Minimum annual: $Z
- Milestones: [List]

### Non-Financial Terms (First Offer)
- Exclusivity scope
- Term length
- Geographic rights
- Field-of-use limits

### Rationale for Each Term
[Why we're asking for this]

## CONCESSION STRATEGY

### Tier 1 Concessions (Small giveaways)
- Extend payment terms
- Reduce audit frequency
- Simplify reporting

### Tier 2 Concessions (Moderate giveaways)
- Lower minimum annual royalty 10-20%
- Extend exclusivity period
- Broaden field-of-use slightly

### Tier 3 Concessions (Major giveaways)
- Reduce royalty rate 0.5-1%
- Lower upfront payment 20-30%
- Remove milestone payments

**Rule:** Never give Tier 2-3 concessions without getting something in return

## NEGOTIATION TACTICS

### Building Rapport
- Find common ground
- Understand their business challenges
- Position as partnership, not transaction

### Handling Objections
- "Your royalty rate is too high"
  Response: [Justify with comparables and value creation]
  
- "We can't afford upfront payment"
  Response: [Propose payment plan or increase royalty]
  
- "We need broader exclusivity"
  Response: [Link to development commitments]

### Creating Urgency
- Other interested parties (if true)
- Limited licensing window
- Market opportunity timing

## MEETING STRUCTURE

### Meeting 1: Introduction
- Agenda: [30-min format]
- Objectives: Build rapport, assess interest
- Materials: One-pager, demo video

### Meeting 2: Deep Dive
- Agenda: [60-min format]
- Objectives: Technical Q&A, business case
- Materials: Full patent disclosure, test data

### Meeting 3: Terms Discussion
- Agenda: [90-min format]
- Objectives: Present term sheet, negotiate
- Materials: Draft license agreement

### Meeting 4: Final Negotiations
[etc.]

## RED FLAGS TO WATCH FOR

- Excessive due diligence delays (stalling)
- Requests for exclusive option without payment
- Pressure to disclose trade secrets early
- Unreasonable demands suggesting bad faith

## CLOSING STRATEGY

### Deal Momentum
How to keep negotiations moving forward

### Term Sheet Finalization
Key terms to lock in first

### Legal Documentation
Attorney review process

### Signature Authority
Who signs for both parties?

## POST-SIGNATURE

- Announcement strategy
- Relationship management
- Performance monitoring
- Renewal planning

Generate comprehensive negotiation playbook.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=4000
        )
        return completion.choices[0].message.content
    
    def term_sheet_generator(self, deal_summary):
        """Generate licensing term sheet"""
        prompt = f"""
Generate licensing term sheet for:

DEAL SUMMARY:
{deal_summary}

Create formal term sheet:

---

# LICENSE AGREEMENT TERM SHEET

**Date:** [DATE]

**Licensor:** ResonanceEnergy Inc.  
**Licensee:** [COMPANY NAME]  
**Technology:** [PATENT TITLE/NUMBER]

## 1. GRANT OF LICENSE

**Type:** Exclusive / Non-Exclusive / Semi-Exclusive  
**Field of Use:** [Specific applications]  
**Territory:** [Geographic scope]  
**Term:** [Years] from Effective Date

## 2. FINANCIAL TERMS

### 2.1 Upfront Payment
- Amount: $[X]
- Due: Within [days] of execution
- Non-refundable

### 2.2 Royalty
- Rate: [X]% of Net Sales
- Definition of Net Sales: Gross revenue less [exclusions]
- Reporting: Quarterly
- Payment: Within 30 days of quarter end

### 2.3 Minimum Annual Royalty
- Year 1: $[X]
- Year 2: $[Y]
- Year 3: $[Z]
- [If minimum not met, license may convert to non-exclusive]

### 2.4 Milestone Payments
- First Commercial Sale: $[X]
- $1M in Cumulative Sales: $[Y]
- $5M in Cumulative Sales: $[Z]

## 3. DILIGENCE OBLIGATIONS

- Licensee shall use commercially reasonable efforts to develop Products
- First commercial sale within [18] months or [penalty]
- Minimum annual sales targets: [If applicable]

## 4. EXCLUSIVITY TERMS

- Exclusive rights in [Territory/Field]
- Sublicensing permitted: Yes/No
- If sublicensing: [X]% of sublicense revenue to Licensor
- MFN clause: [Most favored nation terms if applicable]

## 5. PATENT PROSECUTION & MAINTENANCE

- Licensor maintains patent
- Licensee reimburses [X]% of maintenance fees
- Licensee has right to review prosecution

## 6. IMPROVEMENTS

- Licensor improvements: Licensed under this agreement
- Licensee improvements: [Cross-licensed / Not shared / Shared with royalty]

## 7. QUALITY CONTROL

- Licensee products must meet quality standards
- Licensor has approval rights on [marketing materials / product designs]
- Proper patent marking required

## 8. AUDIT RIGHTS

- Licensor may audit books annually
- [30] days notice required
- If underpayment > [5]%, Licensee pays audit costs

## 9. INTELLECTUAL PROPERTY

- Licensor retains all patent rights
- Licensee may not challenge patent validity
- Infringement: [Who handles, cost allocation]

## 10. CONFIDENTIALITY

- 5-year confidentiality obligation
- Exceptions: [Standard exclusions]

## 11. WARRANTIES & LIABILITY

- Licensor warranties: [Limited to patent ownership]
- No warranty of merchantability or fitness
- Liability cap: [Amount paid under agreement]

## 12. TERMINATION

- Term: [Years] with auto-renewal unless terminated
- Early termination by Licensee: [90] days notice
- Termination for cause: Material breach, [30] days to cure
- Effect of termination: [Wind-down period, inventory sell-off]

## 13. GOVERNING LAW

- State: [Alberta / Delaware]
- Dispute resolution: Binding arbitration

## 14. MISCELLANEOUS

- Assignment: Not permitted without consent
- Entire agreement
- Amendments in writing
- Counterparts permitted

---

**AGREED:**

**LICENSOR:**  
Signature: _______________  
Name: [NAME]  
Title: [TITLE]  
Date: _______________

**LICENSEE:**  
Signature: _______________  
Name: [NAME]  
Title: [TITLE]  
Date: _______________

---

Generate complete term sheet with all key provisions.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=4000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"🤝 LICENSING STRATEGIST")
    print(f"{'='*70}\n")
    
    agent = LicensingStrategist()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "targets":
            if len(sys.argv) > 2:
                tech = " ".join(sys.argv[2:])
                print(f"TARGET LICENSEES FOR: {tech}\n")
                print(agent.target_licensees(tech))
            else:
                print("❌ Usage: python licensing_strategist.py targets '<technology>'")
                print("Example: python licensing_strategist.py targets 'φ-turbine technology'")
        
        elif command == "deal":
            if len(sys.argv) > 2:
                profile = " ".join(sys.argv[2:])
                print("DEAL STRUCTURE OPTIONS\n")
                print(agent.deal_structure(profile))
            else:
                print("❌ Usage: python licensing_strategist.py deal '<licensee profile>'")
        
        elif command == "negotiate":
            if len(sys.argv) > 2:
                company = " ".join(sys.argv[2:])
                print(f"NEGOTIATION PLAYBOOK: {company}\n")
                print(agent.negotiation_playbook(company))
            else:
                print("❌ Usage: python licensing_strategist.py negotiate '<company name>'")
        
        elif command == "termsheet":
            if len(sys.argv) > 2:
                deal = " ".join(sys.argv[2:])
                print("LICENSE TERM SHEET\n")
                print(agent.term_sheet_generator(deal))
            else:
                print("❌ Usage: python licensing_strategist.py termsheet '<deal summary>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  targets '<tech>'         - Identify target licensees")
            print("  deal '<profile>'         - Design deal structure")
            print("  negotiate '<company>'    - Negotiation playbook")
            print("  termsheet '<deal>'       - Generate term sheet")
    else:
        print("Available commands:")
        print("  targets '<tech>'         - Identify target licensees")
        print("  deal '<profile>'         - Design deal structure")
        print("  negotiate '<company>'    - Negotiation playbook")
        print("  termsheet '<deal>'       - Generate term sheet")
        print("\nExample:")
        print('  python licensing_strategist.py targets "micro-hydro turbine efficiency technology"')
