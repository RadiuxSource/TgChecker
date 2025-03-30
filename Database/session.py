from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

Base = declarative_base()

class DatabaseSession:
    def __init__(self):
        self.engine = create_async_engine(
            Config.DB_URL,
            echo=True,
            future=True,
            connect_args={"check_same_thread": False} if "sqlite" in Config.DB_URL else {}
        )
        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

async def init_db():
    """Initialize database connection and create tables"""
    db = DatabaseSession()
    await db.create_all()
    return db

AsyncSessionLocal = DatabaseSession().async_session
