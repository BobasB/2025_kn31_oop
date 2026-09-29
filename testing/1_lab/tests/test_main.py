import unittest

from lab1.main import celsius_to_fahrenheit, main, SimpleClass


def test():
    if main() == 0:
        print("Test passed")
    else:
        print("Test failed")

    if main(1) == 0:
        print("Test passed")
    else:
        print("Test failed")

    if isinstance(main(1), int):
        print("Test passed")
    else:
        print("Test failed")
        raise AssertionError("Викликаємо помилку спеціально для перевірки роботи assert")


def test_via_assert():
    assert main() == 0, "Assert / твердження є неправдиве, тест не пройшов функція має повернути 0"
    #assert False, "Спеціально створена помилка для перевірки роботи assert"
    # assert не вважається тестом, а лише перевіркою умови, тест складається з безлічі assert
    for i in [int(0), int(100)]:
        assert main(i) == 0, "Assert / твердження є неправдиве, тест не пройшов, функція ма єповернути 0"
        assert isinstance(main(i), int), "Assert / твердження є неправдиве, тест не пройшов"


def test_main():
    print(f"{20*'#'} Починаємо тестування... {20*'#'}")
    #test()
    test_via_assert() 
    print(f"{20*'#'} Тестування завершено. {20*'#'}") 


class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit_with_assets(self) -> None:
        """Пробуємо через assert"""
        assert celsius_to_fahrenheit(0.0) == 32.0, f"Expected 32!"
        assert celsius_to_fahrenheit(100.0) == 212.0, f"Expected 212!"
        assert celsius_to_fahrenheit(-40.0) == -40.0, f"Expected -40!"
        assert isinstance(celsius_to_fahrenheit(36.6), float), f"Expected float!"
        assert abs(celsius_to_fahrenheit(36.6) - 97.88) < 1e-2, f"Expected 97.88!"

    def test_celsius_to_fahrenheit_with_unittest_assets(self) -> None:
        """Пробуємо через unittest assert"""
        self.assertEqual(celsius_to_fahrenheit(0.0), 32.0, f"Expected 32!")
        self.assertEqual(celsius_to_fahrenheit(100.0), 212.0, f"Expected 212!")
        self.assertEqual(celsius_to_fahrenheit(-40.0), -40.0, f"Expected -40!")
        self.assertIsInstance(celsius_to_fahrenheit(36.6), float, f"Expected float!")
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, msg="Expected 97.88!")

    def test_celsius_to_fahrenheit_with_input_data(self) -> None:
        cases = [
            (0, 32),
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (36.6, 97.88),
        ]
        for c, fr in cases:
            self.assertAlmostEqual(
                celsius_to_fahrenheit(c), fr, msg=f"Expected {fr} for input {c}"
            )

    def test_celsius_to_fahrenheit_with_subtests(self) -> None:
        cases = [
                    (0, 32),
                    (0.0, 32.0),
                    (100.0, 212.0),
                    (-40.0, -40.0),
                    (36.6, 97.88),
                ]
        for c, fr in cases:
            with self.subTest(celsius=c):
                self.assertAlmostEqual(
                    celsius_to_fahrenheit(c), fr, msg=f"Expected {fr} for input {c}"
                )


class TestSimpleClass(unittest.TestCase):
    def setUp(self) -> None:
        """Цей метод викликається перед кожним тестом"""
        print(f"{20*'#'} Починаємо тестування SimpleClass... {20*'#'}")
        self.obj = SimpleClass(5)

    def tearDown(self) -> None:
        """Цей метод викликається після кожного тесту"""
        print(f"{20*'#'} Тестування SimpleClass завершено. {20*'#'}")
        del self.obj  # Видаляємо об'єкт після тесту

    # Наступного разу setUpClass і tearDownClass
    # Ідемпотентність — це властивість операції або функції, за якої її багаторазове повторення 
    # дає той самий кінцевий результат і стан системи, що й одноразове

    @classmethod
    def setUpClass(cls) -> None:
        """Цей метод викликається один раз перед усіма тестами класу"""
        print(f"{20*'#'} Починаємо тестування SimpleClass... {20*'#'}")
        cls.immutable_global_variable = 42  # Приклад ідемпотентної операції, яка виконується один раз
        # найчастіше перехід через 0 або дані різного поряду величини, наприклад: -10, 0, 20, 10000
        cls.tuple_variable = (0, 20, 10000)  # Приклад ідемпотентної операції, яка виконується один раз
        cls.negative_tuple_variable = (-10, -1, 0, -100, -1000)  # Приклад ідемпотентної операції, яка виконується один раз

    @classmethod
    def tearDownClass(cls) -> None:
        """Цей метод викликається один раз після усіх тестів класу"""
        print(f"{20*'#'} Тестування SimpleClass завершено. {20*'#'}")
        del cls.tuple_variable  # Видаляємо кортеж після тестів
        del cls.immutable_global_variable  # Видаляємо змінну після тестів
    
    def test_increment(self) -> None:
        """Пробуємо через unittest чи відпрацьовує метод increment"""
        self.obj.increment()
        self.assertEqual(self.obj.get_value(), 6)

    def test_get_value(self) -> None:
        """Пробуємо через unittest чи відпрацьовує метод get_value"""
        self.assertEqual(self.obj.get_value(), 5)
        self.assertIsInstance(self.obj.get_value(), int, f"Expected int!")
        assert isinstance(self.obj.get_value(), int), f"Expected int!"

    def test_also_allowed(self) -> None:
        """Можна створювати обєкт тут без setUp, але це не рекомендується"""
        obj = SimpleClass(self.immutable_global_variable)
        self.assertEqual(obj.get_value(), self.immutable_global_variable)
        self.assertIsInstance(obj.get_value(), int, f"Expected int!")
        del obj  # Видаляємо об'єкт після тесту

    #def test_obj_with_tuple(self) -> None:
    #    """Тестуємо функцію return_from_input з використанням кортежу"""
    #    for v in self.tuple_variable: # набір тестових даних
    #        # Ми не тестуємо який алговритим всередині функції, 
    #        # а тестуємо що вона повертає те що їй передали
    #        self.assertEqual(self.obj.return_from_input(v), v)

    def test_obj_with_tuple_subtest(self) -> None:
        """Тестуємо функцію return_from_input з використанням кортежу та підтестів"""
        for v in self.tuple_variable: # набір тестових даних      
            with self.subTest(value=v):
                self.assertEqual(self.obj.return_from_input(v), v)
                self.assertIsInstance(self.obj.return_from_input(v), int, f"Expected int!")

    def test_obj_with_negative_tuple_subtest(self) -> None:
        """Тестуємо функцію return_error_if_less_then_zero з використанням кортежу та підтестів"""
        for v in self.negative_tuple_variable: # набір тестових даних      
            with self.subTest(value=v):
                with self.assertRaises((ValueError, TypeError)):
                    self.obj.return_error_if_less_then_zero(v)


if __name__ == "__main__":
    #test_main()
    unittest.main(verbosity=2)  # Запуск тестів з детальним виводом