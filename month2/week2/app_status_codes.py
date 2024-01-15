# In HTTP, you send a numeric status code of 3 digits as part of the response.

# These status codes have a name associated to recognize them, but the important part is the number.

# In short:

# 100 and above are for "Information". You rarely use them directly.
# 200 and above are for "Successful" responses. These are the ones you would use the most.
#  - 200 is the default status code, which means everything was "OK".
#  - 201, "Created". It is commonly used after creating a new record in the database.
# 300 and above are for "Redirection". You rarely use them directly.
# 400 and above are for "Client error" responses. These are the second type you would probably use the most.
#  - An example is 404, for a "Not Found" response.
#  - For generic errors from the client, you can just use 400.
# 500 and above are for server errors. You almost never use them directly. When something goes wrong at some part
# in your application code, or server, it will automatically return one of these status codes.


# status is a module that contains all the status codes. We can also use the status codes directly.
from fastapi import FastAPI, status, HTTPException
from uuid import UUID
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# We will use Pydantic to define the data model for the book resource.
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int
    language: str


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str


class BookUpdate(BaseModel):
    title: str
    pages: int


class Books(BaseModel):
    books: list[Book]


class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[Book | Books] = None


books: dict[str, Book] = {}


@app.get("/", status_code=200)  # We can also use the status codes directly.
def home():
    return Response(message="Hello from the books API")


@app.get(
    "/books", status_code=status.HTTP_200_OK
)  # We can also use the status codes from the status module.
def get_books():
    return books


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book_in: BookCreate):
    book = Book(
        id=str(UUID(int=len(books) + 1)),
        **book_in.dict(),
    )
    books[book.id] = book
    return Response(message="Book added successfully", data=book)


@app.put("/books/{id}", status_code=status.HTTP_200_OK)
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    book.title = book_in.title
    book.pages = book_in.pages

    return Response(message="Book updated successfully", data=book)


@app.delete("/books/{id}")
def delete_book(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    del books[book.id]

    return Response(message="Book deleted successfully")
