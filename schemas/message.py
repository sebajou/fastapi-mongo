from pydantic import BaseModel

from pydantic import BaseModel, EmailStr
from typing import Optional, Any

from schemas.student import UpdateStudentModel


class MessageSchema(BaseModel):
    message: UpdateStudentModel
