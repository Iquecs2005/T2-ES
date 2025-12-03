from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.user import User


class UserRepository(ABC):
    """Contract for user persistence."""

    @abstractmethod
    def add(self, user: User) -> User:
        """Persist a user and return the stored instance."""
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Retrieve a user by email or return None."""
        raise NotImplementedError
