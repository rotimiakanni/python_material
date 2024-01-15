from pydantic import BaseModel
from uuid import UUID


class BookBase(BaseModel):
    title: str
    price: float
    isbn: str
    publisher: str


class Book(BookBase):
    id: UUID


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str = None
    price: float = None
    isbn: str = None
    publisher: str = None
