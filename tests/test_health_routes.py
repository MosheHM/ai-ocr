"""Tests for health and status routes."""


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'LLM Service'
    assert 'version' in data


def test_status(client):
    """Test the status endpoint."""
    response = client.get('/status')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'running'
    assert data['service'] == 'LLM Service'
    assert 'endpoints' in data
    assert 'generate' in data['endpoints']
    assert 'chat' in data['endpoints']
    assert 'analyze' in data['endpoints']
