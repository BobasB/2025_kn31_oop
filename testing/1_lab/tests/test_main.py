from lab1.main import main


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

if __name__ == "__main__":
    test_main()