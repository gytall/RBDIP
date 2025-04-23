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
        new_user = self._build_user(user_create)
        self.users.append(new_user)
        self.counter += 1
        return new_user

    def _build_user(self, user_create: UserCreate) -> UserResponse:
        return UserResponse(
            id=self.counter,
            username=user_create.username,
            email=user_create.email
        )

    def update(self, user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        user = self.get_by_id(user_id)
        if user:
            self._apply_user_update(user, user_update)
            return user
        return None

    def _apply_user_update(self, user: UserResponse, update: UserUpdate) -> None:
        if update.username:
            user.username = update.username
        if update.email:
            user.email = update.email


    def delete(self, user_id: int) -> bool:
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
