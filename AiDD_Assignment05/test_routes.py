"""
Test suite for Flask application routes (app.py)
Tests all endpoints including GET and POST requests
"""
import pytest
import DAL
from flask import url_for


class TestStaticRoutes:
    """Test class for static page routes"""
    
    def test_index_route(self, client):
        """Test the home page route"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Aneesh Yaramati' in response.data or b'Portfolio' in response.data
    
    def test_about_route(self, client):
        """Test the about page route"""
        response = client.get('/about')
        assert response.status_code == 200
    
    def test_resume_route(self, client):
        """Test the resume page route"""
        response = client.get('/resume')
        assert response.status_code == 200
    
    def test_contact_route_get(self, client):
        """Test the contact page GET request"""
        response = client.get('/contact')
        assert response.status_code == 200
    
    def test_thankyou_route(self, client):
        """Test the thank you page route"""
        response = client.get('/thankyou')
        assert response.status_code == 200


class TestProjectsRoutes:
    """Test class for projects-related routes"""
    
    def test_projects_route_empty(self, client, test_db):
        """Test projects page with no projects in database"""
        response = client.get('/projects')
        assert response.status_code == 200
    
    def test_projects_route_with_data(self, client, test_db, multiple_projects):
        """Test projects page with projects in database"""
        # Insert projects
        for project in multiple_projects:
            DAL.insert_project(
                project['title'],
                project['description'],
                project['image_filename']
            )
        
        response = client.get('/projects')
        assert response.status_code == 200
        
        # Check if project titles appear in response
        for project in multiple_projects:
            assert project['title'].encode() in response.data
    
    def test_add_project_route_get(self, client):
        """Test add project page GET request"""
        response = client.get('/add_project')
        assert response.status_code == 200
    
    def test_add_project_route_post_success(self, client, test_db, sample_project):
        """Test adding a project via POST request"""
        response = client.post('/add_project', data=sample_project, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify project was added to database
        projects = DAL.get_all_projects()
        assert len(projects) == 1
        assert projects[0]['title'] == sample_project['title']
    
    def test_add_project_route_post_missing_fields(self, client, test_db):
        """Test adding a project with missing required fields"""
        incomplete_data = {
            'title': 'Test Project'
            # Missing description and image_filename
        }
        response = client.post('/add_project', data=incomplete_data, follow_redirects=True)
        
        # Should not add project if fields are missing
        projects = DAL.get_all_projects()
        assert len(projects) == 0
    
    def test_add_project_route_post_empty_fields(self, client, test_db):
        """Test adding a project with empty fields"""
        empty_data = {
            'title': '',
            'description': '',
            'image_filename': ''
        }
        response = client.post('/add_project', data=empty_data, follow_redirects=True)
        
        # Should not add project if fields are empty
        projects = DAL.get_all_projects()
        assert len(projects) == 0
    
    def test_delete_project_route(self, client, test_db, sample_project):
        """Test deleting a project via POST request"""
        # First add a project
        project_id = DAL.insert_project(
            sample_project['title'],
            sample_project['description'],
            sample_project['image_filename']
        )
        
        # Verify project exists
        assert DAL.get_project_by_id(project_id) is not None
        
        # Delete the project
        response = client.post(f'/delete_project/{project_id}', follow_redirects=True)
        assert response.status_code == 200
        
        # Verify project was deleted
        assert DAL.get_project_by_id(project_id) is None
    
    def test_delete_project_route_nonexistent(self, client, test_db):
        """Test deleting a project that doesn't exist"""
        response = client.post('/delete_project/99999', follow_redirects=True)
        assert response.status_code == 200  # Should still redirect to projects page


class TestContactForm:
    """Test class for contact form functionality"""
    
    def test_contact_form_submission(self, client):
        """Test submitting contact form with valid data"""
        contact_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }
        response = client.post('/contact', data=contact_data, follow_redirects=True)
        assert response.status_code == 200
        # Should redirect to thank you page
        assert b'thank' in response.data.lower() or response.request.path == '/thankyou'
    
    def test_contact_form_empty_submission(self, client):
        """Test submitting contact form with empty data"""
        empty_data = {}
        response = client.post('/contact', data=empty_data, follow_redirects=True)
        assert response.status_code == 200


class TestErrorHandlers:
    """Test class for error handling"""
    
    def test_404_handler(self, client):
        """Test 404 error handler for nonexistent route"""
        response = client.get('/nonexistent-page-12345')
        assert response.status_code == 404
    
    def test_404_returns_page(self, client):
        """Test that 404 error returns a page (not just error)"""
        response = client.get('/nonexistent-route')
        assert response.status_code == 404
        assert len(response.data) > 0  # Should return some content


class TestContextProcessors:
    """Test class for template context processors"""
    
    def test_current_year_in_context(self, client):
        """Test that current_year is injected into templates"""
        response = client.get('/')
        # The year should appear somewhere in the page (typically in footer)
        import datetime
        current_year = str(datetime.datetime.now().year)
        assert current_year.encode() in response.data


class TestIntegrationScenarios:
    """Test class for end-to-end integration scenarios"""
    
    def test_full_project_lifecycle(self, client, test_db):
        """Test complete project lifecycle: add, view, delete"""
        # 1. View empty projects page
        response = client.get('/projects')
        assert response.status_code == 200
        
        # 2. Add a new project
        new_project = {
            'title': 'Integration Test Project',
            'description': 'Testing the full lifecycle',
            'image_filename': 'test.svg'
        }
        response = client.post('/add_project', data=new_project, follow_redirects=True)
        assert response.status_code == 200
        
        # 3. Verify project appears on projects page
        response = client.get('/projects')
        assert new_project['title'].encode() in response.data
        
        # 4. Get the project ID
        projects = DAL.get_all_projects()
        assert len(projects) == 1
        project_id = projects[0]['id']
        
        # 5. Delete the project
        response = client.post(f'/delete_project/{project_id}', follow_redirects=True)
        assert response.status_code == 200
        
        # 6. Verify project is gone
        projects = DAL.get_all_projects()
        assert len(projects) == 0
    
    def test_multiple_projects_workflow(self, client, test_db, multiple_projects):
        """Test working with multiple projects"""
        # Add multiple projects
        for project in multiple_projects:
            client.post('/add_project', data=project, follow_redirects=True)
        
        # Verify all projects are present
        all_projects = DAL.get_all_projects()
        assert len(all_projects) == len(multiple_projects)
        
        # Delete one project
        project_to_delete = all_projects[1]['id']
        client.post(f'/delete_project/{project_to_delete}', follow_redirects=True)
        
        # Verify correct count
        remaining_projects = DAL.get_all_projects()
        assert len(remaining_projects) == len(multiple_projects) - 1
    
    def test_navigation_flow(self, client):
        """Test navigation between different pages"""
        # Test navigation through different routes
        routes = ['/', '/about', '/resume', '/projects', '/contact']
        
        for route in routes:
            response = client.get(route)
            assert response.status_code == 200


class TestFormValidation:
    """Test class for form validation and edge cases"""
    
    def test_add_project_with_special_characters(self, client, test_db):
        """Test adding project with special characters in fields"""
        special_project = {
            'title': "Project with 'quotes' & special <chars>",
            'description': 'Description with "quotes" and symbols: @#$%',
            'image_filename': 'test-image.svg'
        }
        response = client.post('/add_project', data=special_project, follow_redirects=True)
        assert response.status_code == 200
        
        projects = DAL.get_all_projects()
        assert len(projects) == 1
        assert projects[0]['title'] == special_project['title']
    
    def test_add_project_with_long_content(self, client, test_db):
        """Test adding project with very long content"""
        long_project = {
            'title': 'A' * 200,
            'description': 'B' * 1000,
            'image_filename': 'test.svg'
        }
        response = client.post('/add_project', data=long_project, follow_redirects=True)
        assert response.status_code == 200
        
        projects = DAL.get_all_projects()
        assert len(projects) == 1
    
    def test_contact_form_with_special_characters(self, client):
        """Test contact form with special characters"""
        contact_data = {
            'name': "O'Brien",
            'email': 'test+tag@example.com',
            'subject': 'Subject with "quotes"',
            'message': 'Message with <html> tags & symbols'
        }
        response = client.post('/contact', data=contact_data, follow_redirects=True)
        assert response.status_code == 200
