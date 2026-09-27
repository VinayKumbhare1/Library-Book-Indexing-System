# Library Book Indexing System Using Hash Tables

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, isbn):
        return int(isbn) % self.size

    # Add book
    def add_book(self, isbn, title, author):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book["isbn"] == isbn:
                print("Book with this ISBN already exists!")
                return

        book = {
            "isbn": isbn,
            "title": title,
            "author": author
        }

        self.table[index].append(book)

        print("Book added successfully!")
        print("Hash Index:", index)

    # Search book
    def search_book(self, isbn):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book["isbn"] == isbn:
                print("\nBook Found!")
                print("ISBN:", book["isbn"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                return

        print("Book not found!")

    # Delete book
    def delete_book(self, isbn):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book["isbn"] == isbn:
                self.table[index].remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found!")

    # Update book
    def update_book(self, isbn):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book["isbn"] == isbn:
                print("\nCurrent Details")
                print("Title:", book["title"])
                print("Author:", book["author"])

                book["title"] = input("Enter new title: ")
                book["author"] = input("Enter new author: ")

                print("Book updated successfully!")
                return

        print("Book not found!")

    # Display all books
    def display_books(self):
        found = False

        print("\n===== ALL BOOKS =====")

        for index in range(self.size):
            for book in self.table[index]:
                found = True

                print("Index:", index)
                print("ISBN:", book["isbn"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("--------------------")

        if not found:
            print("No books available!")


def get_isbn():
    while True:
        isbn = input("Enter ISBN: ")

        if isbn.isdigit():
            return isbn

        print("Invalid ISBN! Please enter numbers only.")


def main():
    library = HashTable()

    while True:
        print("\n===== LIBRARY BOOK INDEXING SYSTEM =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Update Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = get_isbn()
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")

            library.add_book(isbn, title, author)

        elif choice == "2":
            isbn = get_isbn()
            library.search_book(isbn)

        elif choice == "3":
            isbn = get_isbn()
            library.delete_book(isbn)

        elif choice == "4":
            isbn = get_isbn()
            library.update_book(isbn)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()
