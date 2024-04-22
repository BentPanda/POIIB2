from unittest.mock import Mock

import pytest

from src.controllers import CreateUserController
from src.controllers import CreateUserRequest
from src.repositories import UserRepository
from src.repositories import CreateUserInDBRequest


@pytest.fixture
def repository() -> Mock:
    return Mock(UserRepository)


@pytest.fixture
def controller(repository: Mock) -> CreateUserController:
    return CreateUserController(repository=repository)


def test_exists_create_user_controller(
    controller: CreateUserController,
) -> None:
    assert isinstance(controller, CreateUserController)


def test_user_repository_is_called(
    controller: CreateUserController,
    repository: Mock,
) -> None:
    controller_req = CreateUserRequest(
        name="Wojciech",
        lastname="Oczkowski",
    )
    repository_req = CreateUserInDBRequest(
        name="Wojciech",
        lastname="Oczkowski",
    )
    controller.create(controller_req)
    repository.create.assert_called_with(repository_req )
