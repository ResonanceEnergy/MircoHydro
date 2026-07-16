"""
Research Agent - Literature review, prior art search, technical analysis
Uses: Gemini (free tier) with web search capability
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class ResearchAgent:
    def __init__(self):
        self.agent_name = "Research Agent"
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ GOOGLE_API_KEY not found in .env")
            exit(1)
        
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Research Agent initialized (Gemini Flash - FREE)")
    
    def search_patents(self, query):
        """Search Google Patents and analyze results"""
        base_url = "https://patents.google.com/"
        search_url = f"{base_url}?q={query.replace(' ', '+')}"
        
        prompt = f"""
Analyze patent landscape for: "{query}"

Provide:
1. KEY SEARCH TERMS for Google Patents
   - Alternative terms
   - CPC classifications (Cooperative Patent Classification)
   - Keywords to include/exclude

2. EXPECTED PRIOR ART
   - Likely existing patents (based on technology)
   - Key players in this space
   - Patent families to investigate

3. NOVELTY OPPORTUNITIES
   - Gaps in existing patents
   - Unexplored combinations
   - Novel applications

4. SEARCH STRATEGY
   - Boolean search strings
   - Date ranges to focus on
   - Assignees to check

Format as actionable patent search guide.
        """
        
        analysis = self.model.generate_content(prompt).text
        
        return {
            "query": query,
            "search_url": search_url,
            "analysis": analysis,
            "instructions": "Visit search URL, use search terms from analysis"
        }
    
    def analyze_prior_art(self, technology):
        """Deep analysis of prior art landscape"""
        prompt = f"""
Conduct comprehensive prior art analysis for: {technology}

Context: Micro-hydro renewable energy startup filing patents.

Provide structured analysis:

## 1. EXISTING TECHNOLOGIES
List 5-10 key existing patents/products in this space:
- Technology name
- Key features
- Assignee/company
- Year introduced
- Limitations

## 2. GAPS IN CURRENT SOLUTIONS
What problems remain unsolved?
- Technical limitations
- Cost barriers
- Performance issues
- Market gaps

## 3. INNOVATION OPPORTUNITIES
Where can we differentiate?
- Novel combinations
- Improved performance
- Cost reduction methods
- New applications

## 4. PATENT STRATEGY
How to position our patent:
- Focus on specific claims
- Avoid infringement risks
- Strengthen novelty arguments
- International considerations

## 5. DEFENSIVE CITATIONS
Papers/patents to cite in our application:
- Shows awareness of prior art
- Demonstrates novelty
- Establishes credibility

Be specific and actionable. Focus on micro-hydro context.
        """
        
        return self.model.generate_content(prompt).text
    
    def literature_review(self, topic):
        """Generate academic literature review"""
        prompt = f"""
Generate comprehensive literature review: {topic}

Context: Technical documentation for patent application and R&D program.

Structure:

## 1. THEORETICAL BACKGROUND (300 words)
- Fundamental principles
- Key equations and relationships
- Physical mechanisms

## 2. HISTORICAL DEVELOPMENT (200 words)
- Pioneering work (cite pioneers: e.g., Schauberger, Betz)
- Evolution of the technology
- Major breakthroughs

## 3. CURRENT STATE OF RESEARCH (400 words)
- Recent advances (2015-2025)
- Leading research groups
- Emerging trends
- Commercial implementations

## 4. EXPERIMENTAL METHODS (300 words)
- Standard test procedures
- Measurement techniques
- Validation approaches
- Common pitfalls

## 5. KEY FINDINGS & METRICS (200 words)
- Typical performance ranges
- Efficiency benchmarks
- Cost metrics
- Reliability data

## 6. RESEARCH GAPS (200 words)
- Unanswered questions
- Conflicting results
- Opportunities for innovation

## 7. REFERENCES (15-20)
Format: Author (Year). Title. Journal/Source.

Academic tone, suitable for patent background section or research proposal.
        """
        
        return self.model.generate_content(prompt).text
    
    def analyze_visionary_tech(self, visionary_name, technology_focus):
        """Analyze specific visionary's contribution to technology"""
        prompt = f"""
Analyze {visionary_name}'s contributions to {technology_focus}.

Context: We're integrating insights from multiple visionaries (Schauberger, Dan Winter, 
Grander, Callahan) into micro-hydro design. Need rigorous technical analysis.

Provide:

## 1. CORE PRINCIPLES
What are the key theoretical claims?
- Physical mechanisms proposed
- Mathematical relationships
- Design implications

## 2. SCIENTIFIC VALIDATION
What evidence exists?
- Peer-reviewed studies
- Experimental validation
- Replication by others
- Skeptical analysis

## 3. ENGINEERING TRANSLATION
How to implement in hardware:
- Design parameters
- Materials requirements
- Measurement methods
- Expected results

## 4. PATENT RELEVANCE
How this supports patent claims:
- Novel aspects
- Measurable improvements
- Prior art differentiation
- Claim language suggestions

## 5. TESTING PROTOCOL
How to validate the claims:
- Test setup
- Measurements needed
- Control experiments
- Success criteria

Be technically rigorous. Distinguish verified facts from speculative claims.
        """
        
        return self.model.generate_content(prompt).text
    
    def competitive_analysis(self, market_segment):
        """Analyze competitive landscape"""
        prompt = f"""
Competitive analysis for: {market_segment}

Context: Micro-hydro startup entering market with φ-optimized technology.

Analyze:

## 1. KEY COMPETITORS
List 5-10 main players:
- Company name
- Product offerings
- Price range
- Market position
- Strengths/weaknesses

## 2. TECHNOLOGY COMPARISON
How does our tech stack up?
- Performance metrics
- Cost position
- Unique features
- IP protection

## 3. MARKET POSITIONING
Where do we fit?
- Target customers
- Value proposition
- Pricing strategy
- Distribution channels

## 4. COMPETITIVE ADVANTAGES
Why customers choose us:
- Technology moat
- Performance edge
- Cost savings
- Service/support

## 5. THREATS & OPPORTUNITIES
- Market trends
- Regulatory changes
- New entrants
- Partnership opportunities

## 6. GO-TO-MARKET STRATEGY
- Initial target segment
- Proof points needed
- Marketing message
- Sales approach

Practical and actionable for small startup competing against established players.
        """
        
        return self.model.generate_content(prompt).text
    
    def generate_test_protocol(self, experiment_name, hypothesis):
        """Generate detailed experimental protocol"""
        prompt = f"""
Design rigorous experimental protocol:

EXPERIMENT: {experiment_name}
HYPOTHESIS: {hypothesis}

Generate complete protocol following scientific method:

## 1. OBJECTIVE
Clear, measurable goal

## 2. HYPOTHESIS
Testable prediction with quantitative targets

## 3. MATERIALS & EQUIPMENT
Complete list with specifications:
- Equipment (with model numbers)
- Materials (with quantities)
- Sensors (with accuracy specs)
- Data acquisition (hardware/software)

## 4. EXPERIMENTAL SETUP
Step-by-step assembly:
- Diagrams needed (describe)
- Connections and wiring
- Calibration procedures
- Safety considerations

## 5. TEST PROCEDURE
Detailed steps:
1. Preparation
2. Baseline measurements
3. Test execution
4. Data collection
5. Shutdown/cleanup

## 6. VARIABLES
- Independent (what we control)
- Dependent (what we measure)
- Control (what we keep constant)

## 7. DATA COLLECTION
- Sampling rate
- Duration
- File format
- Backup procedures

## 8. ANALYSIS PLAN
- Calculations needed
- Statistical tests
- Visualizations
- Success criteria

## 9. QUALITY ASSURANCE
- Calibration checks
- Repeatability tests
- Error sources
- Validation methods

## 10. EXPECTED RESULTS
Quantitative predictions with ranges

Suitable for patent evidence and peer review.
        """
        
        return self.model.generate_content(prompt).text

# CLI Interface
if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    print(f"\n{'='*70}")
    print(f"🔬 RESEARCH AGENT")
    print(f"{'='*70}\n")
    
    agent = ResearchAgent()
    
    # Create Research directory
    research_dir = Path("RnD/Research")
    research_dir.mkdir(parents=True, exist_ok=True)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "patents":
            query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "fibonacci turbine blade golden ratio"
            print(f"🔍 Searching patents: {query}\n")
            
            result = agent.search_patents(query)
            
            print(f"Search URL: {result['search_url']}\n")
            print("="*70)
            print(result['analysis'])
            
            # Save to file
            output_file = research_dir / f"patent_search_{datetime.now().strftime('%Y%m%d')}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# Patent Search: {query}\n\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                f.write(f"**Search URL:** {result['search_url']}\n\n")
                f.write(result['analysis'])
            
            print(f"\n✅ Saved to: {output_file}")
        
        elif command == "prior-art":
            tech = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "golden ratio turbine optimization"
            print(f"🔬 Analyzing prior art: {tech}\n")
            
            analysis = agent.analyze_prior_art(tech)
            print(analysis)
            
            # Save to file
            output_file = research_dir / f"prior_art_{tech.replace(' ', '_')[:30]}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# Prior Art Analysis: {tech}\n\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                f.write(analysis)
            
            print(f"\n✅ Saved to: {output_file}")
        
        elif command == "literature":
            topic = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "vortex flow in hydraulic turbines"
            print(f"📚 Literature review: {topic}\n")
            
            review = agent.literature_review(topic)
            print(review)
            
            # Save to file
            output_file = research_dir / f"literature_{topic.replace(' ', '_')[:30]}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# Literature Review: {topic}\n\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                f.write(review)
            
            print(f"\n✅ Saved to: {output_file}")
        
        elif command == "visionary":
            if len(sys.argv) > 3:
                name = sys.argv[2]
                tech = " ".join(sys.argv[3:])
                print(f"🌟 Analyzing {name}'s work on {tech}\n")
                
                analysis = agent.analyze_visionary_tech(name, tech)
                print(analysis)
                
                # Save to file
                output_file = research_dir / f"visionary_{name.lower().replace(' ', '_')}.md"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f"# Visionary Analysis: {name}\n\n")
                    f.write(f"**Technology Focus:** {tech}\n")
                    f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                    f.write(analysis)
                
                print(f"\n✅ Saved to: {output_file}")
            else:
                print("❌ Usage: python research_agent.py visionary <name> <technology>")
                print("Example: python research_agent.py visionary 'Viktor Schauberger' 'vortex flow dynamics'")
        
        elif command == "competitive":
            market = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "micro-hydro turbines under 50kW"
            print(f"📊 Competitive analysis: {market}\n")
            
            analysis = agent.competitive_analysis(market)
            print(analysis)
            
            # Save to file
            output_file = research_dir / f"competitive_{market.replace(' ', '_')[:30]}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# Competitive Analysis: {market}\n\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                f.write(analysis)
            
            print(f"\n✅ Saved to: {output_file}")
        
        elif command == "protocol":
            if len(sys.argv) > 3:
                name = sys.argv[2]
                hypothesis = " ".join(sys.argv[3:])
                print(f"🧪 Generating protocol: {name}\n")
                
                protocol = agent.generate_test_protocol(name, hypothesis)
                print(protocol)
                
                # Save to protocols directory
                protocol_dir = Path("RnD/Protocols")
                protocol_dir.mkdir(parents=True, exist_ok=True)
                
                output_file = protocol_dir / f"{name.replace(' ', '_').upper()}_PROTOCOL.md"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f"# PROTOCOL: {name}\n\n")
                    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
                    f.write(protocol)
                
                print(f"\n✅ Saved to: {output_file}")
            else:
                print("❌ Usage: python research_agent.py protocol <name> <hypothesis>")
                print("Example: python research_agent.py protocol 'φ-Turbine Test' '21-blade achieves 6-12% higher efficiency'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  patents       - Search patent landscape")
            print("  prior-art     - Analyze prior art for technology")
            print("  literature    - Generate literature review")
            print("  visionary     - Analyze visionary's contributions")
            print("  competitive   - Market competitive analysis")
            print("  protocol      - Generate experimental protocol")
    else:
        print("Usage:")
        print("  python research_agent.py patents <query>")
        print("  python research_agent.py prior-art <technology>")
        print("  python research_agent.py literature <topic>")
        print("  python research_agent.py visionary <name> <technology>")
        print("  python research_agent.py competitive <market>")
        print("  python research_agent.py protocol <name> <hypothesis>")
        print("\nExamples:")
        print("  python research_agent.py patents 'fibonacci blade turbine'")
        print("  python research_agent.py literature 'vortex flow optimization'")
        print("  python research_agent.py protocol 'Desktop Turbine Test' 'φ-spacing improves efficiency'")
