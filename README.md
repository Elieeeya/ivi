
# ivi12
## Тестирование API с использованием Python, pytest, requests, allure 

Этот проект предоставляет пример тестов для API с использованием языка Python, фреймворка pytest и библиотек requests, allure.
Для валидации JSON-ответов, мог бы использовать jsonschema, но мне нравится Pydantic.
Для нагрузки Locust.

## Установка

1. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Создайте файл `.env` в корневой директории проекта и добавьте в него переменные среды для аутентификации:

```
USERNAME=your_username
PASSWORD=your_password
```

## Запуск тестов

Чтобы запустить тесты, выполните следующую команду:

```bash
pytest -sv
```

Вы увидите вывод результатов тестов в консоли.

## Описание проекта

### Структура проекта

- `api_model` - модуль для работы с API.
- `api_methods.py` - класс `ApiMethods` для выполнения API-запросов.
- `api_assertions.py` - функции для проверки ответов от API.
- `tests` - папка с тестами.
- `api_tests.py` - тесты API с использованием библиотеки Allure.

### Использование Allure

В проекте используется библиотека Allure для создания информативных отчетов о выполнении тестов. Allure позволяет легко создавать шаги выполнения, прикреплять вложения и создавать красочные отчеты.

### Запуск тестов

Вы можете запустить тесты, выполнив команду `pytest`. Результаты тестов будут сохранены в директории `allure-results`. Для просмотра отчета в формате Allure выполните команду:

```bash
allure serve allure-results
```


## Описание тестов

- `test_successful_authentication`: Тест на успешную аутентификацию при запросе к API.
- `test_get_characters`: Тест на успешный GET запрос к `/characters`.
- `test_get_character_by_name`: Тест на успешный GET запрос к `/character` с указанием имени персонажа.
- `test_post_character`: Тест на успешный POST запрос к `/character`.
- `test_put_character`: Тест на успешный PUT запрос к `/character`.
- `test_delete_character_by_name`: Тест на успешный DELETE запрос к `/character` с указанием имени персонажа.
- `test_failed_delete_nonexistent_character`: Тест на неудачный DELETE запрос к `/character` с несуществующим именем персонажа.
- `test_reset_collection`: Тест на сброс коллекции в первоначальное состояние.

