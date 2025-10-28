"""LLM Service for Google Gemini integration."""
import os
from typing import Dict, List, Optional, Any
from google import genai
from google.genai import types


class LLMService:
    """Service class for interacting with Google Gemini LLM."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = 'gemini-1.5-flash'):
        """
        Initialize the LLM service.
        
        Args:
            api_key: Google API key for Gemini
            model: Model name to use (default: gemini-1.5-flash)
        """
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Google API key is required")
        
        self.model = model
        self.client = genai.Client(api_key=self.api_key)
    
    def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate text using the LLM.
        
        Args:
            prompt: The input prompt
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            **kwargs: Additional parameters for the model
        
        Returns:
            Dict containing the generated text and metadata
        """
        try:
            config = types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=config
            )
            
            return {
                'success': True,
                'text': response.text,
                'model': self.model,
                'prompt': prompt
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'model': self.model,
                'prompt': prompt
            }
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2048
    ) -> Dict[str, Any]:
        """
        Have a multi-turn conversation with the LLM.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        
        Returns:
            Dict containing the response and metadata
        """
        try:
            # Convert messages to Gemini format
            contents = []
            for msg in messages:
                role = 'user' if msg.get('role') == 'user' else 'model'
                contents.append(types.Content(
                    role=role,
                    parts=[types.Part(text=msg.get('content', ''))]
                ))
            
            config = types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=config
            )
            
            return {
                'success': True,
                'text': response.text,
                'model': self.model,
                'message_count': len(messages)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'model': self.model,
                'message_count': len(messages)
            }
    
    def analyze_text(
        self,
        text: str,
        analysis_type: str = 'summarize'
    ) -> Dict[str, Any]:
        """
        Analyze text using the LLM.
        
        Args:
            text: The text to analyze
            analysis_type: Type of analysis (summarize, sentiment, extract_keywords)
        
        Returns:
            Dict containing the analysis results
        """
        prompts = {
            'summarize': f"Summarize the following text concisely:\n\n{text}",
            'sentiment': f"Analyze the sentiment of the following text (positive, negative, or neutral):\n\n{text}",
            'extract_keywords': f"Extract the main keywords from the following text:\n\n{text}"
        }
        
        prompt = prompts.get(analysis_type, prompts['summarize'])
        result = self.generate_text(prompt)
        
        if result['success']:
            result['analysis_type'] = analysis_type
        
        return result
