from books import Book, BookStatus
from student import Student

class Library:
    def __init__(self):
        self.books_shelf: list[Book] = []
        self.users: list[Student] = []

    @property
    def list_available_books(self):
        """Фільтруємо всі книги, які доступні для позики"""
        return [book for book in self.books_shelf if book.status == BookStatus.AVAILABLE]
    