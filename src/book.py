class Book:
    def __init__(self, isbn, title, author, year, category):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.category = category

    def display(self):
        print("ISBN:", self.isbn)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Category:", self.category)
