"""
Write a function to check whether two lists are circularly identical
Example input: check_circular_lists([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
Expected output: True
Example input: check_circular_lists([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
Expected output: False
"""


def check_circular_lists(l1,l2):
    result = []
    result = l1[-2::-1]
    print(result)



check_circular_lists([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
check_circular_lists([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
check_circular_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 1, 2])