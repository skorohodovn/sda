"""
Write a function to check whether two lists are circularly identical
Example input: check_circular_lists([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
Expected output: True
Example input: check_circular_lists([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
Expected output: False
"""

def check_circular_lists(l1,l2):
    l1len = len(l1) #circurly identical lists would always be the same size
    l1.extend(l1) #by extending we get the actual sequence of elements in line, as in: [3, 4, 5, 1, 2] becomes [3, 4, 5, 1, 2, 3, 4, 5, 1, 2], where the 1,2,3,4,5 is clearly visible in the center
    l2.extend(l2)
    count = 0 #will be searching for matches and these should be the amount equal to len(l1) or the length of the first list
    for i in range(0,len(l1),1):#loop through list 1 items
        count = 0
        for j in range(0,len(l2),1):#loop through list 2 items
            if l1[i] == l2[j]:
                    for k in range(0,min(len(l2)-j,len(l1)-i),1):#loop the nextt items in the SECOND list after the first element that equals to the one in list one is found in list 2
                        if l1[i+k] == l2[j+k]:#if the items in list 2 is found equals to the one currently the loop has in list 1, then look if the next, neighbouring itms in borth list 1  l1[i+k] and list 2  l2[j+k] are also the same
                            print(f'values are:the i value is {i+k} and the j is {j+k}, list one value is {l1[i+k]}, list 2 value is {l2[j+k]} and count {count}')
                            count += 1
                        if count == l1len:
                            print("True")
                            return
    print("False")

check_circular_lists([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
check_circular_lists([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
check_circular_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 1, 2])