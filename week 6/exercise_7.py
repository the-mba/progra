types_of_notes_and_coins = (500, 200, 100,  50, 20, 10, 5, 2, 1)

total = int(input("Please enter the total amount of money: "))

minimum = 0

for i in types_of_notes_and_coins:
    minimum += total // i
    total = total % i

print("The minimum number of notes and coins is: " + str(total))