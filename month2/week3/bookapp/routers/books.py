from fastapi import APIRouter
from schemas.book_schema import Book
from services.book_service import book_service

book_router = APIRouter()


books = [
    Book(title="Harry Potter", author="JK Rowling"),
    Book(title="Guardians", author="Rising Odegua"),
]


@book_router.get("/")
def get_books():
    return books


@book_router.get("/{title}")
def get_book(title: str):
    book = book_service.get_book_by_title(books, title)
    if book:
        return {"message": "Book found successfully!", "data": book}

    return {"message": "Book not found!", "data": None}
