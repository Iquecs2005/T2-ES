from typing import Callable, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from domain.entities.user import User
from domain.interfaces.user_repository import UserRepository
from infra.db.models.user_model import UserModel
from infra.mappers import user_mapper


class SqlAlchemyUserRepository(UserRepository):
    """SQLAlchemy implementation of the recipe repository port."""

    def __init__(self, session_factory: Callable[[], Session]):
        self._session_factory = session_factory

    def add(self, user: User) -> User:
        session = self._session_factory()
        try:
            model = UserModel(
                login=user.login,
                senha=user.senha,
                data_insercao=user.data_insercao,
            )

            session.add(model)
            session.commit()
            session.refresh(model)
            return user_mapper.to_domain(model)
        except IntegrityError:
            session.rollback()
            raise
        except Exception as error:
            session.rollback()
            print(error)
            raise
        finally:
            session.close()

    def get(self, login: str, senha: str) -> Optional[User]:
        session = self._session_factory()
        try:
            model = (
                session.query(UserModel)
                .filter(UserModel.login == login)
                .filter(UserModel.senha == senha)
                .first()
            )
            return user_mapper.to_domain(model) if model else None
        finally:
            session.close()

    def duplicated_login(self, login: str) -> bool:
        session = self._session_factory()
        try:
            model = session.query(UserModel).filter(UserModel.login == login).first()
            return model is not None
        finally:
            session.close()
