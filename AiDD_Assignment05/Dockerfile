# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY DAL.py .
COPY templates/ templates/
COPY static/ static/

# Create directory for database if it doesn't exist
RUN mkdir -p /app

# Expose port 8001 (as configured in app.py)
EXPOSE 8001

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
