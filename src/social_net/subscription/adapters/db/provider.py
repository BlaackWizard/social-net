from collections.abc import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from social_net.subscription.adapters.db.config_loader import SubDBConfig


async def get_engine(config: SubDBConfig) -> AsyncIterator[AsyncEngine]:
    url = config.from_env().postgres_connection()

    engine = create_async_engine(
        url,
        future=True
    )
    yield engine

    await engine.dispose()

async def get_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    sessionmaker = async_sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    return sessionmaker

async def get_session(sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterator[AsyncSession]:
    async with sessionmaker() as session:
        yield session
