"""
Question: 11 {Class Methods}
Assignment:
Create a class Book with a class variable total_books. Add a class method
increment_book_count() to increase the count when a new book is added.
"""

class Book:
    total_books = 0

    @classmethod
    def increament_book_count(cls):
        cls.total_books += 1

Book.increament_book_count()
Book.increament_book_count()
b3 = Book()
b3.increament_book_count()
print(Book.total_books)
