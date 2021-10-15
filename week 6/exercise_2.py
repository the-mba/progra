list_1 = [None] * 30
list_3 = [None] * 30
list_4 = [None] * 30 


for i in range(30):
    list_1[i] = i * i

list_2 = list_1
list_1[4] = 17

print("List 1 is: " + str(list_1))
print("List 2 is: " + str(list_2))


for i in range(30):
    list_3[i] = 30 - i

for i in range(30):
    list_4[i] = list_3[i]

print("List 3 is: " + str(list_3))
print("List 4 is: " + str(list_4))

