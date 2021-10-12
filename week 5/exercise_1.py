import random

number = random.randrange(1, 20)
tries = 0
found = False
while not False:
    attempt = int(input("Guess the number:"))
    if attempt == number:
        found = True
    tries += 1
    if tries == 1:
        print("You have tried %i time".format(tries))
    else:
        print("You have tried %i times".format(tries))
print("Congratulations, you found the number")