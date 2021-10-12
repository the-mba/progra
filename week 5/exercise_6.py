marks =[]
mark = input("Please enter all of the marks, separated by the ENTER key. Whenever you are done, enter a negative number: ")

while True:
    if int(mark) >= 0:
        marks.append(int(mark))
        mark = input("Next mark: ")
    else:
        break

if len(marks) == 0:
    print("You didn't enter any valid mark.")
    exit()

max = marks[0]
min = marks[0]
sum = 0
for mark in marks:
    if mark > max:
        max = mark
    elif mark < min:
        min = mark
    sum += mark

n = len(marks)
avg = sum / n

print("There " + ("is " if n == 1 else "are ") + str(n) + " students in the class.")
print("The average mark is " + str(avg))
print("The highest mark is " + str(max))
print("The lowest mark is " + str(min))


