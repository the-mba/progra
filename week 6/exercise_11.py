import random

NUMBER_OF_VALUES = 100
MIN_VALUE = 1
MAX_VALUE = 1000

list_of_ints = []
for i in range(NUMBER_OF_VALUES):
    list_of_ints.append(random.randint(MIN_VALUE, MAX_VALUE))

print(list_of_ints)

for i in range(len(list_of_ints)):
    if list_of_ints[i] % 2:
        list_of_ints.pop(i)

print(list_of_ints)