import argparse
from modules.asset_core import AssetManager
from modules.security_auditor import SecurityAuditor
from modules.brain_inference import BrainInference

def main():
    parser = argparse.ArgumentParser(description="Docker-Hub-Bot Automation CLI")
    parser.add_argument("--sync", action="store_true", help="Sync the Docker official library assets")
    parser.add_argument("--audit", type=str, help="Run a security audit on a specific Docker image")
    parser.add_argument("--provision", type=str, help="Use the Brain to generate a deployment for a query")
    
    args = parser.parse_args()

    if args.sync:
        AssetManager().sync_ecosystem()
    
    if args.audit:
        SecurityAuditor().run_scout_audit(args.audit)
        
    if args.provision:
        brain = BrainInference()
        config = brain.generate_environment(args.provision)
        with open("generated_infrastructure.yaml", "w") as f:
            f.write(config)
        print("[*] Infrastructure generated and saved to generated_infrastructure.yaml")

if __name__ == "__main__":
    main()

import argparse
from modules.ecosystem_publisher import EcosystemPublisher

def main():
    parser = argparse.ArgumentParser(description="Docker-Hub-Bot Automation CLI")
    parser.add_argument("--release", type=str, help="Tag version for GitHub release (e.g. v1.0.0)")
    parser.add_argument("--push-hub", type=str, help="Docker Hub repository name to sync documentation")
    
    args = parser.parse_args()
    publisher = EcosystemPublisher()

    if args.release:
        # Programmatically triggers release pipeline
        with open("README.md", "r") as f:
            desc = f.read()
        # Change 'your-username/repo' to match your path configuration
        publisher.publish_github_release("credkellar-boop/Docker-Hub-Bot", args.release, desc)

    if args.push_hub:
        with open("README.md", "r") as f:
            desc = f.read()
        publisher.update_docker_hub_readme(args.push_hub, desc)

if __name__ == "__main__":
    main()
    
