def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета.

    :param account_info: Строка с типом и номером карты/счета.
    :return: Строка с замаскированным номером.
    """
    parts = account_info.split()
    if "Счет" in account_info:
        # Маскируем номер счета
        number = parts[-1]
        masked_number = f"**{number[-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number
    else:
        # Маскируем номер карты
        number = parts[-1]
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number
