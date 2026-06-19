import argparse
from utils.platform_db import PlatformDB

def override():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    args = parser.parse_args()
    PlatformDB().update_status(args.platform, "ACTIVE")
    print(f"[+] Manual override successful for {args.platform}.")

if __name__ == "__main__":
    override()
