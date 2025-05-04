import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from typing import List, Dict, Any

# Фикстура для тестовых данных транзакций
@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Пополнение счета",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321"
        },
        {
            "id": 987654321,
            "state": "CANCELED",
            "date": "2021-05-15T18:30:00.000000",
            "operationAmount": {
                "amount": "500.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Отмена операции",
            "from": "Счет 98765432109876543210",
            "to": "Счет 01234567890123456789"
        }
    ]

# Тесты для filter_by_currency
def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    for tx in usd_transactions:
        assert tx["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_empty_list(transactions: List[Dict[str, Any]]) -> None:
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0

# Тесты для transaction_descriptions
def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == len(transactions)
    assert all(isinstance(desc, str) for desc in descriptions)
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Пополнение счета"
    assert descriptions[2] == "Отмена операции"

def test_transaction_descriptions_empty_list(transactions: List[Dict[str, Any]]) -> None:
    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0

# Тесты для card_number_generator
def test_card_number_generator() -> None:
    generator = card_number_generator(1000, 9999)
    numbers = [next(generator) for _ in range(5)]
    assert len(numbers) == 5
    for number in numbers:
        parts = number.split()
        assert len(parts) == 4
        assert all(len(part) == 4 for part in parts)
        assert all(part.isdigit() for part in parts)

def test_card_number_generator_invalid_range() -> None:
    generator = card_number_generator(0, 999)
    with pytest.raises(ValueError):
        next(generator)

#Изменение для коммита
        