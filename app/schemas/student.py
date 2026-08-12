from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    """
    Pydantic schema representing the required payload for creating a new student.
    
    Includes validations for name length, valid email formatting, academic year range (1-4),
    CGPA boundaries (0-10), and phone number digit count limits.
    """
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)
    year: int = Field(ge=1, le=4)
    cgpa: float = Field(ge=0, le=10)
    phone: str = Field(min_length=10, max_length=15)


class StudentUpdate(BaseModel):
    """
    Pydantic schema representing the payload for updating an existing student.
    
    All fields are optional. Only the provided fields will be updated on the resource.
    Includes the same validation constraints as StudentCreate where applicable.
    """
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None
    department: str | None = Field(default=None, min_length=2, max_length=100)
    year: int | None = Field(default=None, ge=1, le=4)
    cgpa: float | None = Field(default=None, ge=0, le=10)
    phone: str | None = Field(default=None, min_length=10, max_length=15)


class StudentResponse(BaseModel):
    """
    Pydantic schema representing the serialized student data returned in API responses.
    
    Features automatic attribute mapping configuration to work seamlessly with SQLAlchemy models.
    """
    id: int
    name: str
    email: EmailStr
    department: str
    year: int
    cgpa: float
    phone: str
    created_at: datetime

    # Enable ORM compatibility so that it can read data directly from the SQLAlchemy object
    model_config = ConfigDict(from_attributes=True)