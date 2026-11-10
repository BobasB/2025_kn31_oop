import pytest
from app.library_with_db import LibraryDatabase
from app.student import Student

# Тестування інтеграції з базою даних SQLite
# База створюється у тимчасовій директорії, щоб уникнути впливу 
# перезаписування у базу
@pytest.fixture(scope="function")
def library(tmp_path):
    return LibraryDatabase(db_name=f"{tmp_path}/library_test.db")

@pytest.mark.parametrize("students", [
                            ["Дмитро", "Елена"], 
                            # дадавання цих користувачів до бази даних буде впливати на наступний тест, 
                            # тому ми можемо бачити що інтеграційний тест буде провалюватися
                            # Це виправлено через тимчасовий шлях до бази даних, який створюється у кожному тесті окремо
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


# Дизайн інтеграційного тесту:
# 1. Запишемо декілька користувачів у базу даних (через фікстуру)
# 2. Додамо одного користувача до бази даних
# 3. Перевіримо, що користувач доданий до бази даних
# 4. Видалимо користувача з бази даних
# 5. Перевіримо, що користувач видалений з бази
# 6. Перевіряємо що студента з ID який ми додавали у базі немає
#маємо декілька кроків і їх результат валідується після кожного кроку, 
# щоб переконатися, що функції роботи з базою даних працюють правильно
@pytest.fixture
def database_with_students(library):
    students = ["Дмитро", "Елена", "Богдан", "Марія", "Олександр"]
    for student_name in students:
        student = Student(name=student_name)
        library.add_student_to_db(student)
    return library, students

def test_add_and_delete_student(database_with_students):
    """"
    Суть інтеграційного тесту якраз відтестувати набір кроків та процедур 
    які відбуваються у бібліотеці з базою даних
    Тому ми прописали довгий ланцюжок дій, 
    які відбуваються у бібліотеці з базою даних
    """
    # Перевіряємо що база даних містить студентів
    # 1. це буде перший крок нашого інтеграційного тесту
    library, students = database_with_students
    number_of_students = len(students)
    students_in_db = library.list_registered_students()
    assert len(students_in_db) == number_of_students

    # 2. Додаємо нового студента до бази даних
    new_student = Student(name="Ірина")
    library.add_student_to_db(new_student)
    students_in_db = library.list_registered_students()
    assert len(students_in_db) == number_of_students + 1
    # 2.1 ID нового студента є у база даних
    student_in_db = library.get_student_by_id(new_student.ID)
    assert student_in_db is not None
    assert student_in_db.name == new_student.name
    assert student_in_db.ID == new_student.ID
    assert isinstance(student_in_db, Student)

    # 3. Видаляємо студента з бази даних
    library.delete_student_from_db(new_student)
    students_in_db = library.list_registered_students()
    assert len(students_in_db) == number_of_students

    # 4. Перевіряємо що студента з ID який ми додавали у базі немає
    student_in_db = library.get_student_by_id(new_student.ID)
    assert student_in_db is None
