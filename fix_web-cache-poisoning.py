"""Web Cache Poisoning Fix"""
from fastapi import Request

def get_cache_key(request: Request) -> str:
    """Generate cache key including security headers."""
    key_parts = [request.url.path]
    security_headers = ["Authorization", "Cookie", "X-Forwarded-For"]
    for header in security_headers:
        if header in request.headers:
            key_parts.append(f"{header}:{request.headers[header]}")
    return "|".join(key_parts)
