from datetime import datetime
from typing import Callable, Optional

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from domain.exceptions import DuplicateUserError
from domain.repositories import UserRepository
from domain.user import User
from infra.db.database import Base


SessionFactory = Callable[[], Session]


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session_factory: SessionFactory):
        self._session_factory = session_factory

    def add(self, user: User) -> User:
        try:
            with self._session_factory() as session:
                model = UserModel(
                    email=user.email,
                    password_hash=user.password_hash,
                )
                session.add(model)
                session.commit()
                session.refresh(model)
                return self._to_domain(model)
        except IntegrityError as exc:
            raise DuplicateUserError("Email already registered") from exc

    def get_by_email(self, email: str) -> Optional[User]:
        with self._session_factory() as session:
            model: Optional[UserModel] = (
                session.query(UserModel).filter(UserModel.email == email).first()
            )
            return self._to_domain(model) if model else None

    @staticmethod
    def _to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            password_hash=model.password_hash,
        )
