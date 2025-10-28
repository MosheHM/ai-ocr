# Quick Start Guide

Get the AI LLM Service up and running in 5 minutes!

## Prerequisites

- Python 3.8+
- Google API key with Gemini API access ([Get one here](https://aistudio.google.com/app/apikey))

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MosheHM/ai-ocr.git
cd ai-ocr
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Google API key
# Replace 'your_google_api_key_here' with your actual key
```

### 4. Run the Service

```bash
# Development mode
python run.py

# Or with make
make run
```

The service will start on `http://localhost:5000`

## Quick Test

### Test 1: Health Check

```bash
curl http://localhost:5000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "LLM Service",
  "version": "1.0.0"
}
```

### Test 2: Generate Text

```bash
curl -X POST http://localhost:5000/api/llm/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a haiku about AI",
    "temperature": 0.7
  }'
```

### Test 3: Chat

```bash
curl -X POST http://localhost:5000/api/llm/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "What is Flask?"}
    ]
  }'
```

### Test 4: Analyze Text

```bash
curl -X POST http://localhost:5000/api/llm/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Python is an amazing programming language for AI and ML.",
    "analysis_type": "sentiment"
  }'
```

## Using Python Example

```bash
# In one terminal, run the service
python run.py

# In another terminal, run the example
python examples/example_usage.py
```

## Docker Quick Start

If you prefer Docker:

```bash
# Build the image
docker build -t llm-service .

# Run with environment variable
docker run -p 5000:5000 -e GOOGLE_API_KEY=your_key_here llm-service

# Or use docker-compose
docker-compose up
```

## Running Tests

```bash
pytest -v tests/
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [examples/example_usage.py](examples/example_usage.py) for more examples
- Explore the [API documentation](#api-endpoints) in README.md
- Review [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute

## Common Issues

### Issue: "Google API key is required"

**Solution**: Make sure you've set `GOOGLE_API_KEY` in your `.env` file

### Issue: Port 5000 already in use

**Solution**: Change the port in `.env`:
```
PORT=8000
```

### Issue: Module not found

**Solution**: Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Getting Help

- Open an [issue on GitHub](https://github.com/MosheHM/ai-ocr/issues)
- Check the [README.md](README.md) for detailed documentation

---

Happy coding! 🚀
