"""
Student Controller module.

Defines API endpoints for student resource management (CRUD operations)
and registers them to the main FastAPI application instance.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.student_repository import StudentRepository
from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services.student_service import StudentService

# Instantiate core repository and service layers
repository = StudentRepository()
service = StudentService(repository)

# Database Session Dependency type alias
DbSession = Annotated[Session, Depends(get_db)]


def register_student_routes(app: FastAPI):
    """
    Registers student routing endpoints on the provided FastAPI application.
    
    Args:
        app (FastAPI): The main FastAPI application instance.
    """

    @app.post(
        "/students",
        response_model=StudentResponse,
        status_code=status.HTTP_201_CREATED
    )
    def create_student(
        student_data: StudentCreate,
        db: DbSession
    ):
        """
        Creates a new student record.
        
        Catches ValueError exceptions (e.g., duplicate email) and raises a 400 Bad Request.
        """
        try:
            return service.create_student(db, student_data)

        except ValueError as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(error)
            )

    @app.get(
        "/students",
        response_model=list[StudentResponse]
    )
    def get_all_students(
        db: DbSession,
        department: str | None = None,
        year: int | None = None
    ):
        """
        Retrieves a list of all students, optionally filtered by department and/or year.
        """
        return service.get_all_students(
            db,
            department,
            year
        )


    @app.get(
        "/students/{student_id}",
        response_model=StudentResponse
    )
    def get_student_by_id(
        student_id: int,
        db: DbSession
    ):
        """
        Retrieves a single student's details by their ID.
        Raises 404 HTTP Exception if student is not found.
        """
        student = service.get_student_by_id(db, student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        return student

    @app.put(
        "/students/{student_id}",
        response_model=StudentResponse
    )
    def update_student(
        student_id: int,
        student_data: StudentUpdate,
        db: DbSession
    ):
        """
        Updates details of a student matching the specified ID.
        Raises 404 HTTP Exception if student is not found.
        """
        student = service.get_student_by_id(db, student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        return service.update_student(
            db,
            student,
            student_data
        )

    @app.delete(
        "/students/{student_id}",
        status_code=status.HTTP_204_NO_CONTENT
    )
    def delete_student(
        student_id: int,
        db: DbSession
    ):
        """
        Deletes a student matching the specified ID.
        Raises 404 HTTP Exception if student is not found.
        """
        student = service.get_student_by_id(db, student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        service.delete_student(db, student)