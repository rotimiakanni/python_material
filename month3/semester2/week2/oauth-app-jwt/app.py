from fastapi import FastAPI, HTTPException, Depends
from schemas import BookCreate, BookUpdate, Book, UserCreate, TokenData, UserInDB
from crud import crud_service
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import verify_password
from datetime import datetime, timedelta
from jose import JWTError, jwt


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "e2f65907d195806863bf8a8e5649974e655bfc5b0e33d3482fa2303870220c31"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = crud_service.get_user_by_username(token_data.username)

    if user is None:
        raise credentials_exception

    return user


@app.post("/auth/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud_service.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    if not verify_password(form_data.password, user.get("password")):
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.get("username")}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/")
def create_book(
    book_in: BookCreate, current_user: UserInDB = Depends(get_current_user)
):
    book = crud_service.create_book(book_in)
    return {"message": "Book created successfully!", "data": book}


@app.get("/books", response_model=list[Book])
def get_all_books(
    skip: int = 0, limit: int = 10, current_user: UserInDB = Depends(get_current_user)
):
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
def delete_book(book_id: str):
    crud_service.delete_book(book_id)

    return {"message": "Book deleted successfully"}


@app.post("/users/create")
def create_user(user_in: UserCreate):
    user = crud_service.create_user(user_in)
    return {"message": "User created successfully!", "data": user}
