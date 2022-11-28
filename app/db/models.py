
from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime
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


