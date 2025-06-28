#!/usr/bin/env python3
"""Test script to verify SQLite database initialization with WAL mode and FTS5"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import engine, init_database
from sqlmodel import text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_database_initialization():
    """Test database initialization and configurations"""
    
    print("=== Testing Database Initialization ===\n")
    
    # Initialize database
    status = init_database()
    print(f"Initialization status: {status}\n")
    
    # Test WAL mode
    print("1. Testing WAL mode:")
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA journal_mode"))
        print(f"   Journal mode: {result.scalar()}")
    
    # Test cache size
    print("\n2. Testing cache size:")
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA cache_size"))
        print(f"   Cache size: {result.scalar()} pages")
    
    # Test foreign keys
    print("\n3. Testing foreign keys:")
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA foreign_keys"))
        print(f"   Foreign keys enabled: {bool(result.scalar())}")
    
    # Test FTS5
    print("\n4. Testing FTS5 support:")
    try:
        with engine.connect() as conn:
            # Insert test data
            conn.execute(text("""
                INSERT INTO notes_fts (note_id, title, content) 
                VALUES ('1', 'Test Note', 'This is a test note with searchable content')
            """))
            
            # Search test
            result = conn.execute(text("""
                SELECT note_id, title FROM notes_fts 
                WHERE notes_fts MATCH 'test'
            """))
            rows = result.fetchall()
            print(f"   FTS5 search found {len(rows)} results")
            for row in rows:
                print(f"   - Note {row[0]}: {row[1]}")
            
            # Cleanup
            conn.execute(text("DELETE FROM notes_fts"))
            conn.commit()
    except Exception as e:
        print(f"   FTS5 test failed: {e}")
    
    print("\n=== All tests completed ===")

if __name__ == "__main__":
    test_database_initialization()