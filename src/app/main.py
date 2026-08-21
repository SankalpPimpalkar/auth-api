from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from app.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Database Initialized")
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "Hello World"}