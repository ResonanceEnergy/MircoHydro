#!/bin/bash
# MicroHydro Complete Automation Launcher
# Automatically finds Python and runs the complete automation system

echo "🚀 MicroHydro Complete Automation System Launcher"
echo "================================================="

WORKSPACE="/Users/gripandripphdd/MircoHydro"
SCRIPT="$WORKSPACE/complete_automation_system.py"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Searching for Python interpreter...${NC}"

# Try different Python executables in order of preference
PYTHON_CMDS=(
    "python3"
    "python"
    "/usr/bin/python3"
    "/usr/local/bin/python3"
    "/opt/homebrew/bin/python3"
    "/Library/Frameworks/Python.framework/Versions/Current/bin/python3"
)

PYTHON_FOUND=""
for cmd in "${PYTHON_CMDS[@]}"; do
    if command -v "$cmd" &> /dev/null; then
        PYTHON_FOUND="$cmd"
        echo -e "${GREEN}✅ Found Python: $cmd${NC}"
        break
    fi
done

if [ -z "$PYTHON_FOUND" ]; then
    echo -e "${RED}❌ No Python interpreter found${NC}"
    echo ""
    echo -e "${YELLOW}📋 MANUAL EXECUTION REQUIRED:${NC}"
    echo "Please run the automation system manually:"
    echo ""
    echo "1. Ensure Python 3.6+ is installed"
    echo "2. Run: python3 $SCRIPT"
    echo ""
    echo "Or try these common Python locations:"
    for cmd in "${PYTHON_CMDS[@]}"; do
        echo "   $cmd $SCRIPT"
    done
    echo ""
    echo -e "${BLUE}💡 RECOMMENDED: Install Python 3 from https://python.org${NC}"
    exit 1
fi

# Check if script exists
if [ ! -f "$SCRIPT" ]; then
    echo -e "${RED}❌ Automation script not found: $SCRIPT${NC}"
    exit 1
fi

echo -e "${BLUE}🔧 Starting complete automation suite...${NC}"
echo ""

# Run the automation system
"$PYTHON_FOUND" "$SCRIPT" "$WORKSPACE"

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}🎉 AUTOMATION COMPLETED SUCCESSFULLY!${NC}"
    echo -e "${GREEN}📊 Check the generated log and report files${NC}"
else
    echo -e "${RED}❌ AUTOMATION COMPLETED WITH ISSUES${NC}"
    echo -e "${YELLOW}📋 Check the log file for details${NC}"
fi

echo ""
echo -e "${BLUE}📁 Generated files:${NC}"
echo "   - automation_log_*.txt (execution log)"
echo "   - automation_report_*.json (detailed results)"
echo "   - ai_agent_manifest_*.json (AI deployment plan)"

exit $EXIT_CODE