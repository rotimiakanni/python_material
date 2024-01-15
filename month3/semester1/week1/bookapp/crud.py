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

    def get_all_books(self, db: Session):
        return db.query(Book).all()

    def get_book_by_id(self, db: Session, book_id: UUID):
        book = db.query(Book).filter(Book.id == str(book_id)).first()
        return book

    def update_book(self, db: Session, book_id: UUID, book_update_in: BookUpdate):
        book = self.get_book_by_id(db, book_id)

        if not book:
            return None

        book_update_in_dict = book_update_in.dict(exclude_unset=True)
        book_dict = jsonable_encoder(book)

        for key in book_dict:
            if key in book_update_in_dict:
                setattr(book, key, book_update_in_dict.get(key))

        db.add(book)
        db.commit()
        db.refresh(book)

        return book

    def delete_book(self, db: Session, book_id: UUID):
        book = self.get_book_by_id(db, book_id)

        db.delete(book)
        db.commit()

        return None


crud_service = CRUDService()
