from functools import lru_cache

from domain.config import EnvConfigService

@lru_cache
def get_env_config_service() -> EnvConfigService:
    return EnvConfigService()