from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.student import Student


Base.metadata.create_all(bind=engine)


app = FastAPI()