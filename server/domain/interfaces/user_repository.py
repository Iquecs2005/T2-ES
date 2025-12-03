from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.user import User


class UserRepository(ABC):
    """Port defining the contract for Recipe persistence."""

    @abstractmethod
    def add(self, user: User) -> User:
        """Persist a recipe and return the stored instance."""

    @abstractmethod
    def get(self, login: str, senha: str) -> Optional[User]:
        """Finds a recipe by id and returns the stored instance."""
