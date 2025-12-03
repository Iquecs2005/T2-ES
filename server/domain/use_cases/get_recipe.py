from typing import Optional

from domain.exceptions import RecipeNotFound
from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.interfaces.usecase_interface import UseCase

class GetRecipeUseCase(UseCase):
    """Use case responsible for registering a new product."""

    def __init__(self, repository: RecipeRepository):
        self._repository = repository

    def execute(
        self, id: int
    ) -> Recipe:
        recipe = self._repository.get_by_id(id)
        if not recipe:
            raise RecipeNotFound(f"Receita com id '{id}' nao encontrada")
        return recipe
