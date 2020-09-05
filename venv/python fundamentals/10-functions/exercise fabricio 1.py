"""
Write a function to count the number of strings
where the string length is 2 or more and the first and
last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

"""
def count_strings(list):
    i = len(list)-1
    result = 0
    while (i != 0):
        if(len(list[i]) >= 2):
            if (list[i][0] == list[i][len(list[i]-1)]):
                result += 1
        i = i - 1


count_strings(['abc', 'xyz', 'aba', '1221'])

"""

def count_str(list):
    result = 0
    for i in range(len(list)):
        if len(list[i]) >= 2:
            if list[i][0] == list[i][-1]:
                result += 1

    return print(result)


count_str(['abc', 'xyz', 'aba', '1221', 'agggggga', '4555554'])