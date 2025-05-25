from typing import Dict, Optional
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest "

def convert_currency(amount: float, from_currency: str, to_currency: str) -> Optional[float]:
    """
    Конвертирует сумму из одной валюты в другую.

    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта (например, 'USD' или 'EUR').
    :param to_currency: Целевая валюта (например, 'RUB').
    :return: Конвертированная сумма в целевой валюте или None при ошибке.
    """
    if from_currency == to_currency:
        return amount

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(f"{BASE_URL}?base={from_currency}&symbols={to_currency}", headers=headers)
        response.raise_for_status()
        data = response.json()
        rate: Optional[float] = data.get("rates", {}).get(to_currency)
        if rate is None:
            return None
        return amount * float(rate)
    except requests.RequestException:
        return None
    