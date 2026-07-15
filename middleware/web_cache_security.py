"""
Web Cache Deception Fix Middleware

This middleware prevents cache poisoning attacks by:
1. Validating cache keys include security-relevant headers
2. Adding Cache-Control headers to sensitive responses
3. Logging suspicious header combinations
"""

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
import logging

logger = logging.getLogger(__name__)

# Headers that should be included in cache key
CACHE_KEY_HEADERS = [
    "Authorization",
    "Cookie",
    "X-Forwarded-For",
    "X-Real-IP",
    "X-Original-URL",
    "X-Forwarded-Host",
]

# Suspicious header patterns
SUSPICIOUS_PATTERNS = [
    "X-Forwarded-For",
    "X-Real-IP",
    "X-Original-URL",
    "X-Forwarded-Host",
]


class WebCacheDeceptionMiddleware(BaseHTTPMiddleware):
    """Middleware to prevent web cache deception attacks."""
    
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Check for suspicious headers
        suspicious_headers = []
        for header in SUSPICIOUS_PATTERNS:
            if header in request.headers:
                suspicious_headers.append(header)
        
        if suspicious_headers:
            logger.warning(
                f"Suspicious headers detected: {suspicious_headers} "
                f"from {request.client.host}"
            )
        
        # Get response
        response = await call_next(request)
        
        # Add security headers to prevent caching
        response.headers["Cache-Control"] = "private, no-store, no-cache"
        response.headers["Vary"] = "Authorization, Cookie"
        response.headers["X-Content-Type-Options"] = "nosniff"
        
        # For sensitive endpoints, add stronger protection
        if request.url.path.startswith("/api/"):
            response.headers["Cache-Control"] = "private, no-store"
            response.headers["Pragma"] = "no-cache"
        
        return response


def get_cache_key(request: Request) -> str:
    """Generate cache key including security-relevant headers."""
    key_parts = [request.url.path]
    
    for header in CACHE_KEY_HEADERS:
        if header in request.headers:
            key_parts.append(f"{header}:{request.headers[header]}")
    
    return "|".join(key_parts)
