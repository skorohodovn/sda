def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        break
    return (fibonacci(n-1) + fibonacci(n-2))

result = fibonacci(-1)

print(result)