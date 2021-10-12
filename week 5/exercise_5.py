import random

MIN_MONEY = 50
MAX_MONEY = 5000
PIN_LENGTH = 4

pin = ""
for i in range(PIN_LENGTH):
    pin += str(random.randrange(0,10))

balance = random.randrange(MIN_MONEY, MAX_MONEY)

remaining_attempts = 3
pin_attempt = ""
while remaining_attempts > 0:
    

pin_attempt = input("Sir, we require your PIN number: ")
