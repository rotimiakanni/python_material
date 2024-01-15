from fastapi import APIRouter
from schemas.user_schema import User

user_router = APIRouter()

users = [User(username="jane", age="30"), User(username="John", age=90)]


@user_router.get("/")
def get_users():
    return users
