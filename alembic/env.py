import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, async_engine_from_config, create_async_engine
from alembic import context
from backend.models.base import Base
from backend.core.config import settings

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData for autogenerate support
target_metadata = Base.metadata


def run_migrations_offline():
    """Миграции в оффлайн-режиме."""
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Основная асинхронная функция для миграций."""
    # Создаем асинхронный движок напрямую
    my_engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, poolclass=pool.NullPool, echo=settings.DB_ECHO)

    async with my_engine.connect() as connection:
        async with connection.begin():
            await connection.run_sync(
                lambda sync_conn: context.configure(
                    connection=sync_conn, target_metadata=target_metadata, compare_type=True, include_schemas=True
                )
            )
            await connection.run_sync(do_run_migrations)

    await my_engine.dispose()


def do_run_migrations():
    """Синхронный запуск миграций."""
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
