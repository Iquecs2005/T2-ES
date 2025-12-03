from domain.exceptions import DuplicateLogin
from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.usecase_interface import UseCase


class AddUserUseCase(UseCase):
    """Use case responsible for registering a new product."""

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, login: str, senha: str) -> User:
        if self._repository.duplicated_login(login):
            raise DuplicateLogin("Login already in use")

        user = User(login=login, senha=senha)
        return self._repository.add(user)
