from functools import lru_cache

from domain.config import EnvConfigService
from domain.use_cases.add_recipe import AddRecipeUseCase
from domain.use_cases.get_recipe import GetRecipeUseCase
from domain.use_cases.add_user import AddUserUseCase
from domain.use_cases.get_user import GetUserUseCase
from infra.db import SessionLocal
from infra.repositories import SqlAlchemyRecipeRepository
from infra.repositories import SqlAlchemyUserRepository

@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()

@lru_cache
def get_recipe_repository() -> SqlAlchemyRecipeRepository:
    return SqlAlchemyRecipeRepository(SessionLocal)

@lru_cache
def get_user_repository() -> SqlAlchemyUserRepository:
    return SqlAlchemyUserRepository(SessionLocal)

@lru_cache
def get_add_recipe_use_case() -> AddRecipeUseCase:
    return AddRecipeUseCase(get_recipe_repository())

@lru_cache
def get_get_recipe_use_case() -> GetRecipeUseCase:
    return GetRecipeUseCase(get_recipe_repository())

@lru_cache
def get_add_user_use_case() -> AddUserUseCase:
    return AddUserUseCase(get_user_repository())

@lru_cache
def get_get_user_use_case() -> GetUserUseCase:
    return GetUserUseCase(get_user_repository())