"""Authentication middleware for single-user token validation."""
import os
from typing import Optional
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    """Simple token-based authentication middleware for single-user system."""
    
    def __init__(self, app, exclude_paths: Optional[list] = None):
        super().__init__(app)
        self.token = os.environ.get("API_TOKEN", "default-dev-token")
        self.exclude_paths = exclude_paths or ["/health", "/docs", "/openapi.json", "/redoc"]
    
    async def dispatch(self, request: Request, call_next):
        """Validate API token for protected endpoints."""
        # Skip auth for excluded paths
        if any(request.url.path.startswith(path) for path in self.exclude_paths):
            return await call_next(request)
        
        # Extract token from header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid authorization header",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Validate token
        token = auth_header.replace("Bearer ", "")
        if token != self.token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Process request
        return await call_next(request)


def get_current_user(request: Request) -> str:
    """Get current user from request context.
    
    For single-user system, returns a constant user identifier.
    """
    return "default-user"