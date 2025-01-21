import secrets
from enum import Enum
from pathlib import Path

from pydantic import EmailStr, AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    MODE: ModeEnum = ModeEnum.development
    PROJECT_NAME: str
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: str
    SECRET_KEY: str = "your-secret-key"
    # SECRET_KEY: str = secrets.token_urlsafe(32)
    ENCRYPT_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: list[str] | list[AnyHttpUrl]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 1  # 1 hour
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 100  # 100 days
    # DB_POOL_SIZE: int = 83
    # WEB_CONCURRENCY: int = 9
    # POOL_SIZE: int = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
    # db_echo: bool = True
    db_echo: bool = False
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    # FIRST_SUPERUSER_EMAIL: EmailStr
    # FIRST_SUPERUSER_PASSWORD: str

    class Config:
        env_file = ".env"

    # @field_validator("BACKEND_CORS_ORIGINS")
    # def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)


settings = Settings()
