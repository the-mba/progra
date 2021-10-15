top_limit = int(input("Please enter the top limit: "))

for i in range(1, top_limit):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if (sum == i):
        print("Number " + str(i) + " is a perfect number!")
