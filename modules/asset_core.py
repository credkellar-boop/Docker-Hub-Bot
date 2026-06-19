import os
import subprocess

class AssetManager:
    def __init__(self):
        self.library_repos = [
            "docker-library-bot",
            "docker-library/official-images",
            "docker-library/docs",
            "docker-library/repo-info",
            "docker-library-transitioner",
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
            
            if not os.path.exists(target_dir):
                org = "docker-library" if "/" not in repo_path else repo_path.split("/")[0]
                url = f"https://github.com/{org}/{repo_name}.git"
                subprocess.run(["git", "clone", url, target_dir], check=True)
            else:
                subprocess.run(["git", "-C", target_dir, "pull"], check=True)
