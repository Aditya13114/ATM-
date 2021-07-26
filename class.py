class Atm:
    def __init__(self,cardNumber, Pin):
        self.cardNumber = cardNumber
        self.Pin = Pin


    def cashWithdrawl(self):

        print (self.cardNumber,'withdrew the cash')
       

    def balanceEnquiry(self):
        print("Your Balance is INR 500,000")

def main():
    n  =input("Enter the card number")
    pin = input("Enter The pin")

    atm = Atm(n, pin)
    atm.cashWithdrawl()
    atm.balanceEnquiry()




main()
        
