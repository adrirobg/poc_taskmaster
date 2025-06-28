"""Logging middleware and configuration."""
import logging
import sys
from typing import Any, Dict
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


# Configure logging format
LOGGING_CONFIG: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream": sys.stdout,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": "logs/app.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
    "loggers": {
        "uvicorn.error": {
            "level": "INFO",
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests and responses."""
    
    def __init__(self, app, logger_name: str = "app.middleware"):
        super().__init__(app)
        self.logger = logging.getLogger(logger_name)
    
    async def dispatch(self, request: Request, call_next):
        """Log request details and response status."""
        start_time = datetime.utcnow()
        
        # Log request
        self.logger.info(
            f"Request: {request.method} {request.url.path} "
            f"from {request.client.host if request.client else 'unknown'}"
        )
        
        # Process request
        response = await call_next(request)
        
        # Calculate duration
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        # Log response
        self.logger.info(
            f"Response: {response.status_code} for {request.method} "
            f"{request.url.path} in {duration:.3f}s"
        )
        
        return response


def setup_logging(config: Dict[str, Any] = None) -> None:
    """Set up logging configuration.
    
    Args:
        config: Logging configuration dict. Uses LOGGING_CONFIG if None.
    """
    import logging.config
    import os
    
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    logging.config.dictConfig(config or LOGGING_CONFIG)