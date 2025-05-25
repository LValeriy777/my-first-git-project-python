import logging
from functools import wraps
from typing import Callable, Any, Optional

def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования работы функции.

    :param filename: Имя файла для записи логов. Если None, логи выводятся в консоль.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Настройка логгера
            logger = logging.getLogger(func.__name__)
            logger.handlers.clear()  # Очистка предыдущих обработчиков
            handler: logging.Handler
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

            # Логирование начала выполнения функции
            logger.info(f"Function {func.__name__} started with args: {args}, kwargs: {kwargs}")

            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Логирование результата
                logger.info(f"Function {func.__name__} finished successfully. Result: {result}")
                return result
            except Exception as e:
                # Логирование ошибки
                logger.error(f"Function {func.__name__} failed with error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                # Удаление хендлера после использования
                logger.removeHandler(handler)

        return wrapper

    return decorator
