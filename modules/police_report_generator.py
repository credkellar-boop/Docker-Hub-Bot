import datetime

class PoliceReportGenerator:
    def create_incident_report(self, platform, contract_text, threat_analysis):
        """Generates a formal legal incident report."""
        timestamp = datetime.datetime.now().isoformat()
        report = f"""INCIDENT REPORT - {timestamp}
        -------------------------------------------
        TARGET PLATFORM: {platform}
        THREAT ANALYSIS: {threat_analysis}
        EVIDENCE: {contract_text}
        
        SUMMARY: This bot has identified a malicious backdoor attempt during the
        contract negotiation phase and has autonomously declined integration.
        """
        filename = f"data/legal/incident_{platform}_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
        with open(filename, "w") as f:
            f.write(report)
        return filename
