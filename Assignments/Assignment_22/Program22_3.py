########################################################################################################################
#
#   Class name      :   Arithmetic
#   Description     :   Implement a class to perform basic arithmetic operations
#                       such as addition, subtraction, multiplication, and division.
#   Input           :   Integer, Integer
#   Output          :   Integer, Float
#   Author          :   Swayam Satish Gunjal
#   Date            :   30/01/2026
#
########################################################################################################################

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first value :")
        self.Value1 = int(input())

        print("Enter second value :")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2
        
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if ((self.Value1 or self.Value2) == 0):
            print("Cannot divide by zero.")
        return self.Value1 / self.Value2

def main():

    Ret = any

    Obj1 = Arithmetic()

    Obj1.Accept()

    Ret = Obj1.Addition()
    print("Addition : ", Ret)

    Ret = Obj1.Substraction()
    print("Substraction : ", Ret)

    Ret = Obj1.Multiplication()
    print("Multiplication : ", Ret)

    Ret = Obj1.Division()
    print("Division : ", Ret)

if __name__ == "__main__":
    main() 