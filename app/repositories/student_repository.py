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

    def get_all(
        self,
        db: Session,
        search: str | None = None,
        department: str | None = None,
        year: int | None = None,
        cgpa: float | None = None
    ) -> list[Student]:
        """
        Retrieves all student records, with optional search and filtering by department, year, and minimum CGPA.
        
        Args:
            db (Session): Active database session.
            search (str | None): Optional search query for the student's name (case-insensitive substring).
            department (str | None): Optional department name to filter by.
            year (int | None): Optional academic year to filter by.
            cgpa (float | None): Optional minimum CGPA score to filter by.
            
        Returns:
            list[Student]: List of matching student database model instances.
        """


        statement = select(Student)

        # Apply search filter if specified
        if search is not None:
            statement = statement.where(
                Student.name.ilike(f"%{search}%")
            )

        # Apply department filter if specified
        if department is not None:
            statement = statement.where(
                Student.department == department
            )

        # Apply year filter if specified
        if year is not None:
            statement = statement.where(
                Student.year == year
            )

        # Apply CGPA filter if specified
        if cgpa is not None:
            statement = statement.where(
                Student.cgpa >= cgpa
            )

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
        """
        Finds a student by their unique email address.
        
        Args:
            db (Session): Active database session.
            email (str): Email address of the student to search for.
            
        Returns:
            Student | None: The student model instance if found, otherwise None.
        """
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