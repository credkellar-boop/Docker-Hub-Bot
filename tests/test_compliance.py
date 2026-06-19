import unittest
from modules.compliance_guardian import ComplianceGuardian

class TestCompliance(unittest.TestCase):
    def test_backdoor_rejection(self):
        guardian = ComplianceGuardian()
        # Mock a backdoor contract
        is_safe, _ = guardian.process_incoming_contract("EvilPlatform", "We reserve the right to seize all data.")
        self.assertFalse(is_safe)
