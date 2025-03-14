# #### Task 1: Create a Library Management System with Custom Exceptions
# 1. Create a Python program to manage a small library system. 
# 2. Define custom exceptions for specific scenarios:
#    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
#    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
#    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# 3. Implement classes for:
#    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
#    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
#    - **`Library`**: Manages books and members, including borrowing and returning books.
# 4. Test your program with the following scenarios:
#    - Adding books and members.
#    - Borrowing and returning books.
#    - Handling exceptions when rules are violated.
# ---
import json

# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book Class
class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if self.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{self.title}' is already borrowed!")
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

# Member Class
class Member:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books!")
        book.borrow()
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)

# Library Class
class Library:
    def __init__(self, data_file="library_data.json"):
        self.data_file = data_file
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_data()

    def add_member(self, name):
        self.members.append(Member(name))
        self.save_data()

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found!")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found!")
            return
        
        book = self.find_book(book_title)
        member.borrow_book(book)
        self.save_data()
        print(f"'{book_title}' borrowed by {member_name}!")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found!")
            return

        book = self.find_book(book_title)
        member.return_book(book)
        self.save_data()
        print(f"'{book_title}' returned by {member_name}!")

    def save_data(self):
        data = {
            "books": [{"title": book.title, "author": book.author, "is_borrowed": book.is_borrowed} for book in self.books],
            "members": [{"name": member.name, "borrowed_books": member.borrowed_books} for member in self.members]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.books = [Book(**book) for book in data.get("books", [])]
                self.members = [Member(member["name"], member["borrowed_books"]) for member in data.get("members", [])]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
            self.members = []


    def display_books(self):
        print("\n Available Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} [{status}]")

    def display_members(self):
        print("\n Library Members:")
        for member in self.members:
            print(f"- {member.name}, Borrowed Books: {', '.join(member.borrowed_books) if member.borrowed_books else 'None'}")

# Main Menu
def main():
    library = Library()

    while True:
        print("\n Library Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books & Members")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print(f"Book '{title}' added!")

        elif choice == "2":
            name = input("Enter member name: ")
            library.add_member(name)
            print(f"Member '{name}' added!")

        elif choice == "3":
            name = input("Enter member name: ")
            title = input("Enter book title: ")
            try:
                library.borrow_book(name, title)
            except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
                print(f"Error: {e}")

        elif choice == "4":
            name = input("Enter member name: ")
            title = input("Enter book title: ")
            try:
                library.return_book(name, title)
            except BookNotFoundException as e:
                print(f"Error: {e}")

        elif choice == "5":
            library.display_books()
            library.display_members()

        elif choice == "6":
            library.save_data()
            print(" Data saved. Exiting...")
            break

        else:
            print(" Invalid choice, try again!")

if __name__ == "__main__":
    main()
