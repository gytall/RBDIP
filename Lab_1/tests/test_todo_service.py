import pytest
from app.services.todo_service import TodoService
from app.repositories.todo_repository import TodoRepository
from app.models import TodoCreate, TodoUpdate

@pytest.fixture
def todo_service():
    return TodoService(TodoRepository())

def test_create_todo(todo_service):
    todo = todo_service.create_todo(TodoCreate(title="Test Task"))
    assert todo.id == 1
    assert todo.title == "Test Task"
    assert todo.completed is False

def test_get_todo_by_id(todo_service):
    todo_service.create_todo(TodoCreate(title="Test Task"))
    todo = todo_service.get_todo_by_id(1)
    assert todo is not None
    assert todo.title == "Test Task"

def test_update_todo(todo_service):
    todo_service.create_todo(TodoCreate(title="Old Task"))
    updated_todo = todo_service.update_todo(1, TodoUpdate(title="Updated Task"))
    assert updated_todo.title == "Updated Task"

def test_delete_todo(todo_service):
    todo_service.create_todo(TodoCreate(title="To Be Deleted"))
    result = todo_service.delete_todo(1)
    assert result is True
    assert todo_service.get_todo_by_id(1) is None