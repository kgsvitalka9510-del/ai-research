"""CORS Misconfiguration Fix"""
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

ALLOWED_ORIGINS = [
    "https://example.com",
    "https://app.example.com",
]

def setup_cors(app):
    """Setup CORS with strict origins."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["Authorization", "Content-Type"],
    )
