from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class Student(Document):
    fullname: str
    email: EmailStr
    course_of_study: str
    year: int
    gpa: float

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@school.com",
                "course_of_study": "Water resources engineering",
                "year": 4,
                "gpa": "3.76",
            }
        }

    class Settings:
        name = "student"


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
