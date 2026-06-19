from cryptography.fernet import Fernet

class EncryptionEngine:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_file(self, file_path):
        """Encrypts sensitive evidence before storage."""
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = self.fernet.encrypt(data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted)
