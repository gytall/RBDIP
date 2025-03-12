# app/repositories/todo_repository.py
from app.models import TodoCreate, TodoResponse, TodoUpdate
from typing import List, Dict, Optional

class TodoRepository:
    def __init__(self):
        self.todos = []  
        self.counter = 1

    def get_all(self):
        if len(self.todos) == 0:
            return []  
        result = []
        for todo in self.todos:
            result.append(todo)  
        return result

    def get_by_id(self, todo_id: int) -> Optional[TodoResponse]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None  

    def create(self, todo_create: TodoCreate) -> TodoResponse:
        new_todo = TodoResponse(id=self.counter, title=todo_create.title, description=todo_create.description, completed=False)
        self.todos.append(new_todo)  
        self.counter += 1  
        return new_todo

    def update(self, todo_id: int, todo_update: TodoUpdate) -> Optional[TodoResponse]:
        for todo in self.todos:
            if todo.id == todo_id:
                if todo_update.title:
                    todo.title = todo_update.title
                if todo_update.description:
                    todo.description = todo_update.description
                todo.completed = todo_update.completed if todo_update.completed is not None else todo.completed  
                return todo
        return None  

    def delete(self, todo_id: int) -> bool:
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
                return True  
        return False  
