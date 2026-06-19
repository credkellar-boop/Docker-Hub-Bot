from modules.contract_scanner import ContractScanner
from modules.police_report_generator import PoliceReportGenerator

class ComplianceGuardian:
    def process_incoming_contract(self, platform, text):
        scanner = ContractScanner()
        status = scanner.scan_for_backdoors(text)
        
        if "BACKDOOR_DETECTED" in status:
            print(f"[!!!] BACKDOOR FOUND ON {platform}. Executing legal defense protocol.")
            reporter = PoliceReportGenerator()
            report_path = reporter.create_incident_report(platform, text, status)
            return False, report_path
        return True, None
