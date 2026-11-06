"""Модуль для роботи зі статистикою бібліотеки.

Містить клас Statistics для аналізу та виведення статистики
використання бібліотеки студентами.
"""

from .library import Library
from .student import Student


class Statistics:
    """Клас для збору та виведення статистики роботи бібліотеки.
    
    Attributes:
        library (Library): Екземпляр бібліотеки для аналізу
        simulation_days (int): Кількість днів симуляції
    """
    
    def __init__(self, library: Library, simulation_days: int = 90) -> None:
        """Ініціалізує об'єкт статистики.
        
        Args:
            library: Екземпляр бібліотеки для аналізу
            simulation_days: Кількість днів симуляції (за замовчуванням 90)
        """
        self.library = library
        self.simulation_days = simulation_days
    
    def print_student_statistics(self, student: Student) -> None:
        """Виводить детальну статистику для одного студента.
        
        Args:
            student: Студент, для якого потрібно вивести статистику
        """
        print(f"\n{'─'*70}")
        print(f"Студент: {student.name}")
        print(f"{'─'*70}")
        
        # Поточні книги у студента
        print(f"  Зараз має {len(student.borrowed_books)} книг(и):")
        if student.borrowed_books:
            for book in student.borrowed_books:
                print(f"    • {book.title}")
        else:
            print("    (немає книг)")
        
        # Загальна статистика
        print(f"\n  📊 Статистика за період:")
        print(f"    Всього книжок взято: {student.total_books_taken}")
        
        # Найулюбленіші книжки
        fav_books = student.favorite_books
        if fav_books:
            print(f"    Найулюбленіші книжки: {', '.join(fav_books)}")
        else:
            print("    Найулюбленіші книжки: немає даних")
        
        # Дні читання повернутих книг
        if student.book_reading_days:
            print("\n  📖 Дні читання повернутих книжок:")
            for book in student.books_taken_history:
                days = student.get_reading_days(book)
                if days > 0:
                    print(f"    • '{book.title}': {days} днів")
        else:
            print("\n  📖 Студент ще не повертав книжки")
    
    def print_library_statistics(self) -> None:
        """Виводить загальну статистику бібліотеки."""
        print(f"\n{'='*70}")
        print(f"СТАТИСТИКА БІБЛІОТЕКИ")
        print(f"{'='*70}")
        print(f"Всього книг у каталозі: {len(self.library.books)}")
        print(f"Доступних книг на полиці: {len(self.library.list_available_books)}")
        
        books_with_students = len(self.library.books) - len(self.library.list_available_books)
        print(f"Книг у студентів: {books_with_students}")
        
        print(f"\nДоступні книги:")
        if self.library.list_available_books:
            for available_book in self.library.list_available_books:
                print(f"  • {available_book.title}")
        else:
            print("  (всі книги зараз у студентів)")
        print("="*70)
    
    def print_full_statistics(self) -> None:
        """Виводить повну статистику: заголовок, статистику по студентам та бібліотеці."""
        # Заголовок
        print("\n" + "="*70)
        print(f"ПІДСУМКОВА СТАТИСТИКА ПІСЛЯ {self.simulation_days} ДНІВ РОБОТИ БІБЛІОТЕКИ")
        print("="*70)
        
        # Статистика по кожному студенту
        for student in self.library.students:
            self.print_student_statistics(student)
        
        # Загальна статистика бібліотеки
        self.print_library_statistics()
    
    def get_total_books_borrowed(self) -> int:
        """Повертає загальну кількість книг, взятих всіма студентами.
        
        Returns:
            int: Загальна кількість взятих книг
        """
        return sum(student.total_books_taken for student in self.library.students)
    
    def get_most_active_student(self) -> Student | None:
        """Визначає найактивнішого студента (який взяв найбільше книг).
        
        Returns:
            Student | None: Найактивніший студент або None, якщо студентів немає
        """
        if not self.library.students:
            return None
        return max(self.library.students, key=lambda s: s.total_books_taken)
    
    def get_most_popular_books(self) -> list[str]:
        """Визначає найпопулярніші книги серед усіх студентів.
        
        Returns:
            list[str]: Список назв найпопулярніших книг
        """
        from collections import Counter
        
        all_books = []
        for student in self.library.students:
            all_books.extend([book.title for book in student.books_taken_history])
        
        if not all_books:
            return []
        
        counter = Counter(all_books)
        max_count = max(counter.values())
        return [title for title, count in counter.items() if count == max_count]
    
    def print_extended_statistics(self) -> None:
        """Виводить розширену статистику з додатковими метриками."""
        self.print_full_statistics()
        
        # Додаткова аналітика
        print(f"\n{'='*70}")
        print("ДОДАТКОВА АНАЛІТИКА")
        print(f"{'='*70}")
        
        total_borrowed = self.get_total_books_borrowed()
        print(f"Загальна кількість книг, взятих за період: {total_borrowed}")
        
        most_active = self.get_most_active_student()
        if most_active:
            print(f"Найактивніший читач: {most_active.name} ({most_active.total_books_taken} книг)")
        
        popular_books = self.get_most_popular_books()
        if popular_books:
            print(f"Найпопулярніші книги: {', '.join(popular_books)}")
        
        # Середня кількість книг на студента
        if self.library.students:
            avg_books = total_borrowed / len(self.library.students)
            print(f"Середня кількість книг на студента: {avg_books:.2f}")
        
        print("="*70)