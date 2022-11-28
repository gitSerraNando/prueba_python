
from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime,Float
from datetime import datetime



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    years_previous_experience = Column(Integer, index=True)
    skills = Column(String)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)



class Vacant(Base):
    __tablename__ = "Vacancies"

    id = Column(Integer, primary_key=True, index=True)
    position_name = Column(String, index=True)
    company_name = Column(String, index=True)
    salary = Column(Integer, index=True)
    currency = Column(String, index=True)
    vacancy_link = Column(String)
    required_skills = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

