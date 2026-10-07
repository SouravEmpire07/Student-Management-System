from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.student import Student
    from app.models.course import Course


class Enrollment(Base):
    """
    SQLAlchemy Database Model representing a Student's Enrollment in a Course.
    Acts as an association entity connecting students and courses.

    Attributes:
        id (int): Unique identifier and primary key for the enrollment record.
        student_id (int): Foreign key referencing the enrolled student's ID.
        course_id (int): Foreign key referencing the enrolled course's ID.
        student (Student): Relationship linking back to the Student model instance.
        course (Course): Relationship linking back to the Course model instance.
    """
    __tablename__ = "enrollments"

    # Unique enrollment ID, auto-incremented primary key
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # Foreign key referencing the associated student record
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )

    # Foreign key referencing the associated course record
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    # Many-to-one relationship: Links this enrollment back to the specific Student
    student: Mapped["Student"] = relationship(
        back_populates="enrollments"
    )

    # Many-to-one relationship: Links this enrollment back to the specific Course
    course: Mapped["Course"] = relationship(
        back_populates="enrollments"
    )