import pytest

from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.use_cases.get_recipe import GetRecipeUseCase
from domain.exceptions import RecipeNotFound

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
    
def test_id_exists() -> None:
    repository = InMemoryRecipeRepository()
    use_case = GetRecipeUseCase(repository)

    testRecipe = Recipe("TEST", "TEST", "TEST", 10, None)
    repository.add(testRecipe)

    result = use_case.execute(1)
    assert result.id == 1
    assert result.titulo == testRecipe.titulo
    assert result.descricao == testRecipe.descricao
    assert result.modo_preparo == testRecipe.modo_preparo
    assert result.preco == testRecipe.preco

def test_id_does_not_exist() -> None:
    repository = InMemoryRecipeRepository()
    use_case = GetRecipeUseCase(repository)

    try:
        result = use_case.execute(45)
        assert False
    except RecipeNotFound:
            assert True

def test_multiple_ids_counter_consistent() -> None:
    repository = InMemoryRecipeRepository()
    use_case = GetRecipeUseCase(repository)

    testRecipe = Recipe("TEST", "TEST", "TEST", 10, None)
    testRecipe2 = Recipe("TEST2", "TEST2", "TEST2", 10, None)
    recipes = [testRecipe, testRecipe2]
    repository.add(testRecipe)
    repository.add(testRecipe2)

    results = [use_case.execute(1), use_case.execute(2)]
    for index,result in enumerate(results):
        assert result.id == (index + 1)
        assert result.titulo == recipes[index].titulo
        assert result.descricao == recipes[index].descricao
        assert result.modo_preparo == recipes[index].modo_preparo
        assert result.preco == recipes[index].preco
