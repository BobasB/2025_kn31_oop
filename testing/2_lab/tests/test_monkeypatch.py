import pytest
import lab.main as main

def test_letter_grade_correct():
    assert main.letter_grade(90) == "A"
    assert main.letter_grade(80) == "B"
    assert main.letter_grade(70) == "C"
    assert main.letter_grade(60) == "D"
    assert main.letter_grade(50) == "F"

def test_letter_grade_with_mock(monkeypatch):
    # Це може бути фікстурою
    def mock_letter_grade(score):
        if 0 < score < 100:
            return "Valid score"
        return "Invalid score"

    # Patch the letter_grade function in the lab.main module
    monkeypatch.setattr(main, "letter_grade", mock_letter_grade)

    # Now we can call letter_grade without triggering validation
    assert main.letter_grade(80) == "Valid score"
    assert main.letter_grade(0) == "Invalid score"
    assert main.letter_grade(100) == "Invalid score"

@pytest.fixture
def mock_letter_grade(monkeypatch):
    def mock_letter_grade(score):
        if 0 < score < 100:
            return "Valid score"
        return "Invalid score"

    # Patch the letter_grade function in the lab.main module
    monkeypatch.setattr(main, "letter_grade", mock_letter_grade)
    return mock_letter_grade

def test_letter_grade_with_fixture(mock_letter_grade):
    # тут вже перевіряється запатчена функція letter_grade
    assert main.letter_grade(80) == "Valid score"
    assert main.letter_grade(0) == "Invalid score"
    assert main.letter_grade(100) == "Invalid score"
