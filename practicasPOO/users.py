from books import *
class user:
    def __init__(self, id_user, name, password):
        self.id = id_user
        self.name = name
        self._password = password
        self.borrowed_books = []
    def show_user_info(self):
        return f"User Id: {self.id} <-+-> Username: {self.name}"

    def borrow_a_book(self, book):
        self.borrowed_books.append(book)
        book.borrow_book()
    
    def return_a_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()
