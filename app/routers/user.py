from typing import List
from fastapi import APIRouter, status, Body, Depends, HTTPException, Path
from app.schema.user import UserBase, UserCreate, ShowUser, UpdateUser
from app.repository import user
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get(
    '/',
    response_model=List[ShowUser],
    status_code=status.HTTP_200_OK,
    summary='Get all Users'
)
def show_all_users(db: Session = Depends(get_db)):
    """
    This path operation shows all users in the app

    Parameters:
        -

    Returns a json list with all users in the app, with the following keys:
        - email: Emailstr
        - first_name: str
        - last_name: str
        - years_previous_experience: int
        - skills: list
    """
    data = user.get_users(db)
    return data


@router.get(
    '/{user_id}',
    response_model=ShowUser,
    status_code=status.HTTP_200_OK,
    summary='Get by id User'
)
def get_user(
    user_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
        db: Session = Depends(get_db)):
    """
    This path operation get by id user in the app

    Parameters:
        - Request path parameter
            - user_id: int

    Returns a json  with user in the app:
        - email: Emailstr
        - first_name: str
        - last_name: str
        - years_previous_experience: int
        - skills: list
    """
    user_data = user.get_user(user_id, db)
    return user_data


@router.post(
    '/create',
    response_model=UserBase,
    status_code=status.HTTP_201_CREATED,
    summary='Create User'
)
def user_create(user_body: UserCreate = Body(...), db: Session = Depends(get_db)):
    """
    Create User

    This path operation create a user in the app

    Parameters:
        - Request body parameter
            - user: UserCreate

    Returns a json with the basic user information:
        - email: Emailstr
        - first_name: str
        - last_name: str
        - years_previous_experience: int
        - skills: list

    """
    db_user = user.get_user_by_email(db, email=user_body.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user.create_user(db, user_body)


@router.patch(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    summary='Update User'
)
def update_user(
    user_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
    update_user: UpdateUser = Body(...),
        db: Session = Depends(get_db)):
    """
    Update User

    This path operation update a user in the app

    Parameters:
        - Request path parameter
            - user_id: int
        - Request body parameter
            - user: UpdateUser

    Returns a message successfully :

    """
    res = user.update_user(user_id, update_user, db)
    return res


@router.delete(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    summary='Delete User'

)
def delete_user(
    user_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
        db: Session = Depends(get_db)):
    """
    Delete User

    This path operation Delete a user in the app

    Parameters:
        - Request path parameter
            - user_id: int

    Returns a message successfully :
    """

    res = user.delete_user(user_id, db)
    return res
