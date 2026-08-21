from sqlmodel import Field, SQLModel

class Token(SQLModel):
    access_token: str = Field(nullable=False)
    token_type: str = Field(default="bearer")

class TokenData(SQLModel):
    id: str = Field(nullable=False)