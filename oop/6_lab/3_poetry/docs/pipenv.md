# Pipenv - Сучасний менеджер пакетів та середовищ

## Огляд

Pipenv - це інструмент, який об'єднує `pip` та `virtualenv` в один зручний робочий процес. Він використовує файл `Pipfile` для управління залежностями та автоматично створює віртуальні середовища.

## Філософія Pipenv

> "Pipenv is a tool that aims to bring the best of all packaging worlds to the Python world."

Pipenv намагається вирішити проблеми, які виникають при використанні pip та venv окремо:

- Автоматичне створення та управління віртуальними середовищами
- Декларативний файл залежностей (Pipfile)
- Детерміністичні збірки через Pipfile.lock
- Розділення dev та production залежностей
- Автоматичне розв'язання конфліктів залежностей

## Встановлення Pipenv

```bash
# Встановлення через pip
pip install pipenv

# Або через Homebrew (macOS)
brew install pipenv
```

## Переваги

- ✅ Автоматичне управління віртуальними середовищами
- ✅ Декларативний Pipfile замість requirements.txt
- ✅ Автоматичне створення Pipfile.lock для детерміністичних збірок
- ✅ Вбудоване розділення dev/production залежностей
- ✅ Автоматичне завантаження змінних з .env файлів
- ✅ Перевірка безпеки залежностей
- ✅ Візуалізація дерева залежностей

## Недоліки

- ❌ Повільніше, ніж venv
- ❌ Потребує додаткового встановлення
- ❌ Іноді проблеми з розв'язанням складних залежностей
- ❌ Менша спільнота, ніж у pip

## Основні команди

### Ініціалізація проекту

```bash
cd 6_lab/2_pipenv
pipenv --python 3.13
```

Це створить:
- Віртуальне середовище
- Файл `Pipfile`

### Встановлення пакетів

```bash
# Встановлення production пакету
pipenv install httpx

# Встановлення кількох пакетів
pipenv install requests Flask jikanpy-v4

# Встановлення dev пакету
pipenv install --dev flake8
```

### Активація середовища

```bash
# Запуск shell в середовищі
pipenv shell

# Або запуск команди в середовищі
pipenv run python app.py
```

### Видалення середовища

```bash
pipenv --rm
```

## Структура Pipfile

Pipfile - це декларативний файл для управління залежностями в форматі TOML:

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
aiohappyeyeballs = "==2.6.1"
aiohttp = "==3.13.3"
flask = "==3.1.2"
httpx = "*"
requests = "*"
jikanpy-v4 = "==1.0.2"

[dev-packages]
flake8 = "*"

[requires]
python_version = "3.13"
python_full_version = "3.13.7"
```

### Секції Pipfile

- **[source]** - джерела пакетів (PyPI, приватні репозиторії)
- **[packages]** - продакшн залежності
- **[dev-packages]** - залежності для розробки
- **[requires]** - вимоги до версії Python

### Специфікація версій

```toml
# Точна версія
flask = "==3.1.2"

# Будь-яка версія
requests = "*"

# Діапазон версій
django = ">=3.0,<4.0"

# Оптимістична версія
numpy = "~=1.20.0"  # >=1.20.0, <1.21.0
```

## Pipfile.lock

Після встановлення пакетів Pipenv створює `Pipfile.lock` - JSON файл з точними версіями всіх залежностей (включаючи транзитивні):

```json
{
    "_meta": {
        "hash": {
            "sha256": "..."
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.13"
        }
    },
    "default": {
        "httpx": {
            "version": "==0.28.1",
            "hashes": [...]
        }
    }
}
```

### Чому Pipfile.lock важливий?

- 🔒 Гарантує однакові версії на всіх машинах
- 🔒 Включає хеші для перевірки цілісності
- 🔒 Фіксує всі транзитивні залежності
- 🔒 Забезпечує відтворюваність середовища

## Встановлення залежностей

### З Pipfile (розв'язання залежностей)

```bash
pipenv install
```

### З Pipfile.lock (точні версії)

```bash
pipenv install --ignore-pipfile
```

### Тільки production залежності

```bash
pipenv install --deploy --ignore-pipfile
```

## Візуалізація залежностей

```bash
pipenv graph
```

Приклад виводу:

```
httpx==0.28.1
├── anyio [required: >=3.0, <5, installed: 4.7.0]
│   ├── idna [required: >=2.8, installed: 3.11]
│   └── sniffio [required: >=1.1, installed: 1.3.1]
├── certifi [required: Any, installed: 2026.1.4]
├── httpcore [required: ==1.*, installed: 1.0.7]
│   ├── certifi [required: Any, installed: 2026.1.4]
│   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
└── idna [required: Any, installed: 3.11]
```

## Робота зі змінними середовища

### Створення .env файлу

```bash
# .env
URL_TEST=https://httpbin.org/get
TEST=1
DEBUG=True
DATABASE_URL=postgresql://localhost/mydb
```

### Автоматичне завантаження

Pipenv автоматично завантажує змінні з `.env` при запуску:

```bash
pipenv run python app.py
```

### Експорт змінних вручну

```bash
export URL_TEST="https://httpbin.org/get"
export TEST=1
```

## Перевірка безпеки

```bash
# Перевірка на відомі вразливості
pipenv check

# Детальне сканування
pipenv check --scan
```

Приклад виводу:

```
Checking PEP 508 requirements...
Passed!
Checking installed package safety...
All good!
```

## Налаштування розташування середовища

### За замовчуванням

Pipenv створює середовище в централізованому місці:

```bash
~/.local/share/virtualenvs/proj-Gdiqmgvz/
```

### В папці проекту

```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install
```

Це створить папку `.venv` в корені проекту.

## Приклад повного робочого процесу

### 1. Створення проекту

```bash
cd 6_lab/2_pipenv
pipenv --python 3.13
```

### 2. Встановлення залежностей

```bash
# Production пакети
pipenv install httpx requests Flask jikanpy-v4

# Dev інструменти
pipenv install --dev flake8
```

### 3. Перегляд дерева залежностей

```bash
pipenv graph
```

### 4. Активація середовища

```bash
pipenv shell
```

### 5. Запуск застосунку

```bash
# В активованому shell
python app.py

# Або без активації
pipenv run python app.py
```

### 6. Перевірка безпеки

```bash
pipenv check --scan
```

### 7. Видалення та перестворення

```bash
# Видалення середовища
pipenv --rm

# Налаштування локального розташування
export PIPENV_VENV_IN_PROJECT=1

# Перестворення
pipenv install
```

## Корисні команди

### Інформація про проект

```bash
# Шлях до віртуального середовища
pipenv --venv

# Шлях до Python
pipenv --py

# Показати, де встановлений пакет
pipenv --where
```

### Оновлення залежностей

```bash
# Оновити всі пакети
pipenv update

# Оновити конкретний пакет
pipenv update requests

# Оновити Pipfile.lock без встановлення
pipenv lock
```

### Видалення пакетів

```bash
# Видалити пакет
pipenv uninstall requests

# Видалити всі dev пакети
pipenv uninstall --all-dev

# Очистити невикористані пакети
pipenv clean
```

## Міграція з requirements.txt

### Імпорт з requirements.txt

```bash
pipenv install -r requirements.txt
```

### Експорт до requirements.txt

```bash
# Production залежності
pipenv requirements > requirements.txt

# Dev залежності
pipenv requirements --dev > requirements-dev.txt

# Все разом
pipenv requirements --dev-only >> requirements.txt
```

## Інтеграція з CI/CD

### GitHub Actions приклад

```yaml
- name: Install Pipenv
  run: pip install pipenv

- name: Install dependencies
  run: pipenv install --deploy --dev

- name: Run tests
  run: pipenv run pytest
```

### Docker приклад

```dockerfile
FROM python:3.13-slim

# Встановлення Pipenv
RUN pip install pipenv

WORKDIR /app

# Копіювання файлів залежностей
COPY Pipfile Pipfile.lock ./

# Встановлення залежностей
RUN pipenv install --deploy --system

COPY . .

CMD ["python", "app.py"]
```

## Pipenv Scripts

Можна додати custom скрипти в Pipfile:

```toml
[scripts]
start = "python app.py"
test = "pytest tests/"
lint = "flake8 ."
dev = "flask run --debug"
```

Запуск:

```bash
pipenv run start
pipenv run test
pipenv run lint
```

## Поширені проблеми та рішення

### Повільне розв'язання залежностей

```bash
# Використання попереднього lock файлу
pipenv install --skip-lock

# Очистка кешу
pipenv --clear
```

### Конфлікти залежностей

```bash
# Спробувати знову
pipenv lock --clear

# Видалити Pipfile.lock та перестворити
rm Pipfile.lock
pipenv install
```

## Кращі практики

1. **Завжди коммітьте Pipfile та Pipfile.lock**
2. **Не коммітьте .env файли** (додайте до .gitignore)
3. **Використовуйте --deploy на production** для перевірки синхронізації
4. **Регулярно оновлюйте залежності**: `pipenv update`
5. **Перевіряйте безпеку**: `pipenv check`
6. **Використовуйте точні версії** для критичних залежностей

## Коли використовувати Pipenv

Pipenv підходить для:

- ✅ Web-застосунків
- ✅ Проектів середнього розміру
- ✅ Коли потрібне автоматичне управління середовищем
- ✅ Коли важлива безпека залежностей
- ✅ Коли працюєте з .env файлами

## Порівняння з іншими інструментами

| Функція | venv + pip | Pipenv | Poetry |
|---------|-----------|--------|--------|
| Автоматичні venv | ❌ | ✅ | ✅ |
| Файл залежностей | requirements.txt | Pipfile | pyproject.toml |
| Lock файл | ❌ | ✅ | ✅ |
| Dev залежності | Вручну | ✅ | ✅ |
| Перевірка безпеки | Вручну | ✅ | ✅ |
| Швидкість | ⚡⚡⚡ | ⚡⚡ | ⚡⚡⚡ |

Детальніше див. [Порівняння інструментів](comparison.md).

## Висновки

Pipenv - це потужний інструмент, що значно покращує робочий процес порівняно з pip та venv. Якщо вам потрібен баланс між функціональністю та простотою, Pipenv - чудовий вибір.

Для ще більш сучасного підходу розгляньте [Poetry](poetry.md).
