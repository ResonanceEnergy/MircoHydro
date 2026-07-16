#!/bin/bash
# MicroHydro Automation Execution Script
# Run this script to execute the complete automation system

echo "🚀 MICROHYDRO COMPLETE AUTOMATION SYSTEM"
echo "========================================"
echo ""

# Check if we're in the right directory
if [ ! -f "complete_automation_system.py" ]; then
    echo "❌ Error: complete_automation_system.py not found"
    echo "Please run this script from the MicroHydro root directory"
    exit 1
fi

echo "📍 Current directory: $(pwd)"
echo "🔍 Checking Python availability..."

# Try different Python commands
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✅ Found python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo "✅ Found python"
else
    echo "❌ Python not found. Please install Python 3.6+ to run automation"
    echo ""
    echo "Manual execution instructions:"
    echo "1. Install Python 3.6 or higher"
    echo "2. Run: python3 complete_automation_system.py"
    echo "3. Or: python complete_automation_system.py"
    exit 1
fi

echo ""
echo "🎯 EXECUTING AUTOMATION SYSTEM..."
echo "=================================="

# Execute the automation system
$PYTHON_CMD complete_automation_system.py

# Check exit code
EXIT_CODE=$?
echo ""
echo "=================================="

if [ $EXIT_CODE -eq 0 ]; then
    echo "🎉 AUTOMATION COMPLETED SUCCESSFULLY!"
    echo ""
    echo "📁 Generated files:"
    ls -la automation_log_*.txt automation_report_*.json ai_agent_manifest_*.json 2>/dev/null || echo "No automation output files found yet"
    echo ""
    echo "📊 Next steps:"
    echo "1. Review automation_log_*.txt for execution details"
    echo "2. Check automation_report_*.json for system status"
    echo "3. Review ai_agent_manifest_*.json for AI deployment"
    echo "4. Execute Phase 1-4 procedures from Ready-Execute Toolkit"
else
    echo "⚠️  AUTOMATION COMPLETED WITH ISSUES (Exit code: $EXIT_CODE)"
    echo ""
    echo "📋 Troubleshooting:"
    echo "1. Check automation_log_*.txt for error details"
    echo "2. Verify all required files are present"
    echo "3. Ensure Python dependencies are installed"
    echo "4. Review MANUAL_EXECUTION_GUIDE.md for manual steps"
fi

echo ""
echo "📖 For detailed information, see:"
echo "- AUTOMATION_README.md (system documentation)"
echo "- MANUAL_EXECUTION_GUIDE.md (step-by-step guide)"
echo "- READY_TO_EXECUTE_TOOLKIT.md (operational procedures)"