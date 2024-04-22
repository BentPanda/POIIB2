from dataclasses import dataclass

from src.repositories import CreateUserInDBRequest
from src.repositories import UserRepository

users = []


@dataclass
class CreateUserRequest:
    name: str
    lastname: str


class CreateUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def create(self, request: CreateUserRequest) -> None:
        repository_req = CreateUserInDBRequest(
            name=request.name,
            lastname=request.lastname,
        )
        self._repository.create(repository_req)
