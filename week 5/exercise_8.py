import random
NUMBER_OF_GAMES = 3

print("******" + str(NUMBER_OF_GAMES) + " games will be played!")
for i in range(NUMBER_OF_GAMES):
    sum = 0
    print("GAME " + str(i) + " - PLAYER 1")
    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("The number of points obtained are " + str(dice_1) + ", " + str(dice_2))
        sum += dice_1 + dice_2
        print("Points accumulated are: " + str(sum))
        again = input("Would you like to roll again (yes/no)?:")
        if sum > 21 or again == "no":
            break

print(again)