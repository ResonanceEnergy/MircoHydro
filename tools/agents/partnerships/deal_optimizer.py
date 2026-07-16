"""
Deal Optimizer - Structure optimal partnership deals
Division: Partnerships
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path='../.env')

class DealOptimizer:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Deal Optimizer initialized (Groq - FREE)")
    
    def optimize_structure(self, deal_description):
        """Analyze and optimize deal structure"""
        prompt = f"""
Optimize partnership deal structure.

**DEAL OVERVIEW:**
{deal_description}

## DEAL STRUCTURE ANALYSIS

### Current Proposed Structure
[Summarize what's currently on the table]

### Alternative Structures

#### Option A: Technology License
**Structure:**
- ResonanceEnergy licenses φ-turbine patents
- Partner manufactures and sells
- Royalty-based revenue

**Terms:**
- Upfront: $[X]
- Royalty: [Y]% of net sales
- Minimum annual: $[Z]
- Exclusivity: [Geographic/Product]

**Pros:**
- Simple structure
- Predictable revenue stream
- Low capital requirement
- Fast to implement

**Cons:**
- Limited control over execution
- Revenue tied to partner performance
- Potential conflicts of interest

**Risk Level:** Low
**Potential Value:** $[X-Y] over 5 years

#### Option B: Joint Development
**Structure:**
- Co-develop products together
- Share costs and profits
- Joint IP ownership

**Terms:**
- Each invests: $[X]
- Profit split: [50/50 or other]
- IP: Jointly owned
- Management: Joint steering committee

**Pros:**
- Shared risk
- Combined capabilities
- Faster time to market
- Strategic alignment

**Cons:**
- More complex
- Requires consensus
- Potential conflicts
- Slower decisions

**Risk Level:** Medium
**Potential Value:** $[X-Y] over 5 years

#### Option C: Distribution Partnership
**Structure:**
- Partner distributes our products
- We maintain control
- Revenue sharing or wholesale pricing

**Terms:**
- Wholesale price: [% off MSRP]
- OR: Revenue share [split]
- Minimum volumes
- Geographic exclusivity

**Pros:**
- Maintain control
- Access to distribution
- Flexible terms
- Scalable

**Cons:**
- Need manufacturing capacity
- Working capital requirements
- Lower margins
- Channel conflicts

**Risk Level:** Medium
**Potential Value:** $[X-Y] over 5 years

#### Option D: Joint Venture
**Structure:**
- Create new legal entity
- Combined investment
- Shared ownership and control

**Terms:**
- Ownership: [X]% us, [Y]% them
- Capital: $[Z] total
- Board: [# seats each]
- Exit: [Terms]

**Pros:**
- Fully aligned incentives
- Dedicated focus
- Clear governance
- Exit options

**Cons:**
- Most complex
- Highest commitment
- Hardest to unwind
- Regulatory complexity

**Risk Level:** High
**Potential Value:** $[X-Y] over 5 years

### OPTIMAL STRUCTURE RECOMMENDATION

**Recommended:** [Option X]

**Rationale:**
1. [Why this structure fits best]
2. [Risk/reward alignment]
3. [Execution feasibility]
4. [Strategic goals alignment]

**Deal Terms:**
[Specific recommended terms]

**Negotiation Strategy:**
- Opening position: [Terms]
- Target outcome: [Terms]
- Walk-away point: [Terms]

Generate optimized deal structure with recommendation.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def valuation_analysis(self, contribution_details):
        """Value each party's contributions"""
        prompt = f"""
Analyze contribution valuations for partnership.

**CONTRIBUTIONS:**
{contribution_details}

## VALUATION ANALYSIS

### ResonanceEnergy Contributions

**Intellectual Property:**
- φ-Turbine patents: $[8-25M] (based on IP valuation)
- Trade secrets and know-how: $[X]
- Patent applications pending: $[Y]
- **Total IP Value:** $[Z]

**Technology & Expertise:**
- R&D investment to date: $[X]
- Proprietary test data: $[Y]
- Technical expertise (hourly rate × hours): $[Z]
- **Total Technology Value:** $[A]

**Market Opportunity:**
- Identified customer leads: $[X] potential value
- Brand/reputation: $[Y]
- Go-to-market strategy: $[Z]
- **Total Market Value:** $[B]

**Time & Effort:**
- Founder time commitment: [X] hours/month @ $[rate] = $[Y]/year
- Ongoing R&D and support: $[Z]/year
- **Annual Value:** $[A]/year

**TOTAL RESONANCEENERGY VALUE:** $[SUM]

### Partner Contributions

**Financial:**
- Cash investment: $[X]
- Credit/financing: $[Y]
- **Total Financial:** $[Z]

**Manufacturing:**
- Production capacity: [X] units/year
- Equipment and facilities: $[Y] value
- Quality systems and certifications: $[Z]
- **Total Manufacturing Value:** $[A]

**Distribution:**
- Sales channels: [X] customers reachable
- Customer relationships: $[Y] lifetime value
- Brand reputation: $[Z]
- **Total Distribution Value:** $[B]

**Expertise:**
- Industry knowledge and relationships
- Regulatory/compliance capability
- Operations and logistics
- **Total Expertise Value:** $[C]

**TOTAL PARTNER VALUE:** $[SUM]

### VALUATION COMPARISON

| Contribution | ResonanceEnergy | Partner | Total |
|--------------|-----------------|---------|-------|
| Cash | $[X] | $[Y] | $[Z] |
| IP/Technology | $[X] | $[Y] | $[Z] |
| Manufacturing | $[X] | $[Y] | $[Z] |
| Distribution | $[X] | $[Y] | $[Z] |
| Expertise | $[X] | $[Y] | $[Z] |
| **TOTAL** | **$[X]** | **$[Y]** | **$[Z]** |

### FAIR EQUITY SPLIT

**Based on Contributed Value:**
- ResonanceEnergy: [X]%
- Partner: [Y]%

**Adjusted for Risk/Effort:**
- ResonanceEnergy vesting: [Consider sweat equity]
- Partner vesting: [Immediate if cash, vesting if services]

**Final Recommendation:**
- ResonanceEnergy: [X]%
- Partner: [Y]%

**Rationale:**
[Explain the reasoning]

Generate comprehensive valuation analysis with fair equity split.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def deal_comparison(self, deals_list):
        """Compare multiple deal options side-by-side"""
        prompt = f"""
Compare deal options:

{deals_list}

## DEAL COMPARISON MATRIX

### Financial Comparison

| Metric | Deal A | Deal B | Deal C |
|--------|--------|--------|--------|
| Upfront Payment | $[X] | $[Y] | $[Z] |
| Year 1 Revenue | $[X] | $[Y] | $[Z] |
| Year 3 Revenue | $[X] | $[Y] | $[Z] |
| Year 5 Total | $[X] | $[Y] | $[Z] |
| NPV (15% discount) | $[X] | $[Y] | $[Z] |
| Payback Period | [X] months | [Y] months | [Z] months |

### Strategic Comparison

| Factor | Deal A | Deal B | Deal C |
|--------|--------|--------|--------|
| Market Access | [Rating] | [Rating] | [Rating] |
| Control Level | [High/Med/Low] | [High/Med/Low] | [High/Med/Low] |
| Speed to Market | [X] months | [Y] months | [Z] months |
| Scalability | [Rating] | [Rating] | [Rating] |
| Partner Fit | [Rating] | [Rating] | [Rating] |

### Risk Comparison

| Risk Factor | Deal A | Deal B | Deal C |
|-------------|--------|--------|--------|
| Execution Risk | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] |
| Financial Risk | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] |
| Partnership Risk | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] |
| Market Risk | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] |
| Overall Risk | [Score] | [Score] | [Score] |

### Pros & Cons

**Deal A:**
✅ Pros: [List]
❌ Cons: [List]

**Deal B:**
✅ Pros: [List]
❌ Cons: [List]

**Deal C:**
✅ Pros: [List]
❌ Cons: [List]

### RECOMMENDATION

**Best Deal:** [X]

**Rationale:**
1. [Financial reasoning]
2. [Strategic reasoning]
3. [Risk reasoning]
4. [Execution reasoning]

**Second Choice:** [Y] (if Deal [X] falls through)

**Avoid:** [Z] because [reasons]

Generate comprehensive deal comparison with clear recommendation.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def negotiation_tactics(self, negotiation_context):
        """Develop negotiation strategy and tactics"""
        prompt = f"""
Develop negotiation strategy.

**CONTEXT:**
{negotiation_context}

## NEGOTIATION STRATEGY

### Power Dynamics

**Our Strengths:**
- Patented technology (they can't get elsewhere)
- Strong IP position ($20M-63M portfolio)
- Novel approach (6-12% efficiency gains)
- First-mover advantage in φ-optimization

**Their Strengths:**
- [Manufacturing capacity / Distribution / Capital / etc.]
- Established market presence
- Customer relationships
- Brand recognition

**Power Balance:** [We have leverage / Equal / They have leverage]

### BATNA Analysis

**Our BATNA (Best Alternative To Negotiated Agreement):**
- Option 1: [Partner with competitor]
- Option 2: [Self-develop and bootstrap]
- Option 3: [License to multiple non-exclusive partners]
- **Best BATNA:** [Which option]
- **Walk-Away Point:** [Minimum acceptable terms]

**Their BATNA:**
- Option 1: [Develop in-house]
- Option 2: [License competing technology]
- Option 3: [Acquire different company]
- **Their Walk-Away:** [Estimated]

### Negotiation Positioning

**Opening Position (Ambitious but defensible):**
- [Terms we start with]
- [Justification for each term]

**Target Outcome (Realistic goal):**
- [Terms we want to achieve]
- [What we're willing to give up]

**Bottom Line (Walk-away point):**
- [Minimum acceptable terms]
- [If they won't meet this, we walk]

### Concession Strategy

**Tier 1 Concessions (Low cost to us):**
- [Give: Payment schedule flexibility]
- [Give: Reporting frequency]
- [Give: Non-material terms]

**Tier 2 Concessions (Moderate cost):**
- [Give: Slightly lower royalty rate]
- [Give: Narrow exclusivity]
- [Give: Extended payment terms]

**Tier 3 Concessions (High cost - only for major wins):**
- [Give: Significant royalty reduction]
- [Give: Broad exclusivity]
- [Give: IP rights]

**Rule:** Never give Tier 2-3 without getting equivalent value in return

### Negotiation Tactics

**Building Rapport:**
- Find common ground (mission, values)
- Show genuine interest in their business
- Be collaborative, not adversarial
- Build personal relationships

**Creating Value:**
- Look for win-win solutions
- Expand the pie before dividing it
- Consider creative structures
- Think long-term relationship

**Leveraging FOMO (Fear Of Missing Out):**
- Mention other interested parties (if true)
- Create deadline pressure (not artificial)
- Highlight competitive advantage of moving fast

**Handling Difficult Tactics:**
- **If they lowball:** Anchor high, show value, be willing to walk
- **If they create urgency:** Don't rush, take time to evaluate
- **If they nibble:** Bundle changes, don't give one-off concessions
- **If they go silent:** Follow up once, then move to other opportunities

### Key Terms to Negotiate

**Priority 1 (Most Important):**
1. [Term]: Target [X], Floor [Y]
2. [Term]: Target [X], Floor [Y]
3. [Term]: Target [X], Floor [Y]

**Priority 2 (Important but flexible):**
- [Terms we can negotiate]

**Priority 3 (Nice to have):**
- [Terms we can easily concede]

### Meeting Structure

**Pre-Meeting:**
- Know their position and constraints
- Prepare justifications for all terms
- Have alternatives ready
- Role-play difficult scenarios

**Opening:**
- Set collaborative tone
- Align on objectives
- Agree on process

**Middle:**
- Discuss all terms
- Explore options
- Make conditional offers ("If you can do X, we can do Y")

**Closing:**
- Summarize agreements
- Document open items
- Set next steps and timeline

**Post-Meeting:**
- Send written summary immediately
- Confirm understanding
- Follow up on commitments

### Psychology & Influence

**Reciprocity:** Give small concessions first to create obligation
**Consistency:** Get small agreements early, build to bigger ones
**Social Proof:** Reference similar deals we've done (or industry standards)
**Authority:** Cite industry experts, test data, patents
**Scarcity:** Limited licensing opportunities, other interested parties
**Likability:** Be genuine, find commonalities, show respect

### Red Flags to Watch For

🚩 Unreasonable demands with no flexibility
🚩 Unwilling to share information (lack of transparency)
🚩 No decision-making authority (can't commit)
🚩 Constantly moving goalposts
🚩 Adversarial vs. collaborative approach

**If you see these:** Reassess if this is right partner

### Closing the Deal

**When to Close:**
- All major terms agreed
- Both sides feel fair
- Momentum is positive
- No major unresolved issues

**How to Close:**
- "I think we're aligned. Should we move to documentation?"
- Set specific timeline for agreements
- Identify who does what next
- Celebrate the partnership!

Generate comprehensive negotiation strategy with specific tactics.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=3500
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"🎯 DEAL OPTIMIZER")
    print(f"{'='*70}\n")
    
    agent = DealOptimizer()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "optimize":
            if len(sys.argv) > 2:
                deal = " ".join(sys.argv[2:])
                print("OPTIMIZING DEAL STRUCTURE\n")
                print(agent.optimize_structure(deal))
            else:
                print("❌ Usage: python deal_optimizer.py optimize '<deal description>'")
        
        elif command == "value":
            if len(sys.argv) > 2:
                contributions = " ".join(sys.argv[2:])
                print("CONTRIBUTION VALUATION\n")
                print(agent.valuation_analysis(contributions))
            else:
                print("❌ Usage: python deal_optimizer.py value '<contribution details>'")
        
        elif command == "compare":
            if len(sys.argv) > 2:
                deals = " ".join(sys.argv[2:])
                print("DEAL COMPARISON\n")
                print(agent.deal_comparison(deals))
            else:
                print("❌ Usage: python deal_optimizer.py compare '<deals list>'")
        
        elif command == "negotiate":
            if len(sys.argv) > 2:
                context = " ".join(sys.argv[2:])
                print("NEGOTIATION STRATEGY\n")
                print(agent.negotiation_tactics(context))
            else:
                print("❌ Usage: python deal_optimizer.py negotiate '<negotiation context>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  optimize '<deal>'       - Optimize deal structure")
            print("  value '<contributions>' - Value contributions")
            print("  compare '<deals>'       - Compare deal options")
            print("  negotiate '<context>'   - Negotiation strategy")
    else:
        print("Available commands:")
        print("  optimize '<deal>'       - Optimize deal structure")
        print("  value '<contributions>' - Value contributions")
        print("  compare '<deals>'       - Compare deal options")
        print("  negotiate '<context>'   - Negotiation strategy")
        print("\nQuick start:")
        print('  python deal_optimizer.py optimize "Technology license with Voith"')
        print('  python deal_optimizer.py negotiate "Discussing royalty rates"')
