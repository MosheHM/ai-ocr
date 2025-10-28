# AI LLM Service

A scalable, modular Flask-based service for running LLM tasks using Google Gemini API.

## Features

- 🚀 **Modular Architecture**: Well-organized folders for scalability (routes, services, models, config)
- 🤖 **Google Gemini Integration**: Powered by [python-genai](https://github.com/googleapis/python-genai)
- 🔌 **RESTful API**: Clean API endpoints for text generation, chat, and text analysis
- ✅ **Comprehensive Tests**: Full test coverage with pytest
- 🔧 **Configurable**: Environment-based configuration management
- 📦 **Production-Ready**: Includes gunicorn for production deployment

## Project Structure

```
ai-ocr/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── config/               # Configuration management
│   │   ├── __init__.py
│   │   └── config.py
│   ├── routes/               # API routes
│   │   ├── __init__.py
│   │   ├── health_routes.py
│   │   └── llm_routes.py
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   └── llm_service.py
│   ├── models/               # Data models (future use)
│   │   └── __init__.py
│   └── utils/                # Utility functions (future use)
│       └── __init__.py
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_health_routes.py
│   ├── test_llm_routes.py
│   └── test_llm_service.py
├── .env.example              # Environment variables template
├── .gitignore
├── requirements.txt
├── run.py                    # Application entry point
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Cloud API key with Gemini API access

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MosheHM/ai-ocr.git
   cd ai-ocr
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Usage

### Running the Service

**Development mode**:
```bash
python run.py
```

**Production mode with gunicorn**:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

The service will be available at `http://localhost:5000`

### API Endpoints

#### Health Check
```bash
GET /health
```

Response:
```json
{
  "status": "healthy",
  "service": "LLM Service",
  "version": "1.0.0"
}
```

#### Service Status
```bash
GET /status
```

#### Generate Text
```bash
POST /api/llm/generate
Content-Type: application/json

{
  "prompt": "Write a short poem about AI",
  "temperature": 0.7,
  "max_tokens": 2048
}
```

Response:
```json
{
  "success": true,
  "text": "Generated text response...",
  "model": "gemini-1.5-flash",
  "prompt": "Write a short poem about AI"
}
```

#### Chat (Multi-turn Conversation)
```bash
POST /api/llm/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you!"},
    {"role": "user", "content": "What can you help me with?"}
  ],
  "temperature": 0.7,
  "max_tokens": 2048
}
```

#### Analyze Text
```bash
POST /api/llm/analyze
Content-Type: application/json

{
  "text": "Your text to analyze here...",
  "analysis_type": "summarize"
}
```

Analysis types: `summarize`, `sentiment`, `extract_keywords`

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app tests/
```

Run specific test file:

```bash
pytest tests/test_llm_service.py
```

## Configuration

The service supports multiple configuration environments:

- **Development**: Debug mode enabled, verbose logging
- **Production**: Optimized for production use
- **Testing**: Test configuration with mocked services

Set the environment using the `FLASK_ENV` variable:

```bash
export FLASK_ENV=production  # or development, testing
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_API_KEY` | Google Gemini API key | *Required* |
| `FLASK_ENV` | Environment (development/production/testing) | development |
| `FLASK_DEBUG` | Enable debug mode | True |
| `HOST` | Server host | 0.0.0.0 |
| `PORT` | Server port | 5000 |
| `DEFAULT_MODEL` | Gemini model to use | gemini-1.5-flash |
| `MAX_TOKENS` | Maximum tokens to generate | 2048 |
| `TEMPERATURE` | Sampling temperature | 0.7 |

## Development

### Adding New Features

1. **New API endpoint**: Add to `app/routes/`
2. **Business logic**: Add to `app/services/`
3. **Data models**: Add to `app/models/`
4. **Utilities**: Add to `app/utils/`
5. **Tests**: Add corresponding tests in `tests/`

### Code Style

Follow PEP 8 guidelines for Python code.

## Deployment

### Using Docker (Future Enhancement)

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
```

### Using systemd (Linux)

Create a service file at `/etc/systemd/system/llm-service.service`:

```ini
[Unit]
Description=LLM Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/ai-ocr
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 run:app

[Install]
WantedBy=multi-user.target
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Powered by [Google Gemini](https://ai.google.dev/)
- Uses [python-genai](https://github.com/googleapis/python-genai) 
