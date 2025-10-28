"""Health check and status routes."""
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    Returns:
        JSON response with service health status
    """
    return jsonify({
        'status': 'healthy',
        'service': 'LLM Service',
        'version': '1.0.0'
    }), 200


@health_bp.route('/status', methods=['GET'])
def status():
    """
    Service status endpoint.
    
    Returns:
        JSON response with detailed service status
    """
    return jsonify({
        'status': 'running',
        'service': 'LLM Service',
        'version': '1.0.0',
        'endpoints': {
            'generate': '/api/llm/generate',
            'chat': '/api/llm/chat',
            'analyze': '/api/llm/analyze'
        }
    }), 200
