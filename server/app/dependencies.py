from functools import lru_cache

from domain.config import EnvConfigService
from infra.db.session import engine, SessionLocal
from infra.repositories import SqlAlchemyUserRepository
from infra.security.password_hasher import WerkzeugPasswordHasher
from domain.use_cases.auth_use_cases import LoginUserUseCase, RegisterUserUseCase


@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()


@lru_cache
def get_engine():
    return engine


@lru_cache
def get_session_factory():
    return SessionLocal


@lru_cache
def get_user_repository() -> SqlAlchemyUserRepository:
    return SqlAlchemyUserRepository(get_session_factory())


@lru_cache
def get_password_hasher() -> WerkzeugPasswordHasher:
    return WerkzeugPasswordHasher()


@lru_cache
def get_register_user_use_case() -> RegisterUserUseCase:
    return RegisterUserUseCase(get_user_repository(), get_password_hasher())


@lru_cache
def get_login_user_use_case() -> LoginUserUseCase:
    return LoginUserUseCase(get_user_repository(), get_password_hasher())
