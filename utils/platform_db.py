import json

class PlatformDB:
    def update_status(self, platform, status):
        """Updates the status of a target platform in the ledger."""
        print(f"[*] DB: Updating {platform} status to {status}")
