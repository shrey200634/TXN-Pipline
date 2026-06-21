from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,          
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Drops stale connections before using them
)

# Session factory — use this to create DB sessions
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Don't expire objects after commit (safer for async)
)

# Base class all ORM models will inherit from
class Base(DeclarativeBase):
    pass


# Dependency for FastAPI routes — yields a session, auto-closes after request
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise