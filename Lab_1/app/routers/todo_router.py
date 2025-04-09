from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.models import TodoCreate, TodoResponse, TodoUpdate
from app.services.todo_service import TodoService
from app.repositories.todo_repository import TodoRepository

router = APIRouter(prefix="/todos", tags=["Todos"])

todo_repository = TodoRepository() 

def get_todo_service() -> TodoService:
    return TodoService(todo_repository)

def get_todo_or_404(todo_id: int, service: TodoService) -> TodoResponse:
    todo = service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/", response_model=List[TodoResponse])
def get_todos(service: TodoService = Depends(get_todo_service)):
    """Получить список всех задач"""
    return service.get_all_todos()

@router.post("/", response_model=TodoResponse, status_code=201)
def create_todo(todo_create: TodoCreate, service: TodoService = Depends(get_todo_service)):
    """Создать новую задачу."""
    return service.create_todo(todo_create)

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    """Получить задачу"""
    return get_todo_or_404(todo_id, service)

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, service: TodoService = Depends(get_todo_service)):
    """Обновить задачу"""
    get_todo_or_404(todo_id, service)  
    return service.update_todo(todo_id, todo_update)

@router.delete("/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    """Удалить задачу"""
    get_todo_or_404(todo_id, service)  
    service.delete_todo(todo_id)
    return {"message": "Todo deleted successfully"}