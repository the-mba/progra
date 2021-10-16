import random

NUM_OF_JUDGES = 5
MIN_SCORE = 1
MAX_SCORE = 10

list_of_scores = []
for judge in range(NUM_OF_JUDGES):
    list_of_scores.append(random.randint(MIN_SCORE, MAX_SCORE))
    print("Judge " + str(judge) + " gave the gymnast " + int(list_of_scores[-1]) + " point" + ("s" if list_of_scores[-1] > 1 else ""))

minimum = MAX_SCORE
maximum = MIN_SCORE
for score in list_of_scores:
    if score < minimum:
        minimum = score
    elif score > maximum:
        maximum = score

print("The lowest score is " + str(minimum) + ", and the highest score is " + str(maximum) + ".")