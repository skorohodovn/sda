# Task 1
# Write a recursive function that calculates a to the power of b (a^b).

def power(a, b):
    if b == 0:
        return 1 # any number to the power of 0 is 1
    elif b < 0:
        return 1/a * (power(a,b+1)) # if b is negative - increase b until it is zero
    return a * (power(a,b-1)) #decrease b until it is zero


p = power(2, -10)
print(p)
p = power(2, 10)
print(p)
p = power(2, 0)
print(p)