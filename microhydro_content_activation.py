#!/usr/bin/env python3
"""
MicroHydro Repository Content Activation Script
Automates downloading and transferring complete repository content from GitHub
"""

import os
import sys
import zipfile
import shutil
import urllib.request
from pathlib import Path

def download_repository():
    """Download the complete MircoHydro repository from GitHub"""
    print("🚀 Starting MicroHydro Repository Content Activation...")

    # Repository details
    repo_url = "https://github.com/ResonanceEnergy/MircoHydro/archive/refs/heads/main.zip"
    download_path = "/tmp/mircohydro_repo.zip"
    extract_path = "/tmp/MircoHydro-main"
    target_path = "/Users/gripandripphdd/MircoHydro"

    try:
        # Step 1: Download the repository
        print(f"📥 Downloading repository from {repo_url}...")
        urllib.request.urlretrieve(repo_url, download_path)
        print(f"✅ Downloaded to {download_path}")

        # Step 2: Extract the ZIP file
        print(f"📦 Extracting to {extract_path}...")
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall("/tmp/")
        print(f"✅ Extracted repository contents")

        # Step 3: Analyze repository contents
        if os.path.exists(extract_path):
            total_files = sum([len(files) for r, d, files in os.walk(extract_path)])
            print(f"📊 Repository contains {total_files} files")

            # List main directories
            main_dirs = [d for d in os.listdir(extract_path) if os.path.isdir(os.path.join(extract_path, d))]
            print(f"📁 Main directories: {', '.join(main_dirs[:10])}{'...' if len(main_dirs) > 10 else ''}")

        # Step 4: Transfer contents to workspace
        print(f"🔄 Transferring contents to {target_path}...")

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        transferred_count = 0
        for root, dirs, files in os.walk(extract_path):
            # Calculate relative path
            rel_path = os.path.relpath(root, extract_path)
            target_dir = os.path.join(target_path, rel_path) if rel_path != '.' else target_path

            # Create directories
            for dir_name in dirs:
                target_subdir = os.path.join(target_dir, dir_name)
                os.makedirs(target_subdir, exist_ok=True)

            # Copy files
            for file_name in files:
                source_file = os.path.join(root, file_name)
                target_file = os.path.join(target_dir, file_name)

                # Skip if target exists and is newer
                if os.path.exists(target_file):
                    source_mtime = os.path.getmtime(source_file)
                    target_mtime = os.path.getmtime(target_file)
                    if target_mtime >= source_mtime:
                        continue

                shutil.copy2(source_file, target_file)
                transferred_count += 1

        print(f"✅ Transferred {transferred_count} files")

        # Step 5: Verification
        print("🔍 Verifying transfer...")
        final_count = sum([len(files) for r, d, files in os.walk(target_path)])
        print(f"📊 Final workspace contains {final_count} files")

        # Step 6: Cleanup
        print("🧹 Cleaning up temporary files...")
        if os.path.exists(download_path):
            os.remove(download_path)
        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)

        print("🎉 CONTENT ACTIVATION COMPLETE!")
        print(f"✅ Repository successfully integrated into {target_path}")
        print(f"📈 Total files now available: {final_count}")

        return True

    except Exception as e:
        print(f"❌ Error during content activation: {str(e)}")
        return False

def analyze_key_content():
    """Analyze and report on key content areas"""
    workspace_path = "/Users/gripandripphdd/MircoHydro"

    print("\n📋 KEY CONTENT ANALYSIS:")

    key_files = [
        "FOURTH_CHECK_PRODUCTION_READINESS_AUDIT.md",
        "HYBRID_SYSTEM_SPECIFICATION_v2.0.md",
        "VISIONARY_RESEARCH_EXPANSION_SUMMARY.md",
        "WATER_STRUCTURING_TECHNOLOGY_STRATEGY.md",
        "MASTER_PROJECT_OVERVIEW.md",
        "BRAND_IDENTITY.md"
    ]

    found_count = 0
    for file in key_files:
        if os.path.exists(os.path.join(workspace_path, file)):
            found_count += 1
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")

    print(f"\n📊 Key files status: {found_count}/{len(key_files)} found")

    # Check major directories
    major_dirs = ["Engineering", "Research", "Implementation", "scripts", "ARCHIVE"]
    dir_count = 0
    for dir_name in major_dirs:
        if os.path.exists(os.path.join(workspace_path, dir_name)):
            dir_count += 1
            # Count files in directory
            file_count = sum([len(files) for r, d, files in os.walk(os.path.join(workspace_path, dir_name))])
            print(f"✅ {dir_name}/ ({file_count} files)")
        else:
            print(f"❌ {dir_name}/")

    print(f"\n📊 Major directories status: {dir_count}/{len(major_dirs)} found")

if __name__ == "__main__":
    print("🔧 MicroHydro Content Activation Script")
    print("=" * 50)

    success = download_repository()

    if success:
        analyze_key_content()
        print("\n🎯 NEXT STEPS:")
        print("1. Review the transferred content")
        print("2. Run any activation scripts in scripts/")
        print("3. Verify integration with existing files")
        print("4. Proceed with final production readiness checks")
    else:
        print("\n❌ Content activation failed. Please check:")
        print("- Network connectivity")
        print("- File permissions")
        print("- Available disk space")
        print("- Try manual download as alternative")

    sys.exit(0 if success else 1)
<parameter name="filePath">/Users/gripandripphdd/MircoHydro/microhydro_content_activation.py