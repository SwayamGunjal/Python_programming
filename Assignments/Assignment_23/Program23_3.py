########################################################################################################################
#
#   Class name      :   Numbers
#   Description     :   Implement a class to perform number-related operations
#                       such as checking prime number, checking perfect number,
#                       displaying factors, and calculating sum of factors.
#   Input           :   Integer
#   Output          :   Boolean, Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are : ", end="")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i
        return Sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


def main():
    print("Enter number :")
    no = int(input())

    Obj1 = Numbers(no)

    if Obj1.ChkPrime():
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    Obj1.Factors()

    if Obj1.ChkPerfect():
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")


if __name__ == "__main__":
    main()