"""
Write a function that takes a list of positive integers
and removes all even numbers from it; don't return anything
Example input, where l = [1,2,3,4,5,6,7,8,9,10]: remove_evens(l)
Expected output for print(l): [1,3,5,7,9]
"""

def remove_events(l):
    for i in range(len(l)-1,-1,-1):
        if(l[i])%2 == 0:
            l.pop(i)

l = [1,2,3,4,5,6,7,8,9,10,2,3]

remove_events(l)

print(l)

"""
def del_postive_integers(list):
    for i in range(len(list)-1, -1, -1):
        if list[i] % 2 == 0:
            list.pop(i)
    return list
print(del_postive_integers([1,2,3,4,5,6,7,8,9,10,2,3]))
"""

