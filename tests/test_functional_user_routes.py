import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def sample_user():
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_user(sample_user):
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 200
    assert response.json() == sample_user

def test_create_user_duplicate_email(sample_user):
    client.post("/users/", json=sample_user)
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_get_user(sample_user):
    client.post("/users/", json=sample_user)
    response = client.get(f"/users/{sample_user['id']}")
    assert response.status_code == 200
    assert response.json() == sample_user

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user(sample_user):
    client.post("/users/", json=sample_user)
    response = client.delete(f"/users/{sample_user['id']}")
    assert response.status_code == 204

def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
