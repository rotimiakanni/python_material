from schemas import BookCreate, BookUpdate
from uuid import UUID
import uuid
from models import Book
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


class CRUDService:
    def create_book(self, db: Session, book_in: BookCreate):
        book = Book(id=str(uuid.uuid4()), **book_in.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def get_all_books(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Book).order_by(Book.title).offset(skip).limit(limit).all()

    def get_book_by_id(self, db: Session, book_id: UUID):
        book = db.query(Book).filter(Book.id == str(book_id)).first()
        return book

    def update_book(self, db: Session, book_id: UUID, book_update_in: BookUpdate):
        book = self.get_book_by_id(db, book_id)
        book_data = jsonable_encoder(book)
        update_data = book_update_in.dict(skip_defaults=True)

        for field in book_data:
            if field in update_data:
                setattr(book, field, update_data[field])

        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def delete_book(self, db: Session, book_id):
        book = self.get_book_by_id(db, book_id)
        if not book:
            return None

        db.delete(book)
        db.commit()

        return book


crud_service = CRUDService()
