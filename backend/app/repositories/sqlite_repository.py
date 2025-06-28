"""SQLite-specific repository implementation."""
from typing import Type, Optional, List, Any
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, func

from .base import BaseRepository, T


class SQLiteRepository(BaseRepository[T]):
    """SQLite implementation of the repository pattern."""
    
    def __init__(self, session: AsyncSession, model: Type[T]):
        """Initialize SQLite repository.
        
        Args:
            session: SQLAlchemy AsyncSession instance
            model: SQLAlchemy model class
        """
        super().__init__(session)
        self.model = model
    
    async def get(self, id: UUID) -> Optional[T]:
        """Retrieve entity by ID.
        
        # From L1264, L1267, L1268: Using session for queries
        """
        try:
            stmt = select(self.model).where(self.model.id == id)
            result = await self.session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            # Log error in production
            return None
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Retrieve all entities with pagination."""
        try:
            stmt = select(self.model).offset(skip).limit(limit)
            result = await self.session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            # Log error in production
            return []
    
    async def create(self, entity: T) -> T:
        """Create new entity.
        
        # From L1268: Using session.add and commit
        """
        try:
            self.session.add(entity)
            await self.session.commit()
            await self.session.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise
    
    async def update(self, id: UUID, entity: T) -> Optional[T]:
        """Update existing entity."""
        try:
            existing = await self.get(id)
            if not existing:
                return None
            
            # Update attributes
            for key, value in entity.__dict__.items():
                if not key.startswith('_'):
                    setattr(existing, key, value)
            
            await self.session.commit()
            await self.session.refresh(existing)
            return existing
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise
    
    async def delete(self, id: UUID) -> bool:
        """Delete entity by ID."""
        try:
            entity = await self.get(id)
            if not entity:
                return False
            
            await self.session.delete(entity)
            await self.session.commit()
            return True
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise
    
    async def exists(self, id: UUID) -> bool:
        """Check if entity exists."""
        try:
            stmt = select(func.count()).select_from(self.model).where(self.model.id == id)
            result = await self.session.execute(stmt)
            count = result.scalar() # scalar() is synchronous, no await needed
            return count > 0
        except SQLAlchemyError as e:
            return False
    
    async def find_by(self, **kwargs: Any) -> List[T]:
        """Find entities by criteria."""
        try:
            stmt = select(self.model)
            for key, value in kwargs.items():
                if hasattr(self.model, key):
                    stmt = stmt.where(getattr(self.model, key) == value)
            
            result = await self.session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            return []
    
    async def count(self, **kwargs: Any) -> int:
        """Count entities matching criteria."""
        try:
            stmt = select(func.count()).select_from(self.model)
            for key, value in kwargs.items():
                if hasattr(self.model, key):
                    stmt = stmt.where(getattr(self.model, key) == value)
            
            result = await self.session.execute(stmt)
            count = result.scalar() # scalar() is synchronous, no await needed
            return count or 0
        except SQLAlchemyError as e:
            return 0