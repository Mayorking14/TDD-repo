
from book_record import Book


class BookLibrary:
    book_list = []

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        self.book_list.append(book)
        return f"The book {book} has been added to the library"