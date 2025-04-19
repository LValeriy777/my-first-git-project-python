from typing import List, Dict


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указанному значению.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате ('date').

    :param transactions: Список словарей с транзакциями.
    :param reverse: Определяет порядок сортировки (True — убывание, False — возрастание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)
