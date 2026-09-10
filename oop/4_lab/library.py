"""Модуль для управління бібліотекою.

Містить клас Library для управління книгами та студентами.
"""

from books import Book, BookStatus
from student import Student


class Library:
    """Клас для представлення бібліотеки.
    
    Attributes:
        books (list[Book]): Повний список всіх книг бібліотеки
        books_shelf (list[Book]): Список книг, які зараз на полиці (доступні)
        students (list[Student]): Список зареєстрованих студентів
    """
    
    def __init__(self) -> None:
        """Ініціалізує нову бібліотеку з порожніми списками."""
        # Повний каталог всіх книг бібліотеки
        self.books: list[Book] = []
        # Книги, які зараз доступні на полиці
        self.books_shelf: list[Book] = []
        # Зареєстровані студенти
        self.students: list[Student] = []

    @property
    def list_available_books(self) -> list[Book]:
        """Повертає список всіх книг, доступних для позики.
        
        Returns:
            list[Book]: Список книг зі статусом AVAILABLE
        """
        # Фільтруємо книги на полиці за статусом "доступна"
        return [book for book in self.books_shelf if book.status == BookStatus.AVAILABLE]
    
    @property
    def list_registered_students(self) -> list[Student]:
        """Повертає список всіх зареєстрованих студентів бібліотеки.
        
        Returns:
            list[Student]: Список зареєстрованих студентів
        """
        return self.students
    
    def lend_book(self, book: Book, student: Student, current_day: int) -> bool:
        """Видає книгу студенту.
        
        Перевіряє наявність книги на полиці, видаляє її з полиці
        та передає студенту.
        
        Args:
            book: Книга для видачі
            student: Студент, який бере книгу
            current_day: Поточний день симуляції
            
        Returns:
            bool: True, якщо книга успішно видана, False - якщо недоступна
        """
        # Перевіряємо, чи книга на полиці (доступна)
        if book in self.books_shelf:
            # Видаляємо книгу з полиці
            self.books_shelf.remove(book)
            
            # Передаємо книгу студенту з фіксацією дати
            if student.borrow_book(book, current_day=current_day):
                print(f"Книга '{book.title}' успішно видана користувачу {student.name}.")
            return True
        
        # Перевіряємо, чи книга є в каталозі, але зайнята
        elif book in self.books:
            # Шукаємо, у кого книга
            for registered_student in self.students:
                if book in registered_student.borrowed_books:
                    print(f"Книга '{book.title}' недоступна для читання, її взяв студент {book.taken_by}.")
                    return False
        else:
            # Книги немає в бібліотеці взагалі
            print(f"Такої книги в бібліотеці немає: '{book.title}'.")
            return False
        
    def return_book(self, book: Book, student: Student, current_day: int) -> bool:
        """Приймає книгу від студента назад до бібліотеки.
        
        Перевіряє, чи книга у студента, забирає її та повертає на полицю.
        
        Args:
            book: Книга для повернення
            student: Студент, який повертає книгу
            current_day: Поточний день симуляції
            
        Returns:
            bool: True, якщо книга успішно повернута, False - якщо книги немає у студента
        """
        # Перевіряємо, чи книга дійсно у студента
        if book in student.borrowed_books:
            print(f"Книга '{book.title}' успішно повернена до бібліотеки {student.name}.")
            
            # Студент повертає книгу з фіксацією днів читання
            if student.return_book(book, current_day=current_day):
                # Повертаємо книгу на полицю
                self.books_shelf.append(book)
                return True
        
        # Книги немає у студента
        print(f"Книга '{book.title}' не знаходиться у користувача {student.name}.")
        return False

            
                    
    