#!/usr/bin/env python3
"""
MicroHydro GitHub Source Activation
Clone and use GitHub repository as source for missing files
"""

import os
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Any

class GitHubActivator:
    def __init__(self, github_repo: str, dest_base: str):
        self.github_repo = github_repo  # "https://github.com/ResonanceEnergy/MicroHydro"
        self.dest_base = Path(dest_base)
        self.clone_dir = Path("/tmp/github_source")
        self.manifest_file = Path("/tmp/empty_files_manifest.txt")

    def clone_repository(self) -> bool:
        """Clone the GitHub repository to local temp directory."""
        try:
            print(f"📥 Cloning repository: {self.github_repo}")

            # Remove existing clone if it exists
            if self.clone_dir.exists():
                shutil.rmtree(self.clone_dir)

            # Clone the repository
            result = subprocess.run([
                "git", "clone", "--depth", "1", self.github_repo, str(self.clone_dir)
            ], capture_output=True, text=True, timeout=300)

            if result.returncode == 0:
                print("✅ Repository cloned successfully")
                return True
            else:
                print(f"❌ Clone failed: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            print("❌ Clone timed out")
            return False
        except Exception as e:
            print(f"❌ Clone error: {e}")
            return False

    def analyze_github_content(self) -> Dict[str, Any]:
        """Analyze what content is available in the GitHub repository."""
        if not self.clone_dir.exists():
            return {'available': False}

        # Get all files in the repository
        github_files = set()
        for file_path in self.clone_dir.rglob("*"):
            if file_path.is_file():
                relative_path = file_path.relative_to(self.clone_dir)
                github_files.add(str(relative_path))

        # Load empty files manifest
        empty_files = self.load_empty_files()

        # Analyze mapping
        mappable = []
        unmappable = []

        for empty_file in empty_files:
            if empty_file.startswith(str(self.dest_base)):
                relative_path = empty_file[len(str(self.dest_base)):].lstrip('/')

                if relative_path in github_files:
                    mappable.append({
                        'dest': Path(empty_file),
                        'source': self.clone_dir / relative_path,
                        'relative': relative_path
                    })
                else:
                    unmappable.append(relative_path)

        return {
            'available': True,
            'total_github_files': len(github_files),
            'mappable_files': len(mappable),
            'unmappable_files': len(unmappable),
            'mappable_details': mappable,
            'sample_unmappable': unmappable[:10]
        }

    def load_empty_files(self) -> List[str]:
        """Load the list of empty files."""
        if not self.manifest_file.exists():
            return []

        with open(self.manifest_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def activate_from_github(self) -> Dict[str, int]:
        """Activate files from GitHub repository."""
        analysis = self.analyze_github_content()

        if not analysis['available']:
            print("❌ GitHub repository not available")
            return {'successful': 0, 'failed': 0}

        mappable = analysis['mappable_details']
        results = {'successful': 0, 'failed': 0}

        print(f"🚀 ACTIVATING {len(mappable)} FILES FROM GITHUB")
        print("=" * 45)

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

    def cleanup(self):
        """Clean up temporary clone directory."""
        if self.clone_dir.exists():
            shutil.rmtree(self.clone_dir)
            print("🧹 Cleaned up temporary files")

def main():
    # Configuration
    GITHUB_REPO = "https://github.com/ResonanceEnergy/MicroHydro"
    DEST_BASE = "/Users/gripandripphdd/MircoHydro"

    activator = GitHubActivator(GITHUB_REPO, DEST_BASE)

    try:
        print("🔍 MICROHYDRO GITHUB SOURCE ACTIVATION")
        print("=" * 40)
        print(f"📂 GitHub Repo: {GITHUB_REPO}")
        print(f"📂 Destination: {DEST_BASE}")
        print()

        # Clone repository
        if not activator.clone_repository():
            print("❌ Failed to access GitHub repository")
            return 1

        # Analyze content
        analysis = activator.analyze_github_content()
        print("📊 CONTENT ANALYSIS:")
        print(f"   GitHub files available: {analysis['total_github_files']}")
        print(f"   Files that can be activated: {analysis['mappable_files']}")
        print(f"   Files still missing: {analysis['unmappable_files']}")
        print()

        if analysis['mappable_files'] > 0:
            # Activate files
            results = activator.activate_from_github()

            print("\n📈 ACTIVATION RESULTS")
            print("=" * 20)
            print(f"✅ Successful: {results['successful']}")
            print(f"❌ Failed: {results['failed']}")

            if results['successful'] > 0:
                print("\n🎉 Partial activation successful!")
                print(f"🌟 {results['successful']} files now active from GitHub!")
        else:
            print("⚠️  No mappable files found in GitHub repository")

        # Cleanup
        activator.cleanup()

    except Exception as e:
        print(f"❌ Activation failed: {e}")
        activator.cleanup()
        return 1

    return 0

if __name__ == "__main__":
    exit(main())