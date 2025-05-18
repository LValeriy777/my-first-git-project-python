## Описание проекта
Проект представляет собой учебное задание по созданию виджета для отображения банковских операций клиента. Цель проекта — изучить основы работы с Git, Python и обработки данных.

В рамках задания реализованы функции для:
- Маскировки номеров карт и счетов.
- Преобразования дат из формата ISO в удобный для чтения формат `ДД.ММ.ГГГГ`.
- Генерации номеров банковских карт и фильтрации транзакций по валюте.
  
## Структура проекта
```
/my-first-git-project-python/
├── .gitignore # Файл для игнорирования системных и временных файлов
├── src/ # Папка с исходным кодом
│ ├── masks.py # Модуль для маскировки номеров карт и счетов
│ ├── processing.py # Модуль для обработки данных
│ └── generators.py # Модуль с генераторами для работы с транзакциями
├── tests/ # Папка с тестами
│ ├── test_masks.py # Тесты для модуля masks.py
│ ├── test_processing.py # Тесты для модуля processing.py
│ └── test_generators.py # Тесты для модуля generators.py
└── README.md # Документация проекта
```

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/LValeriy777/my-first-git-project-python.git
   ```
2. Перейдите в папку проекта:
   ```bash
   cd my-first-git-project-python
   ```

> **Примечание:** Для выполнения задания установка дополнительных зависимостей не требуется.

## Использование

### Функция `mask_account_card`
Функция маскирует номер карты или счета.

#### Пример использования:
```python
from src.masks import mask_account_card

# Пример для карты
card_number = "Visa Platinum 7000792289606361"
masked_card = mask_account_card(card_number)
print(masked_card)
# Visa Platinum 7000 79** **** 6361

# Пример для счета
account_number = "Счет 73654108430135874305"
masked_account = mask_account_card(account_number)
print(masked_account)
# Счет **4305
```

### Функция `get_date`
Функция преобразует дату из формата ISO в формат `ДД.ММ.ГГГГ`.

#### Пример использования:
```python
from src.masks import get_date

date_iso = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_iso)
print(formatted_date)
# 11.03.2024
```

### Функция `filter_by_state`
Функция фильтрует список словарей по значению ключа `state`.

#### Пример использования:
```python
from src.processing import filter_by_state

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}
]

filtered_transactions = filter_by_state(transactions, state='EXECUTED')
print(filtered_transactions)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

### Функция `sort_by_date`
Функция сортирует список словарей по дате (`date`).

#### Пример использования:
```python
from src.processing import sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}
]

sorted_transactions = sort_by_date(transactions, reverse=False)
print(sorted_transactions)
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

## Новый модуль: generators

Модуль `generators` содержит функции-генераторы для работы с массивами транзакций.

### Примеры использования

#### `filter_by_currency`
Фильтрует транзакции по указанной валюте.

```python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
```

#### `transaction_descriptions`
Возвращает описание каждой транзакции.

```python
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```

#### `card_number_generator`
Генерирует номера банковских карт.

```python
for card_number in card_number_generator(1000, 9999):
    print(card_number)
```

## Тестирование

Проект включает набор тестов для проверки корректности работы всех функций. Тесты написаны с использованием библиотеки `pytest`.

### Запуск тестов
Для запуска тестов выполните следующую команду:
```bash
pytest
```
## Новый модуль: decorators

Модуль `decorators` содержит декораторы для логирования работы функций.

### Пример использования декоратора `log`

#### Логирование в файл
```python
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y
```

#### Логирование в консоль
```python
my_function(1, 2)

@log()
def my_function(x, y):
    return x + y
```

#### Логирование при ошибке
```python
my_function(1, 2)

@log(filename="error_log.txt")
def my_function(x, y):
    return x / y

try:
    my_function(1, 0)
except ZeroDivisionError:
    pass
```

---

### Генерация отчета о покрытии кода
Для генерации отчета о покрытии кода используется плагин `pytest-cov`. Выполните команду:
```bash
pytest --cov=src --cov-report=html
```
Отчет будет сохранён в папке `htmlcov/`. Откройте файл `index.html`, чтобы просмотреть результаты.

### Требования к покрытию кода
Покрытие кода составляет не менее 80%. Если покрытие ниже, добавьте дополнительные тесты.

## Линтеры и форматеры
Для проверки и форматирования кода используйте следующие инструменты:
- `flake8` для проверки стиля кода.
- `mypy` для проверки типов.
- `isort` для форматирования импортов.

Пример команд:
```bash
flake8 src/
mypy src/
isort src/
```

## Автор
- **Имя**: Валерий Лысиков
- **Email**: lysikovvalera777@yandex.ru
- **GitHub**: [LValeriy777](https://github.com/LValeriy777)

## Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](http://www.opensource.org/licenses/mit-license.php).
```

### **Что изменено?**
1. **Добавлен раздел "Новый модуль: generators"**:
   - Описаны новые функции-генераторы: `filter_by_currency`, `transaction_descriptions` и `card_number_generator`.
   - Приведены примеры использования.

2. **Расширен раздел "Тестирование"**:
   - Уточнены команды для запуска тестов и генерации отчета о покрытии кода.

3. **Структура проекта обновлена**:
   - Добавлен новый модуль `generators.py` и соответствующий файл тестов `test_generators.py`.

4. **Оформление улучшено**:
   - Добавлены примеры использования для всех функций.
   - Указаны требования к покрытию кода (не менее 80%).
