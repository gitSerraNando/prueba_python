from app.db import models
from fastapi import HTTPException, status
from app.schema.vacant import Vacant
from sqlalchemy.orm import Session
import json



def show_all_vacancies(db:Session):
    data = db.query(models.Vacant).all()
    return data

def get_vacant(vacant_id,db:Session):
    vacant_data = db.query(models.Vacant).filter(models.Vacant.id == vacant_id ).first()
    if not vacant_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The Vacant with the id does not exist {vacant_id}"
        )
    return vacant_data


def create_vacant(db: Session, vacant: Vacant,):
    skills_string = json.dumps(vacant.required_skills)
    vacant.required_skills = skills_string

    vacant = vacant.dict()
    try:
        db_vacant = models.Vacant(
            position_name=vacant['position_name'],
            company_name=vacant['company_name'],
            salary=vacant['salary'],
            currency=vacant['currency'],
            vacancy_link=vacant['vacancy_link'],
            required_skills=skills_string
        )
        db.add(db_vacant)
        db.commit()
        db.refresh(db_vacant)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creating vacant {e}"
        )
    return  db_vacant

def update_vacant(vacant_id,update_vacant,db:Session):
    vacant = db.query(models.Vacant).filter(models.Vacant.id == vacant_id )
    if not vacant.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The vacant with the id does not exist {vacant_id}"
        )
    skills_string= json.dumps(update_vacant.required_skills)
    update_vacant.required_skills = skills_string
    vacant.update(update_vacant.dict( exclude_unset=True))
    db.commit()
    return {"message":"vacant updated successfully!"}

def delete_vacant(vacant_id,db:Session):
    vacant = db.query(models.Vacant).filter(models.Vacant.id == vacant_id )
    if not vacant.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The vacant with the id does not exist{vacant_id}"
        )
    vacant.delete(synchronize_session=False)
    db.commit()
    return {"message":"Vacant delete successfully!"}
