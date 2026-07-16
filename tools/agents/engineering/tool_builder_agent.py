"""
Tool Builder Agent - Generates engineering calculators and utilities
Uses: Groq (ultra-fast, free) or Gemini
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv

load_dotenv()

class ToolBuilderAgent:
    def __init__(self):
        self.agent_name = "Tool Builder Agent"
        
        # Try Groq first (faster), fallback to Gemini
        groq_key = os.getenv('GROQ_API_KEY')
        gemini_key = os.getenv('GOOGLE_API_KEY')
        
        if groq_key:
            from groq import Groq
            self.client = Groq(api_key=groq_key)
            self.provider = "groq"
            self.model = "llama-3.1-70b-versatile"
            print("✅ Tool Builder Agent initialized (Groq - FREE)")
        elif gemini_key:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            self.model_obj = genai.GenerativeModel('gemini-1.5-flash')
            self.provider = "gemini"
            print("✅ Tool Builder Agent initialized (Gemini Flash - FREE)")
        else:
            print("❌ No API key found. Set GROQ_API_KEY or GOOGLE_API_KEY in .env")
            print("Groq (fastest): https://console.groq.com/keys")
            print("Gemini (backup): https://aistudio.google.com/app/apikey")
            exit(1)
    
    def _generate(self, prompt, max_tokens=4000):
        """Generate text using available provider"""
        if self.provider == "groq":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        else:
            response = self.model_obj.generate_content(prompt)
            return response.text
    
    def generate_phi_calculator(self):
        """Generate φ-optimization calculator (Streamlit app)"""
        prompt = """
Create a complete Streamlit web app for φ-optimization calculator.

REQUIREMENTS:
1. Calculate golden ratio (φ = 1.618...) scaled dimensions
2. Generate Fibonacci sequences
3. Calculate golden angle (137.5°) for blade spacing
4. Show visual representation
5. Export results to CSV

INPUTS:
- Base dimension (mm)
- Component type (dropdown: Blade, Nozzle, Penstock, Vortex Chamber)
- Number of iterations (1-10)

OUTPUTS:
- Table of φ-scaled dimensions
- Fibonacci sequence
- Golden angle calculations
- Visualization (plot)
- Download CSV button

Return COMPLETE, RUNNABLE Python code with:
- Import statements
- Streamlit UI elements
- Calculations
- Visualizations
- Export functionality

Code only, no explanations.
        """
        
        return self._generate(prompt)
    
    def generate_efficiency_calculator(self):
        """Generate system efficiency cascade calculator"""
        prompt = """
Create a Streamlit app for micro-hydro system efficiency analysis.

REQUIREMENTS:
1. Component-by-component efficiency input
2. Calculate overall system efficiency (cascade multiplication)
3. Show loss breakdown
4. Sensitivity analysis
5. Visual waterfall chart

COMPONENTS:
- Intake (default 95%)
- Penstock (default 95%)
- Turbine (default 60-75%)
- Mechanical coupling (default 98%)
- Generator (default 90-95%)
- Power electronics (default 95%)

CALCULATIONS:
- Overall efficiency = product of all components
- Power at each stage
- Loss at each stage (%)
- Sensitivity: which component matters most?

VISUALIZATION:
- Waterfall chart showing power loss cascade
- Pie chart of loss distribution
- Sensitivity bar chart

Return complete Streamlit code.
        """
        
        return self._generate(prompt)
    
    def generate_site_assessment_tool(self):
        """Generate micro-hydro site assessment calculator"""
        prompt = """
Create a Streamlit app for micro-hydro site feasibility assessment.

INPUTS:
- Head (m): 1-500
- Flow rate (L/s): 5-5000
- Grid distance (km): 0-50
- Turbine efficiency (%): 50-85
- Generator efficiency (%): 85-95
- Availability factor (%): 70-95

CALCULATIONS:
1. Hydraulic power: P = ρ × g × Q × H (kW)
2. Electrical power: P_elec = P_hydro × η_turbine × η_generator
3. Annual energy: kWh/year = P_elec × availability × 8760
4. Revenue (@ $0.10/kWh): Annual energy × rate
5. CapEx estimate: $3000-5000/kW installed
6. Simple payback: CapEx / Annual revenue

OUTPUTS:
- Power potential (kW)
- Annual energy (MWh/year)
- Revenue projection ($/year)
- CapEx estimate ($)
- Payback period (years)
- Feasibility rating (Excellent/Good/Marginal/Poor)
- Comparison to benchmarks

VISUALIZATION:
- Gauge chart for power output
- Bar chart for revenue vs cost
- Feasibility scorecard

Return complete Streamlit code with proper formatting.
        """
        
        return self._generate(prompt)
    
    def generate_data_logger(self):
        """Generate test data logging script"""
        prompt = """
Create a Python script for logging desktop turbine test data.

REQUIREMENTS:
1. Read from serial port (Arduino or sensors)
2. Parse flow, pressure, RPM, voltage, current
3. Calculate efficiency in real-time
4. Save to CSV with timestamp
5. Display live metrics

INPUTS (from serial):
- Flow rate (L/s)
- Pressure/Head (m)
- RPM
- Voltage (V)
- Current (A)

CALCULATIONS:
- Hydraulic power: P_h = ρ × g × Q × H
- Electrical power: P_e = V × I
- Efficiency: η = P_e / P_h × 100%

OUTPUT:
- CSV file: timestamp, flow, head, rpm, voltage, current, P_h, P_e, efficiency
- Console display of live data
- Summary statistics

Include error handling, data validation, graceful exit.

Return complete Python script with argparse CLI.
        """
        
        return self._generate(prompt, max_tokens=6000)
    
    def generate_automation_script(self, task_description):
        """Generate custom automation script"""
        prompt = f"""
Create a Python automation script for this task:

{task_description}

REQUIREMENTS:
- Error handling (try/except)
- Logging (to file and console)
- Idempotent (safe to re-run)
- Configuration via .env or config file
- Progress indicators
- Summary report at end

Return complete, production-ready Python code.
        """
        
        return self._generate(prompt, max_tokens=6000)

# CLI Interface
if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    print(f"\n{'='*70}")
    print(f"🔧 TOOL BUILDER AGENT")
    print(f"{'='*70}\n")
    
    agent = ToolBuilderAgent()
    
    # Create Tools directory if not exists
    tools_dir = Path("Tools")
    tools_dir.mkdir(exist_ok=True)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "phi":
            print("🔧 Generating φ-Optimization Calculator...\n")
            code = agent.generate_phi_calculator()
            
            output_file = tools_dir / "phi_calculator.py"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(code)
            
            print(f"✅ Generated: {output_file}")
            print("\nTo run:")
            print(f"  streamlit run {output_file}")
        
        elif command == "efficiency":
            print("🔧 Generating Efficiency Cascade Calculator...\n")
            code = agent.generate_efficiency_calculator()
            
            output_file = tools_dir / "efficiency_calculator.py"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(code)
            
            print(f"✅ Generated: {output_file}")
            print("\nTo run:")
            print(f"  streamlit run {output_file}")
        
        elif command == "site":
            print("🔧 Generating Site Assessment Tool...\n")
            code = agent.generate_site_assessment_tool()
            
            output_file = tools_dir / "site_assessment.py"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(code)
            
            print(f"✅ Generated: {output_file}")
            print("\nTo run:")
            print(f"  streamlit run {output_file}")
        
        elif command == "logger":
            print("🔧 Generating Data Logger Script...\n")
            code = agent.generate_data_logger()
            
            output_file = tools_dir / "data_logger.py"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(code)
            
            print(f"✅ Generated: {output_file}")
            print("\nTo run:")
            print(f"  python {output_file} --port COM3 --output test_data.csv")
        
        elif command == "automate":
            if len(sys.argv) > 2:
                task = " ".join(sys.argv[2:])
                print(f"🔧 Generating automation for: {task}\n")
                code = agent.generate_automation_script(task)
                
                # Generate filename from task
                filename = task.lower().replace(" ", "_")[:30] + "_automation.py"
                output_file = tools_dir / filename
                
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(code)
                
                print(f"✅ Generated: {output_file}")
            else:
                print("❌ Usage: python tool_builder_agent.py automate <task_description>")
        
        elif command == "all":
            print("🔧 Generating ALL core tools...\n")
            
            # Generate all core tools
            tools = [
                ("phi", agent.generate_phi_calculator, "phi_calculator.py"),
                ("efficiency", agent.generate_efficiency_calculator, "efficiency_calculator.py"),
                ("site", agent.generate_site_assessment_tool, "site_assessment.py"),
                ("logger", agent.generate_data_logger, "data_logger.py")
            ]
            
            for name, generator, filename in tools:
                print(f"Generating {name}...")
                code = generator()
                output_file = tools_dir / filename
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"✅ {filename}")
            
            print(f"\n✅ All tools generated in {tools_dir}/")
            print("\nTo run any tool:")
            print("  streamlit run Tools/<filename>.py")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  phi        - Generate φ-optimization calculator")
            print("  efficiency - Generate efficiency cascade calculator")
            print("  site       - Generate site assessment tool")
            print("  logger     - Generate data logging script")
            print("  automate   - Generate custom automation")
            print("  all        - Generate all core tools")
    else:
        print("Available commands:")
        print("  phi        - Generate φ-optimization calculator")
        print("  efficiency - Generate efficiency cascade calculator")
        print("  site       - Generate site assessment tool")
        print("  logger     - Generate data logging script")
        print("  automate   - Generate custom automation script")
        print("  all        - Generate ALL core tools at once")
        print("\nExample:")
        print("  python tool_builder_agent.py all")
        print("  python tool_builder_agent.py phi")
