from pydantic import BaseModel


class User(BaseModel):
    username: str
    age: int


class UserCreate(User):
    pass
