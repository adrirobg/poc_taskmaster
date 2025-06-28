from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.pool import StaticPool
import os

# From L2-8 + L1335: SQLite engine creation with event listeners for PRAGMA
sqlite_file_name = os.environ.get("DATABASE_FILE", "database.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"

# From L2-8: Create engine with check_same_thread=False for FastAPI
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=os.environ.get("SQL_ECHO", "false").lower() == "true"
)

# From L1335: Event listener to set SQLite PRAGMA statements
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    
    # Enable WAL mode for better concurrency
    cursor.execute("PRAGMA journal_mode=WAL")
    
    # Set cache size to 64MB (negative value = KB)
    cursor.execute("PRAGMA cache_size=-64000")
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys=ON")
    
    # Optimize for performance
    cursor.execute("PRAGMA synchronous=NORMAL")
    cursor.execute("PRAGMA temp_store=MEMORY")
    
    # Page size optimization
    cursor.execute("PRAGMA page_size=4096")
    
    cursor.close()