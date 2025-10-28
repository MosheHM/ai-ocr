"""LLM routes for the Flask application."""
from flask import Blueprint, request, jsonify
from app.services import LLMService
from app.config import Config

llm_bp = Blueprint('llm', __name__, url_prefix='/api/llm')


def get_llm_service():
    """Get an instance of the LLM service."""
    return LLMService(
        api_key=Config.GOOGLE_API_KEY,
        model=Config.DEFAULT_MODEL
    )


@llm_bp.route('/generate', methods=['POST'])
def generate_text():
    """
    Generate text from a prompt.
    
    Request body:
        {
            "prompt": "Your prompt here",
            "temperature": 0.7,  # optional
            "max_tokens": 2048   # optional
        }
    
    Returns:
        JSON response with generated text
    """
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: prompt'
            }), 400
        
        prompt = data['prompt']
        temperature = data.get('temperature', Config.TEMPERATURE)
        max_tokens = data.get('max_tokens', Config.MAX_TOKENS)
        
        llm_service = get_llm_service()
        result = llm_service.generate_text(
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to generate text'
            }), 500
            
    except Exception:
        return jsonify({
            'success': False,
            'error': 'An internal error occurred'
        }), 500


@llm_bp.route('/chat', methods=['POST'])
def chat():
    """
    Have a conversation with the LLM.
    
    Request body:
        {
            "messages": [
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi there!"},
                {"role": "user", "content": "How are you?"}
            ],
            "temperature": 0.7,  # optional
            "max_tokens": 2048   # optional
        }
    
    Returns:
        JSON response with the LLM's reply
    """
    try:
        data = request.get_json()
        
        if not data or 'messages' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: messages'
            }), 400
        
        messages = data['messages']
        temperature = data.get('temperature', Config.TEMPERATURE)
        max_tokens = data.get('max_tokens', Config.MAX_TOKENS)
        
        if not isinstance(messages, list) or len(messages) == 0:
            return jsonify({
                'success': False,
                'error': 'messages must be a non-empty list'
            }), 400
        
        llm_service = get_llm_service()
        result = llm_service.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to process chat request'
            }), 500
            
    except Exception:
        return jsonify({
            'success': False,
            'error': 'An internal error occurred'
        }), 500


@llm_bp.route('/analyze', methods=['POST'])
def analyze_text():
    """
    Analyze text using the LLM.
    
    Request body:
        {
            "text": "Text to analyze",
            "analysis_type": "summarize"  # or "sentiment", "extract_keywords"
        }
    
    Returns:
        JSON response with analysis results
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: text'
            }), 400
        
        text = data['text']
        analysis_type = data.get('analysis_type', 'summarize')
        
        valid_types = ['summarize', 'sentiment', 'extract_keywords']
        if analysis_type not in valid_types:
            return jsonify({
                'success': False,
                'error': f'Invalid analysis_type. Must be one of: {", ".join(valid_types)}'
            }), 400
        
        llm_service = get_llm_service()
        result = llm_service.analyze_text(
            text=text,
            analysis_type=analysis_type
        )
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to analyze text'
            }), 500
            
    except Exception:
        return jsonify({
            'success': False,
            'error': 'An internal error occurred'
        }), 500
