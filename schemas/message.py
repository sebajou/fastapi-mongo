from pydantic import BaseModel

from pydantic import BaseModel, EmailStr
from typing import Optional, Any

from schemas.student import UpdateStudentModel
from schemas.spring import UpdateSpringModel


class MessageSchema(BaseModel):
    message: UpdateStudentModel | UpdateSpringModel
