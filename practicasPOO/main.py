import books as b, library as l, users as u

mainlib = l.library()
options = ""

while options != "7":
    print("\033c")
    options = input("What do you want to do?\n1)Register a book\n2)Register an user\n3)Borrow a book\n4)Return a book\n5)Show books\n6)Show users\n7)Exit\n")
    match options:
        case "1":
            mainlib.register_book()
        case "2":
            mainlib.register_user()
        case "3":
            mainlib.borrow_book()
        case "4":
            mainlib.return_book()
        case "5":
            mainlib.show_books()
        case "6":
            mainlib.show_users()
        case "7":
            print("Thanks for using our software ~ ")
        case _:
            input("That option does not exist")

#Requirementes
#1.- The system must allow register books. Done!
#2.- The system must allow register users. Done!
#3.- The system must allow a book to be borrow by an user. Done!
#4.- A book that has already been borrowed canot be borrowed again Done!
#5.- The sistem must allow a book to be returned Done!
