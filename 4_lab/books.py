from enum import Enum

class BookStatus(Enum):
    AVAILABLE = 'в наявності'
    BORROWED = 'взята'
    RESERVED = 'зарезервована'

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.status = BookStatus.AVAILABLE
        self.taken_by = None
    
    @property
    def description(self):
        return f"""
                Назва: {self.title}.
                Автор: {self.author}.
                Видання: ({self.year}) - ISBN: {self.isbn}.
                Статус: {self.status.value}.
                """
    
    @property
    def info(self):
        return f"Книга '{self.title}' зараз {self.status.value} та {f'взята студентом {self.taken_by}' if self.taken_by else 'доступна для позики'}."
