import pytest
from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state
def test_filter_by_state() -> None:
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}
    ]

    # Тест для EXECUTED
    assert filter_by_state(transactions) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    # Тест для CANCELED
    assert filter_by_state(transactions, state='CANCELED') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}]

# Тесты для sort_by_date
def test_sort_by_date() -> None:
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}
    ]

    # Тест для сортировки по убыванию
    assert sort_by_date(transactions, reverse=True) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'}
    ]
    # Тест для сортировки по возрастанию
    assert sort_by_date(transactions, reverse=False) == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.345678'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    
#Изменение для коммита
    