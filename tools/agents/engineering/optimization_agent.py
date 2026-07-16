"""
Optimization Agent - Design optimization and decision support
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv

load_dotenv()

class OptimizationAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Optimization Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Optimization Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def optimize_blade_geometry(self, constraints):
        """Optimize turbine blade design"""
        prompt = f"""
Optimize turbine blade geometry:

CONSTRAINTS:
{constraints}

Provide:
## OPTIMIZATION OBJECTIVE
[Maximize efficiency? Minimize cost? Multi-objective?]

## DESIGN VARIABLES
[Blade count, angle, thickness, length, etc.]

## OPTIMIZATION METHOD
[Genetic algorithm, gradient descent, response surface?]

## RECOMMENDED DESIGN
[Optimal parameter values]

## SENSITIVITY ANALYSIS
[Which parameters matter most?]

## PYTHON CODE
[Generate optimization script using scipy.optimize or DEAP]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def phi_optimization(self, parameter_name):
        """Apply golden ratio optimization"""
        prompt = f"""
Apply φ (golden ratio 1.618) optimization to: {parameter_name}

Explain:
## PHI RELATIONSHIP
[How does φ apply to this parameter?]

## FIBONACCI SEQUENCE
[Relevant Fibonacci numbers?]

## OPTIMIZATION RATIONALE
[Why φ is optimal here]

## DESIGN FORMULA
[Mathematical relationship with φ]

## EXPECTED IMPROVEMENT
[Performance gain from φ-optimization]

Include references to Dan Winter's work on coherence.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def cost_benefit_analysis(self, decision_description):
        """Analyze engineering decisions"""
        prompt = f"""
Cost-benefit analysis for:

{decision_description}

Provide:
## OPTIONS COMPARISON
[Compare alternatives with pros/cons]

## FINANCIAL ANALYSIS
- Initial cost
- Operating cost
- ROI timeline
- Break-even point

## RISK ASSESSMENT
[Technical, financial, timeline risks]

## DECISION MATRIX
[Weighted scoring of options]

## RECOMMENDATION
[Best choice and why]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def multi_objective_optimization(self, objectives):
        """Pareto optimization for multiple goals"""
        prompt = f"""
Multi-objective optimization:

OBJECTIVES:
{objectives}

Analyze:
## PARETO FRONTIER
[Trade-offs between objectives]

## WEIGHTING STRATEGY
[How to balance competing goals?]

## PARETO-OPTIMAL SOLUTIONS
[Best compromise designs]

## PYTHON IMPLEMENTATION
[Code for NSGA-II or similar]

## VISUALIZATION
[How to plot Pareto front?]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"🎯 OPTIMIZATION AGENT")
    print(f"{'='*70}\n")
    
    agent = OptimizationAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "blade":
            constraints = sys.argv[2] if len(sys.argv) > 2 else "Diameter 100mm, material PLA, flow rate 5 L/min"
            print(agent.optimize_blade_geometry(constraints))
        
        elif command == "phi":
            parameter = sys.argv[2] if len(sys.argv) > 2 else "blade spacing angle"
            print(agent.phi_optimization(parameter))
        
        elif command == "cost-benefit":
            decision = sys.argv[2] if len(sys.argv) > 2 else "3D print vs CNC machining for turbine runners"
            print(agent.cost_benefit_analysis(decision))
        
        elif command == "multi-objective":
            objectives = sys.argv[2] if len(sys.argv) > 2 else "Maximize efficiency, minimize cost, minimize noise"
            print(agent.multi_objective_optimization(objectives))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: blade | phi | cost-benefit | multi-objective")
    else:
        print("Commands:")
        print("  blade '<constraints>'      - Optimize blade geometry")
        print("  phi '<parameter>'          - Golden ratio optimization")
        print("  cost-benefit '<decision>'  - Decision analysis")
        print("  multi-objective '<goals>'  - Pareto optimization")
