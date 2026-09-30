def get_isbn():
    while True:
        isbn = input("Enter ISBN: ")

        if isbn.isdigit():
            return isbn

        print("Invalid ISBN! Enter numbers only.")


def get_book_details():
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Publication Year: ")
    category = input("Enter Category: ")

    return title, author, year, category
