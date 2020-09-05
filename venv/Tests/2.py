from timeit import timeit

code = """
from time import sleep

def method():
 sleep(1)

 method()
"""


print(timeit(code, number=1))