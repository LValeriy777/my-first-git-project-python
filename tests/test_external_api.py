import pytest
from src.external_api import convert_currency
from unittest.mock import patch
import requests


def test_convert_currency_success() -> None:
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"rates": {"RUB": 70.0}}
        result = convert_currency(100, "USD", "RUB")
        assert result == 7000.0

def test_convert_currency_same_currency() -> None:
    result = convert_currency(100, "RUB", "RUB")
    assert result == 100

def test_convert_currency_failure() -> None:
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException
        result = convert_currency(100, "USD", "RUB")
        assert result is None
        