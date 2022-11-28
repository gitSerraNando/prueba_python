from typing import List
from fastapi import APIRouter, status, Body, Depends, HTTPException, Path
from app.schema.vacant import VacantCreate,Vacant
from app.repository import vacant
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter(
    prefix="/vacant",
    tags=["Vacancies"]
)


@router.get(
    '/',
    response_model=List[VacantCreate],
    status_code=status.HTTP_200_OK,
    summary='Get all Vacancies'
)
def show_all_vacancies(db: Session = Depends(get_db)):
    """
    This path operation shows all vacancies in the app

    Parameters:
        -

    Returns a json list with all vacancies in the app, with the following keys:
        - position_name str
        - company_name tr
        - salary int
        - currency str
        - vacancy_link list
    """
    data = vacant.show_all_vacancies(db)
    return data


@router.get(
    '/{vacant_id}',
    response_model=VacantCreate,
    status_code=status.HTTP_200_OK,
    summary='Get by id Vacant'
)
def get_vacant(
    vacant_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
        db: Session = Depends(get_db)):
    """
    This path operation get by id vacant in the app

    Parameters:
        - Request path parameter
            - vacant_id: int

    Returns a json  with vacant in the app:
        - position_name str
        - company_name tr
        - salary int
        - currency str
        - vacancy_link list
    """
    vacant_data = vacant.get_vacant(vacant_id, db)
    return vacant_data


@router.post(
    '/create',
    response_model=VacantCreate,
    status_code=status.HTTP_201_CREATED,
    summary='Create Vacant'
)
def create_vacant(vacant_body: Vacant = Body(...), db: Session = Depends(get_db)):
    """
    Create Vacant

    This path operation create a Vacant in the app

    Parameters:
        - Request body parameter
            - vacant_body: Vacant

    Returns a json with the basic vacant information:
        - position_name str
        - company_name str
        - salary str
        - currency str
        - vacancy_link HttpUrl
        - required_skills str

    """

    return vacant.create_vacant(db, vacant_body)


@router.patch(
    '/{vacant_id}',
    status_code=status.HTTP_200_OK,
    summary='Update vacant'
)
def update_vacant(
    vacant_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
    update_vacant: Vacant = Body(...),
        db: Session = Depends(get_db)):
    """
    Update vacant

    This path operation update a vacant in the app

    Parameters:
        - Request path parameter
            - vacant_id: int
        - Request body parameter
            - vacant: Updatevacant

    Returns a message successfully :

    """
    res = vacant.update_vacant(vacant_id, update_vacant, db)
    return res


@router.delete(
    '/{vacant_id}',
    status_code=status.HTTP_200_OK,
    summary='Delete Vacant'

)
def delete_vacant(
    vacant_id: int = Path(
        ...,
        gt=0,
        example=1
    ),
        db: Session = Depends(get_db)):
    """
    Delete vacant

    This path operation Delete a vacant in the app

    Parameters:
        - Request path parameter
            - vacant_id: int

    Returns a message successfully :
    """

    res = vacant.delete_vacant(vacant_id, db)
    return res
