# tests/test_user_service.py

import pytest
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.models import UserCreate, UserUpdate

@pytest.fixture
def user_service():
    return UserService(UserRepository())

def test_create_user(user_service):
    user = user_service.create_user(UserCreate(username="johndoe", email="john@example.com", password="secure123"))
    assert user.id == 1
    assert user.username == "johndoe"
    assert user.email == "john@example.com"

def test_get_user_by_id(user_service):
    user_service.create_user(UserCreate(username="johndoe", email="john@example.com", password="secure123"))
    user = user_service.get_user_by_id(1)
    assert user is not None
    assert user.username == "johndoe"

def test_update_user(user_service):
    user_service.create_user(UserCreate(username="oldname", email="old@example.com", password="pass"))
    updated_user = user_service.update_user(1, UserUpdate(username="newname"))
    assert updated_user.username == "newname"

def test_delete_user(user_service):
    user_service.create_user(UserCreate(username="temp", email="temp@example.com", password="pass"))
    result = user_service.delete_user(1)
    assert result is True
    assert user_service.get_user_by_id(1) is None
