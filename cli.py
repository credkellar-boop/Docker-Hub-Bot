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
