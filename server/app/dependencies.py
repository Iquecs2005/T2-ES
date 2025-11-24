from functools import lru_cache

from src.core.config import EnvConfigService

@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()