from books import Book, BookStatus
from student import Student

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.books_shelf: list[Book] = []
        self.students: list[Student] = []

    @property
    def list_available_books(self):
        """Фільтруємо всі книги, які доступні для позики"""
        return [book for book in self.books_shelf if book.status == BookStatus.AVAILABLE]
    
    @property
    def list_registered_students(self):
        """Повертаємо список зареєстрованих користувачів бібліотеки"""
        return self.students
    
    # створюємо метод для видачі книги студенту
    def lend_book(self, book: Book, student: Student):
        if book in self.books_shelf:
            book.status = BookStatus.BORROWED
            self.books_shelf.remove(book)
            student.borrowed_books.append(book)
            book.taken_by = student.name
            if student.borrow_book(book):
                print(f"Книга '{book.title}' успішно видана користувачу {student.name}.")
            return True
        elif book in self.books:
            for student in self.students:
                if book in student.borrowed_books:
                    print(f"Книга '{book.title}' недоступна для читання, її взяв студент {book.taken_by}.")
                    return False
        else:
            print(f"Такої книги в бібліотеці немає: '{book.title}'.")
            return False

            
                    
    