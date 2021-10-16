import time, random

NUMBER_OF_VALUES = 100000
MIN_VALUE = 1
MAX_VALUE = 100


start = time.time()

list_1 = []

for i in range(NUMBER_OF_VALUES):
    list_1.append(random.randint(MIN_VALUE, MAX_VALUE))

end = time.time()

time_1 = end - start


start = time.time()

list_2 = []

for i in range(NUMBER_OF_VALUES):
    list_2 += [random.randint(MIN_VALUE, MAX_VALUE)]

end = time.time()

time_2 = end - start


start = time.time()

list_3 = []

for i in range(NUMBER_OF_VALUES):
    list_3= list_3 + [random.randint(MIN_VALUE, MAX_VALUE)]

end = time.time()

time_3 = end - start

print("Time with append was: " + str(time_1))
print("Time with += was: " + str(time_2))
print("Time with + was: " + str(time_3))

print("The + method is substantually slower, by two orders of magnitude.")