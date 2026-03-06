# Operations Division Agent Activation & Validation Plan

## 1. Prerequisites
- Ensure Python 3.14.2+ and all dependencies are installed (`groq`, `python-dotenv`, `argparse`).
- Activate the virtual environment:  
  `& C:/MircoHydro/.venv/Scripts/Activate.ps1`
- Confirm `.env` file with valid `GROQ_API_KEY` is present in `Operations/`.

## 2. Agent CLI Usage Examples

### Operations Dashboard
- Monitor:  
  `python operations_dashboard.py monitor "all"`
- KPI Report:  
  `python operations_dashboard.py kpi "energy_output"`
- Alerts:  
  `python operations_dashboard.py alerts "last24h"`
- Report:  
  `python operations_dashboard.py report "weekly"`

### Process Automation
- Workflow:  
  `python process_automation.py workflow "site startup"`
- Automate:  
  `python process_automation.py automate "turbine check"`
- Efficiency:  
  `python process_automation.py efficiency "all"`
- Recommend:  
  `python process_automation.py recommend "maintenance"`

### Quality Control
- Standards:  
  `python quality_control.py standards "ISO9001"`
- Inspection:  
  `python quality_control.py inspection "site_12"`
- Defects:  
  `python quality_control.py defects "last_month"`
- Improvement:  
  `python quality_control.py improvement "all"`

### Maintenance Management
- Schedule:  
  `python maintenance_management.py schedule "turbine_1" "2026-02-01" "oil change"`
- Track:  
  `python maintenance_management.py track "turbine_1"`
- Report:  
  `python maintenance_management.py report "turbine_1" "vibration detected"`

### Resource Allocation
- Plan:  
  `python resource_allocation.py plan "expansion" "crew, excavator" "Q2 2026"`
- Optimize:  
  `python resource_allocation.py optimize "current allocation summary"`
- Track:  
  `python resource_allocation.py track "excavator"`

### Incident Response
- Detect:  
  `python incident_response.py detect "unexpected shutdown at site_7"`
- Coordinate:  
  `python incident_response.py coordinate "INC123" "crew, tools"`
- Report:  
  `python incident_response.py report "INC123" "resolved, root cause: sensor failure"`

## 3. Validation Steps
- Run each example command above and verify:
  - The agent responds with a detailed, relevant output.
  - No errors or missing dependencies.
  - Each agent’s CLI help (`-h`) displays all commands and options.
- Document any issues or improvements needed.

## 4. Next Steps
- Integrate agents into workflow scripts or dashboards as needed.
- Schedule regular reviews and updates for prompt templates and logic.
