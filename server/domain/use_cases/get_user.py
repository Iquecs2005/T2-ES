from domain.exceptions import UserNotFound
from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.usecase_interface import UseCase


class GetUserUseCase(UseCase):
    """Use case responsible for registering a new product."""

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, login: str, senha: str) -> User:
        user = self._repository.get(login=login, senha=senha)
        print(login, senha)
        if not user:
            raise UserNotFound(f"User com login '{login}' nao encontrada")
        return user
