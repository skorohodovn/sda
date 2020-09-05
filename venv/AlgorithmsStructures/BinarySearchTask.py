def search(list, element):
    result = []
    for x in range(0,len(list)):
        if list[x] == element:
            result.append(x)
    if len(result) == 0:
        return -1
    else:
        return result

print(search([1,2,3,4,5,6,7,8,9,9],9))
