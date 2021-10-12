import random

MIN_MONEY = 50
MAX_MONEY = 5000
PIN_LENGTH = 4

DEBUG = True

pin = ""
for i in range(PIN_LENGTH):
    pin += str(random.randrange(0,10))

balance = random.randrange(MIN_MONEY, MAX_MONEY)

if DEBUG:
    pin = "1234"

remaining_attempts = 3
while remaining_attempts > 0:
    pin_attempt = input("Sir, we require your PIN number: ")
    if pin_attempt == pin:
        break
    remaining_attempts -= 1

if remaining_attempts == 0:
    exit()

menu = """Welcome
---------------------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation: """

while True:
    action = input(menu)
    if action == "1" or action == "Deposit":
        amount = int(input("Please enter the amount to deposit (in EUROS): "))
        balance += amount
        print("You withdrew " + str(amount) + "€ succesfully. Your current balance is: " + str(balance) + "€")
    elif action == "2" or action == "Cash withdrawal":
        amount = int(input("Please enter the amount to withdrawal (in EUROS): "))
        if amount <= balance:
            balance -= amount
            print("You deposited " + str(amount) + "€ succesfully. Your current balance is: " + str(balance) + "€")
        else:
            print("Insufficient funds. Your current balance is: " + str(balance))
    elif action == "3" or action == "Exit":
        exit()


