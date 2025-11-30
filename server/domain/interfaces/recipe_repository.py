from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.recipe import Recipe


class RecipeRepository(ABC):
    """Port defining the contract for Recipe persistence."""

    @abstractmethod
    def add(self, recipe: Recipe) -> Recipe:
        """Persist a product and return the stored instance."""

    @abstractmethod
    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        """Return the recipe with the given id, or None if not found."""
