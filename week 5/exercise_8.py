import random
NUMBER_OF_GAMES = 3

print("******" + str(NUMBER_OF_GAMES) + " games will be played!")
for i in range(NUMBER_OF_GAMES):

    sum_1 = 0
    print("GAME " + str(i) + " - PLAYER 1")
    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("The number of points obtained are " + str(dice_1) + ", " + str(dice_2))
        sum_1 += dice_1 + dice_2
        print("Points accumulated are: " + str(sum_1))
        if sum_1 > 21:
            break
        again = input("Would you like to roll again (yes/no)?:")
        if again == "no":
            break
    if sum_1 > 21:
        print("****** PLAYER 2 wins ******")
        break

    sum_2 = 0
    print("GAME " + str(i) + " - PLAYER 2")
    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("The number of points obtained are " + str(dice_1) + ", " + str(dice_2))
        sum_2 += dice_1 + dice_2
        print("Points accumulated are: " + str(sum_2))
        if sum_2 > 21:
            break
        again = input("Would you like to roll again (yes/no)?:")
        if again == "no":
            break
    if sum_2 > 21:
        print("****** PLAYER 1 wins ******")
        break

    if sum_1 > sum_2:
        print("****** PLAYER 1 wins ******")
    elif sum_1 < sum_2:
        print("****** PLAYER 2 wins ******")
    else:
        print("****** TIE ******")