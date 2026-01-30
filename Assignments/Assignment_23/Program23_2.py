########################################################################################################################
#
#   Class name      :   BankAccount
#   Description     :   Implement a class to perform banking operations such as
#                       deposit, withdrawal, display account details, and
#                       calculate interest using a class variable.
#   Input           :   Str, Integer
#   Output          :   Integer, Float
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount
    
    def Display(self):
        print("Account holder name : ",self.Name)
        print("Current balance : ",self.Amount)

    def Deposit(self, credit):
        self.Credit = credit
        self.Amount += self.Credit
        return self.Amount

    def Withdraw(self, debit):
        self.Debit = debit

        if self.Amount > self.Debit:
            self.Amount -= self.Debit
        else:
            print("Insufficient balance!")

        return self.Amount

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():

    Ret = 0

    name = input("Enter name : ")
    amount = int(input("Enter amount : "))

    Obj1 = BankAccount(name, amount)

    Obj1.Display()

    credit = int(input("Deposit amount : "))
    Ret = Obj1.Deposit(credit)
    print("Current Balance : ",Ret)

    debit = int(input("Debit amount : "))
    Ret = Obj1.Withdraw(debit) 
    print("Amount remaining : ",Ret)

    Ret = Obj1.CalculateInterest()  
    print("Interest : ",Ret)

if __name__ == "__main__":
    main()