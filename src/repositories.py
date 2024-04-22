from dataclasses import dataclass
from typing import Generator

from sqlalchemy.orm import Session

from src.db_models import User
from src.db_flask import SessionFactory

users = []


@dataclass
class CreateUserInDBRequest:
    name: str
    lastname: str


class UserRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self._session = next(self.session(session_factory))

    def session(self, session_factory: SessionFactory) -> Generator[Session, None, None]:
        with session_factory() as session:
            yield session

    def create(self, request: CreateUserInDBRequest) -> None:
        user = User(name=request.name)
        self._session.add(user)
        self._session.commit()
