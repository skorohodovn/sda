my_list = [1, 2, 3, 4, 5]

print(list)
print(f"The length is {len(list)}")

list.append(2)
print(list)

print(f"The amount of 2s in the list is {list.count(2)}")

print(f"The amount of 7s in the list is {list.count(7)}")

list.extend([6,7,8])

print(list)

print(list.index(7))
print(f"It is indeed on the position of {list[7]}")

list.insert(0,10)
print(list)
print(f"The last one in the lsit is {list[-1]}")

print(f"The last element in the list using pop is {list.pop()}")

list.remove(4)
print(list)

list.reverse()
print(list)

list.sort()

print(list)

list.clear()
print(list)

