import pytest

from lab.main import GradeBook

@pytest.fixture
def grade_book_object_original():
    g = GradeBook()
    return g
