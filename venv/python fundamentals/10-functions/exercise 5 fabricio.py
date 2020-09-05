"""
Write a function that, given a number n,
returns a dictionary containing all the squares from 1 to n (not from 0 to n-1) as values
Example input: squares(4)
Expected output: {1: 1, 2: 4, 3: 9, 4: 16}
"""

squares = {}

def squares(n):
    result = {}
    for i in range(1, n + 1):
        result[i] = i * i

    return result

print(squares(20))
