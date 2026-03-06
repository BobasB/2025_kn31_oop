# Poetry - Сучасний інструмент управління залежностями та пакетами

## Огляд

Poetry - це найсучасніший інструмент для управління залежностями та пакетами Python. Він пропонує повний набір функцій для розробки, збірки та публікації Python-проектів.

## Філософія Poetry

> "Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you."

Poetry прагне вирішити всі проблеми управління проектами Python в одному інструменті:

- 📦 Управління залежностями
- 🏗️ Збірка пакетів
- 📤 Публікація в PyPI
- 🔒 Детерміністичні збірки
- ⚡ Швидке розв'язання залежностей
- 🎯 Використання стандарту pyproject.toml

## Встановлення Poetry

### Офіційний інсталятор (рекомендовано)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Через pip

```bash
pip install poetry
```

### Через Homebrew (macOS)

```bash
brew install poetry
```

### Перевірка встановлення

```bash
poetry --version
```

## Переваги

- ✅ Єдиний інструмент для всього: залежності, збірка, публікація
- ✅ Використання стандарту pyproject.toml (PEP 518)
- ✅ Дуже швидке розв'язання залежностей
- ✅ Автоматичне створення віртуальних середовищ
- ✅ Детерміністичні збірки через poetry.lock
- ✅ Вбудована підтримка семантичного версіонування
- ✅ Підтримка приватних репозиторіїв
- ✅ Інтуїтивний CLI
- ✅ Велика і активна спільнота

## Недоліки

- ❌ Потребує встановлення
- ❌ Іноді несумісність з деякими legacy проектами
- ❌ Може бути надлишковим для дуже простих проектів

## Основні команди

### Ініціалізація проекту

```bash
# Інтерактивна ініціалізація
poetry init

# Створення нового проекту
poetry new my-project
```

### Встановлення залежностей

```bash
# Додати production залежність
poetry add httpx

# Додати кілька пакетів
poetry add httpx requests

# Додати dev залежність
poetry add mkdocs --group dev

# Або старий синтаксис
poetry add flake8 --dev
```

### Активація середовища

```bash
# Запуск нової оболонки
poetry shell

# Запуск команди
poetry run python app.py

# Eval для активації в поточному shell (bash/zsh)
eval $(poetry env activate)
```

### Видалення пакетів

```bash
poetry remove requests
```

## Структура pyproject.toml

`pyproject.toml` - це стандартний файл конфігурації Python проектів (PEP 518):

```toml
[project]
name = "3-poetry"
version = "0.1.1"
description = ""
authors = [
    {name = "BobasB", email = "bugil.bogdan@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "httpx (>=0.28.1,<0.29.0)",
    "requests (>=2.32.5,<3.0.0)"
]

[tool.poetry]
packages = [{include = "3_poetry", from = "src"}]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Основні секції

#### [project]
Метадані проекту згідно PEP 621:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Опис проекту"
authors = [
    {name = "Ваше Ім'я", email = "email@example.com"}
]
readme = "README.md"
requires-python = ">=3.8,<4.0"
license = {text = "MIT"}
keywords = ["example", "tutorial"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.13",
]
```

#### [project.dependencies]
Основні залежності проекту:

```toml
dependencies = [
    "httpx (>=0.28.1,<0.29.0)",
    "requests (>=2.32.5,<3.0.0)",
    "django (>=4.0,<5.0)",
]
```

#### [project.optional-dependencies]
Додаткові групи залежностей:

```toml
[project.optional-dependencies]
dev = [
    "pytest (>=7.0.0)",
    "flake8 (>=6.0.0)",
    "black (>=23.0.0)",
]
docs = [
    "mkdocs (>=1.5.0)",
    "mkdocs-material (>=9.0.0)",
]
```

#### [tool.poetry]
Специфічні налаштування Poetry:

```toml
[tool.poetry]
packages = [{include = "my_package", from = "src"}]
```

#### [build-system]
Конфігурація системи збірки (PEP 517):

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Специфікація версій

Poetry використовує семантичне версіонування:

```bash
# Точна версія
poetry add django==4.2.0

# Caret вимоги (^) - за замовчуванням
poetry add django  # ^4.2.0 означає >=4.2.0,<5.0.0

# Tilde вимоги (~)
poetry add django~=4.2.0  # >=4.2.0,<4.3.0

# Діапазон
poetry add "django>=4.0,<5.0"

# Wildcards
poetry add django==4.*

# Останя версія
poetry add django@latest
```

### Пояснення операторів

- `^1.2.3` - `>=1.2.3,<2.0.0` (мінімальна версія, але не наступна мажорна)
- `~1.2.3` - `>=1.2.3,<1.3.0` (мінімальна версія, але не наступна мінорна)
- `>=1.2,<2.0` - явний діапазон
- `*` - будь-яка версія

## Poetry.lock файл

Poetry автоматично створює `poetry.lock` файл, який містить точні версії всіх залежностей:

- 🔒 Гарантує однакові версії на всіх машинах
- 🔒 Включає хеші для безпеки
- 🔒 Фіксує всі транзитивні залежності
- 🔒 Автоматично оновлюється при зміні залежностей

### Важливо
**Завжди коммітьте poetry.lock** в систему контролю версій!

## Управління віртуальними середовищами

### Автоматичне створення

Poetry автоматично створює віртуальне середовище при першому `poetry install`.

### Конфігурація розташування

```bash
# Створювати .venv в папці проекту
poetry config virtualenvs.in-project true

# Повернути до системного розташування
poetry config virtualenvs.in-project false

# Переглянути налаштування
poetry config --list
```

### Інформація про середовище

```bash
# Показати шлях до середовища
poetry env info

# Показати тільки шлях
poetry env info --path

# Список всіх середовищ
poetry env list
```

### Управління середовищами

```bash
# Видалити поточне середовище
poetry env remove python

# Видалити конкретне середовище
poetry env remove python3.13

# Використати конкретний Python
poetry env use python3.12
poetry env use /usr/bin/python3.13
```

## Встановлення залежностей

### З pyproject.toml та poetry.lock

```bash
# Встановити всі залежності (включаючи dev)
poetry install

# Тільки production залежності
poetry install --without dev

# Тільки dev залежності
poetry install --only dev

# З конкретною групою
poetry install --with docs

# Синхронізація (видалити зайве)
poetry install --sync
```

### Оновлення залежностей

```bash
# Оновити всі залежності
poetry update

# Оновити конкретний пакет
poetry update requests

# Оновити lock без встановлення
poetry lock

# Оновити lock без оновлення залежностей
poetry lock --no-update
```

## Групи залежностей

Poetry підтримує кілька груп залежностей:

```toml
[project.dependencies]
httpx = ">=0.28.1"
requests = ">=2.32.5"

[project.optional-dependencies]
dev = [
    "pytest",
    "flake8",
    "black",
]
test = [
    "pytest",
    "pytest-cov",
    "pytest-mock",
]
docs = [
    "mkdocs",
    "mkdocs-material",
]
```

### Встановлення груп

```bash
# Додати до групи dev
poetry add pytest --group dev

# Встановити з групою
poetry install --with docs

# Встановити без групи
poetry install --without test

# Встановити тільки групу
poetry install --only dev
```

## Скрипти та команди

### Додавання скриптів

```toml
[project.scripts]
my-script = "my_package.module:function"
```

### Запуск команд

```bash
# Запуск Python
poetry run python app.py

# Запуск pytest
poetry run pytest

# Запуск mkdocs
poetry run mkdocs serve

# Запуск custom скрипту
poetry run my-script
```

## Приклад повного робочого процесу

### 1. Ініціалізація проекту

```bash
cd 6_lab/3_poetry
poetry init
```

Інтерактивні запити:
```
Package name [3_poetry]: 3-poetry
Version [0.1.0]: 0.1.1
Description []: Приклад роботи з Poetry
Author [BobasB <bugil.bogdan@gmail.com>, n to skip]: 
License []: MIT
Compatible Python versions [^3.13]: >=3.13
```

### 2. Додавання залежностей

```bash
# Production залежності
poetry add httpx requests

# Dev залежності
poetry add mkdocs --group dev
```

### 3. Активація середовища

```bash
# Варіант 1: Poetry shell
poetry shell

# Варіант 2: Eval (для поточного shell)
eval $(poetry env activate)

# Варіант 3: Запуск без активації
poetry run python app.py
```

### 4. Робота з застосунком

```bash
export URL_TEST="https://httpbin.org/get"
poetry run python ../app.py
```

### 5. Запуск документації

```bash
poetry run mkdocs serve
```

### 6. Деактивація

```bash
deactivate
```

## Збірка та публікація пакетів

### Збірка пакету

```bash
# Створити wheel та tar.gz
poetry build
```

Результат у папці `dist/`:
```
dist/
├── 3_poetry-0.1.1-py3-none-any.whl
└── 3_poetry-0.1.1.tar.gz
```

### Публікація в PyPI

```bash
# Налаштування облікових даних
poetry config pypi-token.pypi <your-token>

# Публікація
poetry publish

# Або build + publish
poetry publish --build
```

### Публікація в TestPyPI

```bash
# Додати репозиторій
poetry config repositories.testpypi https://test.pypi.org/legacy/

# Публікація
poetry publish -r testpypi
```

## Робота з приватними репозиторіями

```bash
# Додати джерело
poetry source add my-repo https://pypi.example.com/simple/

# Додати credentials
poetry config http-basic.my-repo username password

# Встановити з конкретного джерела
poetry add my-package --source my-repo
```

## Перевірка та налагодження

### Показати залежності

```bash
# Дерево залежностей
poetry show --tree

# Список всіх пакетів
poetry show

# Інформація про пакет
poetry show httpx

# Тільки production
poetry show --without dev

# Тільки останні версії
poetry show --latest
```

### Перевірка конфігурації

```bash
# Перевірити pyproject.toml
poetry check

# Показати конфігурацію
poetry config --list
```

### Налагодження

```bash
# Verbose режим
poetry install -vvv

# Очистити кеш
poetry cache clear pypi --all
```

## Експорт залежностей

### У requirements.txt

```bash
# Production залежності
poetry export -f requirements.txt -o requirements.txt

# З dev залежностями
poetry export -f requirements.txt -o requirements.txt --with dev

# Без хешів
poetry export -f requirements.txt -o requirements.txt --without-hashes
```

### Використання в Docker

```dockerfile
FROM python:3.13-slim

# Встановлення Poetry
RUN pip install poetry

WORKDIR /app

# Копіювання файлів залежностей
COPY pyproject.toml poetry.lock ./

# Встановлення залежностей без dev
RUN poetry install --without dev --no-root

# Копіювання коду
COPY . .

# Встановлення проекту
RUN poetry install --without dev

CMD ["poetry", "run", "python", "app.py"]
```

## Інтеграція з MkDocs

Наш приклад використання mkdocs:

### 1. Встановлення mkdocs

```bash
poetry add mkdocs --group dev
```

### 2. Конфігурація mkdocs.yml

```yaml
site_name: Лабораторна робота №6
theme:
  name: readthedocs
nav:
  - Головна: index.md
  - venv: venv.md
  - Pipenv: pipenv.md
  - Poetry: poetry.md
```

### 3. Запуск документації

```bash
poetry run mkdocs serve
```

### 4. Збірка статичного сайту

```bash
poetry run mkdocs build
```

## Корисні плагіни та інтеграції

### Pre-commit hooks

```bash
poetry add pre-commit --group dev
```

### Pytest

```bash
poetry add pytest pytest-cov --group dev
```

### Code formatters

```bash
poetry add black isort --group dev
poetry add flake8 mypy --group dev
```

## Конфігурація Poetry

### Глобальна конфігурація

```bash
# Показати всі налаштування
poetry config --list

# Встановити налаштування
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true

# Видалити налаштування
poetry config virtualenvs.in-project --unset
```

### Локальна конфігурація (poetry.toml)

```toml
[virtualenvs]
in-project = true
prefer-active-python = true
```

## Міграція з інших інструментів

### З requirements.txt

```bash
# Створити pyproject.toml
poetry init

# Додати залежності з requirements.txt
cat requirements.txt | xargs poetry add
```

### З Pipenv

```bash
# Poetry може імпортувати з Pipfile
poetry add $(cat Pipfile | grep '=' | cut -d'"' -f2)
```

## Кращі практики

1. **Завжди коммітьте pyproject.toml та poetry.lock**
2. **Використовуйте групи залежностей** для організації
3. **Використовуйте `virtualenvs.in-project = true`** для проектів
4. **Регулярно оновлюйте**: `poetry update`
5. **Перевіряйте конфігурацію**: `poetry check`
6. **Використовуйте `poetry.lock` для детермінізму**
7. **Документуйте версії Python** в requires-python
8. **Використовуйте semantic versioning** правильно
9. **Тестуйте чисте встановлення**: `poetry install --sync`

## Команди, які ми використовували

```bash
# Ініціалізація
cd 6_lab/3_poetry
poetry init

# Додавання залежностей
poetry add httpx requests

# Активація середовища
eval $(poetry env activate)

# Деактивація
deactivate

# Додавання dev-залежностей
poetry add mkdocs --group dev

# Запуск MkDocs
poetry run mkdocs serve
```

## Структура проекту з Poetry

```
3_poetry/
├── pyproject.toml        # Конфігурація проекту та залежності
├── poetry.lock           # Lock-файл з точними версіями
├── README.md             # Опис проекту
├── mkdocs.yml            # Конфігурація MkDocs
├── .venv/                # Віртуальне середовище (якщо in-project=true)
├── src/                  # Вихідний код
│   └── 3_poetry/
│       └── __init__.py
├── docs/                 # Документація MkDocs
│   ├── index.md
│   ├── venv.md
│   ├── pipenv.md
│   └── poetry.md
└── tests/                # Тести
    └── __init__.py
```

## Порівняння з іншими інструментами

| Функція | venv + pip | Pipenv | Poetry |
|---------|-----------|--------|--------|
| Автоматичні venv | ❌ | ✅ | ✅ |
| Файл залежностей | requirements.txt | Pipfile | pyproject.toml |
| Стандарт (PEP) | ❌ | ❌ | ✅ (PEP 518, 621) |
| Lock файл | ❌ | ✅ | ✅ |
| Dev залежності | Вручну | ✅ | ✅ |
| Групи залежностей | ❌ | ❌ | ✅ |
| Збірка пакетів | setuptools | ❌ | ✅ |
| Публікація | twine | ❌ | ✅ |
| Швидкість | ⚡⚡⚡ | ⚡⚡ | ⚡⚡⚡ |
| Популярність | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

## Коли використовувати Poetry

Poetry ідеально підходить для:

- ✅ Нових проектів будь-якого розміру
- ✅ Бібліотек та пакетів для публікації
- ✅ Проектів, що потребують строгого управління версіями
- ✅ Команд, які хочуть сучасний workflow
- ✅ Монорепозиторіїв з кількома пакетами
- ✅ Проектів з складними залежностями

## Ресурси

- 📖 [Офіційна документація](https://python-poetry.org/docs/)
- 🐙 [GitHub репозиторій](https://github.com/python-poetry/poetry)
- 💬 [Discord спільнота](https://discord.com/invite/awxPgve)
- 📚 [Poetry основи](https://python-poetry.org/docs/basic-usage/)

## Висновки

Poetry - це найсучасніший та найпотужніший інструмент для управління Python-проектами. Він об'єднує управління залежностями, віртуальними середовищами, збіркою та публікацією в один інтуїтивний інструмент.

Якщо ви починаєте новий проект або хочете модернізувати існуючий - Poetry є рекомендованим вибором у 2025 році.

Для порівняння з іншими інструментами див. [Порівняння інструментів](comparison.md).
