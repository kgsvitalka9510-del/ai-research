"""
Timing Attack Prevention

This module prevents timing attacks on password verification by using
constant-time comparison functions.
"""

import hmac
import hashlib
import secrets


def secure_compare(a: str, b: str) -> bool:
    """
    Constant-time string comparison to prevent timing attacks.
    
    This function compares two strings in constant time, regardless of
    where they differ. This prevents an attacker from determining the
    correct password by measuring response times.
    
    Args:
        a: First string to compare
        b: Second string to compare
    
    Returns:
        True if strings are equal, False otherwise
    """
    return hmac.compare_digest(a.encode(), b.encode())


def verify_password(password: str, stored_hash: str, salt: str = None) -> bool:
    """
    Verify a password against a stored hash using constant-time comparison.
    
    Args:
        password: The password to verify
        stored_hash: The stored password hash
        salt: Optional salt (if not provided, extract from stored_hash)
    
    Returns:
        True if password matches, False otherwise
    """
    if salt is None:
        # Extract salt from stored hash (first 32 chars)
        salt = stored_hash[:32]
    
    # Hash the provided password with the same salt
    computed_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt.encode(),
        100000
    ).hex()
    
    # Use constant-time comparison
    return secure_compare(computed_hash, stored_hash[32:])


def hash_password(password: str, salt: str = None) -> str:
    """
    Hash a password with a salt using PBKDF2.
    
    Args:
        password: The password to hash
        salt: Optional salt (if not provided, generate random)
    
    Returns:
        The hashed password (salt + hash)
    """
    if salt is None:
        salt = secrets.token_hex(16)
    
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt.encode(),
        100000
    ).hex()
    
    return salt + hashed
