import pytest

from domain.exceptions import DuplicateUserError, ValidationError
from domain.user import User
from domain.repositories import UserRepository
from domain.services import PasswordHasher
from use_cases.register_user import RegisterUserUseCase


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def add(self, user: User) -> User:
        if any(saved.email == user.email for saved in self._users.values()):
            raise DuplicateUserError("Email already registered")
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


def build_use_case():
    return RegisterUserUseCase(InMemoryUserRepository(), FakePasswordHasher())


def test_registers_new_user_with_hashed_password():
    use_case = build_use_case()

    user = use_case.execute("User@Email.com", "strongpass")

    assert user.id == 1
    assert user.email == "user@email.com"
    assert user.password_hash == "hashed-strongpass"


def test_raises_error_when_email_exists():
    use_case = build_use_case()
    use_case.execute("test@example.com", "password123")

    with pytest.raises(DuplicateUserError):
        use_case.execute("test@example.com", "anotherpass")


def test_requires_valid_email():
    use_case = build_use_case()

    with pytest.raises(ValidationError):
        use_case.execute("invalid-email", "password123")
