list_1 = [1, 2, 3, 4, 5]
list_1[2] = list_1[4]
list_1[4] = 55
print(list_1[2])
list_1[2] = 33
print(list_1[2], list_1[4])