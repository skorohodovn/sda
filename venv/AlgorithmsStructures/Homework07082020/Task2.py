#Task 2
#Write a recursive function that returns the index of an element in the list if it exists, otherwise returns -1.
# bad implementation that creates additional lists every time its called, but at least doesnt destroy the original
def return_index(list, a):
    list2 = list.copy()
    if list2.pop() == a: #we pop the LAST element of the list
        return len(list2) #if we manage to find the element it will be the last in the last and its position is the lenght of the list offset by 1
    elif len(list2) == 0:
        return -1
    return return_index(list2, a) #continue searching before the list is empty


list = [1,2,3,4,5]
a = 1
s = return_index(list, a)
print(s)


