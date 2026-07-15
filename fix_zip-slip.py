"""Zip Slip Fix"""
import os

def safe_extract(zip_path, extract_to):
    """Safely extract zip file preventing path traversal."""
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # Prevent path traversal
            member_path = os.path.join(extract_to, member)
            if not member_path.startswith(os.path.abspath(extract_to)):
                raise ValueError("Path traversal detected")
            # Extract
            zip_ref.extract(member, extract_to)
