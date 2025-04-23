from sqlalchemy.orm import Session
from app.models import TodoCreate, TodoUpdate
from app.db_models import Todo
from typing import List, Optional

def get_all(db: Session) -> List[Todo]:
    return db.query(Todo).all()

def get_by_id(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create(db: Session, todo_create: TodoCreate) -> Todo:
    todo = Todo(
        title=todo_create.title,
        description=todo_create.description,
        completed=False
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    todo = get_by_id(db, todo_id)
    if not todo:
        return None
    if todo_update.title is not None:
        todo.title = todo_update.title
    if todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.completed is not None:
        todo.completed = todo_update.completed
    db.commit()
    db.refresh(todo)
    return todo

def delete(db: Session, todo_id: int) -> bool:
    todo = get_by_id(db, todo_id)
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True
