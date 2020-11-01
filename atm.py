class Atm(object):

    atm = input("enter your card number: ")

    atm = input("enter your pin number: ")


    def __init__(self,color):
        self.color= color

    def start(self):
        print("CashWithdrawl")

    def stop(self):
        print("BalanceEnquiry")

atm = Atm("Blue") 

print(atm.start())

print(atm.stop())