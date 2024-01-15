from fastapi import FastAPI
from uuid import UUID


app = FastAPI()

# Now we will create a book api, that performs CRUD operations
# on a book resource. We will use a list to store the books in memory.
# We will use a dictionary to store the book data.
# The book data will have the following fields:
# - id: int
# - title: str
# - author: str
# - year: int
# - pages: int
# - language: str

# Create a dict to store the books in memory.
books = {}

# Create a dictionary to store the book data.
book_data = {"id": 0, "title": "", "author": "", "year": 0, "pages": 0, "language": ""}


@app.get("/")
def home():
    return {"message": "Hello from the books API"}


# Get all books.
@app.get("/books")  # GET method to get a resource
def get_books():
    return books


# Get a single book using a path parameter
# You can declare path "parameters" or "variables" with the same syntax used by Python format strings
# The value of the path parameter item_id will be passed to your function as the argument item_id
@app.get("/books/{id}")  # GET method to get a resource
def get_book_by_id(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}

    return book


# Add a book.
@app.post("/books")  # POST method to create a new resource
def add_book(
    title: str, author: str, year: int, pages: int, language: str
):  # These parameters are called "query parameters", The query is the set of key-value pairs
    # that go after the ? in a URL, separated by & characters.
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int=len(books) + 1))
    new_book["title"] = title
    new_book["author"] = author
    new_book["year"] = year
    new_book["pages"] = pages
    new_book["language"] = language

    books[new_book["id"]] = new_book

    return {"message": "Book added successfully", "data": new_book}


# Update a book.
@app.put("/books/{id}")  # PUT method to update a resource
def update_book(
    id: str, title: str, author: str, year: int, pages: int, language: str
):  # A combination of path and query parameters
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}

    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["pages"] = pages
    book["language"] = language

    return {"message": "Book updated successfully", "data": book}


# Delete a book.
@app.delete("/books/{id}")  # DELETE method to delete a resource
def delete_book(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}

    del books[id]

    return {"message": "Book deleted successfully"}
