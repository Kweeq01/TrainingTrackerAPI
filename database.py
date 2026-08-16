# Настройки подключения к бд
import os
from typing import Annotated
from fastapi import Depends
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_async_engine(database_url, echo=True)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as db:
        yield db

SessionDep = Annotated[AsyncSession, Depends(get_db)]