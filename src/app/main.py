from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session, select
from ..app.utils.db import engine, get_session
from ..app.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Database Initialized")
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users", response_model=list[User])
def list_users(session: Session = Depends(get_session)):
    stmt = select(User)
    users = session.exec(stmt).all()
    return users