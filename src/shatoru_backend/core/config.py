from functools import cache
from pathlib import Path
from typing import List, Optional

from loguru._defaults import LOGURU_FORMAT
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn

_BASE_PATH = Path(__file__).parent.parent.parent.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "shatoru-backend"

    DEBUG: bool = False

    CONFIG_PATH: str | Path = _BASE_PATH / "configs"
    LOG_PATH: str | Path = _BASE_PATH / "logs"

    LOG_FORMAT: str = LOGURU_FORMAT

    API_PREFIX: str = "/api"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    class Config:
        env_prefix = "SHATORU_"
        env_file = ".env.local", ".env", ".env.dev", ".env.stage", ".env.prod"
        case_sensitive = True


@cache
def get_settings():
    return Settings()


settings = get_settings()
