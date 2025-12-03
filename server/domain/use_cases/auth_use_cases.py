from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.usecase_interface import UseCase
from domain.services import PasswordHasher
from domain.exceptions import DuplicateUserError, InvalidCredentialsError
from domain.use_cases.validation import normalize_email, validate_password


class RegisterUserUseCase(UseCase):
    """Use case responsible for registering a new user."""

    def __init__(self, repository: UserRepository, password_hasher: PasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    def execute(self, email: str, password: str) -> User:
        normalized_email = normalize_email(email)
        valid_password = validate_password(password)

        if self._repository.get_by_email(normalized_email):
            raise DuplicateUserError("E-mail já registrado")

        password_hash = self._password_hasher.hash_password(valid_password)
        user = User(id=None, email=normalized_email, password_hash=password_hash)
        return self._repository.add(user)


class LoginUserUseCase(UseCase):
    """Use case responsible for authenticating a user."""

    def __init__(self, repository: UserRepository, password_hasher: PasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    def execute(self, email: str, password: str) -> User:
        normalized_email = normalize_email(email)
        valid_password = validate_password(password)

        user = self._repository.get_by_email(normalized_email)
        if not user:
            raise InvalidCredentialsError("E-mail inexistente")

        if not self._password_hasher.verify_password(valid_password, user.password_hash):
            raise InvalidCredentialsError("Email ou senha incorreto")

        return user
