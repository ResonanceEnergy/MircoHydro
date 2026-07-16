"""
International Patent Filer - PCT and foreign filing strategy
Division: IP & Patent Strategy
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime, timedelta

load_dotenv(dotenv_path='../.env')

class InternationalPatentFiler:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ International Patent Filer initialized (Groq - FREE)")
    
    def pct_strategy(self, patent_description):
        """Generate PCT (Patent Cooperation Treaty) filing strategy"""
        prompt = f"""
You are an international patent strategist. Design PCT filing strategy.

PATENT:
{patent_description}

## PCT OVERVIEW

### What is PCT?
- File ONE international application
- Delays national phase entry by 30-31 months
- Get international search report (ISR)
- Extends decision timeline while preserving rights

### Timeline
- Month 0: US provisional filing
- Month 12: PCT filing (before provisional expires)
- Month 30-31: National phase entry (select countries)

### Costs
- PCT filing: ~$4,000 (international filing + search)
- National phase (per country): $3,000-$10,000
- Annuities (per country): $500-$2,000/year

## PCT STRATEGY RECOMMENDATION

### Should We File PCT?

#### YES if:
- Target multiple countries (3+)
- Need time to assess market potential
- Want international search feedback
- Cost savings vs. direct filing

#### NO if:
- Only targeting 1-2 countries
- Need immediate protection abroad
- Very cost-constrained

**Recommendation for this patent:** [YES/NO with reasoning]

## PCT FILING CHECKLIST

### Month 0-11 (Before US Provisional Expires)
- [ ] Finalize US provisional application
- [ ] Assess international market potential
- [ ] Budget for PCT filing (~$4k)
- [ ] Engage PCT filing agent

### Month 12 (Critical Deadline)
- [ ] File PCT application with WIPO
- [ ] Include: specification, claims, abstract, drawings
- [ ] Request international search
- [ ] Pay filing fees

### Month 18-19 (International Search Report)
- [ ] Receive ISR from WIPO
- [ ] Assess patentability feedback
- [ ] Decide whether to proceed to national phase

### Month 30-31 (National Phase Entry)
- [ ] Select target countries
- [ ] File national phase applications
- [ ] Engage local patent attorneys
- [ ] Pay national phase fees

## COUNTRY SELECTION STRATEGY

Based on:
1. **Market Size** (where is demand?)
2. **Manufacturing** (where will it be made?)
3. **Competition** (where are competitors?)
4. **Enforcement** (strong IP protection?)
5. **Cost** (filing + maintenance fees)

Generate comprehensive PCT filing strategy.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def country_selection(self, market_analysis=""):
        """Select optimal countries for patent protection"""
        prompt = f"""
Recommend countries for international patent filing.

MARKET ANALYSIS:
{market_analysis if market_analysis else "Micro-hydro market: Global, $2.8B"}

## TIER 1 COUNTRIES (Must File)

### United States
- **Market Size:** Largest clean energy market
- **Filing Cost:** $10,000-$15,000 (utility patent)
- **Maintenance:** $4,000-$8,000 over 20 years
- **Enforcement:** Strong IP protection
- **Manufacturing:** Limited local production
- **Strategic Value:** HIGH (licensing potential)
- **Recommendation:** Already filed (priority country)

### European Patent (EP)
- **Coverage:** Validates in multiple countries (Germany, France, UK, etc.)
- **Filing Cost:** $5,000-$8,000 (EPO)
- **Validation Costs:** $1,000-$3,000 per country
- **Maintenance:** $15,000-$25,000 over 20 years (all countries)
- **Strategic Value:** HIGH (large market)
- **Recommendation:** **FILE** - Select 3-5 countries for validation

### China
- **Market Size:** Largest hydro market globally
- **Filing Cost:** $4,000-$6,000
- **Maintenance:** $3,000-$5,000 over 20 years
- **Enforcement:** Improving but challenging
- **Manufacturing:** Major manufacturing base
- **Strategic Value:** CRITICAL (manufacturing risk)
- **Recommendation:** **FILE** - Defensive protection

### Canada
- **Market Size:** Moderate hydro market
- **Filing Cost:** $3,000-$5,000
- **Maintenance:** $2,000-$4,000 over 20 years
- **Enforcement:** Strong
- **Strategic Value:** MEDIUM (regional market)
- **Recommendation:** **FILE** - Geographic proximity

## TIER 2 COUNTRIES (Consider Filing)

### Japan
- Cost: $7,000-$10,000
- Value: Advanced technology market, strong IP culture
- Decision: File if targeting Asian manufacturers

### South Korea
- Cost: $4,000-$6,000
- Value: Manufacturing hub, growing renewable market
- Decision: File if licensing to Korean companies

### Australia
- Cost: $3,000-$5,000
- Value: Growing micro-hydro market
- Decision: File if targeting Oceania region

### India
- Cost: $2,000-$3,000
- Value: Massive potential market, low cost
- Decision: File if targeting developing markets

### Brazil
- Cost: $3,000-$5,000
- Value: Large hydro market, growing renewables
- Decision: File if targeting South America

## TIER 3 COUNTRIES (Skip Unless Specific Reason)

- Mexico, Chile, South Africa, Norway, Switzerland, etc.
- File only if specific licensing opportunity or manufacturing

## COST-BENEFIT ANALYSIS

### Scenario A: US Only
- Cost: $15,000 total
- Coverage: 25% of global market
- Risk: Unprotected in manufacturing centers

### Scenario B: US + EP(3) + China + Canada
- Cost: $35,000-$45,000 total
- Coverage: 70% of global market
- Risk: Balanced protection

### Scenario C: US + PCT → 8 Countries
- Cost: $60,000-$80,000 total
- Coverage: 85% of global market
- Risk: High upfront cost

## RECOMMENDATION

**Optimal Strategy for Micro-Hydro Patent:**

1. **Priority 1 (Month 12):** File PCT application
   - Cost: $4,000
   - Preserves rights in all PCT countries

2. **Priority 2 (Month 30):** National Phase Entry
   - US (already filed)
   - EP: Germany, France, UK
   - China
   - Canada
   - **Total Cost:** ~$35,000

3. **Priority 3 (If revenue justifies):** Expand Coverage
   - Japan, South Korea, Australia
   - **Additional Cost:** ~$20,000

**Total Investment:** $35,000-$55,000 over 30 months
**Coverage:** 70-80% of global market value

Generate country selection strategy with clear recommendations.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def filing_timeline(self, us_filing_date):
        """Generate international filing timeline"""
        prompt = f"""
Generate international patent filing timeline.

US PROVISIONAL FILING DATE: {us_filing_date}

Calculate all critical deadlines:

## TIMELINE & DEADLINES

### Month 0: {us_filing_date}
✅ US Provisional Application Filed
- Cost: $75-$300
- 12-month priority window begins

### Month 11: [DATE]
⚠️ CRITICAL: Prepare PCT Application
- Begin drafting international application
- Review provisional for completeness
- Budget for PCT filing (~$4k)
- Engage WIPO filing agent

### Month 12: [DATE] 
🚨 DEADLINE: PCT Filing
- File PCT application with WIPO
- Must file before provisional expires
- Pay international filing fee + search fee
- Request International Search Report (ISR)
- **CANNOT MISS THIS DEADLINE**

### Month 16-18: [DATE]
📄 Receive International Search Report
- WIPO examiner provides prior art search
- Assess patentability
- Identify potential issues
- Option: File response or amendments

### Month 28: [DATE]
⚠️ WARNING: 30-Month Deadline Approaching
- Finalize country selection strategy
- Budget for national phase (~$5k per country)
- Engage local patent attorneys
- Prepare translations if needed

### Month 30: [DATE]
🚨 DEADLINE: National Phase Entry (Most Countries)
- Enter national phase in selected countries
- File translations (if required)
- Pay national filing fees
- Engage local counsel in each jurisdiction

### Month 31: [DATE]
🚨 DEADLINE: National Phase Entry (Some Countries)
- US: 30 months (can extend to 31)
- EP: 31 months
- Check specific country deadlines

## COST TIMELINE

| Milestone | Date | Cost |
|-----------|------|------|
| US Provisional | Month 0 | $300 |
| PCT Filing | Month 12 | $4,000 |
| ISR Response (optional) | Month 18 | $1,000 |
| National Phase (4 countries) | Month 30 | $25,000 |
| **Total (First 30 months)** | | **$30,300** |

## CRITICAL REMINDERS

### Month 10-11: URGENT
Set up calendar alerts, engage attorneys, prepare documents

### Month 12: CANNOT MISS
Missing this deadline = lose international rights forever

### Month 28-29: URGENT
Final country selection, budget approval, attorney engagement

### Month 30-31: CANNOT MISS
Missing this deadline = lose rights in specific countries

## CONTINGENCY PLANNING

### If tight on budget at Month 12:
- Still file PCT (only $4k)
- Reassess countries at Month 28 based on ISR feedback
- Can abandon weak patents without national phase costs

### If tight on budget at Month 30:
- File in fewer countries initially
- Can add countries later (but lose priority date benefit)

Generate complete timeline with specific dates for all deadlines.

Current date: {datetime.now().strftime('%B %d, %Y')}
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def translation_requirements(self, target_countries):
        """Assess translation needs and costs"""
        prompt = f"""
Assess translation requirements for patent filing in: {target_countries}

## TRANSLATION REQUIREMENTS BY COUNTRY

### English-Language Countries (No Translation)
- United States: English
- United Kingdom: English (via EP)
- Canada: English or French
- Australia: English
- **Cost:** $0

### European Patent Office
- **Filing:** English accepted
- **Validation:** Translations required for each country
  - Germany: German translation
  - France: French translation
  - Spain: Spanish translation
  - Italy: Italian translation
- **Cost:** $1,000-$3,000 per country
- **Page Count:** ~50-80 pages typical patent
- **Rate:** $0.15-$0.25 per word

### China
- **Language:** Simplified Chinese (Mandarin)
- **Cost:** $3,000-$5,000 for full patent
- **Technical Challenge:** High (technical terminology)
- **Must Use:** Certified patent translator

### Japan
- **Language:** Japanese
- **Cost:** $4,000-$6,000 for full patent
- **Technical Challenge:** Very High
- **Must Use:** Certified patent translator with technical expertise

### South Korea
- **Language:** Korean
- **Cost:** $2,500-$4,000 for full patent
- **Must Use:** Certified patent translator

### Other Languages
- French: $2,000-$3,000
- German: $2,000-$3,000
- Spanish: $1,500-$2,500
- Portuguese (Brazil): $1,500-$2,500

## COST ESTIMATES

### Scenario: US + EP(3) + China + Canada
- Germany translation: $2,500
- France translation: $2,500
- China translation: $4,000
- Canada: $0 (English)
- **Total Translation Cost:** $9,000

### Scenario: US + EP(5) + China + Japan + Korea
- EP translations (5): $12,500
- China: $4,000
- Japan: $5,000
- Korea: $3,000
- **Total Translation Cost:** $24,500

## COST REDUCTION STRATEGIES

### 1. Limit EP Validation Countries
- File EP but only validate in 2-3 key countries
- Savings: $5,000-$10,000

### 2. Defer Non-Critical Countries
- File in English countries first (US, UK, Canada, Australia)
- Add others later if revenue justifies
- Savings: Preserve cash flow

### 3. Use Machine Translation + Review
- Google/DeepL for initial draft
- Certified translator for review only
- Savings: 30-50% reduction
- Risk: Lower quality

### 4. Streamline Claims
- Reduce claim count (fewer words to translate)
- Focus specification on essentials
- Savings: 20-30% reduction

### 5. Claims-Only Translation
- Some countries accept: Claims translated + English specification
- Check specific country rules
- Savings: 50-70% reduction

## RECOMMENDED APPROACH

**Phase 1 (Month 12): PCT Filing**
- File in English
- Cost: $0 translation
- Preserves all options

**Phase 2 (Month 30): Strategic Translation**
- Required translations only:
  - China: $4,000 (manufacturing risk)
  - Germany: $2,500 (key EU market)
  - France: $2,500 (key EU market)
- **Total:** $9,000

**Phase 3 (If Budget Allows):**
- Add Japan, Korea, additional EP countries
- **Additional:** $10,000-$15,000

## VENDOR SELECTION

### Recommended Translation Services
- **LexTranslations:** Patent-specific, certified
- **Toppan Merrill:** Large volume, competitive rates
- **Patent Translations Inc:** Technical expertise
- **Local patent attorneys:** Usually have preferred vendors

### Quality Control
- Use back-translation to verify accuracy
- Technical review by engineer + translator
- Critical for claims (small error = big problem)

Generate translation strategy with cost estimates.
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
    print(f"🌍 INTERNATIONAL PATENT FILER")
    print(f"{'='*70}\n")
    
    agent = InternationalPatentFiler()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "pct":
            if len(sys.argv) > 2:
                patent = " ".join(sys.argv[2:])
                print(f"PCT STRATEGY FOR: {patent}\n")
                print(agent.pct_strategy(patent))
            else:
                print("❌ Usage: python international_filer.py pct '<patent description>'")
                print("Example: python international_filer.py pct 'φ-turbine efficiency technology'")
        
        elif command == "countries":
            market = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
            print("COUNTRY SELECTION STRATEGY\n")
            print(agent.country_selection(market))
        
        elif command == "timeline":
            if len(sys.argv) > 2:
                filing_date = " ".join(sys.argv[2:])
                print(f"FILING TIMELINE FROM: {filing_date}\n")
                print(agent.filing_timeline(filing_date))
            else:
                print("❌ Usage: python international_filer.py timeline '<US filing date>'")
                print("Example: python international_filer.py timeline 'January 15, 2026'")
        
        elif command == "translation":
            if len(sys.argv) > 2:
                countries = " ".join(sys.argv[2:])
                print(f"TRANSLATION REQUIREMENTS FOR: {countries}\n")
                print(agent.translation_requirements(countries))
            else:
                print("❌ Usage: python international_filer.py translation '<target countries>'")
                print("Example: python international_filer.py translation 'China, Germany, Japan'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  pct '<patent>'           - PCT filing strategy")
            print("  countries '<market>'     - Country selection")
            print("  timeline '<date>'        - Filing timeline")
            print("  translation '<countries>' - Translation requirements")
    else:
        print("Available commands:")
        print("  pct '<patent>'           - PCT filing strategy")
        print("  countries '<market>'     - Country selection")
        print("  timeline '<date>'        - Filing timeline")
        print("  translation '<countries>' - Translation requirements")
        print("\nExample:")
        print('  python international_filer.py pct "micro-hydro turbine patent"')
