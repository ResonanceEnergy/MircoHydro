#!/usr/bin/env python3
"""
MicroHydro Content Activation Automation
Automated content restoration for 1,570 empty files
"""

import os
import shutil
import time
from pathlib import Path
from typing import List, Tuple

class MicroHydroActivator:
    def __init__(self, source_base: str, dest_base: str):
        self.source_base = Path(source_base)
        self.dest_base = Path(dest_base)
        self.manifest_file = Path("/tmp/empty_files_manifest.txt")
        self.log_file = Path("/tmp/activation_log.txt")

        # Validate paths
        if not self.source_base.exists():
            raise ValueError(f"Source path does not exist: {self.source_base}")

        if not self.dest_base.exists():
            raise ValueError(f"Destination path does not exist: {self.dest_base}")

        print("🚀 MICROHYDRO CONTENT ACTIVATION AUTOMATION")
        print("=" * 50)
        print(f"📂 Source: {self.source_base}")
        print(f"📂 Destination: {self.dest_base}")
        print(f"📋 Manifest: {self.manifest_file}")
        print()

    def load_manifest(self) -> List[str]:
        """Load the list of empty files to activate."""
        if not self.manifest_file.exists():
            raise FileNotFoundError(f"Manifest file not found: {self.manifest_file}")

        with open(self.manifest_file, 'r') as f:
            empty_files = [line.strip() for line in f if line.strip()]

        print(f"📋 Loaded {len(empty_files)} files from manifest")
        return empty_files

    def get_source_dest_pair(self, dest_path: str) -> Tuple[Path, Path]:
        """Convert destination path to source-destination pair."""
        # Remove the destination base to get relative path
        relative_path = dest_path.replace(str(self.dest_base), "").lstrip("/")
        source_path = self.source_base / relative_path
        dest_path_obj = Path(dest_path)

        return source_path, dest_path_obj

    def copy_file(self, source: Path, dest: Path) -> bool:
        """Copy a single file with error handling."""
        try:
            # Ensure destination directory exists
            dest.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            shutil.copy2(source, dest)

            # Verify the copy
            if dest.exists() and dest.stat().st_size > 0:
                return True
            else:
                print(f"❌ Copy verification failed: {dest}")
                return False

        except Exception as e:
            print(f"❌ Error copying {source} -> {dest}: {e}")
            return False

    def activate_content(self, batch_size: int = 50, delay: float = 0.1) -> Tuple[int, int, int]:
        """Activate content in batches with progress reporting."""
        empty_files = self.load_manifest()
        total_files = len(empty_files)

        successful = 0
        failed = 0
        skipped = 0

        print(f"🎯 Starting activation of {total_files} files")
        print(f"📦 Batch size: {batch_size}")
        print()

        start_time = time.time()

        for i, dest_path in enumerate(empty_files, 1):
            source_path, dest_path_obj = self.get_source_dest_pair(dest_path)

            # Check if source exists
            if not source_path.exists():
                print(f"⚠️  Source missing: {source_path}")
                skipped += 1
                continue

            # Check if destination is already populated
            if dest_path_obj.exists() and dest_path_obj.stat().st_size > 0:
                print(f"⏭️  Already exists: {dest_path_obj}")
                skipped += 1
                continue

            # Copy the file
            if self.copy_file(source_path, dest_path_obj):
                successful += 1
                if i % 10 == 0:  # Progress update every 10 files
                    elapsed = time.time() - start_time
                    rate = i / elapsed if elapsed > 0 else 0
                    eta = (total_files - i) / rate if rate > 0 else 0
                    print(f"Processed {i}/{total_files} files ({i/total_files*100:.1f}%) - Success: {successful}, Failed: {failed}, Skipped: {skipped} - ETA: {eta:.1f}s")
            else:
                failed += 1

            # Small delay between operations
            time.sleep(delay)

            # Batch pause
            if i % batch_size == 0 and i < total_files:
                print(f"⏸️  Batch {i//batch_size} complete. Continuing...")
                time.sleep(1)

        total_time = time.time() - start_time
        return successful, failed, skipped

    def verify_activation(self) -> Tuple[int, int]:
        """Verify that activation was successful."""
        print("\n🔍 VERIFICATION PHASE")
        print("-" * 30)

        # Count remaining empty files
        empty_count = 0
        for root, dirs, files in os.walk(self.dest_base):
            for file in files:
                file_path = Path(root) / file
                if file_path.stat().st_size == 0:
                    empty_count += 1

        total_files = sum(1 for _ in self.dest_base.rglob("*") if _.is_file())
        filled_files = total_files - empty_count

        print(f"📊 Total files: {total_files}")
        print(f"📂 Empty files: {empty_count}")
        print(f"✅ Filled files: {filled_files}")

        if empty_count == 0:
            print("🎉 ACTIVATION COMPLETE - 100% SUCCESS!")
        else:
            print(f"⚠️  {empty_count} files still empty")

        return filled_files, empty_count

def main():
    # Configuration
    SOURCE_BASE = "/Users/gripandripphdd/Library/CloudStorage/OneDrive-GripandRipp(2)/mastermaster/ResonanceEnergy_Enterprise"
    DEST_BASE = "/Users/gripandripphdd/MircoHydro"

    try:
        # Initialize activator
        activator = MicroHydroActivator(SOURCE_BASE, DEST_BASE)

        # Run activation
        successful, failed, skipped = activator.activate_content(
            batch_size=50,  # Process 50 files at a time
            delay=0.05     # 50ms delay between files
        )

        # Final verification
        filled, empty = activator.verify_activation()

        # Summary
        print("\n📈 FINAL SUMMARY")
        print("=" * 30)
        print(f"✅ Successful copies: {successful}")
        print(f"❌ Failed copies: {failed}")
        print(f"⏭️  Skipped: {skipped}")
        print(f"📂 Files filled: {filled}")
        print(f"📭 Files still empty: {empty}")

        if empty == 0:
            print("\n🎯 MISSION ACCOMPLISHED!")
            print("🌟 Your MicroHydro system is now 100% operational!")
        else:
            print(f"\n⚠️  {empty} files require manual attention")

    except Exception as e:
        print(f"❌ Activation failed: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())