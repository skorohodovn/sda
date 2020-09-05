"""
Write a Python function to find the list of words
that are longer than n from a given list of words
Example input: find_gt_n(['a', 'be', 'cee'], 1)
Expected output: ['be', 'cee']
Example input: find_gt_n(['name', 'age', 'gender'], 4)
Expected output: ['gender']
"""

def find_gt_n(list,n):
    result_list = []
    for word in list:
        if(len(word) > n):
            result_list.append(word)

    return result_list

print(find_gt_n(['a', 'be', 'cee'], 1))

print(find_gt_n(['name', 'age', 'gender'], 4))
