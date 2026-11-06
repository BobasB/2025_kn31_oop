import sqlite3
from .student import Student

class LibraryDatabase:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_student_to_db(self, student: Student) -> None:
        """Додає студента до бази даних SQLite.
        
        Args:
            student: Студент для додавання
        """
        self.cursor.execute("INSERT INTO students (id, name) VALUES (?, ?)", (student.ID, student.name))
        self.connection.commit()
    
    def delete_student_from_db(self, student: Student) -> None:
        """Видаляє студента з бази даних SQLite.
        
        Args:
            student: Студент для видалення
        """
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student.ID,))
        self.connection.commit()

    def list_registered_students(self) -> list[Student]:
        """Повертає список всіх зареєстрованих студентів бібліотеки.
        
        Returns:
            list[Student]: Список зареєстрованих студентів
        """
        self.cursor.execute("SELECT id, name FROM students")
        rows = self.cursor.fetchall()
        return [Student(name=row[1]) for row in rows]
