from datetime import datetime


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


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    :param date_str: Строка с датой в формате ISO (например, "2024-03-11T02:26:18.671407").
    :return: Строка с датой в формате ДД.ММ.ГГГГ.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
