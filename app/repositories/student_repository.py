from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.student import Student


class StudentRepository:

    def create(self, db: Session, student: Student) -> Student:
        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    def get_all(self, db: Session) -> list[Student]:
        statement = select(Student)
        result = db.execute(statement)

        return list(result.scalars().all())

    def get_by_id(self, db: Session, student_id: int) -> Student | None:
        statement = select(Student).where(Student.id == student_id)
        result = db.execute(statement)

        return result.scalar_one_or_none()

    def update(self, db: Session, student: Student) -> Student:
        db.commit()
        db.refresh(student)

        return student

    def delete(self, db: Session, student: Student) -> None:
        db.delete(student)
        db.commit()