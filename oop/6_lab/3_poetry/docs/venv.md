# venv - Стандартний інструмент Python

## Огляд

`venv` - це вбудований модуль Python (починаючи з версії 3.3), який дозволяє створювати віртуальні середовища. Це найпростіший і найбазовіший інструмент для ізоляції залежностей проектів.

## Переваги

- ✅ Вбудований в Python - не потрібно нічого встановлювати
- ✅ Легкий у використанні
- ✅ Швидкий та ефективний
- ✅ Підтримується офіційно

## Недоліки

- ❌ Немає вбудованого управління залежностями
- ❌ Потребує ручного управління файлами requirements.txt
- ❌ Немає автоматичного розв'язання конфліктів залежностей
- ❌ Не відстежує dev-залежності окремо (потрібні додаткові файли)

## Створення віртуального середовища

### Базовий синтаксис

```bash
python -m venv <назва_середовища>
```

### Приклад

```bash
cd 6_lab/1_venv
python -m venv my_env
```

Це створить папку `my_env` з ізольованим Python-середовищем.

## Активація середовища

### На macOS/Linux

```bash
source my_env/bin/activate
```

### На Windows

```cmd
my_env\Scripts\activate
```

Після активації у терміналі з'явиться префікс `(my_env)`, що вказує на активне середовище.

## Деактивація середовища

```bash
deactivate
```

## Управління залежностями

### Встановлення пакетів

```bash
# Активуйте середовище
source my_env/bin/activate

# Встановіть необхідні пакети
pip install httpx
pip install requests
pip install Flask
```

### Заморожування залежностей

Для збереження списку встановлених пакетів:

```bash
pip freeze > requirements.txt
```

Це створить файл `requirements.txt` зі списком усіх пакетів та їх версій:

```text
aiohappyeyeballs==2.6.1
aiohttp==3.13.3
Flask==3.1.2
httpx==0.28.1
requests==2.32.5
...
```

### Встановлення з requirements.txt

```bash
pip install -r requirements.txt
```

## Робота з dev-залежностями

venv не має вбудованої підтримки dev-залежностей, тому прийнято створювати окремі файли:

- `requirements.txt` - продакшн залежності
- `requirements-dev.txt` - залежності для розробки

### requirements-dev.txt

```text
# Включаємо всі продакшн залежності
-r requirements.txt

# Додаємо dev інструменти
flake8==7.0.0
pytest==8.0.0
black==24.0.0
```

### Встановлення dev-залежностей

```bash
pip install -r requirements-dev.txt
```

## Приклад повного робочого процесу

### 1. Створення та активація середовища

```bash
cd 6_lab/1_venv
python -m venv my_env
source my_env/bin/activate
```

### 2. Встановлення пакетів

```bash
pip install httpx requests Flask jikanpy-v4
```

### 3. Збереження залежностей

```bash
pip freeze > requirements.txt
```

### 4. Встановлення dev-інструментів

```bash
pip install flake8
pip freeze > requirements-dev.txt
```

### 5. Перевірка встановлених пакетів

```bash
pip list
```

### 6. Робота в одну команду

```bash
# Створення середовища, активація та встановлення залежностей
python -m venv ./my_env && \
  source ./my_env/bin/activate && \
  pip install -r requirements.txt
```

## Перевірка коду з flake8

Після встановлення flake8:

```bash
cd 6_lab
flake8 ./app.py
```

flake8 перевірить код на відповідність стандартам PEP 8.

## Структура віртуального середовища

```
my_env/
├── bin/              # Виконавчі файли (на Linux/macOS)
│   ├── activate      # Скрипт активації
│   ├── python        # Символьне посилання на Python
│   ├── pip           # pip для цього середовища
│   └── ...
├── include/          # C заголовки
├── lib/              # Встановлені пакети
│   └── python3.13/
│       └── site-packages/
└── pyvenv.cfg        # Конфігурація середовища
```

## Видалення віртуального середовища

Просто видаліть папку:

```bash
rm -rf my_env
```

## Gitignore

Завжди додавайте віртуальні середовища до `.gitignore`:

```gitignore
# Virtual environments
venv/
env/
my_env/
.venv/
ENV/
```

## Коли використовувати venv

venv підходить для:

- ✅ Невеликих проектів
- ✅ Швидких прототипів
- ✅ Навчальних цілей
- ✅ Коли не потрібні складні залежності
- ✅ Коли хочете мінімальний набір інструментів

## Кращі практики

1. **Завжди використовуйте віртуальне середовище** для кожного проекту
2. **Зберігайте requirements.txt** у системі контролю версій
3. **Не коммітьте саме середовище** (додайте до .gitignore)
4. **Використовуйте точні версії** в requirements.txt для продакшну
5. **Оновлюйте requirements.txt** після встановлення нових пакетів
6. **Перевіряйте чисте встановлення** періодично:
   ```bash
   deactivate
   rm -rf my_env
   python -m venv my_env
   source my_env/bin/activate
   pip install -r requirements.txt
   ```

## Альтернативні команди

### Створення з системними пакетами

```bash
python -m venv --system-site-packages my_env
```

Це дозволить використовувати глобально встановлені пакети.

### Створення без pip

```bash
python -m venv --without-pip my_env
```

### Оновлення pip у середовищі

```bash
source my_env/bin/activate
pip install --upgrade pip
```

## Приклад app.py з нашого проекту

```python
import httpx
import requests
import os

# Використовуємо змінні середовища
u = os.getenv('URL_TEST')

# httpx запит
r = httpx.get(u)
print(f"httpx: {r} коли доступаємось до URL_TEST: {u}")

# requests запит
r = requests.get(u)
print(f"requests: {r} коли доступаємось до URL_TEST: {u}")
```

Для запуску:

```bash
export URL_TEST="https://httpbin.org/get"
source my_env/bin/activate
python app.py
```

## Висновки

venv - це чудовий вибір для початку роботи з віртуальними середовищами Python. Хоча він не має всіх функцій сучасних інструментів як Pipenv чи Poetry, його простота та вбудованість роблять його ідеальним для навчання та невеликих проектів.

Для більш складних проектів розгляньте використання [Pipenv](pipenv.md) або [Poetry](poetry.md).
