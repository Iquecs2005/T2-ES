from typing import Optional

from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.interfaces.usecase_interface import UseCase

class AddRecipeUseCase(UseCase):
    """Use case responsible for registering a new product."""

    def __init__(self, repository: RecipeRepository):
        self._repository = repository

    def execute(
        self, titulo: str, descricao: str, modo_preparo: str, preco: float
    ) -> Recipe:
        recipe = Recipe(titulo=titulo, descricao=descricao, modo_preparo=modo_preparo, preco=preco)
        return self._repository.add(recipe)
