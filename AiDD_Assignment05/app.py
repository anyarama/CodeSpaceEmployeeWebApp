"""
Personal Portfolio Website - Flask Application
Author: Aneesh Yaramati
Description: Data Engineering & Analytics Professional Portfolio
"""

from flask import Flask, render_template, request, redirect, url_for
import datetime
import DAL

app = Flask(__name__)

# Initialize database on startup
DAL.init_database()

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/resume')
def resume():
    """Resume page"""
    return render_template('resume.html')

@app.route('/projects')
def projects():
    """Projects page - displays all projects from database"""
    all_projects = DAL.get_all_projects()
    return render_template('projects.html', projects=all_projects)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    """Add new project page with form"""
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description')
        image_filename = request.form.get('image_filename')
        
        # Insert into database
        if title and description and image_filename:
            DAL.insert_project(title, description, image_filename)
            return redirect(url_for('projects'))
        
    return render_template('add_project.html')

@app.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """Delete a project by ID"""
    DAL.delete_project(project_id)
    return redirect(url_for('projects'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # In a production app, you would:
        # 1. Validate the data
        # 2. Send email or save to database
        # 3. Add CSRF protection
        
        # For now, redirect to thank you page
        return redirect(url_for('thankyou'))
    
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    """Thank you page after form submission"""
    return render_template('thankyou.html')

@app.context_processor
def inject_year():
    """Inject current year into all templates"""
    return {'current_year': datetime.datetime.now().year}

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page"""
    return render_template('index.html'), 500

if __name__ == '__main__':
    # Development server configuration
    # In production, use a proper WSGI server like Gunicorn
    # Changed to port 8001 to avoid conflict with AirPlay Receiver on macOS
    app.run(debug=True, host='0.0.0.0', port=8001)
