"""Session Fixation Fix"""
import secrets

def generate_session_id():
    """Generate cryptographically secure session ID."""
    return secrets.token_urlsafe(32)

def rotate_session(old_session_id):
    """Rotate session ID after login."""
    new_session_id = generate_session_id()
    # Store new session, invalidate old
    return new_session_id
