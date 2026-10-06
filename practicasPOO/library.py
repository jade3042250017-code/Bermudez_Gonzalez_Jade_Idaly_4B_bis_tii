from books import *;
from users import *;
class library:
    def __init__(self):
        self.users = []
        self.books = []
        self._user_indexes = 1 if self.books == [] else users[len(books)-1].id+1
        self._book_indexes = 1 if self.books == [] else books[len(books)-1].id+1
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        if (self.books != []):
            for book in self.books:
                print(book.show_book_info())
        else:
            print("Empty...")
        input("[Enter]")

    def show_users(self):
        if (self.users != []):
            for user in self.users:
                print(user.show_user_info())
        else:
            print("Empty...")
        input("[Enter]")

    def register_book(self):
        title = input("Enter the title of the book to register down bellow:\n")
        author = input("Enter the author of the book to register down bellow:\n")
        editorial = input("Enter the editorial of the book to register down bellow:\n")
        generated_book = book(str(self._book_indexes), title, author, editorial)
        self._book_indexes+=1
        input(f"Registered as: {generated_book.show_book_info()}[Enter]")
        self.books.append(generated_book)
        return True
    
    def register_user(self):
        name = input("Write the name of the user:\n")
        password = input("Write a new password please:\n")
        conf_password = input("Confirm the user password please:\n")
        if (password != conf_password):
            input("The passwords were not the same. Try again later... [Enter]")
            return False
        generated_user = user(str(self._user_indexes), name, password)
        self._user_indexes+=1
        input(f"Registered as: {generated_user.show_user_info()}[Enter]")
        self.users.append(generated_user)
        return True
    
    def borrow_book(self):
        name = input("Who is borrowing? ")
        user_exists = False
        user_picker = None
        book_borrowed = None
        for loc_user in self.users:
            if (loc_user.name == name):
                user_picker = loc_user
                user_exists = True
        if (not user_exists):
            input("The user was not found... [Enter]")
            return False
        id_book = input("Which book is the user looking for? ")
        book_exists = False
        for book in self.books:
            if (id_book == book.id):
                book_borrowed = book
                book_exists = True
        if (not book_exists):
            input("The book was not found... [Enter]")
            return False
        if (book_borrowed.available):
            input (f"Book {book_borrowed.title} borrowed by {user_picker.name}")
            user_picker.borrow_a_book(book_borrowed)
        else:
            input("That book is already taken.[Enter]")
    
    def return_book(self):
        name = input("Who is borrowing? ")
        user_exists = False
        user_picker = None
        for loc_user in self.users:
            if (loc_user.name == name):
                user_picker = loc_user
                user_exists = True
        if (not user_exists):
            input("The user was not found... [Enter]")
            return False
        print("Which book is the user returning?:")
        for i in range(0,len(user_picker.borrowed_books)):
            print(f"\t{i+1} <-+-> {user_picker.borrowed_books[i].title}")
        
        try: 
            id_book = int(input("\n"))
        except:
            input("That is not allowed!")
        if (id_book > 0 and id_book < len(user_picker.borrowed_books)+1):
            input(f"{user_picker.borrowed_books[id_book-1].title} was returned")
            user_picker.return_a_book(user_picker.borrowed_books[id_book-1])
        else:
            input("That book is not in the list of borrowed books")