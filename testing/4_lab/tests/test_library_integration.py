"""Інтеграційні тести класу Library разом з реальними Book і Student."""

import pytest

from books import Book, BookStatus
from library import Library
from student import Student

# задаємо фікстури для книжок, бібліотеки та студентів, щоб використовувати їх у тестах
@pytest.fixture
def book():
    return Book("Кобзар", "Т. Шевченко", 1840, "111")


@pytest.fixture
def other_book():
    return Book("Лісова пісня", "Леся Українка", 1911, "222")


@pytest.fixture
def library(book, other_book):
    lib = Library()
    lib.books = [book, other_book]
    lib.books_shelf = [book, other_book]
    yield lib
    lib.books.clear()
    lib.books_shelf.clear()
    lib.students.clear()


DEFAULT_NAMES = ["Аліса", "Боб"]


@pytest.fixture
def students(request, library):
    """Створює й реєструє студентів; імена беруться з request.param (indirect)."""
    # names потрбіний що отримати імя з параметрів
    names = getattr(request, "param", DEFAULT_NAMES)
    created = [Student(name) for name in names]
    library.students.extend(created)
    return created


@pytest.fixture
def alice(students):
    return students[0]


@pytest.fixture
def bob(students):
    return students[1]

# Це перший інтеграційний тест, який перевіряє, що всі студенти, 
# створені через фікстуру students, дійсно зареєстровані в бібліотеці.
# Тобто взаємодія між Library і Student працює коректно, 
# і бібліотека правильнь опрацьовує інформацію про студентів (поля name).
@pytest.mark.parametrize(
    "students", # ми параметризуємо фікстуру students, щоб перевірити різні набори студентів
    [
        ["Аліса"], 
        ["Аліса", "Боб", "Кейт"], 
        ["А", "Б", "Rodger", "1"],
        [1, 2, 3]
    ],
    indirect=True,
)
def test_all_students_are_registered(library, students):
    assert library.list_registered_students == students
    for student in library.list_registered_students:
        assert student.name is not None, "Студент повинен мати ім'я" 
# 5 Листопада 2026 року дійшли до цього тесту

@pytest.mark.parametrize("students", [["Аліса", "Боб", "Кейт"]], indirect=True)
def test_only_one_of_many_students_can_hold_book(library, book, students):
    results = [library.lend_book(book, s, current_day=1) for s in students]

    assert results == [True, False, False]
    assert book.taken_by == "Аліса"


def test_new_library_is_empty():
    lib = Library()
    assert lib.books == []
    assert lib.list_available_books == []
    assert lib.list_registered_students == []


def test_list_registered_students(library, alice, bob):
    assert library.list_registered_students == [alice, bob]


def test_lend_book_updates_library_student_and_book(library, book, alice):
    assert library.lend_book(book, alice, current_day=1) is True

    assert book not in library.books_shelf
    assert book in library.books
    assert book in alice.borrowed_books
    assert book in alice.books_taken_history
    assert book.status == BookStatus.BORROWED
    assert book.taken_by == "Аліса"
    assert alice.book_borrow_dates[id(book)] == 1


def test_lent_book_is_not_in_available_list(library, book, other_book, alice):
    library.lend_book(book, alice, current_day=1)
    assert library.list_available_books == [other_book]


def test_lend_already_borrowed_book_to_another_student_fails(library, book, alice, bob):
    library.lend_book(book, alice, current_day=1)

    assert library.lend_book(book, bob, current_day=2) is False
    assert book.taken_by == "Аліса"
    assert book not in bob.borrowed_books


def test_lend_unknown_book_fails(library, alice):
    stranger = Book("Невідома", "Автор", 2000, "999")

    assert library.lend_book(stranger, alice, current_day=1) is False
    assert alice.borrowed_books == []


def test_return_book_restores_state(library, book, alice):
    library.lend_book(book, alice, current_day=1)

    assert library.return_book(book, alice, current_day=6) is True

    assert book in library.books_shelf
    assert book not in alice.borrowed_books
    assert book.status == BookStatus.AVAILABLE
    assert book.taken_by is None
    assert alice.get_reading_days(book) == 5
    assert book in library.list_available_books


def test_return_book_not_held_by_student_fails(library, book, alice, bob):
    library.lend_book(book, alice, current_day=1)

    assert library.return_book(book, bob, current_day=2) is False
    assert book in alice.borrowed_books
    assert book not in library.books_shelf


def test_book_can_be_lent_again_after_return(library, book, alice, bob):
    library.lend_book(book, alice, current_day=1)
    library.return_book(book, alice, current_day=3)

    assert library.lend_book(book, bob, current_day=4) is True
    assert book.taken_by == "Боб"
    assert library.books_shelf.count(book) == 0


def test_repeated_borrowing_is_tracked_in_student_history(library, book, alice):
    for day in (1, 10):
        library.lend_book(book, alice, current_day=day)
        library.return_book(book, alice, current_day=day + 2)

    assert alice.total_books_taken == 2
    assert alice.favorite_books == ["Кобзар"]


def test_lend_book_messages(library, book, alice, bob, capsys):
    library.lend_book(book, alice, current_day=1)
    library.lend_book(book, bob, current_day=2)

    out = capsys.readouterr().out
    assert "успішно видана користувачу Аліса" in out
    assert "недоступна для читання" in out


@pytest.mark.xfail(
    reason="lend_book повертає None, якщо книга зайнята студентом, якого немає в library.students",
    strict=True,
)
def test_lend_book_borrowed_by_unregistered_student_returns_false(library, book):
    outsider = Student("Сторонній")
    library.books_shelf.remove(book)
    outsider.borrow_book(book, current_day=1)

    assert library.lend_book(book, Student("Інший"), current_day=2) is False
