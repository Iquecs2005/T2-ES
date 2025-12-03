from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from domain.use_cases.add_user import AddUserUseCase
from domain.exceptions import DuplicateLogin


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


def test_execute_adds_new_user() -> None:
    repository = InMemoryUserRepository()
    use_case = AddUserUseCase(repository)

    created = use_case.execute(login="John", senha="abc")

    assert created.login == "John"
    assert created.senha == "abc"
    assert repository.get("John", "abc") is created


def test_execute_duplicate_user() -> None:
    repository = InMemoryUserRepository()
    use_case = AddUserUseCase(repository)

    use_case.execute(login="John", senha="abc")
    try:
        use_case.execute(login="John", senha="abc")
        assert False
    except DuplicateLogin:
        assert True
