import unittest
from modules.asset_core import AssetManager
from modules.security_auditor import SecurityAuditor

class TestBotTriad(unittest.TestCase):
    
    def test_asset_manager_initialization(self):
        asset = AssetManager()
        self.assertIn("docker-library/official-images", asset.library_repos)
        self.assertEqual(asset.workspace, "data/repos")
        
    def test_security_auditor_config(self):
        auditor = SecurityAuditor(fail_on_critical=True)
        self.assertTrue(auditor.fail_on_critical)

if __name__ == "__main__":
    unittest.main()
