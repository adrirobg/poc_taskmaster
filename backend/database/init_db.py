from sqlmodel import SQLModel, text
from sqlalchemy.exc import OperationalError
from .engine import engine
import logging

logger = logging.getLogger(__name__)

# From L3-9: Create database tables function
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created successfully")

def check_fts5_support():
    """Verify FTS5 extension is available"""
    try:
        with engine.connect() as conn:
            # Test FTS5 support by creating a temporary virtual table
            conn.execute(text("""
                CREATE VIRTUAL TABLE IF NOT EXISTS temp.fts5_test 
                USING fts5(content)
            """))
            conn.execute(text("DROP TABLE IF EXISTS temp.fts5_test"))
            conn.commit()
            logger.info("FTS5 extension verified successfully")
            return True
    except OperationalError as e:
        logger.error(f"FTS5 extension not available: {e}")
        return False

def create_sample_fts_table():
    """Create a sample FTS5 virtual table for notes search"""
    with engine.connect() as conn:
        # Create FTS5 virtual table for full-text search on notes
        conn.execute(text("""
            CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts 
            USING fts5(
                note_id UNINDEXED,
                title,
                content,
                tokenize='porter unicode61'
            )
        """))
        conn.commit()
        logger.info("FTS5 virtual table created successfully")

def verify_wal_mode():
    """Verify WAL mode is enabled"""
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA journal_mode"))
        mode = result.scalar()
        if mode == "wal":
            logger.info("WAL mode verified successfully")
            return True
        else:
            logger.warning(f"Expected WAL mode but got: {mode}")
            return False

def init_database():
    """Initialize database with all configurations"""
    logger.info("Initializing database...")
    
    # Create tables
    create_db_and_tables()
    
    # Verify configurations
    wal_ok = verify_wal_mode()
    fts5_ok = check_fts5_support()
    
    if fts5_ok:
        create_sample_fts_table()
    
    # Log cache size for verification
    with engine.connect() as conn:
        cache_size = conn.execute(text("PRAGMA cache_size")).scalar()
        logger.info(f"Cache size: {cache_size} pages")
    
    return {
        "wal_mode": wal_ok,
        "fts5_support": fts5_ok,
        "cache_size": cache_size
    }