"""
Patent Drafting Specialist - Draft claims, specifications, and figures
Division: IP & Patent Strategy
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv(dotenv_path='../.env')

class PatentDraftingSpecialist:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Patent Drafting Specialist initialized (Groq - FREE)")
    
    def draft_claims(self, innovation_description):
        """Draft independent and dependent patent claims"""
        prompt = f"""
You are a patent drafting specialist. Draft comprehensive patent claims.

INNOVATION:
{innovation_description}

Draft patent claims in proper USPTO format:

## INDEPENDENT CLAIMS (3-5)
Write broad, fundamental claims covering the core invention.
Use proper claim language:
- "A turbine comprising..."
- "A method comprising..."
- Clear antecedent basis
- Definite claim scope

## DEPENDENT CLAIMS (10-15)
Write specific implementations that depend on independent claims.
Cover:
- Specific dimensions/ratios
- Material choices
- Optional features
- Preferred embodiments

## CLAIM STRATEGY
Explain:
- Claim breadth vs. patentability
- Key novelty aspects
- Infringement considerations
- Design-around difficulty

Format in proper patent claim structure with numbering.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def draft_specification(self, title):
        """Draft patent specification sections"""
        prompt = f"""
Draft patent specification for: {title}

Create comprehensive specification sections:

## TITLE OF THE INVENTION
[Clear, descriptive title]

## FIELD OF THE INVENTION
[Technical field and industry]

## BACKGROUND
- Current state of the art
- Problems with existing solutions
- Need for improvement

## SUMMARY OF THE INVENTION
[Brief overview of the invention and advantages]

## BRIEF DESCRIPTION OF THE DRAWINGS
Figure 1: [Description]
Figure 2: [Description]
[etc.]

## DETAILED DESCRIPTION
### Overview
[General description]

### Preferred Embodiment
[Detailed description with reference to figures]

### Alternative Embodiments
[Variations and modifications]

### Operation
[How it works]

### Advantages
[Benefits over prior art]

Format in proper patent specification style with clear section headers.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=4000
        )
        return completion.choices[0].message.content
    
    def draft_abstract(self, invention_summary):
        """Draft patent abstract (150 words max)"""
        prompt = f"""
Draft a patent abstract (150 words maximum) for:

{invention_summary}

Requirements:
- Concise technical summary
- Clearly state the problem solved
- Describe the key features
- Mention primary advantages
- Use present tense
- No marketing language
- USPTO format

Generate a single paragraph abstract.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=500
        )
        return completion.choices[0].message.content
    
    def generate_figure_descriptions(self, design_description):
        """Generate figure descriptions for patent drawings"""
        prompt = f"""
Generate figure descriptions for patent drawings:

DESIGN:
{design_description}

Create figure list with descriptions:

## FIGURE DESCRIPTIONS

### Figure 1: [Title]
- View type (front, side, perspective, cross-section)
- What it shows
- Key elements numbered
- Purpose of this view

### Figure 2: [Title]
[etc.]

Include:
- Overall assembly views
- Detail views of key features
- Cross-sectional views
- Exploded views if applicable
- Flow diagrams if applicable

For each figure, list numbered elements (1, 2, 3...) with descriptions.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def format_for_filing(self, patent_title):
        """Generate filing checklist and format requirements"""
        prompt = f"""
Generate USPTO provisional patent filing checklist for: {patent_title}

## FILING CHECKLIST

### Required Documents
- [ ] Cover sheet (USPTO Form SB/16)
- [ ] Specification (with all sections)
- [ ] Claims (independent and dependent)
- [ ] Abstract (150 words max)
- [ ] Drawings (if applicable)
- [ ] Filing fee payment

### Specification Format Requirements
- Font: Times New Roman, 12pt
- Margins: 1" top, 1" bottom, 1" left, 1" right
- Line spacing: 1.5 or double
- Line numbering: Every 5th line
- Page numbering: Centered at bottom

### Drawing Requirements
- Black ink on white paper
- Minimum size: 8.5" x 11"
- Margins: 1" top/bottom, 0.5" sides
- View labels: Fig. 1, Fig. 2, etc.
- Element numbers: Consistent throughout

### Pre-Filing Review
- [ ] All claims have antecedent basis
- [ ] All figures referenced in specification
- [ ] All elements numbered and described
- [ ] Abstract within word limit
- [ ] Inventor names and addresses correct
- [ ] Title clear and descriptive

### Filing Options
- USPTO e-filing (preferred)
- Registered e-filer required
- Filing fee: $75 (micro entity), $150 (small entity), $300 (large entity)

Generate complete checklist with specific format requirements.
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
    print(f"📝 PATENT DRAFTING SPECIALIST")
    print(f"{'='*70}\n")
    
    agent = PatentDraftingSpecialist()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "claims":
            if len(sys.argv) > 2:
                innovation = " ".join(sys.argv[2:])
                print(f"DRAFTING CLAIMS FOR: {innovation}\n")
                print(agent.draft_claims(innovation))
            else:
                print("❌ Usage: python patent_drafter.py claims '<innovation description>'")
                print("Example: python patent_drafter.py claims '21-blade Fibonacci turbine'")
        
        elif command == "specification":
            if len(sys.argv) > 2:
                title = " ".join(sys.argv[2:])
                print(f"DRAFTING SPECIFICATION FOR: {title}\n")
                print(agent.draft_specification(title))
            else:
                print("❌ Usage: python patent_drafter.py specification '<patent title>'")
        
        elif command == "abstract":
            if len(sys.argv) > 2:
                summary = " ".join(sys.argv[2:])
                print("DRAFTING ABSTRACT\n")
                print(agent.draft_abstract(summary))
            else:
                print("❌ Usage: python patent_drafter.py abstract '<invention summary>'")
        
        elif command == "figures":
            if len(sys.argv) > 2:
                design = " ".join(sys.argv[2:])
                print("GENERATING FIGURE DESCRIPTIONS\n")
                print(agent.generate_figure_descriptions(design))
            else:
                print("❌ Usage: python patent_drafter.py figures '<design description>'")
        
        elif command == "filing":
            title = sys.argv[2] if len(sys.argv) > 2 else "Patent Application"
            print(f"FILING CHECKLIST FOR: {title}\n")
            print(agent.format_for_filing(title))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  claims '<description>'       - Draft patent claims")
            print("  specification '<title>'      - Draft full specification")
            print("  abstract '<summary>'         - Draft abstract")
            print("  figures '<design>'           - Generate figure descriptions")
            print("  filing '<title>'             - Filing checklist")
    else:
        print("Available commands:")
        print("  claims '<description>'       - Draft patent claims")
        print("  specification '<title>'      - Draft full specification")
        print("  abstract '<summary>'         - Draft abstract")
        print("  figures '<design>'           - Generate figure descriptions")
        print("  filing '<title>'             - Filing checklist")
        print("\nExample:")
        print('  python patent_drafter.py claims "21-blade Fibonacci turbine with golden angle spacing"')
