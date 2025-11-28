from typing import Optional, Protocol

from domain.user import User


class UserRepository(Protocol):
    """Abstraction for user persistence."""

    def add(self, user: User) -> User:
        ...

    def get_by_email(self, email: str) -> Optional[User]:
        ...
