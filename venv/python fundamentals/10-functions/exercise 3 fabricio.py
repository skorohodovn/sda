"""
Write a function that takes a list
and return a new list without the 3rd, 5th, and 6th elements
Example input: remove_3_5_6(['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN'])
Expected output: ['RED', 'GREEN', 'BLUE']
"""

def remove_3_5_6(list):
    new_list = list[0:]
    new_list.pop(5)
    new_list.pop(4)
    new_list.pop(2)
    return new_list


print(remove_3_5_6(['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN']))
