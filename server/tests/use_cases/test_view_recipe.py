import pytest

from domain.entities.recipe import Recipe
from domain.exceptions import RecipeNotFound
from domain.interfaces.recipe_repository import RecipeRepository
from domain.use_cases.view_recipe import ViewRecipeUseCase


class InMemoryRecipeRepository(RecipeRepository):
    def __init__(self):
        self._items = {}
        self._next_id = 1

    def add(self, recipe: Recipe) -> Recipe:
        recipe.id = self._next_id
        self._items[self._next_id] = recipe
        self._next_id += 1
        return recipe

    def get_by_id(self, recipe_id: int):
        return self._items.get(recipe_id)


def test_returns_recipe_when_found():
    repo = InMemoryRecipeRepository()
    saved = repo.add(
        Recipe(titulo="Bolo", descricao="Bolo de chocolate", modo_preparo="Misturar", preco=10.0)
    )
    use_case = ViewRecipeUseCase(repo)

    result = use_case.execute(saved.id)

    assert result is saved
    assert result.titulo == "Bolo"


def test_raises_when_not_found():
    repo = InMemoryRecipeRepository()
    use_case = ViewRecipeUseCase(repo)

    with pytest.raises(RecipeNotFound):
        use_case.execute(123)
