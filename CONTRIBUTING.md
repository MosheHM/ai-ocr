# Contributing to AI LLM Service

Thank you for considering contributing to the AI LLM Service! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-ocr.git
   cd ai-ocr
   ```

3. **Set up the development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Running Tests

Always run tests before submitting changes:

```bash
# Run all tests
pytest -v tests/

# Run with coverage
pytest --cov=app tests/
```

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small

### Adding New Features

1. **Create tests first** (TDD approach recommended)
2. **Implement the feature** in the appropriate module:
   - API endpoints → `app/routes/`
   - Business logic → `app/services/`
   - Data models → `app/models/`
   - Utilities → `app/utils/`

3. **Update documentation** in README.md if needed
4. **Run tests** to ensure everything works

### Project Structure

```
ai-ocr/
├── app/
│   ├── config/      # Configuration management
│   ├── routes/      # API endpoints
│   ├── services/    # Business logic
│   ├── models/      # Data models
│   └── utils/       # Utility functions
├── tests/           # Test suite
└── examples/        # Usage examples
```

## Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub:
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure all tests pass

## Pull Request Guidelines

- **One feature per PR**: Keep PRs focused on a single feature or bug fix
- **Write tests**: All new features should have corresponding tests
- **Update documentation**: Update README.md and docstrings as needed
- **Pass CI/CD**: Ensure all automated checks pass
- **Clean commit history**: Use meaningful commit messages

## Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Test both success and error cases
- Mock external dependencies (like API calls)

Example:
```python
def test_generate_text_success(client):
    """Test successful text generation."""
    # Test implementation
```

### Test Coverage

Aim for at least 80% code coverage. Run:
```bash
pytest --cov=app tests/ --cov-report=html
```

## Adding Dependencies

If you need to add a new dependency:

1. Add it to `requirements.txt`
2. Document why it's needed in your PR
3. Ensure it doesn't conflict with existing dependencies

## Reporting Bugs

When reporting bugs, include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: How to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, etc.

## Feature Requests

We welcome feature requests! Please:

- Check if the feature has already been requested
- Clearly describe the feature and its use case
- Explain why it would be valuable

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

## Questions?

If you have questions, feel free to:
- Open an issue on GitHub
- Start a discussion in the repository

Thank you for contributing! 🎉
