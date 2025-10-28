"""Tests for LLM routes."""
import json
from unittest.mock import patch, MagicMock


def test_generate_text_missing_prompt(client):
    """Test generate endpoint with missing prompt."""
    response = client.post(
        '/api/llm/generate',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    
    data = response.get_json()
    assert data['success'] is False
    assert 'prompt' in data['error']


def test_generate_text_success(client):
    """Test generate endpoint with valid prompt."""
    with patch('app.routes.llm_routes.get_llm_service') as mock_service:
        # Mock the LLM service response
        mock_llm = MagicMock()
        mock_llm.generate_text.return_value = {
            'success': True,
            'text': 'Generated response',
            'model': 'gemini-1.5-flash',
            'prompt': 'Test prompt'
        }
        mock_service.return_value = mock_llm
        
        response = client.post(
            '/api/llm/generate',
            data=json.dumps({'prompt': 'Test prompt'}),
            content_type='application/json'
        )
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['success'] is True
        assert data['text'] == 'Generated response'


def test_chat_missing_messages(client):
    """Test chat endpoint with missing messages."""
    response = client.post(
        '/api/llm/chat',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    
    data = response.get_json()
    assert data['success'] is False
    assert 'messages' in data['error']


def test_chat_empty_messages(client):
    """Test chat endpoint with empty messages list."""
    response = client.post(
        '/api/llm/chat',
        data=json.dumps({'messages': []}),
        content_type='application/json'
    )
    assert response.status_code == 400
    
    data = response.get_json()
    assert data['success'] is False


def test_chat_success(client):
    """Test chat endpoint with valid messages."""
    with patch('app.routes.llm_routes.get_llm_service') as mock_service:
        # Mock the LLM service response
        mock_llm = MagicMock()
        mock_llm.chat.return_value = {
            'success': True,
            'text': 'Chat response',
            'model': 'gemini-1.5-flash',
            'message_count': 2
        }
        mock_service.return_value = mock_llm
        
        response = client.post(
            '/api/llm/chat',
            data=json.dumps({
                'messages': [
                    {'role': 'user', 'content': 'Hello'},
                    {'role': 'assistant', 'content': 'Hi there!'}
                ]
            }),
            content_type='application/json'
        )
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['success'] is True
        assert data['text'] == 'Chat response'


def test_analyze_missing_text(client):
    """Test analyze endpoint with missing text."""
    response = client.post(
        '/api/llm/analyze',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    
    data = response.get_json()
    assert data['success'] is False
    assert 'text' in data['error']


def test_analyze_invalid_type(client):
    """Test analyze endpoint with invalid analysis type."""
    response = client.post(
        '/api/llm/analyze',
        data=json.dumps({
            'text': 'Sample text',
            'analysis_type': 'invalid_type'
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    
    data = response.get_json()
    assert data['success'] is False
    assert 'Invalid analysis_type' in data['error']


def test_analyze_success(client):
    """Test analyze endpoint with valid input."""
    with patch('app.routes.llm_routes.get_llm_service') as mock_service:
        # Mock the LLM service response
        mock_llm = MagicMock()
        mock_llm.analyze_text.return_value = {
            'success': True,
            'text': 'Analysis result',
            'model': 'gemini-1.5-flash',
            'analysis_type': 'summarize'
        }
        mock_service.return_value = mock_llm
        
        response = client.post(
            '/api/llm/analyze',
            data=json.dumps({
                'text': 'Sample text to analyze',
                'analysis_type': 'summarize'
            }),
            content_type='application/json'
        )
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['success'] is True
        assert data['text'] == 'Analysis result'
        assert data['analysis_type'] == 'summarize'
