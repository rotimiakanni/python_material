from fastapi import FastAPI, HTTPException, Depends
from schemas import BookCreate, BookUpdate
from uuid import UUID
from crud import crud_service
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/")
def create_book(book_in: BookCreate, db: Session = Depends(get_db)):
    crud_service.create_book(db, book_in)
    return {"message": "Book created successfully!"}


@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    books = crud_service.get_all_books(db)
    return {"data": books}


@app.get("/books/{book_id}")
def get_book_id(book_id: UUID, db: Session = Depends(get_db)):
    book = crud_service.get_book_by_id(db, book_id)

    if book:
        return book

    raise HTTPException(status_code=401, detail={"message": "Book does not exists"})


@app.put("/")
def update_book(
    book_id: UUID, book_update_in: BookUpdate, db: Session = Depends(get_db)
):
    book = crud_service.update_book(db, book_id, book_update_in)
    if book is None:
        raise HTTPException(status_code=401, detail={"message": "Book does not exists"})

    return {"message": "Book updated successfully", "data": book}


@app.delete("/")
def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    book = crud_service.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(status_code=401, detail={"message": "Book does not exists"})

    crud_service.delete_book(db, book_id)

    return {"message": "Book deleted successfully"}
