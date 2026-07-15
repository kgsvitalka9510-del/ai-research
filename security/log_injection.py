"""Log Injection Fix"""
import re

def sanitize_log_input(user_input):
    """Sanitize input for logging."""
    # Remove CRLF characters
    sanitized = re.sub(r'[\r\n]', '', user_input)
    # Truncate long inputs
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000] + "..."
    return sanitized

def log_event(event_type, user_input):
    """Log event with sanitized input."""
    sanitized = sanitize_log_input(user_input)
    # Use structured logging
    log_entry = {
        "event": event_type,
        "input": sanitized,
        "timestamp": time.time()
    }
    return log_entry
