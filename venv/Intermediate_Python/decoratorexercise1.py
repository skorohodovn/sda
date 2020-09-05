import random
import string
import functools

alphabet = string.ascii_letters + string.punctuation + string.digits

def lowercase_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.lower()
        return result
    return wrapper

class Shortener:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func()
        if len(result) > 40:
            result = result[0:39]
        return result



@Shortener
@lowercase_decorator
def random_string():
    length = random.randint(30, 60)
    population = []
    for _ in range(length):
        index = random.randint(0, len(alphabet) - 1)
        population.append(alphabet[index])
    return "".join(population)

print(random_string())
print(random_string())
print(random_string())
print(random_string())