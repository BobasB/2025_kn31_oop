# Замороження залежностей проекту в requirements.txt та створення віртуального середовища для встановлення цих залежностей.
```bash
pip freeze > requirements.txt
python -m venv ./my_env && source ./my_env/bin/activate && pip install -r requirements.txt

pip install flake8
cd 6_lab
flake8 ./app.py

pip freeze > requirements-dev.txt
pip install -r requirements.txt && pip install -r requirements-dev.txt
pip list


pipenv --python 3.13
pipenv install
pipenv graph
```

## додамо dev залежності
```bash
pipenv install --dev flake8
pipenv graph
```

### перестворення середовища
```bash
cd 6_lab
pipenv --rm
export PIPENV_VENV_IN_PROJECT=1

pipenv install
pipenv check --scan
```

### Змінні середовища
```bash
export TEST=1
python app.py
```

## Робота з poetry
```bash
cd 6_lab/3_poetry
poetry init
poetry add httpx requests

eval $(poetry env activate)
deactivate

```

## Робимо секції в pyproject.toml
```bash
poetry add flake8 --dev
poetry add --group docs mkdocs

poetry install --only docs
evel $(poetry env activate)
mkdocs serve
deactivate
```
> попросили АІ заповнити документацію, все зроблено в папці 3_poetry/docs

# Доробляєте звід до роботи самостійно