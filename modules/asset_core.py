import os
import subprocess

class AssetManager:
    def __init__(self):
        self.library_repos = [
            "docker-library/official-images",
            "docker-library/docs",
            "docker-library/repo-info",
            "docker-library/faq"
        ]
        self.workspace = "data/repos"

    def sync_ecosystem(self):
        """Synchronizes the core docker-library repositories into the workspace."""
        os.makedirs(self.workspace, exist_ok=True)
        print("[*] Asset Module: Synchronizing Docker library ecosystem...")

        for repo_path in self.library_repos:
            repo_name = repo_path.split("/")[-1]
            target_dir = os.path.join(self.workspace, repo_name)
            url = f"https://github.com/{repo_path}.git"

            if not os.path.exists(target_dir):
                print(f"[*] Cloning {repo_path}...")
                subprocess.run(["git", "clone", "--depth", "1", url, target_dir], check=True)
            else:
                print(f"[*] Updating {repo_path}...")
                subprocess.run(["git", "-C", target_dir, "pull"], check=True)
