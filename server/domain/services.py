from typing import Protocol


class PasswordHasher(Protocol):
    """Abstraction for hashing and verifying passwords."""

    def hash_password(self, password: str) -> str:
        ...

    def verify_password(self, password: str, password_hash: str) -> bool:
        ...
