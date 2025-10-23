"""
Pytest configuration and fixtures for Flask application testing
"""
import pytest
import os
import sys
import sqlite3
from app import app as flask_app
import DAL

# Test database name
TEST_DB = 'test_projects.db'

@pytest.fixture(scope='session')
def app():
    """Create and configure a Flask app instance for testing"""
    flask_app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
        'SECRET_KEY': 'test-secret-key'
    })
    yield flask_app

@pytest.fixture(scope='function')
def client(app):
    """Create a test client for the Flask app"""
    return app.test_client()

@pytest.fixture(scope='function')
def test_db():
    """Create a fresh test database for each test"""
    # Override the database name for testing
    original_db = DAL.DB_NAME
    DAL.DB_NAME = TEST_DB
    
    # Remove test database if it exists
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    
    # Initialize fresh database
    DAL.init_database()
    
    yield TEST_DB
    
    # Cleanup: restore original DB name and remove test database
    DAL.DB_NAME = original_db
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

@pytest.fixture(scope='function')
def sample_project():
    """Provide sample project data for testing"""
    return {
        'title': 'Test Project',
        'description': 'This is a test project description',
        'image_filename': 'test-image.svg'
    }

@pytest.fixture(scope='function')
def multiple_projects():
    """Provide multiple sample projects for testing"""
    return [
        {
            'title': 'Project One',
            'description': 'Description for project one',
            'image_filename': 'project1.svg'
        },
        {
            'title': 'Project Two',
            'description': 'Description for project two',
            'image_filename': 'project2.svg'
        },
        {
            'title': 'Project Three',
            'description': 'Description for project three',
            'image_filename': 'project3.svg'
        }
    ]
