# app/main.py
from fastapi import FastAPI
from app.routers import todo_router, user_router

app = FastAPI(title="TODO API", description="Простое API для управления задачами")

app.include_router(todo_router.router)
app.include_router(user_router.router)