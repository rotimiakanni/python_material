from schemas import BookCreate, BookUpdate, UserCreate
from fastapi.encoders import jsonable_encoder
from database import books_collection, users_collection
from bson.objectid import ObjectId
from serializers import (
    book_serializer,
    books_serializer,
    user_serializer,
)
from utils import get_password_hash


class CRUDService:
    def create_book(self, book_in: BookCreate):
        book_in_data = jsonable_encoder(book_in)
        book_id = books_collection.insert_one(book_in_data).inserted_id
        book = books_collection.find_one({"_id": book_id})
        return book_serializer(book)

    def get_all_books(self, skip: int = 0, limit: int = 10):
        books = books_collection.find().skip(skip).limit(limit).sort("title")
        return books_serializer(books)

    def get_book_by_id(self, book_id: str):
        book = books_collection.find_one({"_id": ObjectId(book_id)})
        if book:
            return book_serializer(book)

        return None

    def update_book(self, book_id: str, book_update_in: BookUpdate):
        book = books_collection.find_one({"_id": ObjectId(book_id)})

        if not book:
            return None

        book_update_data = book_update_in.dict(exclude_unset=True)
        book_updated = books_collection.find_one_and_update(
            {"_id": ObjectId(book_id)}, {"$set": book_update_data}, return_document=True
        )

        return book_serializer(book_updated)

    def delete_book(self, book_id):
        books_collection.find_one_and_delete({"_id": ObjectId(book_id)})
        return None

    def create_user(self, user_in: UserCreate):
        user_in_data = jsonable_encoder(user_in)
        user_in_data["password"] = get_password_hash(user_in_data["password"])
        user_id = users_collection.insert_one(user_in_data).inserted_id
        user = users_collection.find_one({"_id": user_id})
        return user_serializer(user)

    def get_user_by_username(self, username: str):
        user = users_collection.find_one({"username": username})
        if user:
            return user_serializer(user)

        return None


crud_service = CRUDService()
