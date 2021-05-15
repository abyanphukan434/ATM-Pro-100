class Atm:
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin
    def checkBalance(self):
        print('yr bance is 40000')
    def withrawl(self,amount):
        newAmount=40000-amount
        print('u hv withdrawn amount '+str(amount)+'ur remaining balance is'+str(newAmount))
def main ():
    card_number=input('insert yr card no.')
    pin_number=input("enter yr pin no.")
    newUser=Atm(card_number,pin_number)
    print('choose yr activity')
    print('1) Balance enquiry  2) Withrawl')
    activity=int(input('enter the activity number'))
    if (activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input('amount'))
        newUser.withrawl(amount)
    else:
        print('Are u mad?')
main()