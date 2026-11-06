"""Перевірка імпортів усіх модулів пакета."""

from app import __main__, library, stats, student
from app.books import Book, BookStatus
from app.library import Library
from app.student import Student


def test_modules_share_package_classes():
    assert __main__.Book is Book
    assert __main__.Library is Library
    assert __main__.Student is Student
    assert __main__.Statistics is stats.Statistics
    assert stats.Library is Library
    assert stats.Student is Student
    assert library.BookStatus is BookStatus
    assert student.BookStatus is BookStatus
