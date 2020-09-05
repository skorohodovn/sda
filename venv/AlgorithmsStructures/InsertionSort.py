def insertion_sort(l):
    for i in range(1,len(l)):
        temp = l[i]
        print(temp)
        j = i
        while l[j-1] > temp and j > 0:
            l[j] = l[j-1]
            j = j- 1
        l[j] = temp
        print(f"lj: {l[j]}")
    return l

l = [5, 3, 7, 1, 4, 4, 2, 10]
insertion_sort(l)
print(f"Sorted list: {l}")