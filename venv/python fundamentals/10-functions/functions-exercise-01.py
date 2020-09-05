def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    return b if b > a and b > c else c

print(max_of_three(1,2,3))
print(max_of_three(4,2,3))
print(max_of_three(3,2,3))
print(max_of_three(2,1,3))