#!/bin/bash
# MicroHydro Automation Runner
# Executes the master automation orchestrator

echo "🚀 MicroHydro Master Automation Orchestrator"
echo "==========================================="

WORKSPACE="/Users/gripandripphdd/MircoHydro"
SCRIPT="$WORKSPACE/master_automation_orchestrator.py"

# Try different Python executables
PYTHON_CMDS=("python3" "python" "/usr/bin/python3" "/usr/local/bin/python3" "/opt/homebrew/bin/python3")

for cmd in "${PYTHON_CMDS[@]}"; do
    if command -v "$cmd" &> /dev/null; then
        echo "✅ Found Python: $cmd"
        echo "🔧 Running automation suite..."
        echo ""

        if [ "$1" = "--component" ] && [ -n "$2" ]; then
            "$cmd" "$SCRIPT" --component "$2"
        else
            "$cmd" "$SCRIPT"
        fi

        exit $?
    fi
done

echo "❌ No Python interpreter found"
echo ""
echo "📋 MANUAL EXECUTION INSTRUCTIONS:"
echo "1. Ensure Python 3 is installed on your system"
echo "2. Run: python3 $SCRIPT"
echo "3. Or: python3 $SCRIPT --component [component_name]"
echo ""
echo "Available components:"
echo "  - consolidation (workspace consolidation)"
echo "  - validation (repository validation)"
echo "  - import (data import automation)"
echo "  - build (build automation)"
echo "  - release (release packaging)"
echo "  - ai-agents (AI agent deployment)"
echo "  - toolkit (ready-execute toolkit)"
echo "  - all (complete automation suite)"
echo ""
echo "Example: python3 $SCRIPT --component validation"

exit 1