# Практичні приклади

## Огляд

На цій сторінці зібрані практичні приклади використання віртуальних середовищ з реальними застосунками, які ми створювали в рамках лабораторної роботи №6.

## Структура проекту

```
6_lab/
├── app.py              # Базовий застосунок з HTTP-запитами
├── anime.py            # Flask веб-застосунок з Jikan API
├── 1_venv/             # Приклад з venv
│   ├── requirements.txt
│   └── requirements-dev.txt
├── 2_pipenv/           # Приклад з Pipenv
│   └── Pipfile
└── 3_poetry/           # Приклад з Poetry
    ├── pyproject.toml
    └── docs/
```

## Приклад 1: Базовий застосунок (app.py)

### Опис

Простий Python скрипт, який демонструє:
- Роботу з HTTP-клієнтами (httpx та requests)
- Використання змінних середовища
- Імпорт зовнішніх бібліотек

### Вихідний код

```python
import math
import random 
import os

# Це все вбудовані бібліотеки, які не потрібно встановлювати через pip

# в нас ще немає Flask, встановимо її пізніше
#from flask import Flask

# є бібліотеки які не є вбудованими, але їх можна встановити через pip
import httpx

u = os.getenv('URL_TEST')
r = httpx.get(u)
print(f"httpx: {r} коли доступаємось до URL_TEST: {u}")

import requests
r = requests.get(u)
print(f"requests: {r} коли доступаємось до URL_TEST: {u}")

def nonConventionalFunction(x):
    return math.sin(x) + random.random()


print(f"Витягуємо змінні TEST: {os.getenv('TEST')}")
```

### Запуск з venv

```bash
cd 6_lab

# Створення та активація середовища
python -m venv venv
source venv/bin/activate

# Встановлення залежностей
pip install httpx requests

# Налаштування змінних середовища
export URL_TEST="https://httpbin.org/get"
export TEST="1"

# Запуск
python app.py
```

**Очікуваний вивід:**
```
httpx: <Response [200 OK]> коли доступаємось до URL_TEST: https://httpbin.org/get
requests: <Response [200]> коли доступаємось до URL_TEST: https://httpbin.org/get
Витягуємо змінні TEST: 1
```

### Запуск з Pipenv

```bash
cd 6_lab/2_pipenv

# Встановлення залежностей
pipenv install httpx requests

# Створення .env файлу
cat > .env << EOF
URL_TEST=https://httpbin.org/get
TEST=1
EOF

# Запуск (автоматично завантажить .env)
pipenv run python ../app.py
```

### Запуск з Poetry

```bash
cd 6_lab/3_poetry

# Встановлення залежностей
poetry add httpx requests

# Налаштування змінних
export URL_TEST="https://httpbin.org/get"
export TEST="1"

# Запуск
poetry run python ../app.py
```

## Приклад 2: Flask веб-застосунок (anime.py)

### Опис

Веб-застосунок на Flask, який:
- Використовує Jikan API для отримання даних про аніме
- Відображає інформацію про епізоди
- Демонструє роботу з веб-фреймворками

### Вихідний код

```python
from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(59978, extension='episodes')

@app.route('/')
def home():
    a = str()
    for episode in j["data"]: 
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    return a

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Запуск з venv

```bash
cd 6_lab/1_venv

# Активація середовища
source my_env/bin/activate

# Встановлення залежностей
pip install Flask jikanpy-v4

# Збереження залежностей
pip freeze > requirements.txt

# Запуск
python ../anime.py
```

**Доступ:** http://127.0.0.1:5000

### Запуск з Pipenv

```bash
cd 6_lab/2_pipenv

# Встановлення залежностей
pipenv install Flask jikanpy-v4

# Оновлення Pipfile
pipenv lock

# Запуск
pipenv run python ../anime.py

# Або в shell
pipenv shell
python ../anime.py
```

### Запуск з Poetry

```bash
cd 6_lab/3_poetry

# Додавання залежностей
poetry add Flask jikanpy-v4

# Запуск
poetry run python ../anime.py

# Або через shell
poetry shell
python ../anime.py
```

## Приклад 3: Робота з requirements.txt

### Створення requirements.txt

#### З активним venv

```bash
# Встановлення пакетів
pip install httpx requests Flask jikanpy-v4

# Заморожування всіх залежностей
pip freeze > requirements.txt
```

**Результат (requirements.txt):**
```text
aiohappyeyeballs==2.6.1
aiohttp==3.13.3
aiosignal==1.4.0
attrs==25.4.0
blinker==1.9.0
certifi==2026.1.4
charset-normalizer==3.4.4
click==8.3.1
Flask==3.1.2
frozenlist==1.8.0
httpx==0.28.1
idna==3.11
itsdangerous==2.2.0
jikanpy-v4==1.0.2
...
```

### Розділення dev-залежностей

**requirements.txt** (production):
```text
httpx==0.28.1
requests==2.32.5
Flask==3.1.2
jikanpy-v4==1.0.2
```

**requirements-dev.txt** (development):
```text
# Включаємо production залежності
-r requirements.txt

# Dev інструменти
flake8==7.0.0
pytest==8.0.0
black==24.0.0
mypy==1.8.0
```

### Встановлення з requirements.txt

```bash
# Production
pip install -r requirements.txt

# Development
pip install -r requirements-dev.txt
```

## Приклад 4: Робота з Pipfile

### Створення Pipfile

```bash
cd 6_lab/2_pipenv

# Ініціалізація з Python 3.13
pipenv --python 3.13
```

**Результат (Pipfile):**
```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
httpx = "*"
requests = "*"
flask = "==3.1.2"
jikanpy-v4 = "==1.0.2"

[dev-packages]
flake8 = "*"
pytest = "*"

[requires]
python_version = "3.13"
python_full_version = "3.13.7"
```

### Встановлення пакетів

```bash
# Production пакети
pipenv install httpx requests Flask jikanpy-v4

# Dev пакети
pipenv install --dev flake8 pytest

# З точною версією
pipenv install "Flask==3.1.2"

# З діапазоном версій
pipenv install "Django>=4.0,<5.0"
```

### Перегляд дерева залежностей

```bash
pipenv graph
```

**Вивід:**
```
Flask==3.1.2
├── blinker [required: >=1.6.2, installed: 1.9.0]
├── click [required: >=8.1.3, installed: 8.3.1]
├── itsdangerous [required: >=2.1.2, installed: 2.2.0]
├── Jinja2 [required: >=3.1.2, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
└── Werkzeug [required: >=3.0.0, installed: 3.1.5]
```

### Перевірка безпеки

```bash
# Базова перевірка
pipenv check

# Детальне сканування
pipenv check --scan
```

## Приклад 5: Робота з pyproject.toml (Poetry)

### Створення проекту

```bash
cd 6_lab/3_poetry

# Інтерактивна ініціалізація
poetry init
```

**Результат (pyproject.toml):**
```toml
[project]
name = "3-poetry"
version = "0.1.1"
description = "Приклад роботи з Poetry"
authors = [
    {name = "BobasB", email = "bugil.bogdan@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "httpx (>=0.28.1,<0.29.0)",
    "requests (>=2.32.5,<3.0.0)"
]

[project.optional-dependencies]
dev = [
    "flake8",
    "pytest",
    "black",
]

[tool.poetry]
packages = [{include = "3_poetry", from = "src"}]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Додавання залежностей

```bash
# Production залежності
poetry add httpx requests

# Dev залежності
poetry add flake8 pytest black --group dev

# З версією
poetry add "Flask==3.1.2"

# З діапазоном
poetry add "Django>=4.0,<5.0"

# Остання версія
poetry add requests@latest
```

### Групи залежностей

```bash
# Додати до групи docs
poetry add mkdocs mkdocs-material --group docs

# Встановити з групою
poetry install --with docs

# Встановити без групи
poetry install --without dev

# Тільки певна група
poetry install --only docs
```

## Приклад 6: Перевірка коду з flake8

### Встановлення flake8

#### venv
```bash
pip install flake8
pip freeze > requirements-dev.txt
```

#### Pipenv
```bash
pipenv install --dev flake8
```

#### Poetry
```bash
poetry add flake8 --group dev
```

### Використання flake8

```bash
# Перевірка одного файлу
flake8 app.py

# Перевірка всіх файлів у папці
flake8 .

# З виключеннями
flake8 --exclude=venv,__pycache__ .

# З максимальною довжиною рядка
flake8 --max-line-length=100 app.py
```

### Конфігурація (.flake8)

```ini
[flake8]
max-line-length = 100
exclude = 
    .git,
    __pycache__,
    venv,
    .venv,
    build,
    dist
ignore = 
    E203,  # whitespace before ':'
    W503,  # line break before binary operator
```

## Приклад 7: Змінні середовища

### Використання .env файлу

**.env:**
```bash
# URLs
URL_TEST=https://httpbin.org/get
API_BASE_URL=https://api.jikan.moe/v4

# Конфігурація
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://localhost/mydb

# Опції
MAX_RETRIES=3
TIMEOUT=30
```

### Завантаження в Python

#### З python-dotenv (venv)

```python
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URL_TEST')
debug = os.getenv('DEBUG', 'False') == 'True'
max_retries = int(os.getenv('MAX_RETRIES', '3'))
```

#### З Pipenv (автоматично)

```bash
# .env завантажується автоматично
pipenv run python app.py
```

#### З Poetry (вручну)

```bash
# Встановити python-dotenv
poetry add python-dotenv

# Завантажити в коді
from dotenv import load_dotenv
load_dotenv()
```

### Експорт вручну

```bash
export URL_TEST="https://httpbin.org/get"
export DEBUG=True
python app.py
```

## Приклад 8: Docker інтеграція

### З requirements.txt (venv)

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Копіювання файлів залежностей
COPY requirements.txt .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання коду
COPY . .

# Змінні середовища
ENV URL_TEST=https://httpbin.org/get

CMD ["python", "app.py"]
```

**Збірка та запуск:**
```bash
docker build -t my-app .
docker run -e URL_TEST="https://httpbin.org/get" my-app
```

### З Pipenv

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

# Встановлення Pipenv
RUN pip install pipenv

WORKDIR /app

# Копіювання файлів залежностей
COPY Pipfile Pipfile.lock ./

# Встановлення залежностей в системний Python
RUN pipenv install --system --deploy

# Копіювання коду
COPY . .

CMD ["python", "app.py"]
```

### З Poetry

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

# Встановлення Poetry
RUN pip install poetry

WORKDIR /app

# Налаштування Poetry
RUN poetry config virtualenvs.create false

# Копіювання файлів залежностей
COPY pyproject.toml poetry.lock ./

# Встановлення залежностей
RUN poetry install --without dev --no-root

# Копіювання коду
COPY . .

# Встановлення проекту
RUN poetry install --without dev

CMD ["python", "app.py"]
```

## Приклад 9: CI/CD інтеграція

### GitHub Actions з venv

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    
    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Lint with flake8
      run: |
        source venv/bin/activate
        flake8 .
    
    - name: Run tests
      run: |
        source venv/bin/activate
        pytest
```

### GitHub Actions з Pipenv

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    
    - name: Install Pipenv
      run: pip install pipenv
    
    - name: Install dependencies
      run: pipenv install --dev
    
    - name: Lint with flake8
      run: pipenv run flake8 .
    
    - name: Run tests
      run: pipenv run pytest
```

### GitHub Actions з Poetry

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    
    - name: Install Poetry
      uses: snok/install-poetry@v1
      with:
        version: 2.0.0
        virtualenvs-create: true
        virtualenvs-in-project: true
    
    - name: Load cached venv
      uses: actions/cache@v3
      with:
        path: .venv
        key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}
    
    - name: Install dependencies
      run: poetry install --with dev
    
    - name: Lint with flake8
      run: poetry run flake8 .
    
    - name: Run tests
      run: poetry run pytest
```

## Приклад 10: Створення документації з MkDocs

### Встановлення MkDocs

#### З Poetry (наш приклад)

```bash
cd 6_lab/3_poetry
poetry add mkdocs --group dev
```

### Конфігурація (mkdocs.yml)

```yaml
site_name: Лабораторна робота №6 - Віртуальні середовища Python
site_description: Робота з віртуальними середовищами Python

theme:
  name: readthedocs
  locale: uk

nav:
  - Головна: index.md
  - Інструменти:
    - venv: venv.md
    - Pipenv: pipenv.md
    - Poetry: poetry.md
  - Порівняння інструментів: comparison.md
  - Практичні приклади: examples.md

markdown_extensions:
  - codehilite
  - admonition
  - toc:
      permalink: true
```

### Створення документів

```bash
mkdir -p docs
cd docs

# Створення файлів
touch index.md venv.md pipenv.md poetry.md comparison.md examples.md
```

### Запуск локального сервера

```bash
# З Poetry
poetry run mkdocs serve

# Або з активованим середовищем
poetry shell
mkdocs serve
```

**Доступ:** http://127.0.0.1:8000

### Збірка статичного сайту

```bash
poetry run mkdocs build
```

Результат у папці `site/`.

### Публікація на GitHub Pages

```bash
poetry run mkdocs gh-deploy
```

## Підсумок

У цій лабораторній роботі ми розглянули:

✅ **venv + pip** - базовий підхід для простих проектів  
✅ **Pipenv** - покращене управління з Pipfile та автоматизацією  
✅ **Poetry** - сучасний повнофункціональний інструмент  

Всі три підходи мають свої переваги і використовуються в реальних проектах залежно від потреб та вимог.

---

**Більше інформації:**
- [Головна сторінка](index.md)
- [venv](venv.md)
- [Pipenv](pipenv.md)
- [Poetry](poetry.md)
- [Порівняння](comparison.md)
