from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel,create_engine
from sqlachemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import config

async_engine = AsyncEngine(create_engine(url=config.DATABSE_URL))

async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session()-> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,class_=AsyncSession,expire_on_commit=False
    )
    
    async with Session() as session:
        yield session