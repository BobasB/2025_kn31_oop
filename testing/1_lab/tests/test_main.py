import unittest

from lab1.main import celsius_to_fahrenheit, main


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


if __name__ == "__main__":
    #test_main()
    unittest.main()