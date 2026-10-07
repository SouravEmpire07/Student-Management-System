"""
Main Application Entry Point.

Initializes the FastAPI application, ensures database tables are created
on startup, and registers API routes.
"""

from fastapi import FastAPI

from app.controllers.student_controller import register_student_routes
from app.database.database import Base, engine
# Import all models so SQLAlchemy's Base.metadata discovers them before create_all()
from app.models.student import Student
from app.models.course import Course
from app.models.enrollment import Enrollment


# Synchronously create database tables on startup.
# In production, database migrations (e.g. Alembic) are recommended instead.
Base.metadata.create_all(bind=engine)

# Create the main FastAPI application instance.
app = FastAPI(
    title="Student Management System",
    version="1.0.0"
)

# Register routes for handling student API requests.
register_student_routes(app)