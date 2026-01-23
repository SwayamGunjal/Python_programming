#########################################################################################################
#   Function name   :   Module_Console
#   Description     :   Accepts two integers from user and performs arithmetic operations
#                       (Addition, Subtraction, Multiplication, Division) using Arithmetic module.
#   Input           :   Integer, Integer
#   Output          :   Integer / Float 
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

import Arithmetic

def Module_Console(No1, No2):

    Ret = Arithmetic.Add(No1,No2)
    print("Addition : ",Ret)

    Ret = Arithmetic.Sub(No1,No2)
    print("Substraction : ",Ret)
    
    Ret = Arithmetic.Mult(No1,No2)
    print("Multiplication : ",Ret)

    Ret = Arithmetic.Div(No1,No2)
    print("Division : ",Ret)

#   Main function
def main(): 
    
    Val1 = int(input("Enter first number : "))
    Val2 = int(input("Enter second number : "))

    Module_Console(Val1,Val2)


#   Starter Condition
if __name__ == "__main__":
    main()