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


def user_serializer(user) -> dict:
    """Converts a MongoDB user object to a Python dictionary"""
    return {
        "id": str(user.get("_id")),
        "username": user.get("username"),
        "email": user.get("email"),
        "full_name": user.get("full_name"),
        "password": user.get("password"),
    }


def users_serializer(users) -> list:
    """Converts a MongoDB cursor object to a list of Python dictionaries"""
    return [user_serializer(user) for user in users]
