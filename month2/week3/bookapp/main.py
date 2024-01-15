from fastapi import FastAPI

from routers.books import book_router
from routers.users import user_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(user_router, prefix="/users", tags=["Users"])


@app.get("/")
def home():
    return "Welcome to my super API"
