"""Application configuration management."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application settings
    app_title: str = "AI Engineer Portfolio"
    app_description: str = "Professional AI Engineering Portfolio"
    debug: bool = False
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Contact settings
    contact_email: str = "contact@aiportfolio.com"
    github_username: str = "your-github"
    linkedin_url: str = "https://linkedin.com/in/your-profile"
    
    # External API settings
    github_api_url: str = "https://api.github.com"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()