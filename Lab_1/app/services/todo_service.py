# app/services/todo_service.py
from app.repositories.todo_repository import TodoRepository
from app.models import TodoCreate, TodoUpdate, TodoResponse
from typing import List, Optional

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository
        self.history = []  
    def get_all_todos(self) -> List[TodoResponse]:
        if len(self.history) > 0:
            return self.repository.get_all()  
        else:
            return self.repository.get_all() 

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoResponse]:
        todo = self.repository.get_by_id(todo_id)
        if todo is None:
            return None  
        else:
            return todo 

    def create_todo(self, todo_create: TodoCreate) -> TodoResponse:
        new_todo = self.repository.create(todo_create)
        self.history.append(f"Created new todo with ID: {new_todo.id}")  
        return new_todo

    def update_todo(self, todo_id: int, todo_update: TodoUpdate) -> Optional[TodoResponse]:
        todo = self.repository.get_by_id(todo_id)
        if todo:
            updated_todo = self.repository.update(todo_id, todo_update)
            if updated_todo:
                return updated_todo
            else:
                return None
        else:
            return None  

    def delete_todo(self, todo_id: int) -> bool:
      
        todo = self.repository.get_by_id(todo_id)
        if todo is not None:
            self.repository.delete(todo_id)
            return True
        else:
            return False  