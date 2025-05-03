## Описание проекта
Проект представляет собой учебное задание по созданию виджета для отображения банковских операций клиента. Цель проекта — изучить основы работы с Git, Python и обработки данных.

В рамках задания реализованы функции для:
- Маскировки номеров карт и счетов.
- Преобразования дат из формата ISO в удобный для чтения формат `ДД.ММ.ГГГГ`.

## Структура проекта
```
/my-first-git-project-python/
├── .gitignore          # Файл для игнорирования системных и временных файлов
├── src/                # Папка с исходным кодом
│   ├── masks.py        # Модуль для маскировки номеров карт и счетов
│   └── processing.py   # Модуль для обработки данных
└── README.md           # Документация проекта
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
# Visa Platinum 7000 79**** **** 6361

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

## Тестирование

Проект включает набор тестов для проверки корректности работы всех функций. Тесты написаны с использованием библиотеки `pytest`.

### Запуск тестов
Для запуска тестов выполните следующую команду:
```bash
pytest
```

### Генерация отчета о покрытии кода
Для генерации отчета о покрытии кода используется плагин `pytest-cov`. Выполните команду:
```bash
pytest --cov=src --cov-report=html
```
Отчет будет сохранён в папке `htmlcov/`. Откройте файл `index.html`, чтобы просмотреть результаты.

### Требования к покрытию кода
Покрытие кода составляет не менее 80%. Если покрытие ниже, добавьте дополнительные тесты.

### Примеры тестов
Вот примеры тестов для функции `mask_account_card`:

```python
import pytest
from src.masks import mask_account_card

def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ]
)
def test_mask_account_card_parametrize(input_data: str, expected_output: str):
    assert mask_account_card(input_data) == expected_output
```

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

---

### **Что добавлено?**
1. **Раздел "Тестирование"**:
   - Описано, как запускать тесты.
   - Указано, как генерировать отчет о покрытии кода.
   - Приведены примеры тестов.

2. **Требования к покрытию кода**:
   - Указан минимальный порог покрытия (80%).

3. **Примеры тестов**:
   - Показаны примеры тестов для одной из функций, чтобы продемонстрировать подход к тестированию.