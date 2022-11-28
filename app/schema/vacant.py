# Pydantic
from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import Field


class Vacant(BaseModel):
    position_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Python Dev"

    )
    company_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Test company"

    )
    salary:  int = Field(
        ...,
        gt=0,
        example=10000
    )
    currency: str = Field(
        ...,
        max_length=3,
        example="COP"
    )
    vacancy_link: HttpUrl = Field(
        ...,
        example="https://www.test.com"
    )
    required_skills: list = Field(
        ...,
        example=[{
            "Python": 1
        },
            {
            "NoSQL": 2
        }]
    )

    class Config:
        orm_mode = True

class VacantCreate(BaseModel):
    position_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Python Dev"

    )
    company_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Test company"

    )
  



    class Config:
        orm_mode = True
