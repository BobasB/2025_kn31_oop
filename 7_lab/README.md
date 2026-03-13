# Лабораторная работа 7. AI Агенти з Google ADK

- створення проекту (памятайте про невеликі конфігураційні зміни в `pyproject.toml` для роботи з ADK)
```bash
poetry init
poetry install
eval $(poetry env activate)
```

- робота з ADK
```bash
adk --help
adk create bobbi
adk run bobbi
adk web --port 8000
deactivate
```

- наступна пара, продовжеємо з агентами з інструментами
