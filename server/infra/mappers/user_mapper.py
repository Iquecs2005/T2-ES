from domain.entities.user import User
from infra.db.models.user_model import UserModel


def to_domain(model: UserModel) -> User:
    return User(
        login=model.login,
        senha=model.senha,
        data_insercao=model.data_insercao,
    )
