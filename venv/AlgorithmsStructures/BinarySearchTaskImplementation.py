def search(list, element):
    middle_number = (len(list) // 2)
    if(list[middle_number]) == element:
        return middle_number
    elif(list[middle_number] < element):
        return search(list[((len(list)//2)):], element)
    elif(list[middle_number] > element):
        return search(list[:((len(list)//2))], element)

print(search([1,3,3,3,6,7,8,9, 10],8))