from functools import wraps
from time import sleep, time
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, позволяющий логировать работу функции в текстовый файл/консоль"""

    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None or filename == "":
                    print(f"{func.__name__} ok.")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} ok.\n")
                return result
            except Exception as er:
                if filename is None or filename == "":
                    print(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} error: {er}. Inputs: {args} {kwargs}\n")

        return wrapper

    return inner


def start_end_function(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print(f"The beginning of the function: {func.__name__}")
        func(*args, **kwargs)
        print(f"The end of the function: {func.__name__}")

    return wrapper


def timing(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        start_of_function = time()
        func(*args, **kwargs)
        sleep(1)
        end_of_function = time()
        print(f"Time execution: {end_of_function - start_of_function:.6f}")

    return wrapper


#
@timing
@start_end_function
@log()
def my_function(x: int | float, y: int | float) -> int | float:
    return x + y


my_function(1, 2)  # my_function ok
