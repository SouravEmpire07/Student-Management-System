from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


if TYPE_CHECKING:
    from app.models.student import Student
    from app.models.course import Course


class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False
    )

    student: Mapped["Student"] = relationship(
        back_populates="enrollments"
    )

    course: Mapped["Course"] = relationship(
        back_populates="enrollments"
    )