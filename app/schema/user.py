
# Python
from uuid import UUID
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# User Model
class User(BaseModel):  # Schema
    user_id: UUID = Field(...)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Hernando'

    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Escobar'

    )
    email: EmailStr = Field(
        ...,
        example='test@dominio.com'
    )
    years_previous_experience:  int = Field(
        ...,
        gt=0,
        le=50,
        example=5
    )
    skills: list = Field(
        ...,
        example=[{
            "Python": 1
        },
            {
            "NoSQL": 2
        }]
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
