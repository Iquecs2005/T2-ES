from domain.exceptions import InvalidCredentialsError
from domain.repositories import UserRepository
from domain.services import PasswordHasher
from domain.user import User
from use_cases.validation import normalize_email, validate_password


class LoginUserUseCase:
    def __init__(self, repository: UserRepository, password_hasher: PasswordHasher):
        self._repository = repository
        self._password_hasher = password_hasher

    def execute(self, email: str, password: str) -> User:
        normalized_email = normalize_email(email)
        valid_password = validate_password(password)

        user = self._repository.get_by_email(normalized_email)
        if not user:
            raise InvalidCredentialsError("Invalid email or password")

        if not self._password_hasher.verify_password(
            valid_password, user.password_hash
        ):
            raise InvalidCredentialsError("Invalid email or password")

        return user
