"""Tests for LLM service."""
import pytest
from unittest.mock import patch, MagicMock
from app.services import LLMService


def test_llm_service_init_no_api_key():
    """Test LLM service initialization without API key."""
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="Google API key is required"):
            LLMService()


def test_llm_service_init_with_api_key():
    """Test LLM service initialization with API key."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        service = LLMService(api_key='test-key')
        assert service.api_key == 'test-key'
        assert service.model == 'gemini-1.5-flash'
        mock_client.assert_called_once_with(api_key='test-key')


def test_generate_text_success():
    """Test successful text generation."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = 'Generated text'
        
        mock_instance = MagicMock()
        mock_instance.models.generate_content.return_value = mock_response
        mock_client.return_value = mock_instance
        
        service = LLMService(api_key='test-key')
        result = service.generate_text('Test prompt')
        
        assert result['success'] is True
        assert result['text'] == 'Generated text'
        assert result['model'] == 'gemini-1.5-flash'
        assert result['prompt'] == 'Test prompt'


def test_generate_text_error():
    """Test text generation with error."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        mock_instance = MagicMock()
        mock_instance.models.generate_content.side_effect = Exception('API Error')
        mock_client.return_value = mock_instance
        
        service = LLMService(api_key='test-key')
        result = service.generate_text('Test prompt')
        
        assert result['success'] is False
        assert 'API Error' in result['error']


def test_chat_success():
    """Test successful chat."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = 'Chat response'
        
        mock_instance = MagicMock()
        mock_instance.models.generate_content.return_value = mock_response
        mock_client.return_value = mock_instance
        
        service = LLMService(api_key='test-key')
        messages = [
            {'role': 'user', 'content': 'Hello'},
            {'role': 'assistant', 'content': 'Hi there!'}
        ]
        result = service.chat(messages)
        
        assert result['success'] is True
        assert result['text'] == 'Chat response'
        assert result['message_count'] == 2


def test_analyze_text_summarize():
    """Test text analysis with summarize type."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = 'Summary of the text'
        
        mock_instance = MagicMock()
        mock_instance.models.generate_content.return_value = mock_response
        mock_client.return_value = mock_instance
        
        service = LLMService(api_key='test-key')
        result = service.analyze_text('Long text to summarize', 'summarize')
        
        assert result['success'] is True
        assert result['text'] == 'Summary of the text'
        assert result['analysis_type'] == 'summarize'


def test_analyze_text_sentiment():
    """Test text analysis with sentiment type."""
    with patch('app.services.llm_service.genai.Client') as mock_client:
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = 'Positive sentiment'
        
        mock_instance = MagicMock()
        mock_instance.models.generate_content.return_value = mock_response
        mock_client.return_value = mock_instance
        
        service = LLMService(api_key='test-key')
        result = service.analyze_text('Great product!', 'sentiment')
        
        assert result['success'] is True
        assert result['analysis_type'] == 'sentiment'
