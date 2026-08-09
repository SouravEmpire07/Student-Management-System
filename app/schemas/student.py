from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)
    year: int = Field(ge=1, le=4)
    cgpa: float = Field(ge=0, le=10)
    phone: str = Field(min_length=10, max_length=15)


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None
    department: str | None = Field(default=None, min_length=2, max_length=100)
    year: int | None = Field(default=None, ge=1, le=4)
    cgpa: float | None = Field(default=None, ge=0, le=10)
    phone: str | None = Field(default=None, min_length=10, max_length=15)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    year: int
    cgpa: float
    phone: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)