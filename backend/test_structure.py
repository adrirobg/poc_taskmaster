"""Test script to verify backend structure is set up correctly."""
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def verify_structure():
    """Verify all required directories and files exist."""
    required_dirs = [
        "app",
        "app/api",
        "app/models",
        "app/repositories",
        "app/services",
        "app/middleware",
        "database",
    ]
    
    required_files = [
        "app/__init__.py",
        "app/main.py",
        "app/config.py",
        "app/api/__init__.py",
        "app/api/router.py",
        "app/models/__init__.py",
        "app/repositories/__init__.py",
        "app/repositories/base.py",
        "app/repositories/sqlite_repository.py",
        "app/services/__init__.py",
        "app/services/base.py",
        "app/middleware/__init__.py",
        "app/middleware/auth.py",
        "app/middleware/logging.py",
        "database/__init__.py",
        "database/engine.py",
        "database/session.py",
    ]
    
    print("Verifying backend structure...")
    print("-" * 50)
    
    # Check directories
    print("\nDirectories:")
    for dir_path in required_dirs:
        exists = os.path.isdir(dir_path)
        status = "✓" if exists else "✗"
        print(f"{status} {dir_path}")
    
    # Check files
    print("\nFiles:")
    for file_path in required_files:
        exists = os.path.isfile(file_path)
        status = "✓" if exists else "✗"
        print(f"{status} {file_path}")
    
    print("-" * 50)
    print("\nStructure verification complete!")
    
    # Try importing key modules
    print("\nTesting imports (requires dependencies installed):")
    try:
        from app.repositories.base import BaseRepository
        print("✓ BaseRepository imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import BaseRepository: {e}")
    
    try:
        from app.repositories.sqlite_repository import SQLiteRepository
        print("✓ SQLiteRepository imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import SQLiteRepository: {e}")
    
    try:
        from app.services.base import BaseService
        print("✓ BaseService imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import BaseService: {e}")


if __name__ == "__main__":
    verify_structure()