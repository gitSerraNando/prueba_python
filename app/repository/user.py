from app.db import models
from fastapi import HTTPException, status
from app.schema.user import UserCreate
from sqlalchemy.orm import Session
import json


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db:Session):
    data = db.query(models.User).all()
    return data

def get_user(user_id,db:Session):
    user_data = db.query(models.User).filter(models.User.id == user_id ).first()
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with the id does not exist {user_id}"
        )
    return user_data


def create_user(db:Session,user: UserCreate,):
    skills_string= json.dumps(user.skills)
    user.skills = skills_string
    
    user = user.dict()
    fake_hashed_password = user['password'] + "notreallyhashed"
    
    
    try:
        db_user = models.User(
            email=user['email'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            years_previous_experience=user['years_previous_experience'],
            skills=skills_string,
            hashed_password = fake_hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creating user {e}"
        )
    return db_user



def update_user(user_id,update_user,db:Session):
    user = db.query(models.User).filter(models.User.id == user_id )
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with the id does not exis {user_id}"
        )
    skills_string= json.dumps(update_user.skills)
    update_user.skills = skills_string
    user.update(update_user.dict( exclude_unset=True))
    db.commit()
    return {"message":"User updated successfully!"}

def delete_user(user_id,db:Session):
    user = db.query(models.User).filter(models.User.id == user_id )
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with the id does not exist{user_id}"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return {"message":"User delete successfully!"}