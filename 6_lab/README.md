# Замороження залежностей проекту в requirements.txt та створення віртуального середовища для встановлення цих залежностей.
```bash
pip freeze > requirements.txt
python -m venv ./my_env && source ./my_env/bin/activate && pip install -r requirements.txt
```