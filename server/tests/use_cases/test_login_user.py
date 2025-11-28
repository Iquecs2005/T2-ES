import pytest

from domain.exceptions import InvalidCredentialsError, ValidationError
from domain.user import User
from domain.repositories import UserRepository
from domain.services import PasswordHasher
from use_cases.login_user import LoginUserUseCase


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def add(self, user: User) -> User:
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


def test_logs_in_with_valid_credentials():
    repository = InMemoryUserRepository()
    hasher = FakePasswordHasher()
    repository.add(
        User(id=None, email="user@example.com", password_hash=hasher.hash_password("secret123"))
    )
    use_case = LoginUserUseCase(repository, hasher)

    user = use_case.execute("user@example.com", "secret123")

    assert user.email == "user@example.com"


def test_fails_with_wrong_password():
    repository = InMemoryUserRepository()
    hasher = FakePasswordHasher()
    repository.add(
        User(id=None, email="user@example.com", password_hash=hasher.hash_password("secret123"))
    )
    use_case = LoginUserUseCase(repository, hasher)

    with pytest.raises(InvalidCredentialsError):
        use_case.execute("user@example.com", "badpassword")


def test_requires_valid_email_format():
    repository = InMemoryUserRepository()
    hasher = FakePasswordHasher()
    use_case = LoginUserUseCase(repository, hasher)

    with pytest.raises(ValidationError):
        use_case.execute("invalid-email", "password123")
