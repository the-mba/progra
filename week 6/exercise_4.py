import random

SIZE = 20
MIN = 1
MAX = 9

int_list = [0] * SIZE

for i in range(SIZE):
    int_list[i] = random.randint(MIN,MAX)

valid = None
while not valid:
    number = int(input("Please enter your lucky number (from " + str(MIN) + " to " + str(MAX) + ": "))
    if number <= MAX and number >= MIN:
        valid = True

occurrences = []

for i in range(SIZE):
    if int_list[i] == number:
        occurrences.append(i)

if len(occurrences) == 0:
    print("Sorry, you are not on the list.")
else:
    print("We found your number on position" + ("s " if len(occurrences) > 1 else " ") + str(occurrences))
