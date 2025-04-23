# app/models.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None  

class TodoResponse(TodoBase):
    id: int
    completed: bool

