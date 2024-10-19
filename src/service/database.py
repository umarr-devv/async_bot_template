from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import Config


class Base(DeclarativeBase):
    __abstract__ = True


class DataBase:

    def __init__(self, config: Config):
        self.engine = create_async_engine(
            url=config.db.url
        )
        self.sessions = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
