import os
from datetime import timedelta

class Config:
    """Application configuration"""

    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False

    # Application
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'yaml', 'yml'}
    UPLOAD_FOLDER = '/tmp/yaml-validator-uploads'

    # Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True if os.environ.get('FLASK_ENV') == 'production' else False
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    # Features
    ENABLE_SCHEMA_VALIDATION = True
    ENABLE_LINTING = True
    ENABLE_GITHUB_INTEGRATION = os.environ.get('ENABLE_GITHUB', 'false').lower() == 'true'

    # Rate limiting (simplified)
    RATE_LIMIT = 100  # requests per minute

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

    # GitHub integration
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
    GITHUB_API_URL = 'https://api.github.com'

    @staticmethod
    def init_app(app):
        """Initialize application configuration"""
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
