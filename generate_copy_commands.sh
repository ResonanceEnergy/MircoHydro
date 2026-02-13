#!/bin/bash

# MicroHydro Batch Copy Generator
# Generates copy commands for content activation

echo "🔄 MICROHYDRO BATCH COPY COMMAND GENERATOR"
echo "=========================================="
echo ""

# Define source and destination base paths
SOURCE_BASE="/path/to/OneDrive/MicroHydro_Source"  # User needs to set this
DEST_BASE="/Users/gripandripphdd/MircoHydro"

echo "⚠️  IMPORTANT: Set your OneDrive source path in this script!"
echo "   Edit SOURCE_BASE variable to point to your OneDrive folder"
echo ""
echo "📋 Generated copy commands:"
echo ""

# Generate copy commands for each empty file
while IFS= read -r empty_file; do
    # Remove the destination base to get relative path
    relative_path="${empty_file#$DEST_BASE/}"

    # Construct source path
    source_file="$SOURCE_BASE/$relative_path"

    echo "cp '$source_file' '$empty_file'"
done < /tmp/empty_files_manifest.txt

echo ""
echo "🚀 EXECUTION INSTRUCTIONS:"
echo "========================="
echo ""
echo "1. 📝 Edit this script: set SOURCE_BASE to your OneDrive path"
echo ""
echo "2. 🔍 Verify source files exist in OneDrive"
echo ""
echo "3. ▶️  Run the generated cp commands (consider running in batches)"
echo ""
echo "4. ✅ Verify: find $DEST_BASE -type f -empty | wc -l (should be 0)"
echo ""
echo "💡 TIP: Test with a few files first, then batch the rest"