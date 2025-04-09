# app/repositories/user_repository.py
from app.models import UserCreate, UserUpdate, UserResponse
from typing import List, Optional

class UserRepository:
    def __init__(self):
        self.users = []
        self.counter = 1

    def get_all(self) -> List[UserResponse]:
        return self.users.copy()

    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create(self, user_create: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id=self.counter,
            username=user_create.username,
            email=user_create.email
        )
        self.users.append(new_user)
        self.counter += 1
        return new_user

    def update(self, user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        for user in self.users:
            if user.id == user_id:
                if user_update.username:
                    user.username = user_update.username
                if user_update.email:
                    user.email = user_update.email
                return user
        return None

    def delete(self, user_id: int) -> bool:
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
