import json
from typing import Any
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def financial_transactions(path: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    try:
        logger.info("Открываем JSON-файл со списком транзакций")
        with open(path, encoding="UTF-8") as json_file:
            transaction_data = json.load(json_file)
        logger.info("Список получен успешно! ")
        return transaction_data
    except json.JSONDecodeError as ex:
        print("Invalid JSON data.")
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except FileNotFoundError as ex:
        print("There is no such file")
        logger.error(f"Произошла ошибка: {ex}")
        return []
