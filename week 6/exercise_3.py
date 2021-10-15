import random

list_float = []
valid = False
total = 0

while not valid:
    length_list = int(input("Please, input the desired length for the float list: "))
    if length_list > 0:
        valid = True

for i in range(length_list):
    list_float.append(random.randrange(1, 50))
    total += int(list_float[-1])

print(list_float)
print(total)