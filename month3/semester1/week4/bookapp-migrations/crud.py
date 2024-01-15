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
        book = db.query(Book).filter(Book.id == str(book_id)).first()
        pass

    def delete_book(self, db: Session, book_id):
        pass


crud_service = CRUDService()
