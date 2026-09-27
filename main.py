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


def main():
    library = HashTable()

    while True:
        print("\n===== LIBRARY BOOK INDEXING SYSTEM =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")

            library.add_book(isbn, title, author)

        elif choice == "2":
            isbn = input("Enter ISBN to search: ")
            library.search_book(isbn)

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()
