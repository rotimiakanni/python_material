from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    price: float
    isbn: str
    publisher: str


class Book(BookBase):
    id: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str = None
    price: float = None
    isbn: str = None
    publisher: str = None


class UserBase(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None


class UserInDB(UserBase):
    id: str
    password: str


class UserCreate(UserBase):
    password: str
