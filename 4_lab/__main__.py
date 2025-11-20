import random
from library import Library
from books import Book
from student import Student

if __name__ == "__main__":
    ITCollegeLibrary = Library()
    _book_name = ["Філософський камінь", "Таємна кімната", "В'язень Азкабану", "Кубок вогню", "Орден Фенікса", "Напівкровний принц", "Смертельні реліквії"]
    for b in _book_name:
        book = Book(f"Гаррі Поттер і {b}", "Дж. К. Роулінг", 1997, "978-3-16-148410-0")
        ITCollegeLibrary.books_shelf.append(book)
        ITCollegeLibrary.books.append(book)

    for name in ["Богдан", "Ростислав", "Анна", "Олена", "Ігор", "Марія", "Віктор"]:
        user = Student(name)
        ITCollegeLibrary.students.append(user)
        print(user.student_id_card)

    print("\nДоступні книги в бібліотеці ІТ коледжу:")
    for available_book in ITCollegeLibrary.list_available_books:
        print(available_book.description)
    
    print("У бібліотеці зареєстровано користувачів:")
    for user in ITCollegeLibrary.students:
        print(user.student_id_card)

    non_existing_books = [
        Book("Історія України", "Іван Франко", 2020, "978-3-16-148410-1"),
        Book("Математика для інженерів", "Петро Петров", 2018, "978-3-16-148410-2"),
        Book("Фізика в сучасному світі", "Олександр Олександров", 2019, "978-3-16-148410-3")
        ]

    for day in range(1, 20):
        print(f"\n--- День {day} ---")
        random_book: Book = random.choice(non_existing_books + ITCollegeLibrary.books)
        random_user: Student = random.choice(ITCollegeLibrary.students)
        print(f"\nСпроба видати книгу '{random_book.title}' користувачу {random_user.name}:")
        if ITCollegeLibrary.lend_book(random_book, random_user):
            print(f"Книга '{random_book.title}' успішно видана користувачу {random_user.name}.")
        else:
            print(f"Книга '{random_book.title}' недоступна для читання.")
    
    ######

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
        