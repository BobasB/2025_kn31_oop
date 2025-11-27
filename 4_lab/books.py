"""Модуль для роботи з книгами бібліотеки.

Містить класи для представлення книг та їх статусів.
"""

from enum import Enum


class BookStatus(Enum):
    """Перелік можливих статусів книги в бібліотеці."""
    
    AVAILABLE = 'в наявності'
    BORROWED = 'взята'
    RESERVED = 'зарезервована'


class Book:
    """Клас для представлення книги в бібліотеці.
    
    Attributes:
        title (str): Назва книги
        author (str): Автор книги
        year (int): Рік видання
        isbn (str): Міжнародний стандартний книжковий номер
        status (BookStatus): Поточний статус книги
        taken_by (str | None): Ім'я студента, який взяв книгу, або None
    """
    
    def __init__(self, title: str, author: str, year: int, isbn: str) -> None:
        """Ініціалізує новий екземпляр книги.
        
        Args:
            title: Назва книги
            author: Автор книги
            year: Рік видання
            isbn: ISBN код книги
        """
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        # За замовчуванням книга доступна для позики
        self.status = BookStatus.AVAILABLE
        # Спочатку книга нікому не належить
        self.taken_by = None
    
    @property
    def description(self) -> str:
        """Повертає детальний опис книги.
        
        Returns:
            str: Форматований рядок з повною інформацією про книгу
        """
        return f"""
                Назва: {self.title}.
                Автор: {self.author}.
                Видання: ({self.year}) - ISBN: {self.isbn}.
                Статус: {self.status.value}.
                """
    
    @property
    def info(self) -> str:
        """Повертає коротку інформацію про статус книги.
        
        Returns:
            str: Рядок зі статусом книги та інформацією про того, хто її взяв
        """
        return f"Книга '{self.title}' зараз {self.status.value} та {f'взята студентом {self.taken_by}' if self.taken_by else 'доступна для позики'}."
