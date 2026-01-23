#########################################################################################################
#   File name       :   main
#   Description     :   Accepts two integers from user and performs arithmetic operations
#                       (Addition, Subtraction, Multiplication, Division) using Arithmetic module.
#   Input           :   Integer, Integer
#   Output          :   Integer / Float (Result of arithmetic operations)
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

import Arithmetic

#   Main function
def main(): 
    
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Arithmetic.Add(No1,No2)
    print("Addition : ",Ret)

    Ret = Arithmetic.Sub(No1,No2)
    print("Substraction : ",Ret)
    
    Ret = Arithmetic.Mult(No1,No2)
    print("Multiplication : ",Ret)

    Ret = Arithmetic.Div(No1,No2)
    print("Division : ",Ret)


#   Starter Condition
if __name__ == "__main__":
    main()