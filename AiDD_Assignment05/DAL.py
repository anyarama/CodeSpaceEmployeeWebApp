"""
Data Access Layer for Projects Database
Handles all database operations for the projects table
"""

import sqlite3
import os

# Database configuration
DB_NAME = 'projects.db'

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_database():
    """Initialize the database and create the projects table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create projects table with required columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_filename TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_all_projects():
    """Retrieve all projects from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
    projects = cursor.fetchall()
    conn.close()
    return projects

def get_project_by_id(project_id):
    """Retrieve a single project by its ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    project = cursor.fetchone()
    conn.close()
    return project

def insert_project(title, description, image_filename):
    """Insert a new project into the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projects (title, description, image_filename)
        VALUES (?, ?, ?)
    ''', (title, description, image_filename))
    conn.commit()
    project_id = cursor.lastrowid
    conn.close()
    return project_id

def delete_project(project_id):
    """Delete a project from the database by its ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected

def update_project(project_id, title, description, image_filename):
    """Update an existing project"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE projects 
        SET title = ?, description = ?, image_filename = ?
        WHERE id = ?
    ''', (title, description, image_filename, project_id))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected

# Initialize database when module is imported
if __name__ == '__main__':
    init_database()
    print("Database initialized successfully!")
