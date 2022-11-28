
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from main import app
from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)
client = TestClient(app)


def create_database():
    Base.metadata.create_all(bind=engine)


def test_user_create():
    user = {
        "email": "test@dominio.com",
        "first_name": "Hernando",
        "last_name": "Escobar",
        "years_previous_experience": 5,
        "skills": [
            {
                "Python": 1
            },
            {
                "NoSQL": 2
            }
        ],
        "password": "string"
    }
    response = client.post('/user/create', json=user)
    assert response.status_code == 201
    assert response.json() == {
        "email": "test@dominio.com"
    }


def test_get_all_users():
    response = client.get('/user/')
    assert response.status_code == 200
    assert response.json() == [
        {
            "email": "test@dominio.com",
            "first_name": "Hernando",
            "last_name": "Escobar",
        }
    ]


def test_get_user_by_id():
    response = client.get('/user/1')
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@dominio.com",
        "first_name": "Hernando",
        "last_name": "Escobar",
    }


def test_update_user():
    user = {
        "email": "test_update@dominio.com",
        "first_name": "Hernando",
        "last_name": "Escobar",
        "years_previous_experience": 5,
        "skills": [
            {
                "Python": 1
            },
            {
                "NoSQL": 2
            }
        ],
        "password": "string"
    }
    response = client.patch('/user/1', json= user)
    assert response.status_code == 200
    assert response.json() == {"message":"User updated successfully!"}

def test_delete_user():
    response = client.delete('/user/1')
    assert response.status_code == 200
    assert response.json() == {"message":"User delete successfully!"}