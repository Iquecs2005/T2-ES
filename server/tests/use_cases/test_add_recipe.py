import pytest

from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from domain.use_cases.add_recipe import AddRecipeUseCase
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


def test_execute_duplicate_products() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    created1 = use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo="Esquenta", preco=10.5)
    created2 = use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo="Esquenta", preco=10.5)

    assert created1.id == 1
    assert created2.id == 2
    assert created1.titulo == created2.titulo == "Arroz"
    assert created1.descricao == created2.descricao == "Desc"
    assert created1.modo_preparo == created2.modo_preparo == "Esquenta"
    assert created1.preco == created2.preco == 10.5
    assert repository.get_by_id(1) is created1
    assert repository.get_by_id(2) is created2

def test_execute_raises_titulo_not_string() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    testValues = [10, 10.5, ["alo"]]

    for value in testValues:
        try: 
            use_case.execute(titulo=value, descricao="Desc", modo_preparo="Esquenta", preco=10.5)
            assert False
        except TypeError:
            assert True

def test_execute_raises_descricao_not_string() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    testValues = [10, 10.5, ["alo"]]

    for value in testValues:
        try: 
            use_case.execute(titulo="Arroz", descricao=value, modo_preparo="Esquenta", preco=10.5)
            assert False
        except TypeError:
            assert True

def test_execute_raises_modo_preparo_not_string() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    testValues = [10, 10.5, ["alo"]]

    for value in testValues:
        try: 
            use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo=value, preco=10.5)
            assert False
        except TypeError:
            assert True

def test_execute_raises_preco_not_float() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    testValues = ["Ab", ["alo"]]

    for value in testValues:
        try: 
            use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo="Esquenta", preco=value)
            assert False
        except TypeError:
            assert True

def test_execute_raises_null_values() -> None:
    repository = InMemoryRecipeRepository()
    use_case = AddRecipeUseCase(repository)

    try:
        use_case.execute(titulo="", descricao="Desc", modo_preparo="Esquenta", preco=10.5)
        assert False
    except RecipeInvalidTitle:
        assert True
    
    try:
        use_case.execute(titulo="a"*141, descricao="Desc", modo_preparo="Esquenta", preco=10.5)
        assert False
    except RecipeInvalidTitle:
        assert True