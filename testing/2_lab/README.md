# Команди

```
cd testing/2_lab
pwd
ll
poetry new .
poetry install
poetry add --dev pytest
poetry add --doc mkdocs
poetry add --group doc mkdocs
poetry install --with dev

poetry run python -m unittest -v

poetry run pytest
```

## Мітки тестів

Тести позначені як `unit` і додатково згруповані за темою: `score_validation`,
`grade_book` або `lab_module_one`. Мітка `fixtures` відрізняє тести, що
використовують pytest-фікстури, а `smoke` позначає базову перевірку запуску
тестів. Існуюча мітка `main_testing` збережена для прикладу основного тесту.

Для відбору тестів за кількома мітками використовуйте `or` та `and` у виразі
параметра `-m`:

```sh
# OR: запустити тести з міткою grade_book АБО lab_module_one
poetry run pytest -m "grade_book or lab_module_one"

# AND: запустити лише тести, позначені одночасно unit І fixtures
poetry run pytest -m "unit and fixtures"

# Одна мітка: запустити всі тести категорії grade_book
poetry run pytest -m grade_book
```

`or` включає тести, що відповідають хоча б одній умові; `and` — лише ті,
що відповідають обом умовам.
