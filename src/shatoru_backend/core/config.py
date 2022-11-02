from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "shatoru-backend"

    class Config:
        env_file = ".env.local", ".env", ".env.dev", ".env.stage", ".env.prod"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
