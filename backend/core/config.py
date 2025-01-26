import secrets
from enum import Enum
from pathlib import Path

from pydantic import EmailStr, AnyHttpUrl, field_validator, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")
    MODE: ModeEnum
    PROJECT_NAME: str
    # База данных
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DB_ECHO: bool
    # REDIS_HOST: str
    # REDIS_PORT: str
    # BACKEND_CORS_ORIGINS: list[str] | list[AnyHttpUrl]
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ENCRYPT_KEY: str = secrets.token_urlsafe(32)

    # DB_POOL_SIZE: int = 83
    # WEB_CONCURRENCY: int = 9
    # POOL_SIZE: int = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)

    # FIRST_SUPERUSER_EMAIL: EmailStr
    # FIRST_SUPERUSER_PASSWORD: str

    # @field_validator("BACKEND_CORS_ORIGINS")
    # def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)


settings = Settings()
# print(Settings().model_dump())
