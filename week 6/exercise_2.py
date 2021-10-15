import random

list_1 = [None] * 30
list_3 = [None] * 30
list_4 = [None] * 30 


for i in range(30):
    list_1[i] = random.randrange(i+1)

list_2 = list_1
list_1[4] = 170000

print("\nList 1 is: " + str(list_1))
print("List 2 is: " + str(list_2))


for i in range(30):
    list_3[i] = random.randrange(i+1)

for i in range(30):
    list_4[i] = list_3[i]

list_3[27] = 666666

print("\nList 3 is: " + str(list_3))
print("List 4 is: " + str(list_4))

print("\nList 1 and 2 remain the same, as there is only one list assigned to both variables. In contrast, list 3 and 4 are now different, since I created an entire new list and copied each value individually, thus they are independent from one another.\n")