from functools import lru_cache

from domain.config import EnvConfigService
from domain.use_cases.add_recipe import AddRecipeUseCase
from infra.db import SessionLocal
from infra.repositories import SqlAlchemyRecipeRepository

@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()

@lru_cache
def get_recipe_repository() -> SqlAlchemyRecipeRepository:
    return SqlAlchemyRecipeRepository(SessionLocal)

@lru_cache
def get_add_recipe_use_case() -> AddRecipeUseCase:
    return AddRecipeUseCase(get_recipe_repository())