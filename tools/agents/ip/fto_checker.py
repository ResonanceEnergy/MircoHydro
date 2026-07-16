"""
Freedom to Operate (FTO) Checker - Prior art search and infringement analysis
Division: IP & Patent Strategy
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path='../.env')

class FTOChecker:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ FTO Checker initialized (Groq - FREE)")
    
    def prior_art_search(self, innovation_description):
        """Generate prior art search strategy"""
        prompt = f"""
You are a patent search specialist. Design comprehensive prior art search strategy.

INNOVATION TO SEARCH:
{innovation_description}

Generate search strategy:

## PATENT DATABASES TO SEARCH

### Primary Sources
- USPTO (patents.google.com)
- EPO (espacenet.com)
- WIPO (patentscope.wipo.int)
- Free Patents Online (freepatentsonline.com)

### Secondary Sources
- Google Patents
- Prior Art Archive
- Technical journals (IEEE, etc.)
- Academic publications

## SEARCH KEYWORDS

### Core Terms
[Primary technology terms]

### Alternative Terms
[Synonyms and related concepts]

### Classification Codes
- IPC (International Patent Classification)
- CPC (Cooperative Patent Classification)
- USPC (US Patent Classification)

Example for turbine:
- F03B (machines or engines for liquids)
- F03B3 (hydraulic motors)
- F03B11 (turbine parts)

## SEARCH STRINGS

### Boolean Search 1 (Broad)
"(turbine OR runner OR impeller) AND (fibonacci OR golden OR phi)"

### Boolean Search 2 (Specific)
"(blade AND spacing AND efficiency) AND (hydro OR water)"

### Boolean Search 3 (Adjacent)
[Technology-specific search]

## SEARCH METHODOLOGY

1. **Broad Search** (1-2 hours)
   - Use broad keywords
   - Review 100-200 results
   - Identify key patents

2. **Focused Search** (2-3 hours)
   - Refine based on initial findings
   - Classification code search
   - Citation analysis (forward/backward)

3. **Deep Dive** (1-2 hours)
   - Analyze closest patents in detail
   - Read full specifications
   - Compare claims to our innovation

## EVALUATION CRITERIA

For each patent found:
- ✅ Active or expired?
- ✅ Claim scope (broad or narrow?)
- ✅ How similar to our innovation?
- ✅ Can we design around it?
- ✅ Infringement risk (high/medium/low)

## EXPECTED FINDINGS
[What types of prior art likely exist?]

Generate comprehensive search strategy with specific search strings.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def infringement_analysis(self, our_design, existing_patent):
        """Analyze potential patent infringement"""
        prompt = f"""
You are a patent attorney analyzing potential infringement.

OUR DESIGN:
{our_design}

EXISTING PATENT TO ANALYZE:
{existing_patent}

Perform infringement analysis:

## CLAIM-BY-CLAIM ANALYSIS

### Independent Claim 1
**Claim Text:** [Extract or describe]

**Element-by-Element Comparison:**
| Claim Element | Our Design | Match? | Notes |
|---------------|------------|--------|-------|
| Element 1 | [Our implementation] | ✅/❌ | [Analysis] |
| Element 2 | [Our implementation] | ✅/❌ | [Analysis] |

**Conclusion:** Infringes / Does Not Infringe / Unclear

### Dependent Claims
[Analyze relevant dependent claims]

## INFRINGEMENT RISK ASSESSMENT

### Literal Infringement
Does our design literally read on all claim elements?
Risk: HIGH / MEDIUM / LOW

### Doctrine of Equivalents
Do we perform substantially the same function, in substantially the same way, to achieve substantially the same result?
Risk: HIGH / MEDIUM / LOW

### Overall Risk
Combined assessment: HIGH / MEDIUM / LOW

## DESIGN-AROUND OPTIONS

If infringement risk exists:

### Option 1: [Modification]
- Change: [Specific modification]
- Impact: [Technical/cost impact]
- Avoidance: [How it avoids infringement]

### Option 2: [Alternative approach]
[etc.]

## PATENT VALIDITY CHALLENGES

Could we challenge this patent?
- Prior art that wasn't considered
- Obviousness arguments
- Enablement issues
- Written description issues

## LICENSING OPPORTUNITIES

Could we license this patent instead?
- Likelihood of licensing
- Estimated royalty rate
- Strategic value

## RECOMMENDATION
[Clear go/no-go decision with reasoning]

Generate thorough infringement analysis.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def clearance_report(self, product_description):
        """Generate FTO clearance report for product launch"""
        prompt = f"""
Generate Freedom to Operate (FTO) clearance report for:

PRODUCT:
{product_description}

## EXECUTIVE SUMMARY
- Overall FTO status: CLEAR / CAUTION / BLOCKED
- Number of potentially blocking patents found
- Risk level: HIGH / MEDIUM / LOW
- Recommendation: PROCEED / MODIFY / STOP

## SEARCH METHODOLOGY
- Databases searched
- Search strings used
- Date range covered
- Classification codes
- Time spent

## POTENTIALLY BLOCKING PATENTS

### Patent 1: [Patent Number/Title]
- Patent holder: [Company/individual]
- Status: Active (expires YYYY)
- Relevant claims: [List claim numbers]
- Similarity to our product: HIGH / MEDIUM / LOW
- Infringement risk: HIGH / MEDIUM / LOW
- Recommended action: [License / Design-around / Challenge / Monitor]

### Patent 2: [Patent Number/Title]
[etc.]

## DESIGN-AROUND STRATEGIES
[If blocking patents exist, how to avoid them]

## LICENSING OPPORTUNITIES
[Potential licenses to acquire]

## MONITORING PLAN
- Patents to watch
- New applications in this space
- Competitor filings
- Review frequency

## RECOMMENDATIONS

### Short-term (0-3 months)
[Immediate actions]

### Medium-term (3-12 months)
[Follow-up actions]

### Long-term (12+ months)
[Strategic planning]

## SIGN-OFF
This FTO analysis conducted on [DATE]
Reviewed patents: [NUMBER]
Confidence level: HIGH / MEDIUM / LOW
Next review: [DATE]

Generate comprehensive FTO clearance report.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def patent_validity_challenge(self, patent_number):
        """Analyze potential grounds for challenging a patent"""
        prompt = f"""
Analyze potential validity challenges for patent: {patent_number}

## PATENT VALIDITY ANALYSIS

### Grounds for Challenge

#### 1. LACK OF NOVELTY (35 USC §102)
Was the invention fully disclosed in prior art before the filing date?
- Prior art references to search
- Anticipation analysis
- Likelihood of success: HIGH / MEDIUM / LOW

#### 2. OBVIOUSNESS (35 USC §103)
Would the invention have been obvious to a person skilled in the art?
- Prior art combinations
- Motivation to combine
- Teaching away from combination?
- Likelihood of success: HIGH / MEDIUM / LOW

#### 3. LACK OF ENABLEMENT (35 USC §112a)
Does the patent specification enable a person skilled in the art to make and use the invention?
- Missing details
- Undue experimentation required?
- Likelihood of success: HIGH / MEDIUM / LOW

#### 4. LACK OF WRITTEN DESCRIPTION (35 USC §112a)
Does the specification adequately describe the claimed invention?
- Original disclosure review
- Claim scope vs. specification
- Likelihood of success: HIGH / MEDIUM / LOW

#### 5. INDEFINITENESS (35 USC §112b)
Are the claims indefinite or unclear?
- Ambiguous terms
- Unclear scope
- Likelihood of success: HIGH / MEDIUM / LOW

## CHALLENGE OPTIONS

### Option 1: Inter Partes Review (IPR)
- Cost: $20,000-$50,000
- Timeline: 12-18 months
- Success rate: ~65% claims cancelled
- Best for: Obviousness/novelty challenges

### Option 2: Ex Parte Reexamination
- Cost: $5,000-$15,000
- Timeline: 18-24 months
- Success rate: ~70% claims modified
- Best for: Prior art not considered

### Option 3: District Court Litigation
- Cost: $500,000-$3,000,000
- Timeline: 2-5 years
- All grounds available
- Best for: Active infringement dispute

### Option 4: Covenant Not to Sue
- Cost: Negotiable
- Timeline: Immediate
- Best for: Avoiding litigation

## STRATEGIC CONSIDERATIONS
- Business value of challenge
- Litigation risk
- Alternatives (design-around, licensing)
- Cost-benefit analysis

## RECOMMENDATION
[Which challenge strategy, if any? Why?]

Generate comprehensive validity challenge analysis.
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
    print(f"🔍 FREEDOM TO OPERATE (FTO) CHECKER")
    print(f"{'='*70}\n")
    
    agent = FTOChecker()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "search":
            if len(sys.argv) > 2:
                innovation = " ".join(sys.argv[2:])
                print(f"PRIOR ART SEARCH STRATEGY: {innovation}\n")
                print(agent.prior_art_search(innovation))
            else:
                print("❌ Usage: python fto_checker.py search '<innovation description>'")
                print("Example: python fto_checker.py search 'Fibonacci blade turbine'")
        
        elif command == "infringement":
            if len(sys.argv) > 3:
                our_design = sys.argv[2]
                patent = " ".join(sys.argv[3:])
                print("INFRINGEMENT ANALYSIS\n")
                print(agent.infringement_analysis(our_design, patent))
            else:
                print("❌ Usage: python fto_checker.py infringement '<our design>' '<existing patent>'")
        
        elif command == "clearance":
            if len(sys.argv) > 2:
                product = " ".join(sys.argv[2:])
                print(f"FTO CLEARANCE REPORT: {product}\n")
                print(agent.clearance_report(product))
            else:
                print("❌ Usage: python fto_checker.py clearance '<product description>'")
        
        elif command == "challenge":
            if len(sys.argv) > 2:
                patent_num = sys.argv[2]
                print(f"VALIDITY CHALLENGE ANALYSIS: {patent_num}\n")
                print(agent.patent_validity_challenge(patent_num))
            else:
                print("❌ Usage: python fto_checker.py challenge '<patent number>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  search '<innovation>'        - Prior art search strategy")
            print("  infringement '<ours>' '<theirs>' - Infringement analysis")
            print("  clearance '<product>'        - FTO clearance report")
            print("  challenge '<patent #>'       - Patent validity challenge")
    else:
        print("Available commands:")
        print("  search '<innovation>'        - Prior art search strategy")
        print("  infringement '<ours>' '<theirs>' - Infringement analysis")
        print("  clearance '<product>'        - FTO clearance report")
        print("  challenge '<patent #>'       - Patent validity challenge")
        print("\nExample:")
        print('  python fto_checker.py search "golden ratio turbine blade spacing"')
