from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database import init_database, get_session
from sqlalchemy.orm import Session


# Initialize FastAPI app
app = FastAPI(
    title="TaskMaster API",
    description="Task management API with SQLite backend",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_database()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "TaskMaster API is running"}


@app.get("/health")
async def health_check(db: Session = Depends(get_session)):
    """Health check endpoint with database connectivity"""
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}


@app.get("/api/tasks")
async def list_tasks(db: Session = Depends(get_session)):
    """List all tasks (placeholder)"""
    return {"tasks": [], "message": "Task listing not implemented yet"}


@app.post("/api/tasks")
async def create_task(db: Session = Depends(get_session)):
    """Create new task (placeholder)"""
    return {"message": "Task creation not implemented yet"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)