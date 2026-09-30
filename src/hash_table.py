class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, isbn):
        return int(isbn) % self.size

    def add_book(self, book):
        index = self.hash_function(book.isbn)

        for existing_book in self.table[index]:
            if existing_book.isbn == book.isbn:
                return False

        self.table[index].append(book)
        return True

    def search_book(self, isbn):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book.isbn == isbn:
                return book

        return None

    def update_book(self, isbn, title, author, year, category):
        book = self.search_book(isbn)

        if book:
            book.title = title
            book.author = author
            book.year = year
            book.category = category
            return True

        return False

    def delete_book(self, isbn):
        index = self.hash_function(isbn)

        for book in self.table[index]:
            if book.isbn == isbn:
                self.table[index].remove(book)
                return True

        return False

    def display_books(self):
        found = False

        for index in range(self.size):
            if self.table[index]:
                found = True
                print("\nHash Index:", index)

                for book in self.table[index]:
                    book.display()
                    print("--------------------")

        if not found:
            print("No books available.")
