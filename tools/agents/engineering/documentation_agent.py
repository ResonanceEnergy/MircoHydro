"""
Documentation Agent - Technical writing and report generation
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class DocumentationAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Documentation Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Documentation Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def generate_test_report(self, test_data_summary):
        """Generate formal test report"""
        prompt = f"""
Generate a professional engineering test report:

TEST DATA:
{test_data_summary}

Include these sections:
## EXECUTIVE SUMMARY
[One paragraph overview of results]

## METHODOLOGY
[Test setup, equipment, procedures]

## RESULTS
[Key findings with data tables]

## STATISTICAL ANALYSIS
[Significance testing, confidence intervals]

## DISCUSSION
[Interpretation, implications for design]

## CONCLUSIONS
[Summary of key takeaways]

## RECOMMENDATIONS
[Next steps, design improvements]

Format professionally for patent submission.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def write_patent_claims(self, innovation_description):
        """Draft patent claims"""
        prompt = f"""
Draft provisional patent claims for:

INNOVATION:
{innovation_description}

Provide:
## INDEPENDENT CLAIMS (3-5)
[Broad, fundamental claims]

## DEPENDENT CLAIMS (10-15)
[Specific implementations]

## CLAIM STRUCTURE
- Clear, precise language
- Measurable parameters
- Novel aspects emphasized

Use proper patent claim format.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def generate_user_manual(self, product_name, features):
        """Create user manual/documentation"""
        prompt = f"""
Create user manual for: {product_name}

FEATURES:
{features}

Include:
## INTRODUCTION
## INSTALLATION
## OPERATION
## MAINTENANCE
## TROUBLESHOOTING
## SPECIFICATIONS

Make it clear and user-friendly.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def create_technical_specification(self, system_name):
        """Generate technical specifications document"""
        prompt = f"""
Create technical specification sheet for: {system_name}

Include:
## SYSTEM OVERVIEW
## TECHNICAL PARAMETERS
## PERFORMANCE METRICS
## DIMENSIONS & MATERIALS
## OPERATING CONDITIONS
## COMPLIANCE & STANDARDS

Format as professional spec sheet.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"📝 DOCUMENTATION AGENT")
    print(f"{'='*70}\n")
    
    agent = DocumentationAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "test-report":
            summary = sys.argv[2] if len(sys.argv) > 2 else "21-blade φ-turbine: 8.5% efficiency improvement, p<0.01"
            print(agent.generate_test_report(summary))
        
        elif command == "patent-claims":
            innovation = sys.argv[2] if len(sys.argv) > 2 else "21-blade Fibonacci turbine with golden angle spacing"
            print(agent.write_patent_claims(innovation))
        
        elif command == "manual":
            product = sys.argv[2] if len(sys.argv) > 2 else "φ-Turbine System"
            features = "Self-cleaning, φ-optimized, modular design"
            print(agent.generate_user_manual(product, features))
        
        elif command == "spec":
            system = sys.argv[2] if len(sys.argv) > 2 else "φ-Turbine Micro-Hydro System"
            print(agent.create_technical_specification(system))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: test-report | patent-claims | manual | spec")
    else:
        print("Commands:")
        print("  test-report '<data>'      - Generate test report")
        print("  patent-claims '<desc>'    - Draft patent claims")
        print("  manual '<product>'        - Create user manual")
        print("  spec '<system>'           - Technical spec sheet")
