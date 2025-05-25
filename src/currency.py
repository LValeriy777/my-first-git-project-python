from typing import Dict, Optional
from src.external_api import convert_currency

def convert_transaction_amount(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Конвертированная сумма в рублях или None при ошибке.
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency", {}).get("code")

    if not amount or not currency:
        return None

    if currency == "RUB":
        return float(amount)

    rub_rate = convert_currency(float(amount), currency, "RUB")
    return rub_rate
