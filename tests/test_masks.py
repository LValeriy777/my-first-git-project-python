import pytest 
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from typing import List, Dict


# Тест для get_mask_card_number
def test_get_mask_card_number() -> None:
    # Тест корректного формата
    assert get_mask_card_number("1234567812345678") == "1234 **** **** 5678"

    # Тест на недопустимую длину
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("123456781234567")

# Тест для get_mask_account
def test_get_mask_account() -> None:
    # Тест корректного формата
    assert get_mask_account("123456789012345678") == "**5678"

    # Тест на недопустимую длину
    with pytest.raises(ValueError, match="Номер счета должен содержать не менее 4 цифр"):
        get_mask_account("123")

# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ]
)
def test_mask_account_card_parametrize(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output

def test_mask_account_card() -> None:
    # Тест для карты
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    # Тест для счёта
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

# Тесты для get_date
def test_get_date() -> None:
    # Тест для корректной даты
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    # Тест для некорректной даты (ожидается исключение)
    with pytest.raises(ValueError):
        get_date("invalid-date")
        
# Фикстура для генерации тестовых данных
@pytest.fixture
def sample_account_data() -> list[str]:
    return [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Visa Classic 6831982476737658",
        "Visa Gold 5999414228426353",
    ]

# Тест с использованием фикстуры
def test_mask_account_card_with_fixture(sample_account_data: list[str]) -> None:
    expected_results = [
        "Visa Platinum 7000 79** **** 6361",
        "Счет **4305",
        "Maestro 1596 83** **** 5199",
        "MasterCard 7158 30** **** 6758",
        "Visa Classic 6831 98** **** 7658",
        "Visa Gold 5999 41** **** 6353",
    ]
    for account, expected in zip(sample_account_data, expected_results):
        assert mask_account_card(account) == expected
        