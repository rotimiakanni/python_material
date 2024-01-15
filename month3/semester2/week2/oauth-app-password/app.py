from fastapi import FastAPI, HTTPException, Depends
from schemas import BookCreate, BookUpdate, Book, UserCreate
from crud import crud_service
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import verify_password


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud_service.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    if not verify_password(form_data.password, user.get("password")):
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})


@app.post("/")
def create_book(book_in: BookCreate):
    book = crud_service.create_book(book_in)
    return {"message": "Book created successfully!", "data": book}


@app.get("/books", response_model=list[Book])
def get_all_books(skip: int = 0, limit: int = 10, token: str = Depends(oauth2_scheme)):
    books = crud_service.get_all_books(skip, limit)
    return books


@app.get("/books/{book_id}")
def get_book_id(book_id: str):
    book = crud_service.get_book_by_id(book_id)

    if book:
        return book

    raise HTTPException(status_code=401, detail={"message": "Book does not exists"})


@app.put("/")
def update_book(book_id: str, book_update_in: BookUpdate):
    book = crud_service.update_book(book_id, book_update_in)
    return {"message": "Book updated successfully", "data": book}


@app.delete("/")
def delete_book(book_id: str, token: str = Depends(oauth2_scheme)):
    crud_service.delete_book(book_id)

    return {"message": "Book deleted successfully"}


@app.post("/users/create")
def create_user(user_in: UserCreate):
    user = crud_service.create_user(user_in)
    return {"message": "User created successfully!", "data": user}
