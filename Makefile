.PHONY: help install test run clean docker-build docker-run lint

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make test          - Run tests"
	@echo "  make run           - Run the Flask development server"
	@echo "  make run-prod      - Run with gunicorn"
	@echo "  make clean         - Clean up generated files"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run with Docker Compose"
	@echo "  make lint          - Run code linting"
	@echo "  make example       - Run example usage script"

install:
	pip install -r requirements.txt

test:
	pytest -v tests/

test-cov:
	pytest --cov=app tests/ --cov-report=html

run:
	python run.py

run-prod:
	gunicorn -w 4 -b 0.0.0.0:5000 run:app

example:
	python examples/example_usage.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

docker-build:
	docker build -t llm-service:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

lint:
	@echo "Linting Python files..."
	python -m pylint app/ tests/ --disable=missing-docstring || true
