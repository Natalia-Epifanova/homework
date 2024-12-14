import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Начало работы функции для маскировки номера карты")
    if not isinstance(card_number, str):
        logger.error("Ошибка типа данных")
        raise TypeError("Ошибка типа данных")

    if len(card_number) != 16:
        logger.error("Номер карты должен быть из 16 символов")
        raise ValueError("Номер карты должен быть из 16 символов")
    cards_mask = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger.info("Маскировка карты прошла успешно!")
    return cards_mask


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("Начало работы функции для маскировки номера счета")
    if not isinstance(account_number, str):
        logger.error("Ошибка типа данных")
        raise TypeError("Ошибка типа данных")

    if len(account_number) != 20:
        logger.error("Номер счета должен быть из 20 символов")
        raise ValueError("Номер счета должен быть из 20 символов")

    account_mask = "**" + account_number[-4:]
    logger.info("Маскировка карты прошла успешно!")
    return account_mask
