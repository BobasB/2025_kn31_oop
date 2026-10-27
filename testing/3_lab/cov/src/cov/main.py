import random

def empty_function():
    # Порожня функція, яка нічого не робить
    pass

def combine_strings(str1: str, str2: str) -> str:
    # Функція для об'єднання двох рядків
    return str1 + str2

def get_number_type():
    # Функція для визначення типу числа
    a = random.randint(1, 100)
    if a % 2 == 0:
        return combine_strings("Парне значення: ", str(a))
    return combine_strings("Непарне значення: ", str(a))

def function_1(my_choice: bool) -> str:
    # Новий функціонал для function_1
    if my_choice:
        # Тут може бути багато логіки, яка виконується при випадковому виборі
        return get_number_type()
    # тут вже ніша логіка 
    b = random.choice(["успішно", "неуспішно"])
    return f"Дефолтне значення: {b}"
