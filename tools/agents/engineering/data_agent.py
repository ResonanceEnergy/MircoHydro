"""
Data Analysis Agent - Statistical analysis and visualization
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()

class DataAnalysisAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Data Analysis Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Data Analysis Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def analyze_test_data(self, data_file):
        """Analyze test data and provide statistical insights"""
        try:
            df = pd.read_csv(data_file)
            summary = df.describe().to_string()
            
            prompt = f"""
Analyze this turbine test data:

{summary}

Provide:
## 📊 STATISTICAL SUMMARY
[Key metrics: mean, std dev, min/max]

## 🎯 EFFICIENCY ANALYSIS
[Compare treatments, calculate improvements]

## 📈 SIGNIFICANCE TESTING
[Is the improvement statistically significant? p-value?]

## 💡 INSIGHTS
[What does this data tell us about φ-optimization?]

## ⚠️ DATA QUALITY
[Any outliers, issues, or anomalies?]
            """
            
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
                max_tokens=2000
            )
            return completion.choices[0].message.content
        except FileNotFoundError:
            return f"❌ File not found: {data_file}"
        except Exception as e:
            return f"❌ Error: {e}"
    
    def generate_visualization_code(self, data_type):
        """Generate Python visualization code"""
        prompt = f"""
Generate Python code using matplotlib/seaborn to visualize {data_type}.

Include:
- Efficiency comparison plots
- Statistical distributions
- Box plots for outlier detection
- Regression analysis if applicable

Return complete runnable Python code.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def calculate_sample_size(self, effect_size, power=0.8, alpha=0.05):
        """Calculate required sample size for statistical power"""
        prompt = f"""
Calculate required sample size for:
- Expected effect size: {effect_size}% improvement
- Statistical power: {power}
- Significance level: {alpha}

Use power analysis for t-test. Provide:
- Minimum sample size per group
- Total tests required
- Justification
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=1000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"📊 DATA ANALYSIS AGENT")
    print(f"{'='*70}\n")
    
    agent = DataAnalysisAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "analyze":
            if len(sys.argv) > 2:
                print(agent.analyze_test_data(sys.argv[2]))
            else:
                print("❌ Usage: python data_agent.py analyze <csv_file>")
        
        elif command == "visualize":
            data_type = sys.argv[2] if len(sys.argv) > 2 else "turbine efficiency"
            print(agent.generate_visualization_code(data_type))
        
        elif command == "sample-size":
            effect = float(sys.argv[2]) if len(sys.argv) > 2 else 8.0
            print(agent.calculate_sample_size(effect))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: analyze <csv> | visualize <type> | sample-size <effect>")
    else:
        print("Commands:")
        print("  analyze <file.csv>     - Statistical analysis")
        print("  visualize <data_type>  - Generate plot code")
        print("  sample-size <effect%>  - Calculate sample size")
