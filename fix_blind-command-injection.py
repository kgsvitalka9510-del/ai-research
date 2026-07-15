"""Blind Command Injection Fix"""
import re
import subprocess

def sanitize_input(user_input):
    """Sanitize user input to prevent command injection."""
    # Remove dangerous characters
    sanitized = re.sub(r'[;&|`$(){}]', '', user_input)
    return sanitized

def safe_command(cmd, user_input):
    """Execute command safely with sanitized input."""
    sanitized = sanitize_input(user_input)
    # Use subprocess with list arguments
    return subprocess.run([cmd, sanitized], capture_output=True, text=True)
