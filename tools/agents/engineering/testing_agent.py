"""
Testing/QA Agent - Quality assurance and validation
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv

load_dotenv()

class TestingAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Testing/QA Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Testing Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def generate_test_plan(self, system_name):
        """Create comprehensive test plan"""
        prompt = f"""
Generate test plan for: {system_name}

Include:
## TEST OBJECTIVES
[What are we validating?]

## TEST MATRIX
[All test cases with conditions]

## ACCEPTANCE CRITERIA
[Pass/fail thresholds]

## TEST PROCEDURES
[Step-by-step instructions]

## DATA COLLECTION
[What to measure, how to record]

## RISK MITIGATION
[Safety, equipment protection]

## TIMELINE
[Test schedule]

Format as professional test plan.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def validate_test_data(self, data_description):
        """Check data quality and validity"""
        prompt = f"""
Validate this test data:

{data_description}

Check for:
## DATA QUALITY ISSUES
- Missing values
- Outliers
- Measurement errors
- Calibration drift

## STATISTICAL VALIDITY
- Sample size adequate?
- Distribution normal?
- Variance homogeneous?

## TEST INTEGRITY
- Protocol followed correctly?
- Controls valid?
- Environmental factors stable?

## RECOMMENDATIONS
[Data usable? Retest needed?]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def design_calibration_procedure(self, equipment_list):
        """Create calibration procedures"""
        prompt = f"""
Create calibration procedure for:

{equipment_list}

Include:
## CALIBRATION STANDARDS
[Reference materials/equipment needed]

## PROCEDURE
[Step-by-step calibration process]

## FREQUENCY
[How often to calibrate]

## ACCEPTANCE CRITERIA
[When is calibration valid?]

## RECORDS
[Documentation requirements]
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def create_failure_analysis(self, failure_description):
        """Root cause analysis for test failures"""
        prompt = f"""
Analyze test failure:

{failure_description}

Provide:
## FAILURE DESCRIPTION
[What went wrong?]

## ROOT CAUSE ANALYSIS
[5 Whys, Fishbone diagram logic]

## CONTRIBUTING FACTORS
[Environmental, equipment, human factors]

## CORRECTIVE ACTIONS
[Immediate fixes]

## PREVENTIVE MEASURES
[Long-term solutions]

## RETEST PLAN
[How to verify fix?]
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
    print(f"🧪 TESTING/QA AGENT")
    print(f"{'='*70}\n")
    
    agent = TestingAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "test-plan":
            system = sys.argv[2] if len(sys.argv) > 2 else "φ-Turbine Desktop Test Rig"
            print(agent.generate_test_plan(system))
        
        elif command == "validate":
            data = sys.argv[2] if len(sys.argv) > 2 else "60 tests, efficiency range 45-58%, 3 outliers"
            print(agent.validate_test_data(data))
        
        elif command == "calibration":
            equipment = sys.argv[2] if len(sys.argv) > 2 else "Flow meter, pressure sensor, multimeter"
            print(agent.design_calibration_procedure(equipment))
        
        elif command == "failure":
            description = sys.argv[2] if len(sys.argv) > 2 else "Test #23 failed: pump stopped, voltage dropped to zero"
            print(agent.create_failure_analysis(description))
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: test-plan | validate | calibration | failure")
    else:
        print("Commands:")
        print("  test-plan '<system>'     - Generate test plan")
        print("  validate '<data>'        - Validate test data")
        print("  calibration '<equipment>' - Calibration procedure")
        print("  failure '<description>'  - Failure analysis")
