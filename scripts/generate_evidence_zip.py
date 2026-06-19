import zipfile

def bundle_case(case_id):
    """Bundles all case evidence into a single archive."""
    print(f"[*] Packaging case {case_id} for legal retention.")
    # Zips files from data/legal and data/vault
