import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession as Raw_AsyncSession

from Env.handle import configs

BaseModel = declarative_base()

DATABASE_URL = f"postgresql://{configs.get_postgresql_username()}:{configs.get_postgresql_password()}@{configs.get_postgresql()}/{configs.get_postgresql_database()}"
ASYNC_DATABASE_URL = f"postgresql+asyncpg://{configs.get_postgresql_username()}:{configs.get_postgresql_password()}@{configs.get_postgresql()}/{configs.get_postgresql_database()}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)

async_engine = create_async_engine(ASYNC_DATABASE_URL)
AsyncSession = sessionmaker(
    bind=async_engine,
    class_=Raw_AsyncSession,
)