from book import Book
from hash_table import HashTable
from utils import get_isbn, get_book_details


def main():
    library = HashTable()

    while True:
        print("\n================================")
        print("   LIBRARY BOOK INDEXING SYSTEM")
        print("================================")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Display All Books")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = get_isbn()
            title, author, year, category = get_book_details()

            book = Book(
                isbn,
                title,
                author,
                year,
                category
            )

            if library.add_book(book):
                print("Book added successfully!")
            else:
                print("Book with this ISBN already exists!")

        elif choice == "2":
            isbn = get_isbn()
            book = library.search_book(isbn)

            if book:
                print("\n===== BOOK FOUND =====")
                book.display()
            else:
                print("Book not found!")

        elif choice == "3":
            isbn = get_isbn()
            title, author, year, category = get_book_details()

            if library.update_book(
                isbn,
                title,
                author,
                year,
                category
            ):
                print("Book updated successfully!")
            else:
                print("Book not found!")

        elif choice == "4":
            isbn = get_isbn()

            if library.delete_book(isbn):
                print("Book deleted successfully!")
            else:
                print("Book not found!")

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Select 1-6.")


if __name__ == "__main__":
    main()
