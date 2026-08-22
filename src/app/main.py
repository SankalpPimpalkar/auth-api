from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from .database import engine
from .routes.auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Database Initialized")
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Hello World"}