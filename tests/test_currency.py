import pytest
from src.currency import convert_transaction_amount
from unittest.mock import patch

# Тестовые данные
valid_usd_transaction = {
    "amount": "100",
    "currency": {"code": "USD"}
}

valid_eur_transaction = {
    "amount": "50",
    "currency": {"code": "EUR"}
}

rub_transaction = {
    "amount": "200",
    "currency": {"code": "RUB"}
}

no_amount_transaction = {
    "currency": {"code": "USD"}
}

no_currency_transaction = {
    "amount": "100",
    "currency": {}
}

invalid_transaction = {
    "amount": None,
    "currency": {"code": "USD"}
}

empty_transaction: dict = {}  # Добавлена аннотация типа


def test_convert_transaction_amount_usd_to_rub() -> None:
    #Тестирует конвертацию USD в RUB.
    with patch("src.currency.convert_currency", return_value=90.0):
        result = convert_transaction_amount(valid_usd_transaction)
        assert result == 90.0

def test_convert_transaction_amount_eur_to_rub(mocker: pytest.MonkeyPatch) -> None:
    #Тестирует конвертацию EUR в RUB.
    with patch("src.currency.convert_currency", return_value=80.0):
        result = convert_transaction_amount(valid_eur_transaction)
        assert isinstance(result, float)
        assert result == 80.0


def test_convert_transaction_amount_rub_no_conversion() -> None:
    """
    Тестирует транзакцию в RUB — конвертация не требуется.
    """
    result = convert_transaction_amount(rub_transaction)
    assert result == 200.0


def test_convert_transaction_amount_missing_amount() -> None:
    """
    Тестирует случай, когда отсутствует amount.
    """
    result = convert_transaction_amount(no_amount_transaction)
    assert result is None


def test_convert_transaction_amount_missing_currency() -> None:
    """
    Тестирует случай, когда отсутствует currency.
    """
    result = convert_transaction_amount(no_currency_transaction)
    assert result is None


def test_convert_transaction_amount_invalid_data() -> None:
    """
    Тестирует случай, когда amount равен None.
    """
    result = convert_transaction_amount(invalid_transaction)
    assert result is None


def test_convert_transaction_amount_empty_dict() -> None:
    """
    Тестирует случай, когда передан пустой словарь.
    """
    result = convert_transaction_amount(empty_transaction)
    assert result is None
    