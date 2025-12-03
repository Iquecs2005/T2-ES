from typing import Optional

from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.usecase_interface import UseCase

class AddUserUseCase(UseCase):
    """Use case responsible for registering a new product."""

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(
        self, login: str, senha: str
    ) -> User:
        user = User(login=login, senha=senha)
        return self._repository.add(user)
