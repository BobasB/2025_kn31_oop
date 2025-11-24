import random
from books import Book, BookStatus

class Student:
    def __init__(self, name):
        self.name = name
        self.ID = id(self)
        self.borrowed_books: list[Book] = []
        self.college_name = "ІТ коледж"
        self.books_taken_history: list[Book] = []  # всі книжки, які студент коли-небудь брав
        self.book_reading_days: dict[int, int] = {}  # book.id -> days
        self.book_borrow_dates: dict[int, int] = {}  # book.id -> день, коли взяв
    
    @property
    def student_id_card(self):
        return f"Студент коледжу <<{self.college_name}>>\nІмя: {self.name},\nID: {self.ID}"

    @property
    def total_books_taken(self):
        return len(self.books_taken_history)

    @property
    def favorite_books(self):
        from collections import Counter
        counter = Counter([book.title for book in self.books_taken_history])
        if not counter:
            return []
        max_count = max(counter.values())
        return [title for title, count in counter.items() if count == max_count]

    def get_reading_days(self, book: Book):
        return self.book_reading_days.get(id(book), 0)
    
    def borrow_book(self, book: Book, current_day: int = None):
        if book.status == BookStatus.AVAILABLE:
            book.status = BookStatus.BORROWED
            book.taken_by = self.name
            self.borrowed_books.append(book)
            self.books_taken_history.append(book)
            if current_day is not None:
                self.book_borrow_dates[id(book)] = current_day
            return True
        return False
    
    def return_book(self, book: Book, current_day: int = None):
        if book in self.borrowed_books:
            book.status = BookStatus.AVAILABLE
            self.borrowed_books.remove(book)
            book.taken_by = None
            if current_day is not None and id(book) in self.book_borrow_dates:
                days = current_day - self.book_borrow_dates[id(book)]
                self.book_reading_days[id(book)] = days
                del self.book_borrow_dates[id(book)]
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
