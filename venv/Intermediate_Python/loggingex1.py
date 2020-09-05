"""
Given file exercise-01.py
    1. Convert all calls to `print()` to proper logging
    2. configure logging to log simultaneously to two files and console, using the following formats and levels:
        1. File A: `timestamp - level - message` level DEBUG
        2. File B: `filename - funcname - line number` level INFO
        3. Console: `asctime [level]: message` level WARN
"""

import time
import random
import functools
import logging


def decorate(func):
    def wrapper(*args, **kwargs):
        l = logging.getLogger()
        l.info("calling a function")
        return func(*args, *kwargs)

    return wrapper


@decorate
def complex_calculation(a, b):
    print("DEBUG: performing complex calculation")
    result = a + b
    print(f"DEBUG: result={result}")
    return result


if __name__ == "__main__":
    l = logging.getLogger()
    file_handle1 = logging.FileHandler("loggerA.log","w+")
    file_handle1.setLevel(logging.DEBUG)
    file_handle1.setFormatter(logging.Formatter("%(asctime) in %(filename)s - %(message)s"))
    l.addHandler(file_handle1)

    file_handle2 = logging.FileHandler("loggerB.log", "w+")
    file_handle2.setLevel(logging.INFO)
    file_handle2.setFormatter("(filename - %(levelname)s - %(lineno)s")
    l.addHandler(file_handle2)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARN)
    console_handler.setFormatter(logging.Formatter(("%(asctime)s %(filename)s: %(message)s")))
    l.addHandler(console_handler)

    for _ in range(10):
        result = complex_calculation(random.randint(0, 15), random.randint(0, 15))
        if result <= 10:
            l.warning("a warning")
        elif result <= 20:
            l.error("an error")
        elif result <= 30:
            l.critical("a critical error")
