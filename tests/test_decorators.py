from cgitb import reset

from src.decorators import log

import pytest


@log(filename='')
def add_function(x, y):
    return x + y


def test_log():
    result = add_function(1, 2)
    assert result == 3


def test_decorator_log_console(capsys):
    add_function(1, 2)
    result = capsys.readouterr()
    assert result.out == "add_function ok.\n"

    add_function(1, "2")
    result = capsys.readouterr()
    assert result.out == "add_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2') {}\n"


def test_decorator_log_file():
    @log(filename="./src/logs/mylog.txt")
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    with open('./src/logs/mylog.txt', 'r', encoding='utf-8') as log_file:
        content = log_file.readlines()[-1]

    assert content == "my_function ok.\n"

    my_function('1', 2)
    with open('./src/logs/mylog.txt', 'r', encoding='utf-8') as log_file:
        content = log_file.readlines()[-1]

    assert content == '''my_function error: can only concatenate str (not "int") to str. Inputs: ('1', 2) {}\n'''
