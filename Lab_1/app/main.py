# app/main.py
from fastapi import FastAPI
from app.routers import todo_router

app = FastAPI(title="TODO API", description="Простое API для управления задачами")

# Подключаем маршруты
app.include_router(todo_router.router)
