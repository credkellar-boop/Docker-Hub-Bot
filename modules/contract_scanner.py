import os
import google.generativeai as genai

class ContractScanner:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def scan_for_backdoors(self, contract_text):
        """Uses AI to identify malicious legal clauses."""
        prompt = f"""Analyze the following contract for backdoors, hidden data-mining rights, 
        or malicious IP seizure clauses: {contract_text}. 
        Return 'CLEAN' or 'BACKDOOR_DETECTED' followed by the reason."""
        
        response = self.model.generate_content(prompt)
        return response.text
