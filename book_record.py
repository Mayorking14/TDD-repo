class Book:
    title = ""
    author = ""
    isbn = ""
    description = ""
    is_borrowed = False

    def __init__(self, title, isbn, author = "makavelli"):
        self.title = title
        self.isbn = isbn
        self.author = author

        def get_book_title(self):
            return self.title

        def check_book_status(self):
            return self.is_borrowed

        def add_description(self, description):
            self.description = description
            return "description added succesfuly"

        def borrow_book(self):
            if not self.check_book_status():
                self.is_borrowed = True
