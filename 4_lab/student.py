"""Модуль для роботи зі студентами бібліотеки.

Містить клас Student для управління діями студентів з книгами.
"""

import random
from books import Book, BookStatus


class Student:
    """Клас для представлення студента, який користується бібліотекою.
    
    Attributes:
        name (str): Ім'я студента
        ID (int): Унікальний ідентифікатор студента
        borrowed_books (list[Book]): Список книг, які зараз у студента
        college_name (str): Назва навчального закладу
        books_taken_history (list[Book]): Історія всіх взятих книг
        book_reading_days (dict[int, int]): Словник днів читання повернутих книг
        book_borrow_dates (dict[int, int]): Словник дат взяття книг
    """
    
    def __init__(self, name: str) -> None:
        """Ініціалізує нового студента.
        
        Args:
            name: Ім'я студента
        """
        self.name = name
        # Використовуємо вбудовану функцію id() для унікального ID
        self.ID = id(self)
        # Список книг, які зараз у студента
        self.borrowed_books: list[Book] = []
        self.college_name = "ІТ коледж"
        # Історія всіх книжок, які студент коли-небудь брав (для статистики)
        self.books_taken_history: list[Book] = []
        # Словник для зберігання кількості днів читання кожної книги
        self.book_reading_days: dict[int, int] = {}
        # Словник для зберігання дати взяття кожної книги
        self.book_borrow_dates: dict[int, int] = {}
    
    @property
    def student_id_card(self) -> str:
        """Повертає інформацію про студентський квиток.
        
        Returns:
            str: Форматований рядок з даними студента
        """
        return f"Студент коледжу <<{self.college_name}>>\nІмя: {self.name},\nID: {self.ID}"

    @property
    def total_books_taken(self) -> int:
        """Повертає загальну кількість книг, взятих студентом за весь час.
        
        Returns:
            int: Кількість книг в історії
        """
        return len(self.books_taken_history)

    @property
    def favorite_books(self) -> list[str]:
        """Визначає найулюбленіші книги студента.
        
        Найулюбленішими вважаються книги, які студент брав найбільше разів.
        
        Returns:
            list[str]: Список назв книг, які студент брав найчастіше
        """
        from collections import Counter
        
        # Підраховуємо кількість разів, коли студент брав кожну книгу
        counter = Counter([book.title for book in self.books_taken_history])
        
        if not counter:
            return []
        
        # Знаходимо максимальну кількість
        max_count = max(counter.values())
        
        # Повертаємо всі книги з максимальною кількістю
        return [title for title, count in counter.items() if count == max_count]

    def get_reading_days(self, book: Book) -> int:
        """Повертає кількість днів, протягом яких студент читав книгу.
        
        Args:
            book: Книга, для якої потрібно отримати кількість днів читання
            
        Returns:
            int: Кількість днів читання або 0, якщо книга не була повернута
        """
        return self.book_reading_days.get(id(book), 0)
    
    def borrow_book(self, book: Book, current_day: int = None) -> bool:
        """Видає книгу студенту.
        
        Змінює статус книги на BORROWED, додає її до списку взятих книг
        та фіксує дату взяття для статистики.
        
        Args:
            book: Книга, яку студент хоче взяти
            current_day: Поточний день симуляції (опціонально)
            
        Returns:
            bool: True, якщо книга успішно видана, False - якщо недоступна
        """
        # Перевіряємо, чи книга доступна для позики
        if book.status == BookStatus.AVAILABLE:
            # Змінюємо статус книги
            book.status = BookStatus.BORROWED
            book.taken_by = self.name
            
            # Додаємо книгу до списку поточних книг студента
            self.borrowed_books.append(book)
            
            # Додаємо книгу до історії для статистики
            self.books_taken_history.append(book)
            
            # Фіксуємо дату взяття книги, якщо день вказано
            if current_day is not None:
                self.book_borrow_dates[id(book)] = current_day
            
            return True
        return False
    
    def return_book(self, book: Book, current_day: int = None) -> bool:
        """Повертає книгу до бібліотеки.
        
        Змінює статус книги на AVAILABLE, видаляє її зі списку взятих книг
        та обчислює кількість днів читання для статистики.
        
        Args:
            book: Книга, яку потрібно повернути
            current_day: Поточний день симуляції (опціонально)
            
        Returns:
            bool: True, якщо книга успішно повернута, False - якщо книги немає у студента
        """
        # Перевіряємо, чи книга дійсно у студента
        if book in self.borrowed_books:
            # Змінюємо статус книги на доступну
            book.status = BookStatus.AVAILABLE
            
            # Видаляємо книгу зі списку поточних книг студента
            self.borrowed_books.remove(book)
            
            # Очищаємо інформацію про власника
            book.taken_by = None
            
            # Обчислюємо та зберігаємо кількість днів читання
            if current_day is not None and id(book) in self.book_borrow_dates:
                days = current_day - self.book_borrow_dates[id(book)]
                self.book_reading_days[id(book)] = days
                # Видаляємо дату взяття, оскільки книга повернута
                del self.book_borrow_dates[id(book)]
            
            return True
        return False
    
    def start_reading_book(self, book: Book) -> str:
        """Починає читання книги.
        
        Args:
            book: Книга, яку студент хоче почати читати
            
        Returns:
            str: Повідомлення про початок читання або відсутність книги
        """
        if book in self.borrowed_books:
            return f"{self.name} починає читати описа книги:\n{book.description}"
        return f"{self.name} не має цієї книги"
    
    def think_before_take_a_book(self, book: Book) -> bool:
        """Імітує процес прийняття рішення студентом щодо взяття книги.
        
        Випадково визначає, чи студент зацікавлений у книзі.
        
        Args:
            book: Книга, яку студент розглядає
            
        Returns:
            bool: True, якщо студент вирішив взяти книгу, False - якщо відмовився
        """
        # Випадково приймаємо рішення (50/50)
        if random.choice([True, False]):
            print(f"{self.name} розглядає книгу:\n{book.description}")
            return True
        print(f"{self.name} відмовляється від книги:\n{book.description}")
        return False
