def book_serializer(book) -> dict:
    """Converts a MongoDB book object to a Python dictionary"""
    return {
        "id": str(book.get("_id")),
        "title": book.get("title"),
        "isbn": book.get("isbn"),
        "price": book.get("price"),
        "publisher": book.get("publisher"),
    }


def books_serializer(books) -> list:
    """Converts a MongoDB cursor object to a list of Python dictionaries"""
    return [book_serializer(book) for book in books]
