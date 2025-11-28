from domain.exceptions import DuplicateUserError
from domain.repositories import UserRepository
from domain.services import PasswordHasher
from domain.user import User
from use_cases.validation import normalize_email, validate_password


class RegisterUserUseCase:
    def __init__(self, repository: UserRepository, password_hasher: PasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    def execute(self, email: str, password: str) -> User:
        normalized_email = normalize_email(email)
        valid_password = validate_password(password)

        if self._repository.get_by_email(normalized_email):
            raise DuplicateUserError("Email already registered")

        password_hash = self._password_hasher.hash_password(valid_password)
        user = User(id=None, email=normalized_email, password_hash=password_hash)

        return self._repository.add(user)
