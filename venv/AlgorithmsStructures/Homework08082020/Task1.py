# Task 1
# Implement a search function that returns you a list of all indexes of occurrences of the searched element in a list.

def search(list, element):
    result = []
    for x in range(0,len(list)):
        if list[x] == element:
            result.append(x)
    if len(result) == 0:
        return -1
    else:
        return []

print(search([9,1,2,3,4,9,5,6,7,8,9,9],9))
print(search([9,1,2,3,4,9,5,6,7,8,9,9],-11))
