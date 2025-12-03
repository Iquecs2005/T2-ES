from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.recipe import Recipe


class RecipeRepository(ABC):
    """Port defining the contract for Recipe persistence."""

    @abstractmethod
    def add(self, recipe: Recipe) -> Recipe:
        """Persist a recipe and return the stored instance."""

    @abstractmethod
    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        """Finds a recipe by id and returns the stored instance."""
