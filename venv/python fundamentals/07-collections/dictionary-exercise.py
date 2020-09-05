dictionary = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(len(dictionary))
dictionary[4] = 'four'
print(dictionary)
print(dictionary.get(2))
print(dictionary.get(10))
print(dictionary.get(10),'unknown')
print(dictionary.get(3,'unknown'))
dictionary.pop(2)
print(dictionary)
dictionary2 = {
    0: 'zero'
}
dictionary.update({0: 'zero', 1: '1'}, )
print(dictionary)
dictionary2.clear()