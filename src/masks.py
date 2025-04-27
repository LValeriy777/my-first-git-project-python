def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    :param card_number: Строка с номером карты (16 цифр).
    :return: Строка с замаскированным номером карты.
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} **** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.

    :param account_number: Строка с номером счета (минимум 4 цифры).
    :return: Строка с замаскированным номером счета.
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать не менее 4 цифр")
    return f"**{account_number[-4:]}"
