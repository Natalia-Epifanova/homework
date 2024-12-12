from typing import Any, Dict, List, Hashable

import pandas as pd


def reading_csv(path_to_csv: str) -> List[Dict[Hashable, Any]]:
    """Функция для считывания финансовых операций из CSV файла"""
    if not isinstance(path_to_csv, str):
        raise TypeError("Неправильный формат пути к файлу")
    try:
        csv_file_df = pd.read_csv(path_to_csv, delimiter=";")
        csv_reader = csv_file_df.to_dict(orient="records")
        return csv_reader
    except FileNotFoundError:
        return []


def reading_excel(path_to_excel: str) -> List[Dict[Hashable, Any]]:
    """Функция для считывания финансовых операций из CSV файла"""
    if not isinstance(path_to_excel, str):
        raise TypeError("Неправильный формат пути к файлу")
    try:
        excel_file_df = pd.read_excel(path_to_excel)
        excel_reader = excel_file_df.to_dict(orient="records")
        return excel_reader
    except FileNotFoundError:
        return []


# if __name__ == '__main__':
#     result = reading_csv('../data/transactions.csv')
#     print(result)
#     # result = reading_excel('../data/transactions_excel.xlsx')
#     # print(result)
