class Atm(object):
    def __init__(self, pin, account):
       self.pin = pin
       self.account = account

    def withdraw(self, amount):
        self.balance = 50000 - amount
        print("withdrawn")

    def checkbal(self, pin):
        print(" You have: 50000")

def main():
    account = input("enter card no. : ")
    pin = input("enter pin: ")
    newuser = Atm(pin, account)
    print("1: withdraw, 2: check balance")
    option = input("enter option: ")
    if option == 1:
        amount = input("enter amount: ")
        newuser.withdraw(amount)
    elif option == 2:
        newuser.checkbal(pin)

main()

