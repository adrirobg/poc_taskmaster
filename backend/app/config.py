"""Application configuration settings."""
import os
from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application
    app_name: str = "Personal PKM API"
    app_version: str = "1.0.0"
    debug: bool = Field(default=False, env="DEBUG")
    
    # Database
    database_file: str = Field(default="database.db", env="DATABASE_FILE")
    sql_echo: bool = Field(default=False, env="SQL_ECHO")
    
    # API
    api_token: Optional[str] = Field(default="default-dev-token", env="API_TOKEN")
    api_prefix: str = "/api/v1"
    
    # CORS
    cors_origins: list = Field(
        default=["http://localhost:3000", "http://localhost:5173"],
        env="CORS_ORIGINS"
    )
    
    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_file: str = Field(default="logs/app.log", env="LOG_FILE")
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create global settings instance
settings = Settings()