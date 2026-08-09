from sqlalchemy.orm import Session

from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def create_student(
        self,
        db: Session,
        student_data: StudentCreate
    ) -> Student:
        student = Student(
            name=student_data.name,
            email=student_data.email,
            department=student_data.department,
            year=student_data.year,
            cgpa=student_data.cgpa,
            phone=student_data.phone
        )

        return self.repository.create(db, student)

    def get_all_students(self, db: Session) -> list[Student]:
        return self.repository.get_all(db)

    def get_student_by_id(
        self,
        db: Session,
        student_id: int
    ) -> Student | None:
        return self.repository.get_by_id(db, student_id)

    def update_student(
        self,
        db: Session,
        student: Student,
        student_data: StudentUpdate
    ) -> Student:

        update_data = student_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(student, field, value)

        return self.repository.update(db, student)

    def delete_student(
        self,
        db: Session,
        student: Student
    ) -> None:
        self.repository.delete(db, student)