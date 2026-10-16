import pytest

from lab.main import GradeBook

# Загальний файл для фікстур, які можна використовувати в різних тестових файлах

@pytest.fixture
def grade_book_object_original():
    g = GradeBook()
    return g

# видимість та автовикористання фікстури
@pytest.fixture(scope="session", autouse=True)
def create_grade_book_object():
    obj = GradeBook() 
    for (student, score) in [("Олена", 92), ("Олена", 84), ("Андрій", 67), ("Андрій", 75)]:
        obj.add_grade(student, score)
    return obj

# для глобальних значень найчастіше використовують scope="session", та 
# створюють змінні оточення, які можна використовувати в тестах, наприклад:
@pytest.fixture(scope="session", autouse=True)
def set_environment_variable():
    import os
    for key, value in [("TEST_ENV_VAR", "test_value"), ("ANOTHER_ENV_VAR", "another_value")]:
        os.environ[key] = value
    # нічого повертати не потрібно, бо ми просто встановлюємо змінні оточення, 
    # які будуть доступні в тестах
    return