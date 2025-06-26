from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from pathlib import Path
import os


class Base(DeclarativeBase):
    pass


def setup_sqlite_wal_mode(dbapi_connection, connection_record):
    """Configure SQLite for WAL mode and performance optimizations"""
    cursor = dbapi_connection.cursor()
    
    # Enable WAL mode for better concurrency
    cursor.execute("PRAGMA journal_mode=WAL")
    
    # Set cache size to 64MB (negative value means KB)
    cursor.execute("PRAGMA cache_size=-65536")  # 64MB
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys=ON")
    
    # Optimize for performance
    cursor.execute("PRAGMA synchronous=NORMAL")
    cursor.execute("PRAGMA temp_store=MEMORY")
    cursor.execute("PRAGMA mmap_size=268435456")  # 256MB
    
    cursor.close()


def create_database_engine(database_url: str = None):
    """Create SQLAlchemy engine with SQLite optimizations"""
    if database_url is None:
        # Default to local SQLite database
        db_path = Path("taskmaster.db")
        database_url = f"sqlite:///{db_path}"
    
    engine = create_engine(
        database_url,
        echo=bool(os.getenv("DATABASE_ECHO", False)),
        pool_pre_ping=True,
        # SQLite-specific configurations
        connect_args={"check_same_thread": False}
    )
    
    # Attach WAL mode configuration event listener
    event.listen(engine, "connect", setup_sqlite_wal_mode)
    
    return engine


def create_session_factory(engine):
    """Create SQLAlchemy session factory"""
    return sessionmaker(bind=engine, expire_on_commit=False)


def get_database_session(engine) -> Session:
    """Get database session"""
    SessionLocal = create_session_factory(engine)
    return SessionLocal()


# Global engine instance (will be initialized by FastAPI)
engine = None
SessionLocal = None


def init_database(database_url: str = None):
    """Initialize database engine and session factory"""
    global engine, SessionLocal
    
    engine = create_database_engine(database_url)
    SessionLocal = create_session_factory(engine)
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    return engine


def get_session():
    """Dependency function to get database session"""
    if SessionLocal is None:
        raise RuntimeError("Database not initialized. Call init_database() first.")
    
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()