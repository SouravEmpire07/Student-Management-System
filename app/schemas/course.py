from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    credits: int = Field(
        ge=1,
        le=10
    )


class CourseResponse(BaseModel):
    id: int
    name: str
    credits: int

    model_config = {
        "from_attributes": True
    }