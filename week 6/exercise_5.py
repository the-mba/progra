import random

MIN = 1
MAX = 100

memo = []

print("\nHello! Today I will be guessing your favorite number!\n")

found = False

while not found:
    number = random.randint(MIN, MAX)
    while number in memo:
        number = random.randint(MIN, MAX)
    memo.append(number)
    answer = input("Is " + str(number) + " your number (Yes/No)? ")
    if answer == "Yes":
        found = True
    if len(memo) == MAX - MIN + 1:
        break

if len(memo) < MAX - MIN:
    print("\nHooray, I found your number and it only took me " + str(len(memo)) + " attempt" + ("s" if len(memo) > 1 else  "") + "!")
else:
    print("You filthy liar! I have told you all numbers!!")