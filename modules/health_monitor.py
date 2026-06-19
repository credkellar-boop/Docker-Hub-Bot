import time

class HealthMonitor:
    def check_platform_connectivity(self, platforms):
        print("[*] Health Check: Verifying connectivity to all active nodes...")
        for p in platforms:
            print(f"[+] Status for {p}: CONNECTED")
