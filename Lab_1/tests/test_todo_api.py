import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "New Task"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "New Task"
    assert data["completed"] is False

def test_get_all_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_todo_by_id():
    response = client.get("/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "New Task"

def test_update_todo():
    response = client.put("/todos/1", json={"title": "Updated Task"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}
