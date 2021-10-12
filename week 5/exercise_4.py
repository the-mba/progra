valid = False
number_of_colons = 0

while not valid:
    attempt = input("Please enter a number: ")
    valid = True
    for c in attempt:
        if c == '.':
            number_of_colons += 1
        elif not c.isdigit():
            valid = False
            break
    if number_of_colons > 1:
        valid = False
    if not valid: print("That was not a valid number.")

if number_of_colons == 1:
    number = float(attempt)
else:
    number = int(attempt)
print("Your number squared is: " + str(number * number))

