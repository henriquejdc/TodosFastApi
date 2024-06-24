from fastapi import status
from fastapi.testclient import TestClient

from main import app


def test_get_todos():
    test_client = TestClient(app)
    response = test_client.get("/todo")
    assert response.status_code == status.HTTP_200_OK
    todos = response.json()
    assert len(todos) == 2
    assert todos[0]["name"] == "First Todo"


def test_get_todo_by_id():
    test_client = TestClient(app)
    todo_id = "60af884a6d1b2c6b55b0d36c"
    response = test_client.get(f"/todo/{todo_id}")
    assert response.status_code == status.HTTP_200_OK
    todo = response.json()
    assert todo["name"] == "First Todo"


def test_get_todo_not_found():
    test_client = TestClient(app)
    todo_id = "60af884a6d1b2c6b55b0d36e"  # ID inexistente
    response = test_client.get(f"/todo/{todo_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_todo():
    test_client = TestClient(app)
    new_todo = {"name": "New Todo", "description": "This is a new todo", "completed": False}
    response = test_client.post("/todo", json=new_todo)
    assert response.status_code == status.HTTP_201_CREATED
    todo = response.json()
    assert todo["name"] == "New Todo"


def test_update_todo():
    test_client = TestClient(app)
    todo_id = "60af884a6d1b2c6b55b0d36c"
    updated_todo = {"name": "Updated Todo", "description": "This is an updated todo", "completed": False}
    response = test_client.put(f"/todo/{todo_id}", json=updated_todo)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_todo():
    test_client = TestClient(app)
    todo_id = "60af884a6d1b2c6b55b0d36c"
    response = test_client.delete(f"/todo/{todo_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
