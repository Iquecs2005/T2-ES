from typing import Callable, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from domain.exceptions import DuplicateUserError
from domain.interfaces.user_repository import UserRepository
from domain.entities.user import User
from infra.db.models import UserModel


SessionFactory = Callable[[], Session]


class SqlAlchemyUserRepository(UserRepository):
    """SQLAlchemy implementation of the user repository."""

    def __init__(self, session_factory: SessionFactory):
        self._session_factory = session_factory

    def add(self, user: User) -> User:
        session = self._session_factory()
        try:
            model = UserModel(
                email=user.email,
                password_hash=user.password_hash,
            )
            session.add(model)
            session.commit()
            session.refresh(model)
            return self._to_domain(model)
        except IntegrityError as exc:
            session.rollback()
            raise DuplicateUserError("Email já registrado") from exc
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_by_email(self, email: str) -> Optional[User]:
        session = self._session_factory()
        try:
            model: Optional[UserModel] = (
                session.query(UserModel).filter(UserModel.email == email).first()
            )
            return self._to_domain(model) if model else None
        finally:
            session.close()

    @staticmethod
    def _to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            password_hash=model.password_hash,
        )
