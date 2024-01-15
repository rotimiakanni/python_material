from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class AccountType(str, Enum):
    SavingsAccount = "SavingsAccount"
    CurrentAccount = "CurrentAccount"


class AccountBase(BaseModel):
    account_type: AccountType


class AccountCreate(AccountBase):
    pass


class AccountUpdate(BaseModel):
    account_type: AccountType = None
    balance: float = 0.0


class Account(AccountBase):
    user_id: str
    balance: float = 0.0
    created_at: datetime
    updated_at: datetime


class AccountInDB(AccountBase):
    id: str
    user_id: str
    balance: float = 0.0
    created_at: datetime
    updated_at: datetime
