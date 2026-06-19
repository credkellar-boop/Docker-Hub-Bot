import os
import requests
from github import Github

class EcosystemPublisher:
    def __init__(self):
        self.gh_token = os.environ.get("GITHUB_TOKEN")
        self.docker_user = os.environ.get("DOCKER_HUB_USERNAME")
        self.docker_pass = os.environ.get("DOCKER_HUB_PASSWORD")
        self.dev_to_key = os.environ.get("DEV_TO_API_KEY")

    def publish_github_release(self, repo_name, tag_name, body_text):
        """Creates an official GitHub Release for the repository."""
        if not self.gh_token:
            print("[!] Missing GITHUB_TOKEN.")
            return
        
        print(f"[*] Connecting to GitHub API for release: {tag_name}...")
        g = Github(self.gh_token)
        try:
            repo = g.get_repo(repo_name)
            release = repo.create_git_release(
                tag=tag_name,
                name=f"Release {tag_name}",
                message=body_text,
                draft=False,
                prerelease=False
            )
            print(f"[+] GitHub Release published successfully: {release.html_url}")
        except Exception as e:
            print(f"[!] GitHub Release failed: {e}")

    def update_docker_hub_readme(self, repo_slug, readme_content):
        """Programmatically updates the Repository Overview description on Docker Hub."""
        if not self.docker_user or not self.docker_pass:
            print("[!] Missing Docker Hub authentication credentials.")
            return

        print(f"[*] Authenticating with Docker Hub API for {repo_slug}...")
        login_url = "https://hub.docker.com/v2/users/login/"
        login_res = requests.post(login_url, json={"username": self.docker_user, "password": self.docker_pass})
        
        if login_res.status_code == 200:
            token = login_res.json().get("token")
            headers = {"Authorization": f"JWT {token}"}
            
            # Target the specific repository overview endpoint
            patch_url = f"https://hub.docker.com/v2/repositories/{self.docker_user}/{repo_slug}/"
            payload = {"full_description": readme_content}
            
            patch_res = requests.patch(patch_url, headers=headers, json=payload)
            if patch_res.status_code == 200:
                print("[+] Docker Hub repository overview successfully updated.")
            else:
                print(f"[!] Metadata update failed: {patch_res.text}")
        else:
            print("[!] Docker Hub login failed.")

    def publish_to_dev_to(self, title, body_markdown):
        """Cross-posts the codebase updates to DEV.to (GitHub partner ecosystem)."""
        if not self.dev_to_key:
            print("[!] Missing DEV_TO_API_KEY.")
            return

        print("[*] Broadcasting documentation payload to DEV.to network...")
        url = "https://dev.to/api/articles"
        headers = {"api-key": self.dev_to_key, "Content-Type": "application/json"}
        
        article_data = {
            "article": {
                "title": title,
                "published": True,
                "body_markdown": body_markdown,
                "tags": ["docker", "github", "automation", "ai"]
            }
        }
        
        res = requests.post(url, headers=headers, json=article_data)
        if res.status_code == 201:
            print(f"[+] Post published live on DEV.to: {res.json().get('url')}")
        else:
            print(f"[!] DEV.to cross-posting failed: {res.text}")
