from functools import lru_cache

from domain.config import EnvConfigService
from domain.use_cases.add_recipe import AddRecipeUseCase
from domain.use_cases.view_recipe import ViewRecipeUseCase
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

@lru_cache
def get_view_recipe_use_case() -> ViewRecipeUseCase:
    return ViewRecipeUseCase(get_recipe_repository())
