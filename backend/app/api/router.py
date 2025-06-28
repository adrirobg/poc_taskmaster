"""API router configuration."""
from fastapi import APIRouter

# Create API router with versioning
api_router = APIRouter(prefix="/api/v1")

# Import and include routers as they are created
# Example:
# from .endpoints import projects, notes, tags, search
# api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
# api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
# api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
# api_router.include_router(search.router, prefix="/search", tags=["search"])