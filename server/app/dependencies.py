from functools import lru_cache

from domain.config import EnvConfigService
from infra.db.database import create_engine_from_url, create_session_factory, init_db
from infra.repositories.user_repository_sqlite import SQLAlchemyUserRepository
from infra.security.password_hasher import WerkzeugPasswordHasher
from use_cases.login_user import LoginUserUseCase
from use_cases.register_user import RegisterUserUseCase


@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()


@lru_cache
def get_engine():
    engine = create_engine_from_url(get_env_config_service().get_database_url())
    init_db(engine)
    return engine


@lru_cache
def get_session_factory():
    return create_session_factory(engine=get_engine())


@lru_cache
def get_user_repository() -> SQLAlchemyUserRepository:
    return SQLAlchemyUserRepository(get_session_factory())


@lru_cache
def get_password_hasher() -> WerkzeugPasswordHasher:
    return WerkzeugPasswordHasher()


@lru_cache
def get_register_user_use_case() -> RegisterUserUseCase:
    return RegisterUserUseCase(get_user_repository(), get_password_hasher())


@lru_cache
def get_login_user_use_case() -> LoginUserUseCase:
    return LoginUserUseCase(get_user_repository(), get_password_hasher())
