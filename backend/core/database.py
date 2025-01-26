from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DB_ECHO, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
