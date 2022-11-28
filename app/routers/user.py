from fastapi import APIRouter, status, Body
from app.schema.user import User


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post(
    '/create',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= 'Create User')
def user_create(user: User = Body(...)):
    return user
