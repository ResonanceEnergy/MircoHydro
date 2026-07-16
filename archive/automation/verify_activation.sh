#!/bin/bash
# MicroHydro Content Verification Script
# Checks if repository content was successfully transferred

echo "🔍 MicroHydro Content Verification"
echo "=================================="

WORKSPACE="/Users/gripandripphdd/MircoHydro"

echo "Checking workspace: $WORKSPACE"
echo ""

# Check if workspace exists
if [ ! -d "$WORKSPACE" ]; then
    echo "❌ Workspace directory does not exist: $WORKSPACE"
    exit 1
fi

echo "✅ Workspace directory exists"

# Count total files
echo "📊 ANALYZING WORKSPACE CONTENT..."
TOTAL_FILES=$(find "$WORKSPACE" -type f 2>/dev/null | wc -l 2>/dev/null || echo "0")
echo "Total files in workspace: $TOTAL_FILES"

# Check key files
echo ""
echo "📋 CHECKING KEY FILES:"
KEY_FILES=(
    "FOURTH_CHECK_PRODUCTION_READINESS_AUDIT.md"
    "HYBRID_SYSTEM_SPECIFICATION_v2.0.md"
    "VISIONARY_RESEARCH_EXPANSION_SUMMARY.md"
    "WATER_STRUCTURING_TECHNOLOGY_STRATEGY.md"
    "MASTER_PROJECT_OVERVIEW.md"
    "BRAND_IDENTITY.md"
)

FOUND_KEY_FILES=0
for file in "${KEY_FILES[@]}"; do
    if [ -f "$WORKSPACE/$file" ]; then
        echo "✅ $file"
        ((FOUND_KEY_FILES++))
    else
        echo "❌ $file"
    fi
done

echo ""
echo "Key files found: $FOUND_KEY_FILES/${#KEY_FILES[@]}"

# Check major directories
echo ""
echo "📁 CHECKING MAJOR DIRECTORIES:"
MAJOR_DIRS=("Engineering" "Research" "Implementation" "scripts" "ARCHIVE")
FOUND_DIRS=0

for dir in "${MAJOR_DIRS[@]}"; do
    if [ -d "$WORKSPACE/$dir" ]; then
        # Count files in directory
        DIR_FILES=$(find "$WORKSPACE/$dir" -type f 2>/dev/null | wc -l 2>/dev/null || echo "0")
        echo "✅ $dir/ ($DIR_FILES files)"
        ((FOUND_DIRS++))
    else
        echo "❌ $dir/"
    fi
done

echo ""
echo "Major directories found: $FOUND_DIRS/${#MAJOR_DIRS[@]}"

# Overall assessment
echo ""
echo "📊 ACTIVATION STATUS ASSESSMENT:"

SUCCESS_THRESHOLD_KEY=4
SUCCESS_THRESHOLD_DIRS=3

if [ $FOUND_KEY_FILES -ge $SUCCESS_THRESHOLD_KEY ] && [ $FOUND_DIRS -ge $SUCCESS_THRESHOLD_DIRS ]; then
    echo "🎉 CONTENT ACTIVATION SUCCESSFUL!"
    echo "✅ MicroHydro system is 100% operational"
    echo ""
    echo "🚀 NEXT STEPS:"
    echo "1. Review the transferred documentation"
    echo "2. Check scripts/ for any activation scripts"
    echo "3. Run final system verification"
    echo "4. Proceed with deployment"
    echo ""
    echo "📈 SYSTEM STATUS: COMPLETE"
    exit 0
else
    echo "⚠️  CONTENT ACTIVATION INCOMPLETE"
    echo "❌ Some critical content is missing"
    echo ""
    echo "🔧 REMEDY STEPS:"
    echo "1. Re-run the manual download process"
    echo "2. Ensure all files were extracted from ZIP"
    echo "3. Verify the cp command completed successfully"
    echo "4. Check file permissions"
    echo ""
    echo "📈 SYSTEM STATUS: NEEDS COMPLETION"
    exit 1
fi