from typing import Callable, Any
import pytest
from src.decorators import log

# Тестирование декоратора log
def test_log_decorator_with_file() -> None:
    """
    Тестирование декоратора с указанием файла.
    """
    @log(filename="test_log.txt")
    def test_func(a: int, b: int) -> int:
        return a + b

    test_func(1, 2)
    with open("test_log.txt", "r") as file:
        logs = file.readlines()
    assert len(logs) == 2
    assert "Function test_func started" in logs[0]
    assert "Function test_func finished successfully" in logs[1]

def test_log_decorator_without_file() -> None:
    """
    Тестирование декоратора без указания файла.
    """
    @log()
    def test_func(a: int, b: int) -> int:
        return a + b

    test_func(1, 2)
    # Здесь можно использовать фикстуру для проверки вывода в консоль
    # Например, pytest-capsys

def test_log_decorator_error() -> None:
    """
    Тестирование декоратора при возникновении ошибки.
    """
    @log(filename="error_log.txt")
    def test_func(a: int, b: int) -> int:
        return a / b

    with pytest.raises(ZeroDivisionError):
        test_func(1, 0)

    with open("error_log.txt", "r") as file:
        logs = file.readlines()
    assert len(logs) == 2
    assert "Function test_func started" in logs[0]
    assert "Function test_func failed with error: ZeroDivisionError" in logs[1]