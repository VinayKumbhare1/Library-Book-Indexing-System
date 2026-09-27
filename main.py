# Library Book Indexing System Using Hash Table

books = {}

def add_book():
    isbn = input("Enter ISBN: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    books[isbn] = {
        "title": title,
        "author": author
    }

    print("Book added successfully!")


def search_book():
    isbn = input("Enter ISBN to search: ")

    if isbn in books:
        print("Book Found!")
        print("Title:", books[isbn]["title"])
        print("Author:", books[isbn]["author"])
    else:
        print("Book not found!")


def main():
    while True:
        print("\n===== LIBRARY BOOK INDEXING SYSTEM =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


main()
