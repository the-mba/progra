import random

number = random.randrange(1, 20)
tries = 0
found = False
while not found:
    print(number)
    attempt = int(input("Guess the number: "))
    if attempt == number:
        found = True
    tries += 1
    if tries == 1:
        print("You have tried " + str(tries) + " time.")
    else:
        print("You have tried " + str(tries) + " times.")
print("Congratulations, you found the number.")