import random

list_float = []
valid = False
total = 0

while not valid:
    length_list = int(input("Please, input the desired length for the float list: "))
    if length_list > 0:
        valid = True

for i in range(length_list):
    list_float.append(random.uniform(1, 49))
    total += int(list_float[-1])

print("The list of floats is: " + str(list_float))
print("The total sum of the list of floats is: " + str(total))