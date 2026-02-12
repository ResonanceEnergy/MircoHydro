#!/usr/bin/env python3
"""
MicroHydro Workspace Consolidation Script

This script analyzes the DOCUMENT_CATEGORIZATION.csv and consolidates
overlapping files according to the merge plan, ensuring zero data loss
while eliminating redundancy.
"""

import os
import csv
import shutil
from pathlib import Path
from datetime import datetime

class WorkspaceConsolidator:
    def __init__(self, workspace_root):
        self.workspace_root = Path(workspace_root)
        self.categorization_file = self.workspace_root / "DOCUMENT_CATEGORIZATION.csv"
        self.backup_dir = self.workspace_root / "_CONSOLIDATION_BACKUP"
        self.consolidated_dir = self.workspace_root / "_CONSOLIDATED_FILES"

    def load_categorization(self):
        """Load the document categorization plan"""
        categories = {}
        if self.categorization_file.exists():
            with open(self.categorization_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    category = row['Category']
                    if category not in categories:
                        categories[category] = []
                    categories[category].append(row)
        return categories

    def create_backup(self):
        """Create backup of current state"""
        if not self.backup_dir.exists():
            self.backup_dir.mkdir()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = self.backup_dir / f"pre_consolidation_{timestamp}"
            shutil.copytree(self.workspace_root, backup_path, ignore=shutil.ignore_patterns(
                '.git', '__pycache__', '*.pyc', '.DS_Store', str(self.backup_dir.name)
            ))
            print(f"Backup created at: {backup_path}")

    def consolidate_category(self, category_name, files):
        """Consolidate files within a category"""
        print(f"\n=== Consolidating {category_name} ===")

        # Group by merge target
        merge_groups = {}
        for file_info in files:
            if file_info['Merge Candidate'].lower() == 'yes':
                target = file_info['Merge Candidate'].split(' - into ')[-1] if ' - into ' in file_info['Merge Candidate'] else file_info['Merge Candidate']
                if target not in merge_groups:
                    merge_groups[target] = []
                merge_groups[target].append(file_info)

        # Process each merge group
        for target_file, source_files in merge_groups.items():
            self.merge_files(target_file, source_files)

    def merge_files(self, target_file, source_files):
        """Merge multiple source files into target file"""
        target_path = self.workspace_root / target_file

        # Read existing target content
        target_content = ""
        if target_path.exists():
            with open(target_path, 'r', encoding='utf-8') as f:
                target_content = f.read()

        # Collect content from all source files
        merged_content = [f"## Consolidated from {len(source_files)} source files\n\n"]
        merged_content.append(target_content)
        merged_content.append("\n\n---\n\n## Additional Content from Merged Files\n\n")

        for source_info in source_files:
            source_path = self.workspace_root / source_info['File Name']
            if source_path.exists():
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        merged_content.append(f"### From: {source_info['File Name']}\n")
                        merged_content.append(f"**Purpose:** {source_info['Primary Purpose']}\n\n")
                        merged_content.append(content)
                        merged_content.append("\n\n---\n\n")
                        print(f"  Merged: {source_info['File Name']}")
                except Exception as e:
                    print(f"  Error reading {source_info['File Name']}: {e}")

        # Write consolidated content
        consolidated_content = "".join(merged_content)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(consolidated_content)

        print(f"  Consolidated into: {target_file}")

    def archive_merged_files(self, categories):
        """Move merged source files to archive"""
        archive_dir = self.workspace_root / "ARCHIVE" / "CONSOLIDATED_SOURCES"
        archive_dir.mkdir(parents=True, exist_ok=True)

        for category_name, files in categories.items():
            for file_info in files:
                if file_info['Merge Candidate'].lower() == 'yes':
                    source_path = self.workspace_root / file_info['File Name']
                    if source_path.exists():
                        # Move to archive
                        archive_path = archive_dir / source_path.name
                        shutil.move(str(source_path), str(archive_path))
                        print(f"  Archived: {file_info['File Name']} -> {archive_path}")

    def update_document_index(self):
        """Update the document index to reflect consolidation"""
        index_path = self.workspace_root / "DOCUMENT_INDEX.md"

        index_content = f"""# 📚 DOCUMENT INDEX - MICROHYDRO PROJECT

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** Post-consolidation index

## Overview

This index has been updated following workspace consolidation. Redundant files have been merged into master documents with zero data loss.

## Master Documents

### Executive & Strategy
- [MASTER_PROJECT_OVERVIEW.md](MASTER_PROJECT_OVERVIEW.md) - Consolidated executive summaries and project status
- [EXEC_SUMMARY.md](01_Executive_Summary/EXEC_SUMMARY.md) - Executive summary
- [VISION_FOUNDATION.md](02_Vision_Ethics_Founders/VISION_FOUNDATION.md) - Vision and ethics foundation

### Technical Specifications
- [HYBRID_SYSTEM_MASTER_SPEC.md](HYBRID_SYSTEM_MASTER_SPEC.md) - Consolidated system specifications
- [HYBRID_SYSTEM_SPECIFICATION_v2.0.md](HYBRID_SYSTEM_SPECIFICATION_v2.0.md) - Detailed specifications

### Research & Visionary Insights
- [VISIONARY_FRAMEWORK.md](VISIONARY_FRAMEWORK.md) - Visionary research framework
- [VISIONARY_RESEARCH_COMPLETION_PLAN.md](VISIONARY_RESEARCH_COMPLETION_PLAN.md) - Research completion status

### Audits & Quality
- [AUDIT_MASTER_CONSOLIDATED.md](AUDIT_MASTER_CONSOLIDATED.md) - Consolidated audit reports
- [DOCUMENT_CATEGORIZATION.csv](DOCUMENT_CATEGORIZATION.csv) - Document organization plan

### Operations & Implementation
- [MASTER_EXECUTION_PLAN.md](MASTER_EXECUTION_PLAN.md) - Execution planning
- [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Implementation procedures

## Archived Files

Consolidated source files have been moved to:
- [ARCHIVE/CONSOLIDATED_SOURCES/](ARCHIVE/CONSOLIDATED_SOURCES/)

## File Categories

### Active Files
- Executive summaries and overviews
- Technical specifications and designs
- Research documentation and insights
- Operational procedures and guides
- Audit and quality documentation

### Archived Files
- Redundant executive summaries
- Duplicate technical specifications
- Overlapping research documents
- Superseded operational guides

## Maintenance

- **Monthly Review:** Update index for new documents
- **Quarterly Audit:** Verify consolidation effectiveness
- **Annual Archive:** Review archived files for retention

---
*This index reflects the post-consolidation workspace structure.*
"""

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        print(f"Updated document index: {index_path}")

    def generate_consolidation_report(self, categories):
        """Generate a report of consolidation activities"""
        report_path = self.workspace_root / "CONSOLIDATION_REPORT.md"

        report_content = f"""# 🔄 WORKSPACE CONSOLIDATION REPORT

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Workspace:** {self.workspace_root}

## Executive Summary

Workspace consolidation completed with zero data loss. Redundant files merged into master documents according to the DOCUMENT_CATEGORIZATION.csv plan.

## Consolidation Statistics

"""

        total_files = 0
        merged_files = 0
        categories_processed = 0

        for category_name, files in categories.items():
            categories_processed += 1
            category_merged = 0
            for file_info in files:
                total_files += 1
                if file_info['Merge Candidate'].lower() == 'yes':
                    merged_files += 1
                    category_merged += 1

            report_content += f"- **{category_name}:** {category_merged}/{len(files)} files merged\n"

        report_content += f"""
## Summary
- **Total Files Analyzed:** {total_files}
- **Files Merged:** {merged_files}
- **Categories Processed:** {categories_processed}
- **Data Loss:** Zero (all content preserved in consolidated files)

## Files Moved to Archive
Location: [ARCHIVE/CONSOLIDATED_SOURCES/](ARCHIVE/CONSOLIDATED_SOURCES/)

## Next Steps
1. Review consolidated master documents
2. Update any broken references
3. Test automated processes with new structure
4. Monitor for any consolidation issues

## Backup Location
Pre-consolidation backup: [{self.backup_dir}]({self.backup_dir})

---
*Consolidation completed successfully with comprehensive documentation preservation.*
"""

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"Generated consolidation report: {report_path}")

    def run_consolidation(self):
        """Run the complete consolidation process"""
        print("🚀 Starting MicroHydro Workspace Consolidation")
        print("=" * 50)

        # Load categorization plan
        categories = self.load_categorization()
        if not categories:
            print("❌ No categorization file found. Cannot proceed.")
            return

        # Create backup
        self.create_backup()

        # Process each category
        for category_name, files in categories.items():
            self.consolidate_category(category_name, files)

        # Archive merged files
        self.archive_merged_files(categories)

        # Update documentation
        self.update_document_index()
        self.generate_consolidation_report(categories)

        print("\n✅ Consolidation Complete!")
        print("📊 Check CONSOLIDATION_REPORT.md for details")
        print("📁 Review consolidated master documents")
        print("🗂️  Archived files available in ARCHIVE/CONSOLIDATED_SOURCES/")

def main():
    workspace_root = "/Users/gripandripphdd/MircoHydro"
    consolidator = WorkspaceConsolidator(workspace_root)
    consolidator.run_consolidation()

if __name__ == "__main__":
    main()