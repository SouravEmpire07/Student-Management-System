from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.student_repository import StudentRepository
from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services.student_service import StudentService


router = APIRouter(prefix="/students",tags=["Students"])


repository = StudentRepository()
service = StudentService(repository)


DbSession = Annotated[Session, Depends(get_db)]


@router.post( "",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
def create_student(student_data: StudentCreate,db: DbSession):
    return service.create_student(db, student_data)


@router.get( "",response_model=list[StudentResponse])
def get_all_students(db: DbSession):
    return service.get_all_students(db)


@router.get( "/{student_id}",response_model=StudentResponse)
def get_student_by_id(student_id: int,db: DbSession):
    student = service.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}",response_model=StudentResponse)
def update_student(student_id: int,
    student_data: StudentUpdate,
    db: DbSession
):
    student = service.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return service.update_student(db,student,student_data)


@router.delete("/{student_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int,db: DbSession):
    student = service.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    service.delete_student(db, student)