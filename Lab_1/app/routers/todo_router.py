from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import TodoCreate, TodoUpdate, TodoResponse
from app.repositories import todo_repository
from app.database import get_db

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=List[TodoResponse])
def get_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return todo_repository.get_all(db)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_repository.get_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/", response_model=TodoResponse, status_code=201)
def create_todo(todo_create: TodoCreate, db: Session = Depends(get_db)):
    todo = todo_repository.create(db, todo_create)
    db.commit()                 
    db.refresh(todo)           
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    todo = todo_repository.update(db, todo_id, todo_update)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.commit()               
    db.refresh(todo)          
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    success = todo_repository.delete(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.commit()                 
    return {"message": "Todo deleted successfully"}
