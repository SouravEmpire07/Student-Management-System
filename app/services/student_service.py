from sqlalchemy.orm import Session

from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:
    """
    Service class encapsulating the business logic for managing student records.
    Coordinates between schemas and repository layer.
    """

    def __init__(self, repository: StudentRepository):
        """
        Initializes the service with a StudentRepository instance.
        """
        self.repository = repository

    def create_student(
        self,
        db: Session,
        student_data: StudentCreate
    ) -> Student:
        """
        Converts the incoming StudentCreate schema to a Student model and saves it.
        
        Args:
            db (Session): Active database session.
            student_data (StudentCreate): Input payload for creating a student.
            
        Returns:
            Student: Created student database record.
        """
        existing_student = self.repository.get_by_email(db, student_data.email)
        if existing_student:
            raise ValueError("Student with this email already exists")
        
        # Map the input Pydantic schema to the SQLAlchemy database model
        student = Student(
            name=student_data.name,
            email=student_data.email,
            department=student_data.department,
            year=student_data.year,
            cgpa=student_data.cgpa,
            phone=student_data.phone
        )

        return self.repository.create(db, student)

    # def get_all_students(self, db: Session) -> list[Student]:
    #     """
    #     Retrieves all students list.
        
    #     Args:
    #         db (Session): Active database session.
            
    #     Returns:
    #         list[Student]: List of all students.
    #     """
    #     return self.repository.get_all(db)

    def get_all_students(
        self,
        db: Session,
        department: str | None = None,
        year: int | None = None
    ) -> list[Student]:
        return self.repository.get_all(
            db,
            department,
            year
        )

    def get_student_by_id(
        self,
        db: Session,
        student_id: int
    ) -> Student | None:
        """
        Retrieves a single student by their ID.
        
        Args:
            db (Session): Active database session.
            student_id (int): ID of the student.
            
        Returns:
            Student | None: The student record if found, else None.
        """
        return self.repository.get_by_id(db, student_id)

    def update_student(
        self,
        db: Session,
        student: Student,
        student_data: StudentUpdate
    ) -> Student:
        """
        Updates fields of an existing student object with non-null values from StudentUpdate.
        
        Args:
            db (Session): Active database session.
            student (Student): Existing student database object to update.
            student_data (StudentUpdate): Input fields to update.
            
        Returns:
            Student: The updated student record.
        """
        # Exclude unset fields from the payload so we only update what the client sent
        update_data = student_data.model_dump(exclude_unset=True)

        # Dynamically set updated attribute values on the SQLAlchemy model
        for field, value in update_data.items():
            setattr(student, field, value)

        return self.repository.update(db, student)

    def delete_student(
        self,
        db: Session,
        student: Student
    ) -> None:
        """
        Deletes a student record.
        
        Args:
            db (Session): Active database session.
            student (Student): The database record of the student to delete.
        """
        self.repository.delete(db, student)