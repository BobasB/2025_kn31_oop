import pytest
import unittest

from lab.main import validate_score


class TestDefaultUnit(unittest.TestCase):
    @pytest.mark.unit
    @pytest.mark.score_validation
    def test_validate_score_valid(self):
        # Test valid scores
        self.assertIsNone(validate_score(10))


class TestByPyTest:
    @pytest.mark.unit
    @pytest.mark.score_validation
    def test_pytest_compatible_in_class(self):
        # Просто групуємо тести в класі, але не використовуємо unittest.TestCase
        # Тест починається з test_ і буде виконуватися автоматично
        assert validate_score(10) is None, "Expected None for valid score 10"
