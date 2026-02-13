#!/bin/bash

# MicroHydro Content Activation Script
# Identifies empty files and provides systematic copying procedure

echo "🔍 MICROHYDRO CONTENT ACTIVATION PROCEDURE"
echo "=========================================="
echo ""

# Count empty files
EMPTY_COUNT=$(find /Users/gripandripphdd/MircoHydro -type f -empty | wc -l)
echo "📊 Found $EMPTY_COUNT empty files requiring content activation"
echo ""

# Create activation manifest
echo "📝 Creating activation manifest..."
find /Users/gripandripphdd/MircoHydro -type f -empty | sort > /tmp/empty_files_manifest.txt

echo "📂 Empty files by directory:"
echo ""

# Group by directory and count
find /Users/gripandripphdd/MircoHydro -type f -empty | \
    sed 's|/[^/]*$||' | \
    sort | \
    uniq -c | \
    sort -nr | \
    head -20 | \
    while read count dir; do
        echo "  $count files in: $dir"
    done

echo ""
echo "🚀 ACTIVATION PROCEDURE:"
echo "========================"
echo ""
echo "1. 📋 Review the manifest: /tmp/empty_files_manifest.txt"
echo ""
echo "2. 🔄 For each empty file, locate the corresponding source in OneDrive"
echo ""
echo "3. 📄 Copy content from source to empty file using:"
echo "   cp '/path/to/source/file' '/path/to/empty/file'"
echo ""
echo "4. ✅ Verify copy: ls -la '/path/to/file' (should show size > 0)"
echo ""
echo "5. 🔁 Repeat for all 1,570 files"
echo ""
echo "💡 TIP: Start with high-priority directories (Research, Engineering)"
echo ""
echo "🎯 TARGET: Achieve 100% operational readiness"