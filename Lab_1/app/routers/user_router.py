# app/routers/user_router.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.models import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

user_repository = UserRepository()

def get_user_service() -> UserService:
    return UserService(user_repository)

def get_user_or_404(user_id: int, service: UserService) -> UserResponse:
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_create: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user_create)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return get_user_or_404(user_id, service)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, service: UserService = Depends(get_user_service)):
    get_user_or_404(user_id, service)
    return service.update_user(user_id, user_update)

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    get_user_or_404(user_id, service)
    service.delete_user(user_id)
    return {"message": "User deleted successfully"}
