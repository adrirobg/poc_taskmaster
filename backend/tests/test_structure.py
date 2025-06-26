import pytest
from pathlib import Path


def test_project_structure_exists():
    """Test that basic project structure exists"""
    root = Path(__file__).parent.parent.parent
    
    # Test main directories exist
    assert (root / "backend").exists()
    assert (root / "frontend").exists()
    
    # Test backend structure
    assert (root / "backend" / "app").exists()
    assert (root / "backend" / "tests").exists()
    assert (root / "backend" / "requirements.txt").exists()
    
    # Test frontend structure
    assert (root / "frontend" / "src").exists()
    assert (root / "frontend" / "tests").exists()
    assert (root / "frontend" / "package.json").exists()


def test_requirements_file_contains_dependencies():
    """Test that requirements.txt contains expected dependencies"""
    root = Path(__file__).parent.parent.parent
    requirements_file = root / "backend" / "requirements.txt"
    
    content = requirements_file.read_text()
    assert "fastapi" in content
    assert "sqlalchemy" in content
    assert "pydantic" in content
    assert "pytest" in content


def test_package_json_contains_dependencies():
    """Test that package.json contains expected dependencies"""
    import json
    
    root = Path(__file__).parent.parent.parent
    package_file = root / "frontend" / "package.json"
    
    with open(package_file) as f:
        package_data = json.load(f)
    
    assert "react" in package_data["dependencies"]
    assert "typescript" in package_data["devDependencies"]
    assert "vite" in package_data["devDependencies"]
    assert "vitest" in package_data["devDependencies"]