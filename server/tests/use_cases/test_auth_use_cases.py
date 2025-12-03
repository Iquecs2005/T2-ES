import pytest

from domain.entities.user import User
from domain.exceptions import (
    DuplicateUserError,
    InvalidCredentialsError,
    ValidationError,
)
from domain.interfaces.user_repository import UserRepository
from domain.services import PasswordHasher
from domain.use_cases.auth_use_cases import (
    LoginUserUseCase,
    RegisterUserUseCase,
)


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users = {}
        self._next_id = 1

    def add(self, user: User) -> User:
        if any(saved.email == user.email for saved in self._users.values()):
            raise DuplicateUserError("E-mail já registrado")
        created = User(
            id=self._next_id,
            email=user.email,
            password_hash=user.password_hash,
        )
        self._users[self._next_id] = created
        self._next_id += 1
        return created

    def get_by_email(self, email: str):
        return next((user for user in self._users.values() if user.email == email), None)


class FakePasswordHasher(PasswordHasher):
    def hash_password(self, password: str) -> str:
        return f"hashed-{password}"

    def verify_password(self, password: str, password_hash: str) -> bool:
        return password_hash == f"hashed-{password}"


def build_use_cases():
    repo = InMemoryUserRepository()
    hasher = FakePasswordHasher()
    return RegisterUserUseCase(repo, hasher), LoginUserUseCase(repo, hasher)


def test_register_new_user_with_hash():
    register_use_case, _ = build_use_cases()

    user = register_use_case.execute("User@Email.com", "strongpass")

    assert user.id == 1
    assert user.email == "user@email.com"
    assert user.password_hash == "hashed-strongpass"


def test_register_duplicate_email_raises_error():
    register_use_case, _ = build_use_cases()
    register_use_case.execute("test@example.com", "password123")

    with pytest.raises(DuplicateUserError):
        register_use_case.execute("test@example.com", "anotherpass")


def test_register_invalid_email():
    register_use_case, _ = build_use_cases()

    with pytest.raises(ValidationError):
        register_use_case.execute("invalid-email", "password123")


def test_login_with_valid_credentials():
    register_use_case, login_use_case = build_use_cases()
    register_use_case.execute("user@example.com", "secret123")

    user = login_use_case.execute("user@example.com", "secret123")

    assert user.email == "user@example.com"


def test_login_with_wrong_password():
    register_use_case, login_use_case = build_use_cases()
    register_use_case.execute("user@example.com", "secret123")

    with pytest.raises(InvalidCredentialsError):
        login_use_case.execute("user@example.com", "badpassword")


def test_login_with_invalid_email_format():
    _, login_use_case = build_use_cases()

    with pytest.raises(ValidationError):
        login_use_case.execute("invalid-email", "password123")

