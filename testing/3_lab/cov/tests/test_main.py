import unittest
from cov.main import function_1
from cov.main3 import function_3


class TestMain(unittest.TestCase):
    def test_function_1(self):
        # Тест для function_1
        result = function_1()
        self.assertEqual(result, "Function 1 executed successfully")

    def test_function_3(self):
        # Тест для function_3
        result = function_3()
        self.assertEqual(result, "Function 3 executed successfully")


if __name__ == '__main__':
    unittest.main()
