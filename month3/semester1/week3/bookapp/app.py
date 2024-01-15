from fastapi import FastAPI, HTTPException
from schemas import BookCreate, BookUpdate, Book
from crud import crud_service

app = FastAPI()


@app.post("/")
def create_book(book_in: BookCreate):
    book = crud_service.create_book(book_in)
    return {"message": "Book created successfully!", "data": book}


@app.get("/books", response_model=list[Book])
def get_all_books():
    books = crud_service.get_all_books()
    return books


@app.get("/books/{book_id}")
def get_book_id(book_id: str):
    book = crud_service.get_book_by_id(book_id)

    if book:
        return book

    raise HTTPException(status_code=401, detail={"message": "Book does not exists"})


@app.put("/")
def update_book(book_id: str, book_update_in: BookUpdate):
    book = crud_service.update_book(book_id, book_update_in)
    return {"message": "Book updated successfully", "data": book}


@app.delete("/")
def delete_book(book_id: str):
    crud_service.delete_book(book_id)

    return {"message": "Book deleted successfully"}
