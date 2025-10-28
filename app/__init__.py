"""Flask application factory."""
from flask import Flask
from app.config import config
from app.routes import llm_bp, health_bp
import os


def create_app(config_name: str = None):
    """
    Create and configure the Flask application.
    
    Args:
        config_name: Configuration name (development, production, testing)
    
    Returns:
        Configured Flask application
    """
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(llm_bp)
    
    # Add CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    return app
