"""
Example script demonstrating how to use the LLM service.

This script shows how to interact with the Flask LLM service API.
Make sure the service is running before executing this script.

Run the service first:
    python run.py

Then run this example:
    python examples/example_usage.py
"""
import requests
import json


# Base URL for the service
BASE_URL = "http://localhost:5000"


def check_health():
    """Check if the service is healthy."""
    print("\n=== Health Check ===")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False


def get_status():
    """Get service status."""
    print("\n=== Service Status ===")
    response = requests.get(f"{BASE_URL}/status")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def generate_text_example():
    """Example of text generation."""
    print("\n=== Text Generation Example ===")
    
    payload = {
        "prompt": "Write a short poem about artificial intelligence",
        "temperature": 0.7,
        "max_tokens": 200
    }
    
    response = requests.post(
        f"{BASE_URL}/api/llm/generate",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    
    if result.get('success'):
        print(f"\nPrompt: {result['prompt']}")
        print(f"Model: {result['model']}")
        print(f"\nGenerated Text:\n{result['text']}")
    else:
        print(f"Error: {result.get('error')}")


def chat_example():
    """Example of multi-turn conversation."""
    print("\n=== Chat Example ===")
    
    payload = {
        "messages": [
            {"role": "user", "content": "Hello! What is machine learning?"},
            {"role": "assistant", "content": "Machine learning is a subset of AI that enables systems to learn from data."},
            {"role": "user", "content": "Can you give me a simple example?"}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }
    
    response = requests.post(
        f"{BASE_URL}/api/llm/chat",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    
    if result.get('success'):
        print(f"Model: {result['model']}")
        print(f"Message Count: {result['message_count']}")
        print(f"\nResponse:\n{result['text']}")
    else:
        print(f"Error: {result.get('error')}")


def analyze_text_example():
    """Example of text analysis."""
    print("\n=== Text Analysis Example ===")
    
    sample_text = """
    Artificial intelligence is transforming the world in remarkable ways.
    From healthcare to transportation, AI is solving complex problems and
    creating new opportunities. Machine learning algorithms can now diagnose
    diseases, predict traffic patterns, and even create art. The future of
    AI holds immense potential for improving human lives.
    """
    
    # Summarize
    print("\n--- Summarization ---")
    payload = {
        "text": sample_text,
        "analysis_type": "summarize"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/llm/analyze",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    if result.get('success'):
        print(f"Summary:\n{result['text']}")
    
    # Sentiment Analysis
    print("\n--- Sentiment Analysis ---")
    payload = {
        "text": sample_text,
        "analysis_type": "sentiment"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/llm/analyze",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    if result.get('success'):
        print(f"Sentiment:\n{result['text']}")
    
    # Extract Keywords
    print("\n--- Keyword Extraction ---")
    payload = {
        "text": sample_text,
        "analysis_type": "extract_keywords"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/llm/analyze",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    if result.get('success'):
        print(f"Keywords:\n{result['text']}")


def main():
    """Run all examples."""
    print("=" * 60)
    print("LLM Service API Examples")
    print("=" * 60)
    
    # Check if service is running
    if not check_health():
        print("\n⚠️  Service is not running!")
        print("Please start the service first: python run.py")
        return
    
    # Get service status
    get_status()
    
    print("\n" + "=" * 60)
    print("Note: The following examples require a valid Google API key")
    print("Set GOOGLE_API_KEY in your .env file")
    print("=" * 60)
    
    try:
        # Run examples (these will fail if no API key is set)
        generate_text_example()
        chat_example()
        analyze_text_example()
    except Exception as e:
        print(f"\nError running examples: {str(e)}")
        print("Make sure you have set GOOGLE_API_KEY in your .env file")
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
