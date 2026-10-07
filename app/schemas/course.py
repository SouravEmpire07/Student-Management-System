from pydantic import BaseModel, ConfigDict, Field


class CourseCreate(BaseModel):
    """
    Pydantic schema representing the payload for creating a new course.

    Validates course name length (2 to 100 characters) and credit bounds (1 to 10 credits).
    """
    name: str = Field(
        min_length=2,
        max_length=100
    )

    credits: int = Field(
        ge=1,
        le=10
    )


class CourseResponse(BaseModel):
    """
    Pydantic schema representing the serialized course data returned in API responses.

    Features automatic attribute mapping configuration to work seamlessly with SQLAlchemy models.
    """
    id: int
    name: str
    credits: int

    # Enable ORM compatibility to serialize directly from SQLAlchemy model instances
    model_config = ConfigDict(from_attributes=True)