# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# User Model

class UserBase(BaseModel):
    # user_id: UUID = Field(...)
    email: EmailStr = Field(
        ...,
        example='test@dominio.com'
    )

    class Config:
        orm_mode = True


class User(UserBase):  # Schema
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


class UserCreate(User):
    password: str


class ShowUser(BaseModel):
    email: str
    first_name: str
    last_name: str

    class Config():
        orm_mode = True


class UpdateUser(BaseModel):  
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
    class Config():
        orm_mode = True
