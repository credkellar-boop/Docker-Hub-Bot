from modules.compliance_guardian import ComplianceGuardian

def sweep():
    print("[*] Performing full-network compliance audit...")
    # Loop through all platforms in ledger, re-scan their contracts
    # Trigger legal defense protocol if scan fails
