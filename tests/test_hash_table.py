import sys
sys.path.append("../src")

from book import Book
from hash_table import HashTable


def test_add_book():
    library = HashTable()

    book = Book(
        "101",
        "Python Programming",
        "ABC",
        "2025",
        "Programming"
    )

    assert library.add_book(book) == True


def test_search_book():
    library = HashTable()

    book = Book(
        "101",
        "Python Programming",
        "ABC",
        "2025",
        "Programming"
    )

    library.add_book(book)

    result = library.search_book("101")

    assert result is not None
    assert result.title == "Python Programming"


def test_delete_book():
    library = HashTable()

    book = Book(
        "101",
        "Python Programming",
        "ABC",
        "2025",
        "Programming"
    )

    library.add_book(book)

    assert library.delete_book("101") == True
    assert library.search_book("101") is None


def test_duplicate_isbn():
    library = HashTable()

    book1 = Book("101", "Book One", "Author", "2025", "CS")
    book2 = Book("101", "Book Two", "Author", "2025", "CS")

    assert library.add_book(book1) == True
    assert library.add_book(book2) == False
