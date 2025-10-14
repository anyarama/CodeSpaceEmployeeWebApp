# Complete Setup Instructions with Virtual Environment

## 🐍 Creating and Using a Virtual Environment

### Step 1: Navigate to Project Directory
```bash
cd /Users/aneeshyaramati/Documents/GitHub/CodeSpaceEmployeeWebApp/AiDD_Assignment05
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You'll see `(venv)` appear in your terminal prompt when activated.

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Flask Application
```bash
python app.py
```

The server will start on **http://localhost:8001** (changed from 5000 to avoid AirPlay conflict)

### Step 6: Open Browser
Visit: **http://localhost:8001**

### Step 7: When Done, Deactivate Virtual Environment
```bash
deactivate
```

---

## 📝 Complete Command Sequence:

```bash
# Navigate to project
cd /Users/aneeshyaramati/Documents/GitHub/CodeSpaceEmployeeWebApp/AiDD_Assignment05

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install Flask
pip install -r requirements.txt

# Run the server
python app.py

# Server will be at: http://localhost:8001
```

---

## 🛑 To Stop the Server:
Press **Ctrl + C** in terminal

## 🔄 To Run Again Later:
```bash
cd /Users/aneeshyaramati/Documents/GitHub/CodeSpaceEmployeeWebApp/AiDD_Assignment05
source venv/bin/activate
python app.py
```

---

## ⚠️ Important Notes:

1. **Port Changed to 8001** - Your app.py is now configured to use port 8001 instead of 5000
2. **Don't Include venv in Submission** - The .venv or venv folder should NOT be in your zip file (already excluded)
3. **Virtual Environment Benefits**:
   - Isolates project dependencies
   - Prevents conflicts with other Python projects
   - Cleaner development environment

---

## 🌐 Your Website URLs (when running):
- **Home:** http://localhost:8001/
- **About:** http://localhost:8001/about
- **Resume:** http://localhost:8001/resume
- **Projects:** http://localhost:8001/projects
- **Contact:** http://localhost:8001/contact
