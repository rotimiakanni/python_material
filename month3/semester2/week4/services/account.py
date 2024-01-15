from fastapi import HTTPException
from schemas.account import AccountCreate, Account
from schemas.user import UserInDB
from database import accounts_collection
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from serializers import account_serializer


class AccountService:
    def create_account(self, account_in: AccountCreate, current_user: UserInDB):
        account_schema = Account(
            **account_in.dict(),
            user_id=current_user.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        account_id = accounts_collection.insert_one(
            jsonable_encoder(account_schema)
        ).inserted_id
        account = accounts_collection.find_one({"_id": account_id})

        return account_serializer(account)

    def deposit(self, amount: float, current_user: UserInDB):
        account = accounts_collection.find_one({"user_id": current_user.id})

        if not account:
            return None

        new_balance = account["balance"] + amount
        account = accounts_collection.find_one_and_update(
            {"_id": account["_id"]},
            {"$set": {"balance": new_balance}},
            return_document=True,
        )

        return account_serializer(account)

    def withdraw(self, amount: float, current_user: UserInDB):
        account = accounts_collection.find_one({"user_id": current_user.id})

        if not account:
            return None

        if account["balance"] < amount:
            raise HTTPException(
                status_code=401, detail={"message": "INSUFFICIENT FUNNNNDDDDSSSS"}
            )

        new_balance = account["balance"] - amount
        account = accounts_collection.find_one_and_update(
            {"_id": account["_id"]},
            {"$set": {"balance": new_balance}},
            return_document=True,
        )

        return account_serializer(account)


account_service = AccountService()
