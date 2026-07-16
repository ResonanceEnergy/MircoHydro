"""
IP Valuation Analyst - Assess patent value and licensing potential
Division: IP & Patent Strategy
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path='../.env')

class IPValuationAnalyst:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ IP Valuation Analyst initialized (Groq - FREE)")
    
    def value_patent(self, patent_description, market_context=""):
        """Value a specific patent"""
        prompt = f"""
You are an IP valuation expert. Assess patent value using industry-standard methods.

PATENT:
{patent_description}

MARKET CONTEXT:
{market_context if market_context else "Micro-hydro market: $2.8B globally, growing 7%/year"}

Use these valuation methods:

## COST APPROACH
- R&D costs to develop
- Testing and validation costs
- Patent filing costs
- Replacement cost

## MARKET APPROACH
- Comparable patent transactions
- Industry licensing rates (typically 1-5% of revenue)
- Similar technology valuations

## INCOME APPROACH
- Projected licensing revenue (5-10 years)
- Cost savings from efficiency improvements
- Market share capture potential
- Discount rate: 15-20% (technology risk)
- NPV calculation

## QUALITATIVE FACTORS
- Patent strength (novelty, non-obviousness)
- Claim breadth
- Design-around difficulty
- Remaining patent life
- Market adoption timeline

Generate:
## 💰 VALUATION RANGE
- Low estimate (conservative)
- Base case (most likely)
- High estimate (optimistic)

## 📊 VALUATION BREAKDOWN
[Detailed calculation with assumptions]

## 🎯 LICENSING POTENTIAL
[Annual revenue projections]

## 📈 VALUE DRIVERS
[What increases value? What are risks?]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def licensing_strategy(self, patent_name):
        """Develop licensing strategy for a patent"""
        prompt = f"""
Develop comprehensive licensing strategy for: {patent_name}

## TARGET LICENSEES
### Primary Targets (Top 10)
- Company name
- Why good fit
- Estimated annual revenue potential

### Secondary Targets
- Industry segments
- Geographic markets

## LICENSE STRUCTURE OPTIONS

### Option 1: Exclusive License
- Single licensee
- Higher royalty rate (4-8%)
- Upfront payment + ongoing royalties
- Geographic or field-of-use restrictions

### Option 2: Non-Exclusive License
- Multiple licensees
- Lower royalty rate (1-3%)
- Broader market penetration
- Lower upfront payment

### Option 3: Tiered Licensing
- Different rates for different markets
- Volume-based pricing
- Performance incentives

## DEAL TERMS

### Financial Terms
- Upfront payment: $X-Y
- Royalty rate: Z%
- Minimum annual royalties
- Milestone payments

### Non-Financial Terms
- Field-of-use restrictions
- Geographic limitations
- Sublicensing rights
- Technical support obligations
- Improvement sharing

## NEGOTIATION STRATEGY
[How to maximize value while ensuring adoption]

## LICENSING REVENUE PROJECTIONS
Year 1-5 revenue forecast with multiple scenarios

Generate comprehensive licensing strategy.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def competitive_analysis(self, technology_area):
        """Analyze competitive patent landscape"""
        prompt = f"""
Analyze competitive patent landscape for: {technology_area}

## COMPETITIVE PATENT ANALYSIS

### Major Patent Holders
List top 5-10 companies/entities with patents in this space
- Patent count
- Key technology areas
- Patent strength assessment

### Patent Clusters
Identify technology sub-areas:
- Core technologies
- Adjacent technologies
- White space opportunities

### Freedom to Operate (FTO)
- Active patents that could block commercialization
- Expired patents (public domain)
- Weak patents (potential challenges)
- Patent thickets (dense patent areas)

### STRATEGIC POSITIONING

#### Our Differentiation
- How our approach differs from existing patents
- Novel aspects
- Improvement over prior art

#### Patent Strategy Recommendations
- Where to file patents (technology gaps)
- What to patent first (highest value)
- What to keep as trade secrets
- Defensive vs. offensive strategy

### COMPETITIVE ADVANTAGES
Assess strength vs. competitors:
- Technical superiority
- Cost advantages
- Time-to-market
- Manufacturability

Generate comprehensive competitive landscape analysis.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def roi_analysis(self, patent_investment):
        """Calculate ROI on patent investment"""
        prompt = f"""
Calculate ROI for patent investment:

INVESTMENT:
{patent_investment}

## INVESTMENT BREAKDOWN
- R&D costs
- Testing/validation
- Patent filing (provisional + utility)
- Maintenance fees (years 1-20)
- Legal costs
- Total investment over 20 years

## REVENUE SCENARIOS

### Conservative (70% probability)
- Licensing revenue year 1-5
- Market adoption rate: Low
- ROI calculation

### Base Case (50% probability)
- Licensing revenue year 1-5
- Market adoption rate: Medium
- ROI calculation

### Optimistic (30% probability)
- Licensing revenue year 1-5
- Market adoption rate: High
- ROI calculation

## RISK-ADJUSTED RETURNS
Expected value = Σ(Scenario value × Probability)

## SENSITIVITY ANALYSIS
How ROI changes with:
- Royalty rate (±1%)
- Market adoption (±20%)
- Development cost (±30%)
- Patent maintenance (±$10k)

## DECISION METRICS
- NPV (Net Present Value)
- IRR (Internal Rate of Return)
- Payback period
- Risk-adjusted ROI

## RECOMMENDATION
[Should we invest? Why/why not?]

Generate comprehensive ROI analysis with clear recommendation.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"💰 IP VALUATION ANALYST")
    print(f"{'='*70}\n")
    
    agent = IPValuationAnalyst()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "value":
            if len(sys.argv) > 2:
                patent = " ".join(sys.argv[2:])
                print(f"VALUING PATENT: {patent}\n")
                print(agent.value_patent(patent))
            else:
                print("❌ Usage: python ip_valuator.py value '<patent description>'")
                print("Example: python ip_valuator.py value '21-blade Fibonacci turbine'")
        
        elif command == "licensing":
            if len(sys.argv) > 2:
                patent = " ".join(sys.argv[2:])
                print(f"LICENSING STRATEGY FOR: {patent}\n")
                print(agent.licensing_strategy(patent))
            else:
                print("❌ Usage: python ip_valuator.py licensing '<patent name>'")
        
        elif command == "competitive":
            if len(sys.argv) > 2:
                tech = " ".join(sys.argv[2:])
                print(f"COMPETITIVE ANALYSIS: {tech}\n")
                print(agent.competitive_analysis(tech))
            else:
                print("❌ Usage: python ip_valuator.py competitive '<technology area>'")
        
        elif command == "roi":
            if len(sys.argv) > 2:
                investment = " ".join(sys.argv[2:])
                print("ROI ANALYSIS\n")
                print(agent.roi_analysis(investment))
            else:
                print("❌ Usage: python ip_valuator.py roi '<patent investment description>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  value '<patent>'         - Value specific patent")
            print("  licensing '<patent>'     - Licensing strategy")
            print("  competitive '<tech>'     - Competitive landscape")
            print("  roi '<investment>'       - ROI analysis")
    else:
        print("Available commands:")
        print("  value '<patent>'         - Value specific patent")
        print("  licensing '<patent>'     - Licensing strategy")
        print("  competitive '<tech>'     - Competitive landscape")
        print("  roi '<investment>'       - ROI analysis")
        print("\nExample:")
        print('  python ip_valuator.py value "φ-optimized turbine with 6-12% efficiency gain"')
