import pytest
from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.use_cases.add_recipe import AddRecipeUseCase


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
        return next((p for p in self._recipes if p.nome == name), None)

    def delete_by_name(self, name: str) -> bool:
        before = len(self._recipes)
        self._recipes = [p for p in self._recipes if p.nome != name]
        return len(self._recipes) != before


def test_execute_adds_new_product() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    created = use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo="Esquenta", preco=10.5)

    assert created.id == 1
    assert created.titulo == "Arroz"
    assert created.descricao == "Desc"
    assert created.modo_preparo == "Esquenta"
    assert created.preco == 10.5
    assert repository.get_by_name("Arroz") is created


def test_execute_raises_when_product_already_exists() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    created = use_case.execute(nome="Arroz", quantidade=2, valor=10.5)

    with pytest.raises(ProductAlreadyExists):
        use_case.execute(nome="Arroz", quantidade=2, valor=10.5)