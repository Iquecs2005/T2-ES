import pytest

from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.use_cases.add_user import AddUserUseCase
from domain.use_cases.get_user import GetUserUseCase
from domain.exceptions import UserNotFound

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: list[User] = []

    def add(self, user: User) -> User:
        self._users.append(user)
        return user

    def get(self, login: str, senha: str) -> User | None:
        for u in self._users:
            if u.login == login and u.senha == senha:
                return u
        return None
    
    def duplicated_login(self, login: str) -> bool:
        for u in self._users:
            if u.login == login:
                return True
        return False


def test_execute_get_new_user() -> None:
    repository = InMemoryUserRepository()
    add_use_case = AddUserUseCase(repository)
    get_use_case = GetUserUseCase(repository)

    created = add_use_case.execute(login='John', senha='abc')

    assert created.login == "John"
    assert created.senha == "abc"
    assert repository.get("John", "abc") is created

    user = get_use_case.execute(login='John', senha='abc')

    assert created is user


def test_execute_get_null_user() -> None:
    repository = InMemoryUserRepository()
    get_use_case = GetUserUseCase(repository)

    try:
        user = get_use_case.execute(login='John', senha='abc')
        assert False
    except UserNotFound:
        assert True

def test_execute_get_incorrect_senha() -> None:
    repository = InMemoryUserRepository()
    add_use_case = AddUserUseCase(repository)
    get_use_case = GetUserUseCase(repository)

    created = add_use_case.execute(login='John', senha='abc')

    assert created.login == "John"
    assert created.senha == "abc"
    assert repository.get("John", "abc") is created

    try:
        user = get_use_case.execute(login='John', senha='abcd')
        assert False
    except UserNotFound:
        assert True

# def test_execute_raises_titulo_not_string() -> None:
#     repository = InMemoryRecipeRepository()
#     use_case = AddRecipeUseCase(repository)

#     testValues = [10, 10.5, ["alo"]]

#     for value in testValues:
#         try: 
#             use_case.execute(titulo=value, descricao="Desc", modo_preparo="Esquenta", preco=10.5)
#             assert False
#         except TypeError:
#             assert True

# def test_execute_raises_descricao_not_string() -> None:
#     repository = InMemoryRecipeRepository()
#     use_case = AddRecipeUseCase(repository)

#     testValues = [10, 10.5, ["alo"]]

#     for value in testValues:
#         try: 
#             use_case.execute(titulo="Arroz", descricao=value, modo_preparo="Esquenta", preco=10.5)
#             assert False
#         except TypeError:
#             assert True

# def test_execute_raises_modo_preparo_not_string() -> None:
#     repository = InMemoryRecipeRepository()
#     use_case = AddRecipeUseCase(repository)

#     testValues = [10, 10.5, ["alo"]]

#     for value in testValues:
#         try: 
#             use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo=value, preco=10.5)
#             assert False
#         except TypeError:
#             assert True

# def test_execute_raises_preco_not_float() -> None:
#     repository = InMemoryRecipeRepository()
#     use_case = AddRecipeUseCase(repository)

#     testValues = ["Ab", ["alo"]]

#     for value in testValues:
#         try: 
#             use_case.execute(titulo="Arroz", descricao="Desc", modo_preparo="Esquenta", preco=value)
#             assert False
#         except TypeError:
#             assert True

# def test_execute_raises_null_values() -> None:
#     repository = InMemoryRecipeRepository()
#     use_case = AddRecipeUseCase(repository)

#     try:
#         use_case.execute(titulo="", descricao="Desc", modo_preparo="Esquenta", preco=10.5)
#         assert False
#     except RecipeInvalidTitle:
#         assert True
    
#     try:
#         use_case.execute(titulo="a"*141, descricao="Desc", modo_preparo="Esquenta", preco=10.5)
#         assert False
#     except RecipeInvalidTitle:
#         assert True