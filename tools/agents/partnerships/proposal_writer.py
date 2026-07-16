"""
Proposal Writer - Generate partnership proposals and agreements
Division: Partnerships
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv(dotenv_path='../.env')

class ProposalWriter:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Proposal Writer initialized (Groq - FREE)")
    
    def write_proposal(self, partner_name, partnership_type=""):
        """Generate comprehensive partnership proposal"""
        prompt = f"""
Write partnership proposal for: {partner_name}
Partnership type: {partnership_type if partnership_type else "Strategic technology partnership"}

## PROPOSAL STRUCTURE

### EXECUTIVE SUMMARY (1 page)
- Partnership opportunity overview
- Key benefits for both parties
- Expected outcomes
- Investment required (if any)
- Timeline

### ABOUT RESONANCEENERGY (1 page)

**Company Overview:**
- Founded: 2024
- Focus: Advanced micro-hydro technology
- Innovation: φ-optimized turbine design based on biomimetic principles
- Stage: Pre-revenue, patent filing phase

**Technology:**
- 21-blade Fibonacci turbine with golden angle spacing
- 6-12% efficiency improvement over conventional designs
- Resonant water revitalization integration
- Patent portfolio valued $20M-63M

**Market Opportunity:**
- $2.8B global micro-hydro market
- 7% annual growth rate
- Growing distributed generation demand
- Rural electrification opportunities

**Team:**
- Solo founder with deep expertise
- Virtual team of 20+ AI agents (unique competitive advantage)
- Advisory network in clean energy sector

### PARTNERSHIP OPPORTUNITY (2-3 pages)

**Vision:**
What we can achieve together

**Strategic Rationale:**
Why this partnership makes sense now
- Market timing
- Complementary capabilities
- Shared values/mission
- Competitive advantages

**Partnership Structure:**
Type of collaboration:
- **Technology Licensing:** License our patents for royalty
- **Joint Development:** Co-develop products, share IP
- **Distribution Agreement:** They sell our technology
- **OEM Partnership:** Integrate into their products
- **Joint Venture:** Create new entity together
- **Strategic Investment:** They invest + provide expertise

**Roles & Responsibilities:**

ResonanceEnergy provides:
- Patented technology and IP
- R&D and innovation
- Technical support
- Marketing collateral

Partner provides:
- [Manufacturing / Distribution / Funding / Market access]
- [Sales channels / Customer relationships]
- [Regulatory expertise / Certifications]

### BUSINESS MODEL (1-2 pages)

**Revenue Model:**
How we both make money

**Pricing Structure:**
- Product pricing
- Royalty rates (if applicable)
- Revenue sharing (if applicable)
- Milestone payments

**Financial Projections:**
Year 1-3 revenue forecasts for the partnership

**Investment Required:**
- From us: $X
- From partner: $Y
- Total: $Z

### IMPLEMENTATION PLAN (1-2 pages)

**Phase 1 (Months 1-3): Foundation**
- Legal agreements finalized
- Technical integration planning
- Team alignment
- KPI definition

**Phase 2 (Months 4-6): Development**
- Product development
- Testing and validation
- Regulatory approvals
- Go-to-market planning

**Phase 3 (Months 7-12): Launch**
- Market launch
- Sales ramp-up
- Customer support
- Iteration based on feedback

**Timeline:**
| Quarter | Milestones | Deliverables |
|---------|-----------|--------------|
| Q1 | Foundation | Signed agreement, project plan |
| Q2 | Development | Working prototype |
| Q3 | Testing | Validated product |
| Q4 | Launch | Commercial sales |

### SUCCESS METRICS (1 page)

**Key Performance Indicators:**
- Revenue targets
- Market share
- Customer acquisition
- Product performance
- Partnership satisfaction

**Year 1 Targets:**
- $X revenue
- Y customers
- Z products deployed

**3-Year Vision:**
- $A revenue
- B% market share
- C geographic markets

### RISK MITIGATION (1 page)

**Potential Risks:**
- Technical challenges
- Market adoption
- Competitive response
- Regulatory changes
- Partnership conflicts

**Mitigation Strategies:**
For each risk, how we'll address it

### TERMS & CONDITIONS (1-2 pages)

**Partnership Terms:**
- Duration: X years
- Exclusivity: [Geographic / Product / None]
- Termination conditions
- IP ownership
- Confidentiality
- Dispute resolution

**Governance:**
- Decision-making structure
- Quarterly business reviews
- Communication protocols

### NEXT STEPS (1 page)

**Immediate Actions:**
1. Review proposal (Target: 2 weeks)
2. Schedule alignment meeting
3. Conduct due diligence
4. Draft term sheet
5. Negotiate final terms
6. Execute agreements

**Timeline to Signature:**
Target: 60-90 days from proposal

**Contact Information:**
[Your contact details]

### APPENDICES

**Appendix A:** Technical specifications
**Appendix B:** Patent summaries
**Appendix C:** Market research
**Appendix D:** Financial models
**Appendix E:** References/testimonials

Generate comprehensive proposal (10-15 pages) tailored to partner.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=4000
        )
        return completion.choices[0].message.content
    
    def term_sheet(self, deal_summary):
        """Generate partnership term sheet"""
        prompt = f"""
Generate partnership term sheet.

**DEAL SUMMARY:**
{deal_summary}

---

# PARTNERSHIP TERM SHEET

**Date:** {datetime.now().strftime('%B %d, %Y')}

**Party A:** ResonanceEnergy Inc.  
**Party B:** [PARTNER NAME]  
**Partnership Type:** [Technology/Distribution/JV/etc.]

## 1. PARTNERSHIP STRUCTURE

**Type:** [Specify structure]  
**Objective:** [Clear statement of partnership goals]  
**Term:** [X] years from Effective Date, with [renewal terms]

## 2. SCOPE OF COLLABORATION

**Products/Services Covered:**
[List specific products or technology]

**Geographic Territory:**
[Specific markets or worldwide]

**Exclusivity:**
[Exclusive/Non-exclusive/Semi-exclusive in certain territories]

## 3. FINANCIAL TERMS

### 3.1 Revenue Sharing (if applicable)
- ResonanceEnergy: [X]%
- Partner: [Y]%
- Based on: [Net revenue / Gross revenue]

### 3.2 Royalty Payments (if applicable)
- Royalty Rate: [Z]% of [net sales / licensed products]
- Minimum Annual Royalty: $[amount]
- Payment Terms: [Quarterly / Monthly]

### 3.3 Upfront Payments (if applicable)
- Signing Fee: $[amount]
- Development Milestones: $[amounts]
- Due: [payment schedule]

### 3.4 Profit Sharing (if JV)
- Profit split: [ratio]
- Distribution: [quarterly/annually]

## 4. INVESTMENT & FUNDING

**Total Investment Required:** $[amount]

**ResonanceEnergy Contribution:**
- Cash: $[amount]
- IP/Technology: Valued at $[amount]
- Time/Resources: [description]

**Partner Contribution:**
- Cash: $[amount]
- Manufacturing: [capacity/capability]
- Distribution: [channels/customers]
- Other: [specify]

## 5. INTELLECTUAL PROPERTY

**Existing IP:**
- ResonanceEnergy retains ownership of all existing patents
- Partner granted [exclusive/non-exclusive] license

**New IP ("Joint IP"):**
- Jointly developed IP owned [50/50 / other ratio]
- Both parties can use for partnership purposes
- External licensing requires mutual consent

**Improvements:**
- Each party owns improvements to their own IP
- Cross-license improvements for partnership use

## 6. ROLES & RESPONSIBILITIES

### ResonanceEnergy Responsibilities:
- Technology development and R&D
- Patent prosecution and maintenance
- Technical support and training
- Marketing collateral development

### Partner Responsibilities:
- [Manufacturing / Distribution / Sales]
- Customer support (if distribution)
- Quality control and compliance
- Market feedback and insights

## 7. GOVERNANCE

**Management Structure:**
- Joint Steering Committee (2 reps from each party)
- Quarterly business reviews
- Annual strategic planning

**Decision Making:**
- Routine decisions: Managed independently
- Major decisions: Require unanimous consent
  - Major: New products, significant investments, IP licensing

## 8. MILESTONES & DELIVERABLES

**Quarter 1:**
- [Specific deliverables]
- [Success metrics]

**Quarter 2:**
- [Specific deliverables]
- [Success metrics]

[etc.]

## 9. PERFORMANCE METRICS

**Key Metrics:**
- Revenue: $[target] by [date]
- Customers: [number] by [date]
- Market share: [%] by [date]
- Product performance: [specifications]

**Performance Reviews:**
Quarterly review against targets, corrective actions if needed

## 10. CONFIDENTIALITY

- 5-year confidentiality obligation
- Standard exclusions (public domain, independently developed)
- Survival after termination

## 11. EXCLUSIVITY TERMS (if applicable)

**Exclusive Period:** [X] years in [territory/product]

**Exclusivity Conditions:**
- Minimum performance requirements: $[revenue] annually
- If not met, converts to non-exclusive

**Right of First Refusal:**
Partner has [30/60/90] days to match competitive offers

## 12. TERMINATION

**Term:** [X] years

**Early Termination:**
- By mutual agreement: [notice period]
- For cause (material breach): [cure period], then termination
- For convenience: [notice period], [wind-down provisions]

**Effect of Termination:**
- IP licenses survive for [period] / terminate immediately
- Inventory sell-off: [months] period
- Confidentiality survives
- Revenue sharing on existing contracts continues

## 13. WARRANTIES & LIABILITY

**Warranties:**
- Each party warrants authority to enter agreement
- ResonanceEnergy warrants ownership of IP
- Partner warrants [manufacturing/distribution] capability

**Liability:**
- Each party liable for own negligence
- Liability cap: [$ amount or insurance limits]
- Indemnification for IP infringement claims

## 14. MISCELLANEOUS

**Governing Law:** [State/Province]  
**Dispute Resolution:** Binding arbitration  
**Assignment:** Not permitted without consent  
**Entire Agreement:** Supersedes all prior discussions  
**Amendments:** Must be in writing, signed by both parties

## 15. CONDITIONS PRECEDENT

- Due diligence completion
- Board approvals
- Legal review
- [Other conditions]

## 16. NEXT STEPS

1. Review term sheet (2 weeks)
2. Conduct due diligence (4 weeks)
3. Negotiate definitive agreements (4 weeks)
4. Execute partnership agreement (1 week)

**Target Closing Date:** [DATE]

---

**AGREED:**

**RESONANCEENERGY INC.**

Signature: _______________  
Name: [NAME]  
Title: Founder & CEO  
Date: _______________

**[PARTNER NAME]**

Signature: _______________  
Name: [NAME]  
Title: [TITLE]  
Date: _______________

---

Generate complete term sheet with specific terms for this partnership.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def onepager(self, opportunity_type):
        """Generate one-page partnership opportunity brief"""
        prompt = f"""
Create one-page partnership brief for: {opportunity_type}

## ONE-PAGER FORMAT (Single Page)

### HEADER
**ResonanceEnergy Partnership Opportunity**  
{opportunity_type}

### THE OPPORTUNITY (3 sentences)
Compelling summary of partnership value

### WHY NOW? (3 bullets)
- Market timing
- Technology readiness
- Competitive advantage

### WHAT WE OFFER (5 bullets)
- Patented φ-turbine technology (6-12% efficiency gain)
- $20M-63M patent portfolio
- Biomimetic design principles (Dan Winter/Schauberger)
- Proven test results
- Fast-to-market ready

### WHAT WE NEED (3 bullets)
- [Manufacturing capacity]
- [Distribution channels]
- [Strategic expertise]

### PARTNERSHIP MODELS (3 options)
1. **[Model 1]:** [Brief description, revenue split]
2. **[Model 2]:** [Brief description, terms]
3. **[Model 3]:** [Brief description, investment]

### SUCCESS METRICS (Year 1)
- Revenue: $[X]
- Customers: [Y]
- Market: [Z locations/regions]

### FINANCIAL SNAPSHOT
| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Revenue | $[X] | $[Y] | $[Z] |
| Units | [A] | [B] | [C] |

### NEXT STEPS
1. [15-min intro call]
2. [Detailed proposal]
3. [Due diligence]
4. [Agreement in 60-90 days]

### CONTACT
[Your name, email, phone]

**Format:** Professional, visually clean, printable on single page

Generate compelling one-pager optimized for executive review (2-minute read).
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def jv_agreement(self, venture_details):
        """Draft joint venture agreement outline"""
        prompt = f"""
Draft joint venture agreement outline.

**VENTURE DETAILS:**
{venture_details}

# JOINT VENTURE AGREEMENT OUTLINE

## 1. FORMATION & PURPOSE
- Legal entity creation (LLC, Partnership, etc.)
- Name of joint venture
- Purpose and scope
- Principal place of business

## 2. PARTIES & CONTRIBUTIONS

**ResonanceEnergy Contribution:**
- Technology and IP (fair market value)
- Development expertise
- Patents and trade secrets
- Time commitment

**Partner Contribution:**
- Capital: $[amount]
- Manufacturing facilities
- Distribution networks
- Market expertise

**Total Capitalization:** $[amount]

## 3. OWNERSHIP & EQUITY

**Ownership Split:**
- ResonanceEnergy: [X]%
- Partner: [Y]%

**Basis for Split:**
Reflects contributed value + sweat equity

**Vesting Schedule:**
- Immediate: [%]
- Vesting: [%] over [period]

## 4. GOVERNANCE

**Management Structure:**
- Board of Directors: [# seats each party]
- Officers: CEO, CFO, CTO (appointed by board)
- Decision-making: [Supermajority / Unanimous for major decisions]

**Major Decisions Requiring Unanimous Consent:**
- Annual budget >$[threshold]
- Hiring executives
- Taking on debt
- Selling company/assets
- Entering new markets
- Changing business model

## 5. CAPITAL & FINANCING

**Initial Capital:** $[amount]

**Additional Capital Calls:**
- Pro-rata participation rights
- If party doesn't participate: Dilution

**Profit Distribution:**
- Distributions: [Quarterly/Annually]
- Pro-rata based on ownership

## 6. INTELLECTUAL PROPERTY

**Pre-Existing IP:**
- Each party retains ownership
- Licensed to JV for venture purposes

**Joint Venture IP:**
- Owned by JV entity
- Parties have rights upon JV dissolution

**IP Development:**
- Developed IP belongs to JV
- Each party has license-back rights

## 7. OPERATIONS

**Day-to-Day Management:**
- CEO responsible for operations
- Monthly reports to board
- Annual business plan approval

**Financial Management:**
- Separate bank accounts
- Annual audited financials
- Quarterly reporting

## 8. TERM & TERMINATION

**Term:** [X] years, with renewal options

**Early Termination:**
- Mutual agreement
- Material breach (cure period)
- Bankruptcy/insolvency
- Failure to meet performance targets

## 9. EXIT & DISSOLUTION

**Exit Options:**
- Right of first refusal (before selling to third party)
- Drag-along rights (if 75% vote to sell)
- Tag-along rights (minority protection)

**Buy-Sell Provisions:**
- Shotgun clause (offer price, other party buy or sell)
- Valuation: [Method - multiple of revenue, appraisal, etc.]

**Dissolution:**
- Liquidation preferences
- Asset distribution
- IP rights reversion

## 10. DISPUTE RESOLUTION

**Process:**
1. Good faith negotiation (30 days)
2. Mediation (30 days)
3. Binding arbitration

**Governing Law:** [State/Province]

## 11. NON-COMPETE & NON-SOLICIT

**During Term:**
- Parties may not compete in venture's market
- May not solicit venture's employees/customers

**Post-Termination:**
- [X]-year non-compete
- [Y]-year non-solicit

## 12. REPRESENTATIONS & WARRANTIES

Each party represents:
- Authority to enter agreement
- Ownership of contributed assets
- No conflicts with other agreements
- Financial disclosures accurate

## 13. INSURANCE & INDEMNIFICATION

**Insurance Requirements:**
- General liability: $[amount]
- Professional liability: $[amount]
- Directors & officers: $[amount]

**Indemnification:**
Each party indemnifies for:
- Breaches of representations
- Negligence or misconduct
- IP infringement claims

## 14. DEADLOCK RESOLUTION

If board deadlocks:
1. CEO casting vote (operational matters)
2. Mediation (strategic matters)
3. Buy-sell mechanism (if unresolved)

## 15. CONFIDENTIALITY

- All venture information confidential
- Survives termination ([X] years)
- Standard exclusions

---

Generate complete JV agreement outline (customized for this venture).
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3500
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"📄 PROPOSAL WRITER")
    print(f"{'='*70}\n")
    
    agent = ProposalWriter()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "proposal":
            if len(sys.argv) > 2:
                partner = " ".join(sys.argv[2:])
                print(f"WRITING PROPOSAL FOR: {partner}\n")
                print(agent.write_proposal(partner))
            else:
                print("❌ Usage: python proposal_writer.py proposal '<partner name>'")
        
        elif command == "termsheet":
            if len(sys.argv) > 2:
                deal = " ".join(sys.argv[2:])
                print("GENERATING TERM SHEET\n")
                print(agent.term_sheet(deal))
            else:
                print("❌ Usage: python proposal_writer.py termsheet '<deal summary>'")
        
        elif command == "onepager":
            opp = sys.argv[2] if len(sys.argv) > 2 else "Technology Partnership"
            print(f"ONE-PAGER: {opp}\n")
            print(agent.onepager(opp))
        
        elif command == "jv":
            if len(sys.argv) > 2:
                venture = " ".join(sys.argv[2:])
                print("JOINT VENTURE AGREEMENT\n")
                print(agent.jv_agreement(venture))
            else:
                print("❌ Usage: python proposal_writer.py jv '<venture details>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  proposal '<partner>'     - Full partnership proposal")
            print("  termsheet '<deal>'       - Partnership term sheet")
            print("  onepager '<type>'        - One-page opportunity brief")
            print("  jv '<details>'           - Joint venture agreement")
    else:
        print("Available commands:")
        print("  proposal '<partner>'     - Full partnership proposal")
        print("  termsheet '<deal>'       - Partnership term sheet")
        print("  onepager '<type>'        - One-page opportunity brief")
        print("  jv '<details>'           - Joint venture agreement")
        print("\nQuick start:")
        print('  python proposal_writer.py proposal "Voith Hydro"')
        print('  python proposal_writer.py onepager "Distribution Partnership"')
