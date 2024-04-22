from src.repositories import UserRepository
from src.repositories import users


def test_exists_user_repository():
    actual = UserRepository()
    assert isinstance(actual, UserRepository)


def test_add_user_to_users() -> None:
    repository = UserRepository()
    user = {"name": "Wojciech", "lastname": "Oczkowski"}
    repository.create(user)
    assert user in users
