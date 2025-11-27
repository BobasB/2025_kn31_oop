"""Головний модуль для симуляції роботи бібліотеки ІТ коледжу.

Симулює процес видачі та повернення книг студентами протягом 90 днів.
Виводить статистику використання бібліотеки кожним студентом.
"""

import random
from library import Library
from books import Book
from student import Student


if __name__ == "__main__":
    # Створюємо екземпляр бібліотеки
    ITCollegeLibrary = Library()
    
    # Визначаємо колекції книг різних жанрів
    historian_books = ["Історія України", "Історія світу", "Історія мистецтв"]
    fantastic_books = [
        "Філософський камінь", "Таємна кімната", "В'язень Азкабану",
        "Кубок вогню", "Орден Фенікса", "Напівкровний принц", "Смертельні реліквії"
    ]
    programming_books = [
        "Вступ до Python", "Алгоритми та структури даних",
        "Об'єктно-орієнтоване програмування", "Розробка веб-додатків",
        "Бази даних", "Машинне навчання", "Штучний інтелект"
    ]
    literature_books = [
        "Кобзар", "Лісова пісня", "Енеїда",
        "Майстер і Маргарита", "Вій", "Тіні забутих предків"
    ]
    
    # Наповнюємо бібліотеку книгами різних жанрів
    
    # Додаємо фантастичні книги (серія про Гаррі Поттера)
    for book_name in fantastic_books:
        book = Book(f"Гаррі Поттер і {book_name}", "Дж. К. Роулінг", 1997, "978-3-16-148410-0")
        ITCollegeLibrary.books_shelf.append(book)  # На полицю
        ITCollegeLibrary.books.append(book)  # У загальний каталог
    
    # Додаємо книги з програмування
    for book_name in programming_books:
        book = Book(book_name, "Автор невідомий", 2020, "978-1-23-456789-0")
        ITCollegeLibrary.books_shelf.append(book)
        ITCollegeLibrary.books.append(book)
    
    # Додаємо літературні книги
    for book_name in literature_books:
        book = Book(book_name, "Український класик", 1950, "978-0-12-345678-9")
        ITCollegeLibrary.books_shelf.append(book)
        ITCollegeLibrary.books.append(book)
    
    # Додаємо історичні книги
    for book_name in historian_books:
        book = Book(book_name, "Відомий історик", 2015, "978-9-87-654321-0")
        ITCollegeLibrary.books_shelf.append(book)
        ITCollegeLibrary.books.append(book)

    # Реєструємо студентів у бібліотеці
    student_names = ["Богдан", "Ростислав", "Анна", "Олена", "Ігор", "Марія", "Віктор"]
    for name in student_names:
        user = Student(name)
        ITCollegeLibrary.students.append(user)
        print(user.student_id_card)

    # Виводимо початкову інформацію про бібліотеку
    print(f"\nДоступні книги в бібліотеці ІТ коледжу: {len(ITCollegeLibrary.list_available_books)}")
    print(f"\nУ бібліотеці зареєстровано користувачів: {len(ITCollegeLibrary.students)}")

    # Створюємо список книг, яких немає в бібліотеці (для тестування)
    non_existing_books = [
        Book("Історія України", "Іван Франко", 2020, "978-3-16-148410-1"),
        Book("Математика для інженерів", "Петро Петров", 2018, "978-3-16-148410-2"),
        Book("Фізика в сучасному світі", "Олександр Олександров", 2019, "978-3-16-148410-3")
    ]

    # Симулюємо роботу бібліотеки протягом 90 днів (приблизно 3 місяці)
    SIMULATION_DAYS = 90
    BORROW_PROBABILITY = 0.4  # 40% ймовірність спроби взяти книгу
    
    for day in range(1, SIMULATION_DAYS):
        print(f"\n--- День {day} ---")
        
        # Випадково обираємо книгу (включаючи неіснуючі для реалістичності)
        random_book: Book = random.choice(non_existing_books + ITCollegeLibrary.books)
        # Випадково обираємо студента
        random_user: Student = random.choice(ITCollegeLibrary.students)
        
        print(f"\nСпроба видати книгу '{random_book.title}' користувачу {random_user.name}:")
        
        # З певною ймовірністю студент намагається взяти книгу
        if random.random() < BORROW_PROBABILITY:
            # Студент думає, чи хоче він цю книгу
            if random_user.think_before_take_a_book(random_book):
                # Намагаємося видати книгу
                if ITCollegeLibrary.lend_book(random_book, random_user, day):
                    print(f"Книга '{random_book.title}' успішно видана користувачу {random_user.name}.")
                else:
                    print(f"Книга '{random_book.title}' недоступна для читання.")
        else:
            # В іншому випадку студент намагається повернути книгу
            if ITCollegeLibrary.return_book(random_book, random_user, day):
                print(f"Книга '{random_book.title}' успішно повернена до бібліотеки {random_user.name}.")
            else:
                print(f"Книга '{random_book.title}' не знаходиться у користувача {random_user.name}.")
    
    # === ВИВЕДЕННЯ ФІНАЛЬНОЇ СТАТИСТИКИ ===
    print("\n" + "="*70)
    print(f"ПІДСУМКОВА СТАТИСТИКА ПІСЛЯ {SIMULATION_DAYS} ДНІВ РОБОТИ БІБЛІОТЕКИ")
    print("="*70)
    
    # Статистика по кожному студенту
    for user in ITCollegeLibrary.students:
        print(f"\n{'─'*70}")
        print(f"Студент: {user.name}")
        print(f"{'─'*70}")
        
        # Поточні книги у студента
        print(f"  Зараз має {len(user.borrowed_books)} книг(и):")
        if user.borrowed_books:
            for book in user.borrowed_books:
                print(f"    • {book.title}")
        else:
            print("    (немає книг)")
        
        # Загальна статистика
        print(f"\n  📊 Статистика за період:")
        print(f"    Всього книжок взято: {user.total_books_taken}")
        
        # Найулюбленіші книжки
        fav_books = user.favorite_books
        if fav_books:
            print(f"    Найулюбленіші книжки: {', '.join(fav_books)}")
        else:
            print("    Найулюбленіші книжки: немає даних")
        
        # Дні читання повернутих книг
        if user.book_reading_days:
            print("\n  📖 Дні читання повернутих книжок:")
            for book in user.books_taken_history:
                days = user.get_reading_days(book)
                if days > 0:
                    print(f"    • '{book.title}': {days} днів")
        else:
            print("\n  📖 Студент ще не повертав книжки")
    
    # Статистика бібліотеки
    print(f"\n{'='*70}")
    print(f"СТАТИСТИКА БІБЛІОТЕКИ")
    print(f"{'='*70}")
    print(f"Всього книг у каталозі: {len(ITCollegeLibrary.books)}")
    print(f"Доступних книг на полиці: {len(ITCollegeLibrary.list_available_books)}")
    print(f"Книг у студентів: {len(ITCollegeLibrary.books) - len(ITCollegeLibrary.list_available_books)}")
    
    print(f"\nДоступні книги:")
    for available_book in ITCollegeLibrary.list_available_books:
        print(f"  • {available_book.title}")
    print("="*70)

    # Симулюємо процес видачі книги користувачу та повернення книги до бібліотеки
    # for day in ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]:
    #     print(f"\n--- День {day} ---")
    #     visitors = random.sample(ITCollegeLibrary.users, k=2)
    #     for user in visitors:
    #         print(f"\nКористувач {user.name} заходить до бібліотеки.")
    #         if user.borrowed_books:
    #             return_random_book: Book = random.choice(user.borrowed_books)
    #             if user.return_book(return_random_book):
    #                 print(f"{user.name} повернув книгу:\n{return_random_book.description}")
            
    #         book_to_borrow: Book = random.choice(ITCollegeLibrary.list_available_books)
    #         if user.think_before_take_a_book(book_to_borrow):
    #             if user.borrow_book(book_to_borrow):
    #                 print(f"{user.name} успішно взяв книгу:\n{book_to_borrow.description}")
    #             else:
    #                 print(f"Книга '{book_to_borrow.title}' недоступна для читання, її взяв студент {book_to_borrow.taken_by}.")
    #         else:
    #             print(f"{user.name} не взяв книгу '{book_to_borrow.title}'.")

    #         print(f"{user.name} виходить з бібліотеки.")
        