import random

memo = []

print("Hello! Today I will be guessing your favorite number!")

found = False

while not found:
    number = random.randint(1, 100)
    memo.append(number)
    answer = input("Is " + str(number) + " your number (Yes/No)? ")
    if answer == Yes:
        found = True

if len(memo) < 100:
    print("\nHooray, I found your number and it only took me " + str(len(memo)) + " attempt" + ("s" if len(memo) > 1 else  "") + "!")
else:
    print("You filthy liar! I have told you all numbers!!")