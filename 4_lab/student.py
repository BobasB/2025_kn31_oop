import random
from books import Book, BookStatus

class Student:
    def __init__(self, name):
        self.name = name
        self.ID = id(self)
        self.borrowed_books: list[Book] = []
        self.college_name = "ІТ коледж"
    
    @property
    def student_id_card(self):
        return f"Студент коледжу <<{self.college_name}>>\nІмя: {self.name},\nID: {self.ID}"
    
    def borrow_book(self, book: Book):
        if book.status == BookStatus.AVAILABLE:
            book.status = BookStatus.BORROWED
            book.taken_by = self.name
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.status = BookStatus.AVAILABLE
            self.borrowed_books.remove(book)
            book.taken_by = None
            return True
        return False
    
    def start_reading_book(self, book: Book):
        if book in self.borrowed_books:
            return f"{self.name} починає читати описа книги:\n{book.description}"
        return f"{self.name} не має цієї книги"
    
    def think_before_take_a_book(self, book: Book):
        if random.choice([True, False]):
            print( f"{self.name} розглядає книгу:\n{book.description}" )
            return True
        print( f"{self.name} відмовляється від книги:\n{book.description}" )
        return False
