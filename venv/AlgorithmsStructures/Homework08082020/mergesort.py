# Implement merge_sort (adjust the existing one) to use indexes that
# determine which part of array/list is used, rather than sending a slice of the arry/list.

def merge_sort(l):
    if len(l) < 2:
        return l
    middle = len(l) // 2
    left = l[0:middle - 1]
    right = l[middle:len(l)-1]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    left_i = 0
    right_i = 0
    result = []
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result


l = [5, 3, 7, 1, 4, 4, 2, 10]
l = merge_sort(l)
print(f"Sorted list: {l}")
