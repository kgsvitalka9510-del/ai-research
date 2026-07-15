"""Timing Attack Fix"""
import hmac

def secure_compare(a, b):
    """Constant-time string comparison."""
    return hmac.compare_digest(a.encode(), b.encode())

def verify_password(password, stored_hash, salt):
    """Verify password with constant-time comparison."""
    import hashlib
    computed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return secure_compare(computed.hex(), stored_hash)
