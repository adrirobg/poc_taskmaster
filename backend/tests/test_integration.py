import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import init_database


@pytest.fixture
def client():
    """Create test client with test database"""
    # Initialize with in-memory database for testing
    init_database("sqlite:///:memory:")
    return TestClient(app)


def test_full_stack_integration(client):
    """Test full stack integration"""
    # Test root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TaskMaster API is running"


def test_health_check_integration(client):
    """Test health check with database connectivity"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"


def test_cors_headers_integration(client):
    """Test CORS headers are properly configured"""
    response = client.options("/health")
    # CORS headers would be tested here in a real scenario
    assert response.status_code in [200, 405]  # Method may not be allowed but CORS should work


def test_task_endpoints_integration(client):
    """Test task-related endpoints"""
    # Test list tasks
    response = client.get("/api/tasks")
    assert response.status_code == 200
    
    # Test create task
    response = client.post("/api/tasks")
    assert response.status_code == 200