import math
import time
import functools


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        before = time.time()
        result = self.func(*args, **kwargs)
        after = time.time()
        print(f"spent {after - before} sec")
        return result


@Timer
def power(x, y):
    for _ in range(1_000_000):
        result = math.pow(x, y)
    return result

power(3, 100)