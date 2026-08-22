from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    name: str = Field(nullable=False)
    email: str = Field(unique=True, nullable=False)
    password: str = Field(min_length=8, nullable=False)

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class CreateUser(UserBase):
    pass

class UpdateUser(UserBase):
    pass