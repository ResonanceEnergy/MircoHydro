#!/usr/bin/env python3
"""
MicroHydro Source Analysis and Mapping
Analyze available source files and map to empty destinations
"""

import os
from pathlib import Path
from typing import Dict, List, Set

class SourceAnalyzer:
    def __init__(self, source_base: str, dest_base: str):
        self.source_base = Path(source_base)
        self.dest_base = Path(dest_base)
        self.manifest_file = Path("/tmp/empty_files_manifest.txt")

    def load_empty_files(self) -> List[str]:
        """Load the list of empty files."""
        if not self.manifest_file.exists():
            raise FileNotFoundError(f"Manifest file not found: {self.manifest_file}")

        with open(self.manifest_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def get_all_source_files(self) -> Set[str]:
        """Get all files in source directory as relative paths."""
        source_files = set()
        for file_path in self.source_base.rglob("*"):
            if file_path.is_file():
                relative_path = file_path.relative_to(self.source_base)
                source_files.add(str(relative_path))
        return source_files

    def analyze_mapping(self) -> Dict[str, any]:
        """Analyze how source files map to empty destination files."""
        empty_files = self.load_empty_files()
        source_files = self.get_all_source_files()

        results = {
            'total_empty': len(empty_files),
            'total_source': len(source_files),
            'mapped': [],
            'unmapped': [],
            'source_only': []
        }

        # Check each empty file
        for empty_file in empty_files:
            # Convert dest path to relative path from dest_base
            if empty_file.startswith(str(self.dest_base)):
                relative_path = empty_file[len(str(self.dest_base)):].lstrip('/')

                if relative_path in source_files:
                    results['mapped'].append({
                        'dest': empty_file,
                        'source_relative': relative_path,
                        'source_full': str(self.source_base / relative_path)
                    })
                else:
                    results['unmapped'].append({
                        'dest': empty_file,
                        'needed_relative': relative_path
                    })

        # Find source files that don't map to empty destinations
        dest_relative_paths = set()
        for empty_file in empty_files:
            if empty_file.startswith(str(self.dest_base)):
                relative_path = empty_file[len(str(self.dest_base)):].lstrip('/')
                dest_relative_paths.add(relative_path)

        for source_file in source_files:
            if source_file not in dest_relative_paths:
                results['source_only'].append(source_file)

        return results

    def print_analysis(self):
        """Print comprehensive analysis."""
        print("🔍 MICROHYDRO SOURCE ANALYSIS & MAPPING")
        print("=" * 50)

        try:
            results = self.analyze_mapping()

            print(f"📊 OVERVIEW:")
            print(f"   Empty files to fill: {results['total_empty']}")
            print(f"   Available source files: {results['total_source']}")
            print(f"   Perfect matches: {len(results['mapped'])}")
            print(f"   Missing sources: {len(results['unmapped'])}")
            print(f"   Extra sources: {len(results['source_only'])}")
            print()

            if results['mapped']:
                print("✅ MAPPED FILES (can be copied):")
                for item in results['mapped'][:10]:  # Show first 10
                    print(f"   ✓ {item['source_relative']}")
                if len(results['mapped']) > 10:
                    print(f"   ... and {len(results['mapped']) - 10} more")
                print()

            if results['unmapped']:
                print("❌ UNMAPPED FILES (sources missing):")
                for item in results['unmapped'][:10]:  # Show first 10
                    print(f"   ✗ {item['needed_relative']}")
                if len(results['unmapped']) > 10:
                    print(f"   ... and {len(results['unmapped']) - 10} more")
                print()

            print("🎯 RECOMMENDATIONS:")
            if len(results['mapped']) > 0:
                print(f"   • {len(results['mapped'])} files can be activated immediately")
            if len(results['unmapped']) > 0:
                print(f"   • {len(results['unmapped'])} files need source files located")
                print("   • Check alternative OneDrive directories")
                print("   • Search for backup archives (.zip files)")
            if len(results['source_only']) > 0:
                print(f"   • {len(results['source_only'])} extra source files available")

        except Exception as e:
            print(f"❌ Analysis failed: {e}")

def main():
    # Configuration
    SOURCE_BASE = "/Users/gripandripphdd/Library/CloudStorage/OneDrive-GripandRipp(2)/mastermaster/ResonanceEnergy_Enterprise"
    DEST_BASE = "/Users/gripandripphdd/MircoHydro"

    analyzer = SourceAnalyzer(SOURCE_BASE, DEST_BASE)
    analyzer.print_analysis()

if __name__ == "__main__":
    main()