list_1 = [None] * 30
list_3 = [None] * 30


for i in range(30):
    print(i)
    list_1[i] = i * i

list_2 = list_1

print("List 1 is: " + str(list_1))
print("List 2 is: " + str(list_2))


for i in range(30):
    list_3[i] = 30 - i

for i in range(30):
    list_4[i] = list_3[i]

