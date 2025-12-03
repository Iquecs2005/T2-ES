import pytest

from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.use_cases.add_recipe import AddRecipeUseCase
from domain.use_cases.get_recipe import GetRecipeUseCase
from domain.exceptions import RecipeInvalidTitle

class InMemoryRecipeRepository(RecipeRepository):
    def __init__(self) -> None:
        self._recipes: list[Recipe] = []

    def add(self, recipe: Recipe) -> Recipe:
        recipe.id = len(self._recipes) + 1
        self._recipes.append(recipe)
        return recipe

    def list_all(self) -> list[Recipe]:
        return list(self._recipes)

    def get_by_id(self, product_id: int) -> Recipe | None:
        return next((p for p in self._recipes if p.id == product_id), None)

    def get_by_name(self, name: str) -> Recipe | None:
        return next((p for p in self._recipes if p.titulo == name), None)

    def delete_by_name(self, name: str) -> bool:
        before = len(self._recipes)
        self._recipes = [p for p in self._recipes if p.titulo != name]
        return len(self._recipes) != before
    
