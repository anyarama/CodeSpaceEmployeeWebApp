# Testing Guide for Personal Website

This document provides comprehensive information about testing the Flask personal website application.

## Overview

The test suite includes:
- **Database tests** (`test_database.py`) - Tests for all CRUD operations
- **Route tests** (`test_routes.py`) - Tests for all Flask endpoints and user flows
- **Configuration** (`conftest.py`) - Pytest fixtures and test configuration

## Installation

Install testing dependencies:

```bash
pip install -r requirements.txt
```

This will install:
- `pytest` - Testing framework
- `pytest-flask` - Flask-specific testing utilities
- `pytest-cov` - Code coverage reporting

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test Files

```bash
# Run only database tests
pytest test_database.py

# Run only route tests
pytest test_routes.py
```

### Run Specific Test Classes

```bash
# Run only database operations tests
pytest test_database.py::TestDatabaseOperations

# Run only static routes tests
pytest test_routes.py::TestStaticRoutes
```

### Run Specific Test Functions

```bash
# Run a single test
pytest test_database.py::TestDatabaseOperations::test_insert_project
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Coverage Report

```bash
# Generate coverage report
pytest --cov=. --cov-report=html

# View the report
open htmlcov/index.html
```

### Run with Print Statements (Useful for Debugging)

```bash
pytest -s
```

## Test Structure

### conftest.py - Fixtures

The configuration file provides reusable test fixtures:

- **`app`** - Flask application instance configured for testing
- **`client`** - Test client for making HTTP requests
- **`test_db`** - Clean test database created for each test
- **`sample_project`** - Single project data for testing
- **`multiple_projects`** - Multiple projects data for testing

### test_database.py - Database Tests

Tests all Data Access Layer (DAL) operations:

**TestDatabaseOperations Class:**
- `test_init_database` - Database initialization
- `test_insert_project` - Adding new projects
- `test_get_all_projects_empty` - Retrieving from empty database
- `test_get_all_projects_with_data` - Retrieving multiple projects
- `test_get_project_by_id_exists` - Finding specific project
- `test_get_project_by_id_not_exists` - Handling missing projects
- `test_update_project` - Modifying existing projects
- `test_update_project_not_exists` - Updating non-existent projects
- `test_delete_project` - Removing projects
- `test_delete_project_not_exists` - Deleting non-existent projects
- `test_multiple_inserts_and_deletes` - Complex operations
- `test_project_has_timestamp` - Timestamp validation
- `test_insert_with_special_characters` - Special character handling
- `test_insert_with_long_text` - Long content handling

### test_routes.py - Route Tests

Tests all Flask application endpoints:

**TestStaticRoutes Class:**
- Tests for home, about, resume, contact, and thank you pages

**TestProjectsRoutes Class:**
- `test_projects_route_empty` - Empty projects page
- `test_projects_route_with_data` - Projects page with data
- `test_add_project_route_get` - Add project form display
- `test_add_project_route_post_success` - Successfully adding project
- `test_add_project_route_post_missing_fields` - Validation testing
- `test_add_project_route_post_empty_fields` - Empty field validation
- `test_delete_project_route` - Project deletion
- `test_delete_project_route_nonexistent` - Deleting missing project

**TestContactForm Class:**
- `test_contact_form_submission` - Form submission
- `test_contact_form_empty_submission` - Empty form handling

**TestErrorHandlers Class:**
- `test_404_handler` - 404 error page
- `test_404_returns_page` - Error page content

**TestContextProcessors Class:**
- `test_current_year_in_context` - Template context injection

**TestIntegrationScenarios Class:**
- `test_full_project_lifecycle` - Complete add/view/delete flow
- `test_multiple_projects_workflow` - Multi-project operations
- `test_navigation_flow` - Page navigation testing

**TestFormValidation Class:**
- `test_add_project_with_special_characters` - Special character handling
- `test_add_project_with_long_content` - Long content handling
- `test_contact_form_with_special_characters` - Form validation

## Test Database

Tests use a separate test database (`test_projects.db`) that is:
- Created fresh for each test function
- Automatically cleaned up after each test
- Never affects your production `projects.db`

## Best Practices

### Writing New Tests

1. **Use descriptive test names** - Test names should clearly describe what is being tested
2. **Follow AAA pattern** - Arrange, Act, Assert
3. **Use fixtures** - Leverage existing fixtures from `conftest.py`
4. **Test edge cases** - Include tests for error conditions and edge cases
5. **Keep tests independent** - Each test should work regardless of test execution order

### Example Test

```python
def test_add_new_feature(client, test_db, sample_project):
    """Test description of what this test does"""
    # Arrange - Set up test data
    test_data = sample_project.copy()
    
    # Act - Perform the action
    response = client.post('/add_project', data=test_data)
    
    # Assert - Verify the results
    assert response.status_code == 200
    projects = DAL.get_all_projects()
    assert len(projects) == 1
```

## Continuous Integration

To run tests in CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install -r requirements.txt
    pytest --cov=. --cov-report=xml
```

## Coverage Goals

Aim for:
- **Overall coverage**: >80%
- **Critical paths**: 100% (database operations, form submissions)
- **Error handlers**: 100%

## Troubleshooting

### Tests Failing Due to Database Lock

If you see "database is locked" errors:
```bash
# Ensure no other process is using the database
rm test_projects.db
pytest
```

### Import Errors

If you see import errors:
```bash
# Ensure you're in the project root directory
cd /path/to/project
pytest
```

### Fixture Not Found

If fixtures are not recognized:
```bash
# Ensure conftest.py is in the same directory
ls conftest.py
pytest --fixtures  # List all available fixtures
```

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Flask Testing Documentation](https://flask.palletsprojects.com/en/latest/testing/)
- [pytest-flask Documentation](https://pytest-flask.readthedocs.io/)

## Quick Reference

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_database.py

# Run with coverage
pytest --cov=. --cov-report=html

# Run and show print statements
pytest -s

# Run tests matching a pattern
pytest -k "test_insert"

# Stop after first failure
pytest -x

# Show slowest tests
pytest --durations=10
