from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.enrollment import Enrollment


class Course(Base):
    """
    SQLAlchemy Database Model representing a Course.

    Attributes:
        id (int): Unique identifier and primary key.
        name (str): Name or title of the course (up to 100 characters).
        credits (int): Number of academic credits allocated for the course.
        enrollments (list[Enrollment]): One-to-many relationship with the Enrollment model.
    """
    __tablename__ = "courses"

    # Unique course ID, auto-incremented primary key
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # Name or title of the course
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Credit points assigned to the course
    credits: Mapped[int] = mapped_column(
        nullable=False
    )

    # One-to-many relationship: A course can have multiple enrollments
    enrollments: Mapped[list["Enrollment"]] = relationship(
        back_populates="course"
    )


