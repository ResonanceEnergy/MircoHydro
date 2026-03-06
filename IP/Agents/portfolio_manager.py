"""
Patent Portfolio Manager - Track pipeline, deadlines, and valuation
Division: IP & Patent Strategy
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime, timedelta
import json

load_dotenv(dotenv_path='../.env')

class PatentPortfolioManager:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Patent Portfolio Manager initialized (Groq - FREE)")
    
    def pipeline_status(self):
        """Generate current patent pipeline status"""
        prompt = """
You are a Patent Portfolio Manager for ResonanceEnergy micro-hydro startup.

Current Patent Pipeline (from PATENT_EXECUTION_FOCUS_GROUPS.md):

GROUP A (Weeks 1-3): φ-Turbine Patent
- 21-blade Fibonacci runner with golden angle spacing
- Target: 6-12% efficiency improvement
- Value: $8M-25M
- Status: Week 1 of 3, testing phase
- Deadline: File by Feb 16, 2026

GROUP B (Weeks 4-7): Resonant Water Revitalization Module
- Integration of Schauberger/Grander principles
- Value: $4M-15M
- Status: Design phase

GROUP C (Weeks 8-10): Spiral Penstock Design
- φ-optimized flow path
- Value: $1M-5M
- Status: Planning phase

GROUP D (Weeks 11-13): Integrated System
- Complete system architecture
- Value: $3M-10M
- Status: Concept phase

GROUP E (Weeks 14-16): Advanced Materials
- Novel composites, coatings
- Value: $2M-8M
- Status: Research phase

Generate:
## 📊 PIPELINE OVERVIEW
[Current status of all 7 patents]

## 🚨 CRITICAL DEADLINES (Next 30 Days)
[What must be filed soon?]

## 💰 PORTFOLIO VALUATION
[Current and projected value]

## ⚡ PRIORITY ACTIONS THIS WEEK
[What needs immediate attention?]

## 📈 PROGRESS METRICS
[% complete for active patents]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def deadlines_report(self):
        """Generate upcoming deadlines report"""
        prompt = f"""
You are a Patent Portfolio Manager tracking critical patent deadlines.

Today is {datetime.now().strftime('%A, %B %d, %Y')}.

Patent Timeline:
- Patent #1 (φ-Turbine): File by Feb 16, 2026 (21 days from now)
- Patent #2 (RWR Module): File by Mar 16, 2026
- Patent #3 (Spiral Penstock): File by Apr 6, 2026
- Patents #4-7: File by May 4, 2026

Provisional patents expire 12 months after filing (convert to utility by then).

Generate:
## 🚨 URGENT (Next 7 Days)
[Immediate action items]

## ⚠️ UPCOMING (8-30 Days)
[What's coming up?]

## 📅 FUTURE (30+ Days)
[Long-term planning]

## ✅ CHECKLIST FOR NEXT PATENT FILING
[Step-by-step filing checklist]

Include specific dates and countdown days.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def portfolio_valuation(self):
        """Calculate current and projected portfolio value"""
        prompt = """
Calculate patent portfolio valuation for ResonanceEnergy.

Patent Portfolio:
1. φ-Turbine: $8M-25M (high confidence, proven tech)
2. RWR Module: $4M-15M (medium confidence, niche market)
3. Spiral Penstock: $1M-5M (medium confidence, cost reduction)
4. Integrated System: $3M-10M (high confidence, system value)
5. Advanced Materials: $2M-8M (low confidence, R&D stage)
6-7. Additional innovations: $1M-5M each

Market factors:
- Micro-hydro market: $2.8B globally, growing 7%/year
- Efficiency improvements: High value (direct ROI)
- Licensing potential: Multiple industries
- Patent strength: Novel φ-optimization approach

Generate:
## 💰 CURRENT PORTFOLIO VALUE
- Conservative estimate
- Most likely estimate
- Optimistic estimate

## 📈 VALUATION BY PATENT
[Individual patent values with justification]

## 🎯 LICENSING POTENTIAL
[Annual licensing revenue projections]

## 🏢 M&A VALUATION SCENARIOS
[What acquirers might pay]

## 📊 VALUE DRIVERS
[What increases portfolio value most?]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def weekly_checklist(self):
        """Generate weekly execution checklist"""
        prompt = f"""
Generate weekly patent execution checklist for {datetime.now().strftime('%B %d, %Y')}.

Current Focus: Patent #1 (φ-Turbine) - Week 1 of 3

Tasks to track:
- Test data collection (60 tests planned)
- Statistical analysis (t-tests, significance)
- CAD drawings finalization
- Claims drafting
- Specification writing
- Prior art search
- Figure preparation
- Filing preparation

Generate:
## ✅ THIS WEEK'S CHECKLIST

### Monday
- [ ] Task with specific deliverable
- [ ] Task with specific deliverable

### Tuesday
[etc.]

### Weekly Deliverables
[What must be complete by Friday?]

### Blockers & Risks
[What could delay filing?]

Format as actionable checklist with clear completion criteria.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2500
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"📋 PATENT PORTFOLIO MANAGER")
    print(f"{'='*70}\n")
    
    agent = PatentPortfolioManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "status":
            print("📊 PIPELINE STATUS\n")
            print(agent.pipeline_status())
        
        elif command == "deadlines":
            print("🚨 DEADLINE REPORT\n")
            print(agent.deadlines_report())
        
        elif command == "valuation":
            print("💰 PORTFOLIO VALUATION\n")
            print(agent.portfolio_valuation())
        
        elif command == "checklist":
            print("✅ WEEKLY CHECKLIST\n")
            print(agent.weekly_checklist())
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  status      - Current pipeline status")
            print("  deadlines   - Upcoming deadlines")
            print("  valuation   - Portfolio value analysis")
            print("  checklist   - Weekly execution checklist")
    else:
        # Default: Show status
        print("📊 Generating pipeline status...\n")
        print(agent.pipeline_status())
        print("\n" + "="*70)
        print("\n💡 TIP: Run 'python portfolio_manager.py deadlines' for deadline report")
        print("💡 TIP: Run 'python portfolio_manager.py valuation' for portfolio value")
