"""
Test suite for database operations (DAL.py)
Tests all CRUD operations for the projects database
"""
import pytest
import DAL


class TestDatabaseOperations:
    """Test class for database CRUD operations"""
    
    def test_init_database(self, test_db):
        """Test database initialization creates projects table"""
        # Database is already initialized by fixture
        # Verify table exists by attempting to query it
        projects = DAL.get_all_projects()
        assert projects is not None
        assert isinstance(projects, list)
        assert len(projects) == 0
    
    def test_insert_project(self, test_db, sample_project):
        """Test inserting a new project into the database"""
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        assert project_id is not None
        assert isinstance(project_id, int)
        assert project_id > 0
        
        # Verify project was inserted
        project = DAL.get_project_by_id(project_id)
        assert project is not None
        assert project['title'] == sample_project['title']
        assert project['description'] == sample_project['description']
        assert project['image_filename'] == sample_project['image_filename']
    
    def test_get_all_projects_empty(self, test_db):
        """Test getting all projects from an empty database"""
        projects = DAL.get_all_projects()
        assert isinstance(projects, list)
        assert len(projects) == 0
    
    def test_get_all_projects_with_data(self, test_db, multiple_projects):
        """Test getting all projects when database has multiple entries"""
        # Insert multiple projects
        for project in multiple_projects:
            DAL.insert_project(
                project['title'],
                project['description'],
                project['image_filename']
            )
        
        # Retrieve all projects
        projects = DAL.get_all_projects()
        assert len(projects) == len(multiple_projects)
        
        # Verify all expected project titles are present
        titles = [p['title'] for p in projects]
        for project in multiple_projects:
            assert project['title'] in titles
    
    def test_get_project_by_id_exists(self, test_db, sample_project):
        """Test retrieving a project by its ID when it exists"""
        # Insert project
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        # Retrieve by ID
        project = DAL.get_project_by_id(project_id)
        assert project is not None
        assert project['id'] == project_id
        assert project['title'] == sample_project['title']
    
    def test_get_project_by_id_not_exists(self, test_db):
        """Test retrieving a project by ID when it doesn't exist"""
        project = DAL.get_project_by_id(99999)
        assert project is None
    
    def test_update_project(self, test_db, sample_project):
        """Test updating an existing project"""
        # Insert project
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        # Update project
        new_title = 'Updated Test Project'
        new_description = 'Updated description'
        new_image = 'updated-image.svg'
        
        rows_affected = DAL.update_project(
            project_id,
            new_title,
            new_description,
            new_image
        )
        
        assert rows_affected == 1
        
        # Verify update
        updated_project = DAL.get_project_by_id(project_id)
        assert updated_project['title'] == new_title
        assert updated_project['description'] == new_description
        assert updated_project['image_filename'] == new_image
    
    def test_update_project_not_exists(self, test_db):
        """Test updating a project that doesn't exist"""
        rows_affected = DAL.update_project(
            99999,
            'Title',
            'Description',
            'image.svg'
        )
        assert rows_affected == 0
    
    def test_delete_project(self, test_db, sample_project):
        """Test deleting a project from the database"""
        # Insert project
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        # Delete project
        rows_affected = DAL.delete_project(project_id)
        assert rows_affected == 1
        
        # Verify deletion
        project = DAL.get_project_by_id(project_id)
        assert project is None
    
    def test_delete_project_not_exists(self, test_db):
        """Test deleting a project that doesn't exist"""
        rows_affected = DAL.delete_project(99999)
        assert rows_affected == 0
    
    def test_multiple_inserts_and_deletes(self, test_db, multiple_projects):
        """Test multiple insert and delete operations"""
        project_ids = []
        
        # Insert multiple projects
        for project in multiple_projects:
            project_id = DAL.insert_project(
                project['title'],
                project['description'],
                project['image_filename']
            )
            project_ids.append(project_id)
        
        # Verify all inserted
        all_projects = DAL.get_all_projects()
        assert len(all_projects) == len(multiple_projects)
        
        # Delete middle project
        DAL.delete_project(project_ids[1])
        
        # Verify deletion
        remaining_projects = DAL.get_all_projects()
        assert len(remaining_projects) == len(multiple_projects) - 1
        
        # Verify correct project was deleted
        deleted_project = DAL.get_project_by_id(project_ids[1])
        assert deleted_project is None
    
    def test_project_has_timestamp(self, test_db, sample_project):
        """Test that inserted projects have a created_at timestamp"""
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        project = DAL.get_project_by_id(project_id)
        assert 'created_at' in project.keys()
        assert project['created_at'] is not None
    
    def test_insert_with_special_characters(self, test_db):
        """Test inserting project with special characters"""
        title = "Project with 'quotes' and \"double quotes\""
        description = "Description with special chars: <>&'"
        image = "image-with-special.svg"
        
        project_id = DAL.insert_project(title, description, image)
        project = DAL.get_project_by_id(project_id)
        
        assert project['title'] == title
        assert project['description'] == description
        assert project['image_filename'] == image
    
    def test_insert_with_long_text(self, test_db):
        """Test inserting project with long text content"""
        long_description = "Lorem ipsum " * 200  # Very long text
        project_id = DAL.insert_project(
            "Long Project",
            long_description,
            "image.svg"
        )
        
        project = DAL.get_project_by_id(project_id)
        assert project['description'] == long_description
