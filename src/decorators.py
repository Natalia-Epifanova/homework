from functools import wraps
from time import time


def log(filename):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_of_start = time()
                result = func(*args, **kwargs)
                time_of_end = time()
                if filename is None or filename == "":
                    print(
                        f"{func.__name__} ok.\nРезультат выполнения функции: {result}.\n"
                        f"Время выполнения функции:{time_of_end - time_of_start:.6f}"
                    )
                else:
                    with open(filename, "w", encoding="UTF8") as log_file:
                        log_file.write(
                            f"{func.__name__} ok.\nРезультат выполнения функции: {result}.\n"
                            f"Время выполнения функции:{time_of_end - time_of_start:.6f}"
                        )
            except Exception as er:
                if filename is None or filename == "":
                    print(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}")
                else:
                    with open(filename, "w", encoding="UTF8") as log_file:
                        log_file.write(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}")

        return wrapper

    return inner


@log(filename="logs/mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)  # my_function ok
