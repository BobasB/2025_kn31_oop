from operator import add
import unittest
from cov.main import function_1, empty_function
from cov.main3 import function_3


class TestMain(unittest.TestCase):
    def test_function_1(self):
        # Тест для function_1
        for i in [True, True, True, False, False, False]:
            with self.subTest(i=i):
                result = function_1(i)
                self.assertTrue("значення" in result)       
                self.assertIsInstance(result, str)
                #self.assertTrue(result.startswith("Значення при випадковому виборі:"))
                self.assertTrue("значення" in result)

    def test_function_3(self):
        # Тест для function_3
        result = function_3()
        self.assertEqual(result, "Function 3 executed successfully")

    def test_empty_function(self):
        n = empty_function()
        self.assertIsNone(n)  # Перевірка, що функція повертає None, оскільки вона порожня і не має return


if __name__ == '__main__':
    unittest.main()
