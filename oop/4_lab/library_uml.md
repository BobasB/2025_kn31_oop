# UML Діаграма класів проекту "Бібліотека ІТ Коледжу"

```mermaid
classDiagram
    class BookStatus {
        <<enumeration>>
        +AVAILABLE: str = "в наявності"
        +BORROWED: str = "взята"
        +RESERVED: str = "зарезервована"
    }

    class Book {
        -title: str
        -author: str
        -year: int
        -isbn: str
        -status: BookStatus
        -taken_by: str | None
        +__init__(title: str, author: str, year: int, isbn: str)
        +__str__() str
        +description: str
        +info: str
    }

    class Student {
        -name: str
        -ID: int
        -borrowed_books: list~Book~
        -college_name: str
        -books_taken_history: list~Book~
        -book_reading_days: dict~int, int~
        -book_borrow_dates: dict~int, int~
        +__init__(name: str)
        +student_id_card: str
        +total_books_taken: int
        +favorite_books: list~str~
        +get_reading_days(book: Book) int
        +borrow_book(book: Book, current_day: int) bool
        +return_book(book: Book, current_day: int) bool
        +start_reading_book(book: Book) str
        +think_before_take_a_book(book: Book) bool
    }

    class Library {
        -books: list~Book~
        -books_shelf: list~Book~
        -students: list~Student~
        +__init__()
        +list_available_books: list~Book~
        +list_registered_students: list~Student~
        +lend_book(book: Book, student: Student, current_day: int) bool
        +return_book(book: Book, student: Student, current_day: int) bool
    }

    class Statistics {
        -library: Library
        -simulation_days: int
        +__init__(library: Library, simulation_days: int)
        +print_student_statistics(student: Student) None
        +print_library_statistics() None
        +print_full_statistics() None
        +get_total_books_borrowed() int
        +get_most_active_student() Student | None
        +get_most_popular_books() list~str~
        +print_extended_statistics() None
    }

    %% Relationships
    Book --> BookStatus : uses
    Student "1" --> "*" Book : borrowed_books
    Student "1" --> "*" Book : books_taken_history
    Library "1" --> "*" Book : books
    Library "1" --> "*" Book : books_shelf
    Library "1" --> "*" Student : students
    Statistics "1" --> "1" Library : analyzes
    Statistics --> Student : analyzes
```

## Опис класів та їх взаємозв'язків

### 1. **BookStatus** (Enumeration)
Перелік можливих статусів книги:
- `AVAILABLE` - книга доступна для позики
- `BORROWED` - книга взята студентом
- `RESERVED` - книга зарезервована

### 2. **Book**
Представляє книгу в бібліотеці:
- **Атрибути**: назва, автор, рік видання, ISBN, статус, хто взяв
- **Методи**: ініціалізація, строкове представлення, опис, інформація про статус
- **Зв'язок**: використовує `BookStatus`

### 3. **Student**
Представляє студента, який користується бібліотекою:
- **Атрибути**: ім'я, ID, поточні книги, історія взятих книг, статистика читання
- **Методи**: взяття/повернення книг, перегляд статистики, прийняття рішень
- **Зв'язки**: 
  - Має багато книг у позиці (`borrowed_books`)
  - Зберігає історію взятих книг (`books_taken_history`)

### 4. **Library**
Керує всією бібліотекою:
- **Атрибути**: каталог книг, доступні книги, список студентів
- **Методи**: видача/повернення книг, перегляд доступних ресурсів
- **Зв'язки**:
  - Управляє колекцією всіх книг (`books`)
  - Управляє книгами на полиці (`books_shelf`)
  - Реєструє студентів (`students`)

### 5. **Statistics**
Аналізує та виводить статистику роботи бібліотеки:
- **Атрибути**: посилання на бібліотеку, кількість днів симуляції
- **Методи**: виведення статистики, обчислення метрик
- **Зв'язки**: аналізує бібліотеку та студентів

## Ключові взаємодії

1. **Library ↔ Student ↔ Book**: Бібліотека видає книги студентам через методи `lend_book()` та `return_book()`
2. **Student → Book**: Студент зберігає посилання на взяті книги та історію
3. **Statistics → Library**: Статистика аналізує дані бібліотеки та студентів
4. **Book → BookStatus**: Кожна книга має статус з переліку

## Типи зв'язків

- **Композиція** (◆): Library містить списки Student та Book
- **Асоціація** (→): Student працює з Book, Statistics аналізує Library
- **Залежність** (- - →): Book використовує BookStatus
