from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config import Config


class Base(DeclarativeBase):
    __abstract__ = True


class DataBase:
    url = "postgresql+asyncpg://{}:{}@{}/{}"

    def __init__(self, config: Config):
        self.engine = create_async_engine(
            url=self.url.format(config.db.user, config.db.password,
                                config.db.host, config.db.database)
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def get_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()
