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
        new_todo = self._build_todo(todo_create)
        self.todos.append(new_todo)
        self.counter += 1
        return new_todo

    def _build_todo(self, todo_create: TodoCreate) -> TodoResponse:
        return TodoResponse(
            id=self.counter,
            title=todo_create.title,
            description=todo_create.description,
            completed=False
        )

    def update(self, todo_id: int, todo_update: TodoUpdate) -> Optional[TodoResponse]:
        todo = self.get_by_id(todo_id)
        if todo:
            self._apply_todo_update(todo, todo_update)
            return todo
        return None

    def _apply_todo_update(self, todo: TodoResponse, update: TodoUpdate) -> None:
        if update.title:
            todo.title = update.title
        if update.description:
            todo.description = update.description
        if update.completed is not None:
            todo.completed = update.completed
    

    def delete(self, todo_id: int) -> bool:
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
                return True  
        return False  
