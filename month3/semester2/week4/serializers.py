from schemas.user import UserInDB
from schemas.account import Account
from typing import List


def user_serializer(user) -> UserInDB:
    user_dict = {
        "id": str(user.get("_id")),
        "created_at": user.get("created_at"),
        "updated_at": user.get("updated_at"),
        "first_name": user.get("first_name"),
        "last_name": user.get("last_name"),
        "dob": user.get("dob"),
        "address": user.get("address"),
        "email": user.get("email"),
        "password": user.get("password"),
    }
    return UserInDB(**user_dict)


def users_serializer(users) -> List[UserInDB]:
    user_schemas = []
    for user in users:
        user_schemas.append(user_serializer(user))

    return user_schemas


def account_serializer(account):
    user_dict = {
        "id": account.get("_id"),
        "user_id": account.get("user_id"),
        "created_at": account.get("created_at"),
        "updated_at": account.get("updated_at"),
        "balance": account.get("balance"),
        "account_type": account.get("account_type"),
    }

    return Account(**user_dict)


def accounts_serializer(accounts):
    account_schemas = []
    for account in accounts:
        account_schemas.append(account_serializer(account))

    return account_schemas
