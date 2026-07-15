"""OAuth 2.0 CSRF Fix"""
import secrets
import hashlib

def generate_state():
    """Generate cryptographically secure state parameter."""
    return secrets.token_urlsafe(32)

def validate_state(state, stored_state):
    """Validate OAuth state parameter."""
    return secrets.compare_digest(state, stored_state)

def store_state(state, user_id):
    """Store state with user association."""
    # Store in secure session/database
    pass
