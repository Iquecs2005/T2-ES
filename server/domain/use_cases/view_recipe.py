from domain.entities.recipe import Recipe
from domain.exceptions import RecipeNotFound
from domain.interfaces.recipe_repository import RecipeRepository
from domain.interfaces.usecase_interface import UseCase


class ViewRecipeUseCase(UseCase):
    """Use case responsible for retrieving a recipe by id."""

    def __init__(self, repository: RecipeRepository):
        self._repository = repository

    def execute(self, recipe_id: int) -> Recipe:
        recipe = self._repository.get_by_id(recipe_id)
        if recipe is None:
            raise RecipeNotFound(f"Receita com id {recipe_id} nao encontrada")
        return recipe
