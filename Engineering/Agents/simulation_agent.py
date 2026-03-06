"""
CFD/FEA Agent - Computational fluid dynamics and finite element analysis
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv

load_dotenv()

class SimulationAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "CFD/FEA Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Simulation Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def generate_openfoam_case(self, geometry_description):
        """Create OpenFOAM simulation setup"""
        prompt = f"""
Generate OpenFOAM case files for:

GEOMETRY:
{geometry_description}

Provide:
## MESH CONFIGURATION (blockMeshDict or snappyHexMeshDict)
[Mesh sizing, refinement zones]

## BOUNDARY CONDITIONS (0/ files)
[Inlet velocity, outlet pressure, wall conditions]

## SOLVER SETTINGS (system/fvSchemes, fvSolution)
[Numerical schemes, solvers, convergence criteria]

## TURBULENCE MODEL (constant/turbulenceProperties)
[k-omega SST recommended for turbomachinery]

## CONTROL (system/controlDict)
[Time step, end time, write intervals]

## POST-PROCESSING
[Forces, efficiency calculation, flow visualization]

Return complete OpenFOAM case structure.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def generate_cfd_python_script(self, analysis_type):
        """Create Python CFD script using PyFluent or SimPy"""
        prompt = f"""
Generate Python script for CFD analysis:

TYPE: {analysis_type}

Use appropriate libraries (PyFluent, SimPy, or numerical methods)

Include:
- Geometry definition
- Mesh generation
- Flow solver
- Post-processing
- Visualization

Return complete Python code.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def interpret_cfd_results(self, results_summary):
        """Analyze CFD simulation results"""
        prompt = f"""
Analyze CFD results:

{results_summary}

Provide:
## KEY FINDINGS
[Performance metrics, efficiency, flow patterns]

## FLOW VISUALIZATION INSIGHTS
[Velocity contours, pressure distribution, vorticity]

## DESIGN RECOMMENDATIONS
[How to improve performance based on simulation]

## VALIDATION
[Do results match theory/experiments?]

## MESH SENSITIVITY
[Is mesh refined enough?]

## UNCERTAINTY QUANTIFICATION
[Confidence in results?]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def design_fea_analysis(self, structure_description):
        """Create FEA analysis plan"""
        prompt = f"""
Design FEA analysis for:

{structure_description}

Include:
## ANALYSIS TYPE
[Static, dynamic, modal, thermal?]

## MATERIAL PROPERTIES
[Young's modulus, Poisson's ratio, yield strength]

## BOUNDARY CONDITIONS
[Constraints, loads, pressures]

## MESH REQUIREMENTS
[Element type, sizing, refinement]

## FAILURE CRITERIA
[Von Mises stress, factor of safety]

## POST-PROCESSING
[Stress plots, displacement, safety factors]

Can be done in FreeCAD FEM or similar free tools.
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
    print(f"🌊 CFD/FEA SIMULATION AGENT")
    print(f"{'='*70}\n")
    
    agent = SimulationAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "openfoam":
            geometry = sys.argv[2] if len(sys.argv) > 2 else "21-blade turbine runner, 100mm diameter, φ-spaced blades"
            print(agent.generate_openfoam_case(geometry))
        
        elif command == "cfd-script":
            analysis = sys.argv[2] if len(sys.argv) > 2 else "turbine flow simulation"
            print(agent.generate_cfd_python_script(analysis))
        
        elif command == "interpret":
            results = sys.argv[2] if len(sys.argv) > 2 else "Max velocity 3.2 m/s, efficiency 52%, pressure drop 15 kPa"
            print(agent.interpret_cfd_results(results))
        
        elif command == "fea":
            structure = sys.argv[2] if len(sys.argv) > 2 else "Turbine blade, PLA material, 500 RPM rotation"
            print(agent.design_fea_analysis(structure))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: openfoam | cfd-script | interpret | fea")
    else:
        print("Commands:")
        print("  openfoam '<geometry>'    - OpenFOAM case setup")
        print("  cfd-script '<type>'      - Python CFD script")
        print("  interpret '<results>'    - Analyze CFD results")
        print("  fea '<structure>'        - FEA analysis plan")
