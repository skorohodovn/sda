def get_discount(price, percentage=0):
    multiplier = 1 - percentage
    return price * multiplier

print(get_discount(200))

print(get_discount(200,0.2))

