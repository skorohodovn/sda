# Task 3
# Try to think of a procedure for sorting a list and write code for it. Don’t google any sorting algorithms nor use python provided function sort.


def sort_list(list):
    orig_list = list.copy() #copy the list provided to a temporary list
    list.clear() #clear the original list of all elements to rewrite it with the sorted ones
    for x in range (0, len(orig_list)): #loop through the original list
        min_value = min(orig_list)
        list.append(orig_list.pop(orig_list.index(min_value))) #take the smallest element with MIN(list), remove it from the original list, add the smallest one by one, one after the other

list = [5,4,6,1,11,0,55,5,5,3,9,7]
print(list)
sort_list(list)
print(list)


