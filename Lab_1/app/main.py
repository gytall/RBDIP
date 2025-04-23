# app/main.py
from fastapi import FastAPI
from app.routers import todo_router
from app.db_models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO API", description="Простое API для управления задачами")

app.include_router(todo_router.router)
