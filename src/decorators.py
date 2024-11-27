import os
from functools import wraps


def log(filename):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None or filename == "":
                    print(
                        f"{func.__name__} ok."
                    )
                else:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(
                            f"{func.__name__} ok.\n"
                        )
                return result
            except Exception as er:
                if filename is None or filename == "":
                    print(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}")
                else:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}\n")
        return wrapper

    return inner

#
# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x + y


# my_function(1, 2)  # my_function ok

