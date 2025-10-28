"""Configuration module for the LLM service."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Base configuration class."""
    
    # Flask config
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Google Gemini API config
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Server config
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    
    # LLM config
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gemini-1.5-flash')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2048))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    GOOGLE_API_KEY = 'test-key'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
