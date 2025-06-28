from typing import Annotated
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from .engine import engine

# From L11-18 + L13-17: Session dependency pattern
async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session

# From L11-18: Annotated dependency for easier use
SessionDep = Annotated[AsyncSession, Depends(get_session)]