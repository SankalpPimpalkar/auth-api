from sqlmodel import Field, SQLModel
from pydantic import BaseModel
from datetime import datetime


class Token(SQLModel):
    access_token: str = Field(nullable=False)
    token_type: str = Field(default="bearer")

class TokenData(BaseModel):
    email: str
    exp: datetime | None = None