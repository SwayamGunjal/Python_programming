#########################################################################################################
#   Function name   :   Mult
#   Description     :   Returns multiplication of 2 numbers.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

Mult = lambda No1, No2 : No1 * No2

#   Main function
def main(): 
    
    print("Enter first number : ", end = "")
    Val1 = int(input())

    print("Enter second number : ", end = "")
    Val2 = int(input())

    Ret = Mult(Val1, Val2)  

    print("Multiplication : ",Ret) 


#   Starter Condition
if __name__ == "__main__":
    main()
