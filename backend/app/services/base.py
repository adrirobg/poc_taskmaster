"""Base service class for business logic."""
from typing import Optional, List, Any
from uuid import UUID
from sqlalchemy.orm import Session

from ..repositories.base import BaseRepository


class BaseService:
    """Base service class implementing common business logic operations."""
    
    def __init__(self, repository: BaseRepository):
        """Initialize service with repository.
        
        Args:
            repository: Repository instance for data access
        """
        self.repository = repository
    
    async def get_by_id(self, id: UUID) -> Optional[Any]:
        """Get entity by ID.
        
        Args:
            id: Entity UUID
            
        Returns:
            Entity instance or None
        """
        return await self.repository.get(id)
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Any]:
        """Get all entities with pagination.
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of entities
        """
        return await self.repository.get_all(skip, limit)
    
    async def create(self, entity_data: dict) -> Any:
        """Create new entity.
        
        Args:
            entity_data: Entity data dictionary
            
        Returns:
            Created entity
        """
        # Subclasses should implement validation and entity creation
        raise NotImplementedError("create method must be implemented")
    
    async def update(self, id: UUID, entity_data: dict) -> Optional[Any]:
        """Update existing entity.
        
        Args:
            id: Entity UUID
            entity_data: Updated entity data
            
        Returns:
            Updated entity or None
        """
        # Subclasses should implement validation and entity update
        raise NotImplementedError("update method must be implemented")
    
    async def delete(self, id: UUID) -> bool:
        """Delete entity.
        
        Args:
            id: Entity UUID
            
        Returns:
            True if deleted, False otherwise
        """
        return await self.repository.delete(id)
    
    async def exists(self, id: UUID) -> bool:
        """Check if entity exists.
        
        Args:
            id: Entity UUID
            
        Returns:
            True if exists, False otherwise
        """
        return await self.repository.exists(id)