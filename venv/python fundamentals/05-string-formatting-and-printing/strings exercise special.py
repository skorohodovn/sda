string = '0123456789'
len_string = len(string)
mid = len_string // 2
start = mid - 2
stop = mid + 2
stop += len_string % 2

print(string[start:stop])