import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_user():
    return {"user_id": 1, "username": "test", "role": "admin"}
