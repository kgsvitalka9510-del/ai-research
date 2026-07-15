"""Web Cache Deception Fix"""
from fastapi import Request

def prevent_cache_deception(request: Request, response):
    """Add headers to prevent cache deception."""
    response.headers["Cache-Control"] = "private, no-store"
    response.headers["Vary"] = "Authorization, Cookie"
    return response
