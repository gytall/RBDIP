from sqlalchemy.orm import Session
from app.models import TodoCreate, TodoUpdate
from app.db_models import Todo
from typing import List, Optional


def get_all(db: Session, skip: int = 0, limit: int = 10) -> List[Todo]:
    return db.query(Todo).order_by(Todo.id).offset(skip).limit(limit).all()


def get_by_id(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create(db: Session, todo_create: TodoCreate) -> Todo:
    todo = Todo(
        title=todo_create.title,
        description=todo_create.description,
        completed=False
    )
    db.add(todo)
    return todo


def update(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    result = db.query(Todo).filter(Todo.id == todo_id).first()
    if not result:
        return None

    if todo_update.title is not None:
        result.title = todo_update.title
    if todo_update.description is not None:
        result.description = todo_update.description
    if todo_update.completed is not None:
        result.completed = todo_update.completed

    return result


def delete(db: Session, todo_id: int) -> bool:
    result = db.query(Todo).filter(Todo.id == todo_id).delete(synchronize_session=False)
    return result > 0
