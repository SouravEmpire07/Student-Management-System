from fastapi import FastAPI

from app.controllers.student_controller import register_student_routes
from app.database.database import Base, engine
from app.models.student import Student


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management System",
    version="1.0.0"
)

register_student_routes(app)