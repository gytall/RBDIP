# app/services/user_service.py

from app.repositories.user_repository import UserRepository
from app.models import UserCreate, UserUpdate, UserResponse
from typing import List, Optional

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.history = []  

    def get_all_users(self) -> List[UserResponse]:
        if len(self.history) > 0:
            return self.repository.get_all()
        else:
            return self.repository.get_all()

    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        user = self.repository.get_by_id(user_id)
        if user is None:
            return None
        else:
            return user

    def create_user(self, user_create: UserCreate) -> UserResponse:
        new_user = self.repository.create(user_create)
        self.history.append(f"Created new user with ID: {new_user.id}")
        return new_user

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        user = self.repository.get_by_id(user_id)
        if user:
            updated_user = self.repository.update(user_id, user_update)
            if updated_user:
                return updated_user
            else:
                return None
        else:
            return None

    def delete_user(self, user_id: int) -> bool:
        user = self.repository.get_by_id(user_id)
        if user is not None:
            self.repository.delete(user_id)
            return True
        else:
            return False
