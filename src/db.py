from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database

from src.config import DATABASE_URL

database = Database(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session