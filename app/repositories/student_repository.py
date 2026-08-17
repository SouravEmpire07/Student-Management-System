from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.student import Student


class StudentRepository:
    """
    Repository class handling direct database access and CRUD operations for the Student model.
    """

    def create(self, db: Session, student: Student) -> Student:
        """
        Inserts a new student record into the database.
        
        Args:
            db (Session): Active database session.
            student (Student): SQLAlchemy model instance to be saved.
            
        Returns:
            Student: The persisted student record with populated ID and timestamps.
        """
        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    def get_all(self, db: Session) -> list[Student]:
        """
        Retrieves all student records from the database.
        
        Args:
            db (Session): Active database session.
            
        Returns:
            list[Student]: List of all student model instances.
        """
        statement = select(Student)
        result = db.execute(statement)

        return list(result.scalars().all())

    def get_by_id(self, db: Session, student_id: int) -> Student | None:
        """
        Finds a student by their unique ID.
        
        Args:
            db (Session): Active database session.
            student_id (int): ID of the student to search for.
            
        Returns:
            Student | None: The student model instance if found, otherwise None.
        """
        statement = select(Student).where(Student.id == student_id)
        result = db.execute(statement)

        return result.scalar_one_or_none()

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> Student | None:
        statement = select(Student).where(
            Student.email == email
        )
        result = db.execute(statement)

        return result.scalar_one_or_none() 

    def update(self, db: Session, student: Student) -> Student:
        """
        Saves changes made to an existing student instance.
        
        Args:
            db (Session): Active database session.
            student (Student): Modified student model instance.
            
        Returns:
            Student: The updated student record refreshed from the database.
        """
        db.commit()
        db.refresh(student)

        return student

    def delete(self, db: Session, student: Student) -> None:
        """
        Removes a student record from the database.
        
        Args:
            db (Session): Active database session.
            student (Student): The student model instance to delete.
        """
        db.delete(student)
        db.commit()