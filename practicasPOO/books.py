
class book:
    def __init__(self, id_book, title, author, editorial):
        self.id = id_book
        self.title = title
        self.author = author
        self.editorial = editorial
        self.available = True    
    def show_book_info(self):
        return (f"Book Id: {self.id} <-+-> Title: {self.title} <-+-> Author: {self.author} <-+-> Status: {"Available" if self.available else "Borrowed"}")
    
    def borrow_book(self):
        self.available = False

    def return_book(self):
        self.available = True