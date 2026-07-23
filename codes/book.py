

class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    def show(self):
        print("====================")
        print ("book name: ", self.title)
        print ("Author: ", self.author)
        print ("Publication Year: ", self.year)
        print ("Loan Status: ", self.status)
        print("====================")

book1 = Book("clean code", "Robert Martin", 2008, "Available")
book2 = Book("Python Crash Course", "Eric Matthes", 2019, "Available")

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def show_books (self):
        for book in self.books:
            book.show()
library = Library()

library.add_book(book1)
library.add_book(book2)

library.show_books()

