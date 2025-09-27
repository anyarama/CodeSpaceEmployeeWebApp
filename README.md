# Employee Web App Repository

Comprehensive sample project that pairs a Flask-powered employee directory with
an MCP (Model Context Protocol) server. The web application gives your team a
polished browser UI for day-to-day CRUD on the `employees.db` SQLite database,
while the MCP server lets Cursor run guarded automations against the very same
data set.

---

## Highlights
- Responsive web UI with live employee and department management
- REST API backing the UI with full CRUD coverage for the `employees` table
- Shared SQLite database (`cursor-day01/employees.db`) that powers both
  components
- MCP server exposing safe `run_sql` and `add_employee` tools for Cursor
- Minimal dependencies: Flask for the app, `mcp` for the automation server

---

## Repository Layout
```
cursor-day01/
├── employees.db                 # SQLite database seeded with sample data
├── web_app/                     # Flask application + browser front end
│   ├── app.py                   # API routes and application factory
│   ├── requirements.txt         # Web requirements (Flask)
│   ├── templates/index.html     # Main HTML shell
│   ├── static/app.js            # Front-end behaviour and API calls
│   ├── static/styles.css        # Styling for the dashboard
│   └── README.md                # Component-level documentation
└── mcp_sqlite_server/           # Cursor MCP server for database guardrails
    ├── sqlite_server.py         # Tool implementations and routing logic
    ├── manifest.json            # Cursor manifest for registering the server
    ├── requirements.txt         # MCP server dependency list
    └── README.md                # Component-level documentation
```

You may also see local virtual environment folders such as `.venv/`; feel free
to create or delete those as needed for your development setup.

---

## Prerequisites
- macOS, Linux, or Windows with Python 3.10+ (web app) and 3.9+ (MCP server)
- `pip` available on your PATH
- Git for cloning and committing changes
- Optionally, Cursor if you want to wire the MCP server into your IDE

---

## Getting Started Quickly
1. Clone the repository and move into it:
   ```bash
   git clone https://github.com/<your-account>/CodeSpaceEmployeeWebApp.git
   cd CodeSpaceEmployeeWebApp
   ```
2. Inspect the included `employees.db` database (already seeded). If you need a
   fresh copy, replace it with your own SQLite file structured the same way.
3. Follow the component-specific setup steps below to run either the web app or
   the MCP server.

---

## Running the Flask Web Application
1. Create and activate a virtual environment:
   ```bash
   cd cursor-day01/web_app
   python3 -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```
2. Install dependencies and start the server:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. Visit `http://127.0.0.1:5000` in your browser. The dashboard loads current
   employees and departments from `employees.db` and lets you add, edit, or
   delete records in real time.

### Key UI Workflows
- **Add / Update Employees:** use the left form. Switching into edit mode fills
  the form with the selected row and toggles the submit button.
- **Manage Departments:** adjust the departments list directly inside the UI;
  the dropdown refreshes automatically.
- **Refresh Button:** re-fetches data if the database changes outside the app
  (e.g., via MCP or direct SQL interactions).

---

## REST API Reference
All endpoints live under the Flask root at `http://127.0.0.1:5000`.

| Method | Path                         | Description                                   |
| ------ | ---------------------------- | --------------------------------------------- |
| GET    | `/api/departments`           | List departments ordered alphabetically       |
| POST   | `/api/departments`           | Create a new department (name required)       |
| DELETE | `/api/departments/<id>`      | Delete a department if no employees reference |
| GET    | `/api/employees`             | List employees with department metadata       |
| POST   | `/api/employees`             | Create an employee (name required)            |
| PUT    | `/api/employees/<id>`        | Update any subset of employee fields          |
| DELETE | `/api/employees/<id>`        | Remove an employee                            |

All payloads are JSON. Numeric fields accept either numbers or numeric strings;
missing optional fields can be sent as `null`.

---

## Database Notes
- The project ships with `cursor-day01/employees.db`, which contains an
  `employees` table and related seed rows for demonstration.
- Both the Flask application and the MCP server expect this file to reside one
  level above their respective folders.
- To reset the data, replace the file and restart the services. The UI and API
  do not migrate schemas automatically.

---

## MCP Server Integration (Cursor)
The MCP server lets Cursor run safe operations against your database.

1. Prepare an environment:
   ```bash
   cd cursor-day01/mcp_sqlite_server
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Register the server in Cursor:
   - Cursor Settings → MCP Servers → Add Server → Manifest file
   - Point Cursor to `cursor-day01/mcp_sqlite_server/manifest.json`
3. In a Cursor chat, you will see tools such as `run_sql` (read-only SELECT) and
   `add_employee` (insert). Each call validates inputs and surfaces results as
   JSON without exposing raw file access.

To test manually outside Cursor, you can run `python sqlite_server.py` and send
MCP messages over stdin/stdout, though Cursor will typically orchestrate this
for you.

---

## Development Tips
- The repository is intentionally simple; linting, testing, and formatting are
  not enforced. Feel free to integrate tools such as `ruff`, `pytest`, or
  Prettier if your workflow requires them.
- Keep the database close to the components. If you relocate it, update the
  paths in `web_app/app.py` and `mcp_sqlite_server/sqlite_server.py`.
- When extending CRUD beyond employees (for example, departments), mirror the
  validation helpers already present in `app.py` to ensure consistent error
  handling between the UI and API.

---

## Troubleshooting
- **Flask cannot locate the database:** verify that `employees.db` exists at
  `cursor-day01/employees.db`. The app raises a `FileNotFoundError` if it does
  not.
- **Port already in use:** set the `FLASK_RUN_PORT` environment variable or run
  `python app.py --port <number>`
- **CORS errors in the browser:** the app and API run on the same origin by
  default. If you proxy through another domain, consider adding Flask-CORS.
- **Cursor MCP fails to start:** double-check the virtual environment includes
  the `mcp` package and that the manifest’s working directory is correct.

---

## Contributing
1. Fork the repository (or open a feature branch if you have write access).
2. Make your changes and keep commits focused.
3. Verify the web app and MCP server still interact with the shared database.
4. Open a pull request with a short summary of the change and any testing notes.

---

## License
No explicit license is provided. If you intend to share or publish the project,
please add a license file that matches your distribution goals.

