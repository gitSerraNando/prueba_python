# FastAPI
from fastapi import FastAPI
import uvicorn 
from app.db.database import Base,engine

# Routes
from app.routers import user
from app.routers import vacant


def create_database():
    Base.metadata.create_all(bind=engine)
create_database()

app = FastAPI()
app.include_router(user.router)
app.include_router(vacant.router)




# if __name__=="__main__":
#     uvicorn.run("main:app",port=8080,reload=True)

prueba_python