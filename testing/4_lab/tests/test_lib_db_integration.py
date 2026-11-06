import pytest
from app.library_with_db import LibraryDatabase
from app.student import Student

@pytest.fixture
def library():
    return LibraryDatabase(db_name="library_test.db")

@pytest.mark.parametrize("students", [
                            ["Дмитро", "Елена"], 
                            # дадавання цих користувачів до бази даних буде впливати на наступний тест, 
                            # тому ми можемо бачити що інтеграційний тест буде провалюватися
                            ["Богдан", "Марія", "Олександр", "Ірина", "Сергій"]
                            ]
                         )
def test_add_student_to_db(library, students):
    for student_name in students:
        student = Student(name=student_name)
        library.add_student_to_db(student)
    
    # Перевіряємо, що студент доданий до бази даних
    students_in_db = library.list_registered_students()
    assert len(students_in_db) == len(students)
    # у другому тесті буде AssertionError: assert 7 == 5
    assert any(s.name == student_name for s in students_in_db)
