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
3. Установите необходимые зависимости (если они есть):
   ```bash
   pip install -r requirements.txt
   ```

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

## Автор
- **Имя**: Валерий Лысиков
- **Email**: lysikovvalera777@yandex.ru
- **GitHub**: [LValeriy777](https://github.com/LValeriy777)

## Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](http://www.opensource.org/licenses/mit-license.php).
```
