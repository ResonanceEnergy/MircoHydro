#!/usr/bin/env python3
"""
MicroHydro Partial Activation
Activate the 22 files that have perfect source matches
"""

import os
import shutil
from pathlib import Path
from typing import List, Dict, Any

class PartialActivator:
    def __init__(self, source_base: str, dest_base: str):
        self.source_base = Path(source_base)
        self.dest_base = Path(dest_base)
        self.manifest_file = Path("/tmp/empty_files_manifest.txt")

    def load_empty_files(self) -> List[str]:
        """Load the list of empty files."""
        with open(self.manifest_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def get_mappable_files(self) -> List[Dict[str, Any]]:
        """Find files that can be mapped from source to destination."""
        empty_files = self.load_empty_files()
        mappable = []

        for empty_file in empty_files:
            if empty_file.startswith(str(self.dest_base)):
                relative_path = empty_file[len(str(self.dest_base)):].lstrip('/')
                source_path = self.source_base / relative_path

                if source_path.exists() and source_path.is_file():
                    mappable.append({
                        'dest': Path(empty_file),
                        'source': source_path,
                        'relative': relative_path
                    })

        return mappable

    def activate_mappable_files(self) -> Dict[str, int]:
        """Activate all files that have source matches."""
        mappable = self.get_mappable_files()
        results = {'successful': 0, 'failed': 0}

        print(f"🚀 ACTIVATING {len(mappable)} MAPPABLE FILES")
        print("=" * 40)

        for item in mappable:
            try:
                # Ensure destination directory exists
                item['dest'].parent.mkdir(parents=True, exist_ok=True)

                # Copy the file
                shutil.copy2(item['source'], item['dest'])

                # Verify
                if item['dest'].exists() and item['dest'].stat().st_size > 0:
                    print(f"✅ {item['relative']}")
                    results['successful'] += 1
                else:
                    print(f"❌ {item['relative']} (verification failed)")
                    results['failed'] += 1

            except Exception as e:
                print(f"❌ {item['relative']} (error: {e})")
                results['failed'] += 1

        return results

    def verify_results(self) -> Dict[str, int]:
        """Verify the activation results."""
        # Count remaining empty files
        empty_count = 0
        for root, dirs, files in os.walk(self.dest_base):
            for file in files:
                file_path = Path(root) / file
                if file_path.stat().st_size == 0:
                    empty_count += 1

        total_files = sum(1 for _ in self.dest_base.rglob("*") if _.is_file())
        filled_files = total_files - empty_count

        return {
            'total_files': total_files,
            'empty_files': empty_count,
            'filled_files': filled_files
        }

def main():
    # Configuration
    SOURCE_BASE = "/Users/gripandripphdd/Library/CloudStorage/OneDrive-GripandRipp(2)/mastermaster/ResonanceEnergy_Enterprise"
    DEST_BASE = "/Users/gripandripphdd/MircoHydro"

    activator = PartialActivator(SOURCE_BASE, DEST_BASE)

    # Activate mappable files
    results = activator.activate_mappable_files()

    print(f"\n📈 ACTIVATION RESULTS")
    print("=" * 20)
    print(f"✅ Successful: {results['successful']}")
    print(f"❌ Failed: {results['failed']}")

    # Verify
    verification = activator.verify_results()
    print(f"\n🔍 VERIFICATION")
    print("=" * 15)
    print(f"📊 Total files: {verification['total_files']}")
    print(f"📂 Empty files: {verification['empty_files']}")
    print(f"✅ Filled files: {verification['filled_files']}")

    remaining = verification['empty_files']
    if remaining == 0:
        print("\n🎯 MISSION ACCOMPLISHED!")
        print("🌟 All files successfully activated!")
    else:
        print(f"\n⚠️  {remaining} files still need sources")
        print("💡 Next: Locate backup archives or alternative sources")

if __name__ == "__main__":
    main()