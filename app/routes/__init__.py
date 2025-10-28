"""Routes package initialization."""
from .llm_routes import llm_bp
from .health_routes import health_bp

__all__ = ['llm_bp', 'health_bp']
