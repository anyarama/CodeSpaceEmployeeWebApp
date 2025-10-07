"""Flask-based MCP server for the personal site.

This server delivers the static HTML/CSS/JS assets that live in the
``AiDD_Assignment05`` directory. It provides a minimal routing layer so the
site can be previewed locally while keeping relative paths like
``assets/styles.css`` intact.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from flask import Flask, abort, send_from_directory

BASE_DIR = Path(__file__).parent.resolve()


def create_app() -> Flask:
    """Instantiate the Flask application configured for static delivery."""

    app = Flask(__name__, static_folder=None)

    @app.route("/")
    def serve_root():
        return send_from_directory(BASE_DIR, "index.html")

    @app.route("/<path:resource>")
    def serve_resource(resource: str):
        target = (BASE_DIR / resource).resolve()

        # Prevent path traversal
        if not str(target).startswith(str(BASE_DIR)):
            abort(404)

        if target.is_dir():
            target = target / "index.html"
            resource = str(target.relative_to(BASE_DIR))

        if not target.exists():
            abort(404)

        return send_from_directory(BASE_DIR, resource)

    return app


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the MCP Flask server.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
