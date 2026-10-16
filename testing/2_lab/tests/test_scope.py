import pytest


@pytest.fixture(scope="module")
def initial_list_1():
    return []

@pytest.fixture(scope="module")
def initial_list_2():
    return []

@pytest.fixture(scope="function")
def learn_how_fixture_used_with_scope(initial_list_1):
    initial_list_1.append(1)
    return initial_list_1

@pytest.fixture(scope="function")
def learn_how_fixture_used_with_scope_yield(initial_list_2):
    initial_list_2.append(1)
    yield initial_list_2
    initial_list_2.pop()  # Очистка після тесту, якщо потрібно

def test_learn_how_fixture_used_with_scope_1(
        initial_list_1,
        initial_list_2,
        learn_how_fixture_used_with_scope,
        learn_how_fixture_used_with_scope_yield
        ):
    assert learn_how_fixture_used_with_scope == [1]
    assert learn_how_fixture_used_with_scope_yield == [1]
    assert initial_list_1 == [1]
    assert initial_list_2 == [1]

def test_learn_how_fixture_used_with_scope_2(
        initial_list_1,
        initial_list_2,
        learn_how_fixture_used_with_scope,
        learn_how_fixture_used_with_scope_yield
        ):
    assert initial_list_1 == [1, 1]
    assert learn_how_fixture_used_with_scope == [1, 1]
     
    assert initial_list_2 == [1]
    assert learn_how_fixture_used_with_scope_yield == [1]
    

def test_learn_how_fixture_used_with_scope_3(
        initial_list_1,
        initial_list_2,
        learn_how_fixture_used_with_scope,
        learn_how_fixture_used_with_scope_yield
        ):
    # Завжди накопичується бо кожна фікстура виконується в межах одного модуля
    assert initial_list_1 == [1, 1, 1]
    assert learn_how_fixture_used_with_scope == [1, 1, 1]

    # Але фікстура з yield очищає список після кожного тесту
    assert initial_list_2 == [1]
    assert learn_how_fixture_used_with_scope_yield == [1]

def test_grade_book_object_dict_keys(create_grade_book_object):
    gb_keys = create_grade_book_object._grades.keys()
    assert len(gb_keys) == 2
    assert gb_keys == {"Олена", "Андрій"}

    # ТАК РОБИТИ НЕМОЖНА, але ми можемо додати до фікстури значення
    create_grade_book_object.add_grade("Марія", 88)


def test_grade_book_object_dict_keys_after_modification_in_test(create_grade_book_object):
    gb_keys = create_grade_book_object._grades.keys()
    # тут бачимо наслідки зміни фікстури в попередньому тесті, бо фікстура має scope="session"
    assert len(gb_keys) == 3
    assert gb_keys == {"Олена", "Андрій", "Марія"}

def test_environment_variable_set(set_environment_variable):
    import os
    # на час існування сесії на змінні оточення встановлені, 
    # і ми можемо перевірити їх значення
    assert os.environ.get("TEST_ENV_VAR") == "test_value"
    assert os.environ.get("ANOTHER_ENV_VAR") == "another_value"
