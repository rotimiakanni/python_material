from fastapi import APIRouter, HTTPException, Depends, Request
from schemas.account import AccountCreate
from services.account import account_service
from deps import get_current_user
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

accounts_router = APIRouter()


@accounts_router.get("/")
def get_all_accounts():
    pass


@accounts_router.post("/")
def create_account(account_in: AccountCreate, current_user=Depends(get_current_user)):
    account = account_service.create_account(account_in, current_user)

    if not account:
        raise HTTPException(
            status_code=401,
            detail={"message": "An error occurred when creating your account"},
        )

    return {"message": "Account created successfully!", "data": account}


@accounts_router.post("/deposit/")
def deposit_money(amount: float, current_user=Depends(get_current_user)):
    account = account_service.deposit(amount, current_user)

    if not account:
        raise HTTPException(
            status_code=401,
            detail={"message": "An error occurred! we could not make the deposit"},
        )

    return {"message": "Deposit made successfully!", "data": account}


@accounts_router.post("/withdraw/")
@limiter.limit("10/minute")
def withdraw_money(
    amount: float, request: Request, current_user=Depends(get_current_user)
):
    account = account_service.withdraw(amount, current_user)

    if not account:
        raise HTTPException(
            status_code=401,
            detail={"message": "An error occurred! we could not find your money"},
        )

    return {"message": "Withdraw successfully!", "data": account}
