from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
import time

# From L4-6: Import database initialization
from database import init_database

# Import custom middleware
from .middleware.logging import LoggingMiddleware, setup_logging
from .middleware.auth import AuthMiddleware

# Import API router
from .api.router import api_router

# Setup logging configuration
setup_logging()
logger = logging.getLogger(__name__)


# From L4-6: Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up...")
    db_status = await init_database()
    logger.info(f"Database initialized: {db_status}")
    yield
    # Shutdown
    logger.info("Shutting down...")


app = FastAPI(
    title="Personal PKM API",
    version="1.0.0",
    lifespan=lifespan
)

# From L0, L4, L5: CORS middleware configuration
origins = [
    "http://localhost:3000",  # React dev server
    "http://localhost:5173",  # Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(LoggingMiddleware)
# Uncomment to enable authentication
# app.add_middleware(AuthMiddleware)


# From L11, L25: Custom exception class
class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


# From L6, L10, L24: Validation exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )


# From L11, L25: Custom app exception handler
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message}
    )


# From L108: Middleware for timing requests
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": "PKM API",
        "version": "1.0.0"
    }


# Include API router
app.include_router(api_router)