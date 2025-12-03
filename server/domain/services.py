from typing import Protocol


class PasswordHasher(Protocol):
    """Abstração para hashing e verificação de senhas."""

    def hash_password(self, password: str) -> str:
        ...

    def verify_password(self, password: str, password_hash: str) -> bool:
        ...
