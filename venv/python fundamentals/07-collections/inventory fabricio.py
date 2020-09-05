inventory = {
    'bag': [],
    'cap': 5
}

print(inventory.get('bag'))

print(inventory.get('cap'))

print(inventory.get('armor'))

print(inventory.get('armor', {'defense' : 0}))