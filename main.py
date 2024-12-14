from typing import List, Dict, Any

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_csv_excel import reading_csv, reading_excel
from src.search import search_by_string
from src.utils import financial_transactions
from src.widget import get_date, mask_account_card


def choose_file() -> Any:
    """Функция позволяет пользователю открыть любой из 3 файлов (JSON, CSV, EXCEL)"""
    while True:
        answer = int(input("Поле для ввода: "))
        if answer == 1:
            list_with_data = financial_transactions("data/operations.json")
            print("Для обработки выбран JSON-файл.")
            break
        elif answer == 2:
            list_with_data = reading_csv("data/transactions.csv")
            print("Для обработки выбран CSV-файл.")
            break
        elif answer == 3:
            list_with_data = reading_excel("data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Такого пункта в меню нет. Попробуйте снова")
    return list_with_data


def choose_status(list_with_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция позволяет пользователю отфильтровать транзакции по одному из доступных статусов"""
    while True:
        answer = input("Поле для ввода: ")
        if answer.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            counter = 0
            for element in list_with_data:
                if element.get("state") == answer.upper():
                    counter += 1

            if counter != 0:
                filtered_dict_with_data = filter_by_state(list_with_data, answer.upper())
                print(f'Операции отфильтрованы по статусу "{answer.upper()}"')
                return filtered_dict_with_data

            else:
                print(
                    f"Операции со статусом {answer.upper()} отсутствуют в списке транзакций. "
                    f"Попробуйте поиск по другому статусу"
                )
        else:
            print(f'Статус операции "{answer}" недоступен.')


def choose_sort(list_with_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция предлагает пользователю отсортировать транзакции по дате"""
    while True:
        answer = input("Поле для ввода: ")
        if answer.lower() == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            new_user_answer = input()
            if new_user_answer.lower() == "по возрастанию":
                update_data = sort_by_date(list_with_data, False)
                return update_data
            elif new_user_answer.lower() == "по убыванию":
                update_data = sort_by_date(list_with_data)
                return update_data
            else:
                print("Неверный тип входных данных. Попробуйте снова. Отсортировать операции по дате? Да/Нет")

        elif answer.lower() == "нет":
            return list_with_data
        else:
            print("Неверный тип входных данных. Попробуйте снова")


def choose_rub_currency(list_with_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция позволяет пользователю оставить только рублевые транзакции"""
    while True:
        answer = input("Поле для ввода: ")
        update_data:List[Dict[str, Any]] = []
        if answer.lower() == "да":
            for value in filter_by_currency(list_with_data, "RUB"):
                update_data.append(value)
            return update_data
        elif answer.lower() == "нет":
            return list_with_data
        else:
            print("Неверный тип входных данных. Попробуйте снова")


def choose_string_for_search(list_with_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция предлагает пользователю отфильтровать транзакции по нужному слову"""
    while True:
        answer = input("Поле для ввода: ")
        if answer.lower() == "да":
            answer_2 = str(input("Введите слово для фильтрации: "))

            final_data = search_by_string(list_with_data, answer_2)

            return final_data
        elif answer.lower() == "нет":
            return list_with_data
        else:
            print("Неверный тип входных данных. Попробуйте снова")


def final_printing(list_with_data: List[Dict[str, Any]]) -> None:
    """Функция выводит получившийся список транзакций"""
    if len(list_with_data) != 0:
        for data in list_with_data:
            print(f'{get_date(data["date"])} {data["description"]}')

            try:
                print(f'{mask_account_card(str(data.get("from")))} -> {mask_account_card(str(data.get("to")))}')
            except TypeError:
                print(f'{mask_account_card(str(data.get("to")))}')
            if "operationAmount" in data:
                print(
                    f'Сумма: {data.get("operationAmount").get("amount")} {data.get("operationAmount").get("currency").get("name")}\n'
                )
            else:
                print(f'Сумма: {data.get("amount")} {data.get("currency_code")}\n')
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    """Функция отвечает за логику проекта и связывает все функциональности между собой"""

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    list_of_data = choose_file()

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    list_of_data_2 = choose_status(list_of_data)

    print("Отсортировать операции по дате? Да/Нет")
    list_of_data_3 = choose_sort(list_of_data_2)

    print("Выводить только рублевые транзакции? Да/Нет")
    list_of_data_4 = choose_rub_currency(list_of_data_3)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    list_of_data_5 = choose_string_for_search(list_of_data_4)

    print("Распечатываю итоговый список транзакций...")

    print(f"Всего банковских операций в выборке: {len(list_of_data_5)}")

    final_printing(list_of_data_5)


if __name__ == "__main__":
    main()
