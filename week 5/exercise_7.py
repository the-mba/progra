import random

NUMBER_OF_GAMES = 3
MESSAGE = "ROCK, PAPER OR SCISSORS? "
MOVES = ["ROCK", "PAPER", "SCISSORS"]

print("******" + str(NUMBER_OF_GAMES) + " games will be played!")
for i in range(NUMBER_OF_GAMES):
    human_move_text = input(MESSAGE)

    if human_move_text == MOVES[0]: human_move = 0
    elif human_move_text == MOVES[1]: human_move = 1
    elif human_move_text == MOVES[2]: human_move = 2

    ai_move = random.randrange(0, len(MOVES))
    print("Program chooses " + MOVES[ai_move])

    score = (human_move - ai_move) % 3

    print(score)

    if score == 1:
        print("****** PLAYER wins ******")
    elif score == 2:
        print("****** AI wins ******")
    else:
        print("****** TIE ******")
