from schemas.user import UserCreate, User, UserAccount
from database import users_collection, accounts_collection
from datetime import datetime
from bson.objectid import ObjectId
from serializers import user_serializer
from fastapi.encoders import jsonable_encoder
from utils import get_password_hash
from pydantic import EmailStr


class UserService:
    def create_user(self, user_in: UserCreate):
        user_dict = user_in.dict()
        user_dict["password"] = get_password_hash(user_dict["password"])
        user = User(
            **user_dict, created_at=datetime.utcnow(), updated_at=datetime.utcnow()
        )
        user_id = users_collection.insert_one(jsonable_encoder(user)).inserted_id
        new_user = users_collection.find_one({"_id": user_id})

        return user_serializer(new_user)

    def get_user_by_email(self, email: EmailStr):
        user = users_collection.find_one({"email": email})
        return user_serializer(user)

    def get_user_by_id(self, id: str):
        user = users_collection.find_one({"_id": ObjectId(id)})
        return user_serializer(user)

    def get_user_details(self, id: str) -> UserAccount | None:
        user = self.get_user_by_id(id)

        if not user:
            return None

        account = accounts_collection.find_one({"user_id": user.id})
        user = UserAccount(**user.dict(), account=account)

        return user


user_service = UserService()
