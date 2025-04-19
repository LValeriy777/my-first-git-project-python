def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указанному значению.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]
