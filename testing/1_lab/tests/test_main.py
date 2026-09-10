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


if __name__ == "__main__":
    test()
