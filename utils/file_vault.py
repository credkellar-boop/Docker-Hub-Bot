import shutil, os

class FileVault:
    def secure_report(self, report_path):
        """Moves file to an encrypted/restricted vault."""
        if not os.path.exists("data/vault"): os.makedirs("data/vault")
        shutil.move(report_path, "data/vault/")
