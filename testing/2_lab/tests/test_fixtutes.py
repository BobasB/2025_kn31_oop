import pytest
from lab.main import GradeBook


def test_grade_book_add_and_average():
    grade_book = GradeBook()
    grade_book.add_grade("Олена", 92)
    grade_book.add_grade("Олена", 84)
    grade_book.add_grade("Андрій", 67)

    assert grade_book.get_average("Олена") == pytest.approx(88.0)

def no_fixtures(): # аналогія методу setUp у unittest, створюємо об'єкт GradeBook без використання фікстур
    grade_book = GradeBook()
    grade_book.add_grade("Олена", 92)
    grade_book.add_grade("Олена", 84)
    grade_book.add_grade("Андрій", 67)
    return grade_book

def test_get_average_with_no_fixture():
    grade_book = no_fixtures() # викликати функцію щоб вона повернула об'єкт GradeBook
    assert grade_book.get_average("Олена") == pytest.approx(88.0)

## Це правильний код з кивористанням фікстур у pytest. 
# Фікстура створює об'єкт GradeBook, який можна використовувати у тестах.
@pytest.fixture
def grade_book_object():
    g = GradeBook()
    g.add_grade("Олена", 92)
    g.add_grade("Олена", 84)
    g.add_grade("Андрій", 67)
    return g

def test_add_grade_and_get_average(grade_book_object):
    assert grade_book_object.get_average("Олена") == pytest.approx(88.0)


@pytest.fixture
def grade_book_object_with_grades(grade_book_object_original):
    grade_book = grade_book_object_original #копіюємо щоб не модифікувати оригінальний об'єкт
    # і модифікуємо його, додаючи оцінки
    grade_book.add_grade("Олена", 92)
    grade_book.add_grade("Олена", 84)
    grade_book.add_grade("Андрій", 67)
    return grade_book


def test_object_with_grades_has_same_class(grade_book_object_original, grade_book_object_with_grades):
    """Перевіряємо чи модифікація об'єкта не змінила його клас"""
    assert isinstance(grade_book_object_with_grades, type(grade_book_object_original))


# при використанні pytest, точки входу немає
#if __name__ == "__main__":
#    test_grade_book_add_and_average()
#    test_get_average_with_no_fixture()
#    test_add_grade_and_get_average()
