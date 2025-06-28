# FastAPI Backend Structure

This backend follows a clean architecture pattern with repository pattern for data access.

## Directory Structure

```
app/
├── api/                    # API endpoints and routing
│   ├── __init__.py
│   ├── router.py          # Main API router configuration
│   └── endpoints/         # Individual endpoint modules (to be created)
├── models/                # Data models and schemas
│   ├── __init__.py
│   └── (model files)      # Pydantic schemas and SQLAlchemy models
├── repositories/          # Data access layer
│   ├── __init__.py
│   ├── base.py           # Abstract base repository
│   └── sqlite_repository.py  # SQLite-specific implementation
├── services/              # Business logic layer
│   ├── __init__.py
│   └── base.py           # Base service class
├── middleware/            # Custom middleware
│   ├── __init__.py
│   ├── auth.py           # Authentication middleware
│   └── logging.py        # Logging middleware and config
├── config.py             # Application settings
└── main.py               # FastAPI app initialization

database/                  # Database configuration (separate module)
├── __init__.py
├── engine.py             # SQLAlchemy engine setup
├── session.py            # Session management
└── init_db.py            # Database initialization
```

## Architecture Pattern

The application follows a layered architecture:

1. **API Layer** (`api/`): HTTP endpoints, request/response handling
2. **Service Layer** (`services/`): Business logic and orchestration
3. **Repository Layer** (`repositories/`): Data access abstraction
4. **Model Layer** (`models/`): Data structures and validation

## Key Components

### Repository Pattern

- `BaseRepository`: Abstract base class defining common CRUD operations
- `SQLiteRepository`: Concrete implementation for SQLite database
- Repositories handle all database interactions
- Services use repositories through dependency injection

### Middleware

- **CORS**: Configured for frontend communication
- **Logging**: Request/response logging with rotating file handler
- **Authentication**: Simple token-based auth (disabled by default)
- **Error Handling**: Global exception handlers for validation and app errors
- **Timing**: Adds X-Process-Time header to responses

### Configuration

- Settings managed through `config.py` using Pydantic
- Environment variables supported via `.env` file
- Type-safe configuration with validation

## Usage Example

```python
# In a service
from app.repositories.sqlite_repository import SQLiteRepository
from app.models.project import Project

class ProjectService(BaseService):
    def __init__(self, session: Session):
        repository = SQLiteRepository(session, Project)
        super().__init__(repository)
    
    async def create(self, project_data: dict) -> Project:
        project = Project(**project_data)
        return await self.repository.create(project)

# In an endpoint
@router.get("/projects", response_model=List[Project])
async def list_projects(
    service: ProjectService = Depends(ProjectService)
):
    return await service.get_all()
```

## Next Steps

1. Create Pydantic models in `models/` directory
2. Implement service classes for each resource
3. Create API endpoints in `api/endpoints/`
4. Add endpoints to the main router in `api/router.py`