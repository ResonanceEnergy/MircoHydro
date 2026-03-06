# filepath: automate_all.py

import subprocess
import os
import sys
import time
from datetime import datetime

# --- CONFIGURATION ---
AGENT_COMMANDS = [
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/operations_dashboard.py monitor "all"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/operations_dashboard.py kpi "energy_output"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/operations_dashboard.py alerts "last24h"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/operations_dashboard.py report "weekly"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/process_automation.py workflow "site startup"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/process_automation.py automate "turbine check"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/process_automation.py efficiency "all"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/process_automation.py recommend "maintenance"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/quality_control.py standards "ISO9001"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/quality_control.py inspection "site_12"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/quality_control.py defects "last_month"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/quality_control.py improvement "all"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/maintenance_management.py schedule "turbine_1" "2026-02-01" "oil change"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/maintenance_management.py track "turbine_1"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/maintenance_management.py report "turbine_1" "vibration detected"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/resource_allocation.py plan "expansion" "crew, excavator" "Q2 2026"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/resource_allocation.py optimize "current allocation summary"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/resource_allocation.py track "excavator"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/incident_response.py detect "unexpected shutdown at site_7"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/incident_response.py coordinate "INC123" "crew, tools"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/incident_response.py report "INC123" "resolved, root cause: sensor failure"',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/operations_dashboard.py -h',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/process_automation.py -h',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/quality_control.py -h',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/maintenance_management.py -h',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/resource_allocation.py -h',
    'C:/MircoHydro/.venv/Scripts/python.exe Operations/Agents/incident_response.py -h'
]

EURA_COMMANDS = [
    'C:/MircoHydro/.venv/Scripts/python.exe research/EURA/eura/cli/__main__.py prereg_validate research/EURA/prereg/HC-01/prereg.json',
    'C:/MircoHydro/.venv/Scripts/python.exe research/EURA/eura/cli/__main__.py run_metrics',
    'C:/MircoHydro/.venv/Scripts/python.exe research/EURA/eura/cli/__main__.py build_paper HC-01 --fmt html',
    'C:/MircoHydro/.venv/Scripts/python.exe research/EURA/design_matrix_monitor.py'
]

MONITOR_COMMANDS = [
    'C:/MircoHydro/.venv/Scripts/python.exe research/microhydro_matrix_monitor.py',
    'C:/MircoHydro/.venv/Scripts/python.exe research/microhydro_site_optimization_engine.py'
]

LOG_DIR = "automation_logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def log_result(cmd, code, out, err):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n## Command: {cmd}\nExit Code: {code}\n")
        f.write(f"Stdout:\n{out}\n")
        if err:
            f.write(f"Stderr:\n{err}\n")
        f.write("---\n")

def main():
    while True:
        # 1. Run all agent commands
        for cmd in AGENT_COMMANDS:
            code, out, err = run_command(cmd)
            log_result(cmd, code, out, err)

        # 2. Run EURA research division commands
        for cmd in EURA_COMMANDS:
            code, out, err = run_command(cmd)
            log_result(cmd, code, out, err)

        # 3. Run matrix monitor commands
        for cmd in MONITOR_COMMANDS:
            code, out, err = run_command(cmd)
            log_result(cmd, code, out, err)

        print(f"Automation cycle complete. See log: {LOG_FILE}")
        time.sleep(3600)  # Run every hour

if __name__ == "__main__":
    main()