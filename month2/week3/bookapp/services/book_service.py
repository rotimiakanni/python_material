from schemas.book_schema import Book


class BookService:
    def get_book_by_title(self, books: list[Book], title: str):
        for book in books:
            if book.title == title:
                return book

        return None


book_service = BookService()
