list_1 = [1, 2, 3, 4, 5]
list[2] = list[4]
list[4] = 55
print(list[2])
list[2] = 33
print(list[2], list[4])