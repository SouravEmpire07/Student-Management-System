from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.enrollment import Enrollment


class Student(Base):
    """
    SQLAlchemy Database Model representing a Student.
    
    Attributes:
        id (int): Unique identifier and primary key.
        name (str): Full name of the student (up to 100 characters).
        email (str): Unique email address of the student (indexed).
        department (str): Academic department of the student (e.g., Computer Science).
        year (int): Academic year of the student (1 to 4).
        cgpa (float): Cumulative Grade Point Average of the student (0.0 to 10.0).
        phone (str): Contact phone number of the student.
        created_at (datetime): Timestamp when the student record was created.
        enrollments (list[Enrollment]): One-to-many relationship linking student to their course enrollments.
    """

    __tablename__ = "students"

    # Unique student ID, auto-incremented primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # Name of the student
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Unique email address, indexed for fast retrieval
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    # Academic department name
    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Current year of study
    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # Cumulative Grade Point Average (CGPA)
    cgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # Contact phone number
    phone: Mapped[str] = mapped_column(
        String(15),
        nullable=False
    )

    # Auto-populated creation timestamp
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    
    # One-to-many relationship: A student can be enrolled in multiple courses
    enrollments: Mapped[list["Enrollment"]] = relationship(
        back_populates="student"
    )