# Personal Portfolio Website - Flask Application

**Author:** Aneesh Yaramati  
**Course:** AiDD Assignment 05  
**Description:** Data Engineering & Analytics Professional Portfolio built with Flask

## 📁 Project Structure

```
AiDD_Assignment05/
├── app.py                    # Main Flask application with all routes
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── static/                   # Static files (CSS, JS, Images)
│   ├── css/
│   │   └── styles.css       # Main stylesheet
│   ├── js/
│   │   └── script.js        # JavaScript for navigation
│   └── images/              # Image assets
│       ├── favicon.svg
│       ├── headshot.jpg
│       ├── project-live-in-labs.svg
│       ├── project-mdm.svg
│       ├── project-pothole.svg
│       └── project-sap.svg
└── templates/               # HTML templates (Jinja2)
    ├── index.html           # Home page
    ├── about.html           # About page
    ├── resume.html          # Resume page
    ├── projects.html        # Projects showcase
    ├── contact.html         # Contact form
    └── thankyou.html        # Thank you page
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask==3.0.0
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:8001` (configured to avoid port conflicts on macOS)

**💡 Recommended: Use Virtual Environment**  
See `SETUP_INSTRUCTIONS.md` for complete setup with virtual environment (best practice).

### Step 3: Access the Website

Open your web browser and navigate to:
- **Home:** http://localhost:8001/
- **About:** http://localhost:8001/about
- **Resume:** http://localhost:8001/resume
- **Projects:** http://localhost:8001/projects
- **Contact:** http://localhost:8001/contact

**📖 For detailed setup with virtual environment, see `SETUP_INSTRUCTIONS.md`**

## 📋 Features

### Pages
1. **Home (/)** - Hero section with introduction and feature highlights
2. **About (/about)** - Personal story and background
3. **Resume (/resume)** - Professional experience and education
4. **Projects (/projects)** - Showcase of key projects with detailed descriptions
5. **Contact (/contact)** - Contact form with POST handling
6. **Thank You (/thankyou)** - Confirmation page after form submission

### Technical Features
- ✅ Flask routing with proper URL generation using `url_for()`
- ✅ Static file serving (CSS, JavaScript, Images)
- ✅ Template inheritance with Jinja2
- ✅ Form handling (Contact form with POST method)
- ✅ Dynamic year injection in footer
- ✅ Error handling (404, 500)
- ✅ Responsive design
- ✅ Accessibility features
- ✅ Professional glassmorphism dark theme

## 🏗️ Flask Best Practices Implemented

1. **Project Structure**
   - Proper separation of static files and templates
   - Organized folder structure following Flask conventions

2. **URL Routing**
   - All links use Flask's `url_for()` function
   - Clean, RESTful route names
   - Proper HTTP methods (GET, POST)

3. **Template Management**
   - Jinja2 templating with proper escaping
   - Dynamic content rendering
   - Context processors for global variables

4. **Static Files**
   - Organized in css/, js/, and images/ subdirectories
   - Served via Flask's static file handling
   - Proper URL generation with `url_for('static', filename=...)`

5. **Configuration**
   - Secret key configuration
   - Debug mode for development
   - Host and port configuration

6. **Error Handling**
   - Custom 404 error handler
   - Custom 500 error handler
   - Graceful error recovery

## 🔧 Development

### Running in Debug Mode
The app.py file is configured to run in debug mode by default for development:
```python
app.run(debug=True, host='0.0.0.0', port=8001)
```

### For Production
For production deployment, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

## 📝 Notes

- The contact form currently redirects to a thank you page without sending emails
- For production use, implement:
  - Email sending functionality
  - Form validation
  - CSRF protection
  - Environment-based configuration
  - Proper secret key management

## 🎨 Design

- **Theme:** Premium glassmorphic dark theme
- **Colors:** Professional blue/purple gradient accent
- **Typography:** Inter font family
- **Responsive:** Mobile-first responsive design
- **Accessibility:** WCAG compliant with proper ARIA labels

## 📦 Dependencies

- **Flask 3.0.0** - Web framework
- **Werkzeug 3.0.1** - WSGI utilities (Flask dependency)

## 👤 Author

**Aneesh Yaramati**  
MSIS Candidate at Kelley School of Business  
Data Engineering & Analytics Professional

---

Built with Flask and modern web development best practices.
