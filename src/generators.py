from typing import Iterator, List, Dict
import random

def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по указанной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты (например, "USD").
    :return: Итератор, возвращающий транзакции с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор, возвращающий описание каждой транзакции.
    """
    for transaction in transactions:
        description = transaction.get('description', 'Неизвестная операция')
        yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :return: Итератор, возвращающий номера карт.
    :raises ValueError: Если диапазон некорректный (меньше 1000 или больше 9999).
    """
    if start < 1000 or stop > 9999:
        raise ValueError("Диапазон должен быть в пределах [1000, 9999]")
    
    while True:
        # Генерируем 4 группы по 4 цифры
        card_number_parts = [f"{random.randint(start, stop):04}" for _ in range(4)]
        yield ' '.join(card_number_parts)
        