from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate
from services.user import user_service


users_router = APIRouter()


@users_router.get("/")
def get_all_users():
    pass


@users_router.post("/")
def create_user(user_in: UserCreate):
    user = user_service.create_user(user_in)

    if not user:
        raise HTTPException(
            status_code=401,
            detail={"message": "An error occurred when creating your profile"},
        )

    return {"message": "User created successfully!", "data": user}


@users_router.get("/{id}")
def get_user_details(id: str):
    user = user_service.get_user_details(id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail={"message": "User not found!"},
        )

    return user
