import random

valid = False
while not valid:
    print("I NEED TWO INTEGERS, A AND B, SUCH THAT B IS 5 OR MORE BIGGER THAN A.")
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    if a + 5 < b:
        valid = True

numbers = [ random.randrange(a, b) ]
while len(numbers) < 5:
    number = random.randrange(a, b)
    if ( number + numbers[-1] ) % 2 == 1:
        numbers.append( number )

print( numbers )