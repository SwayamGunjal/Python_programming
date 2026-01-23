#########################################################################################################
#   Function name   :   Factorial
#   Description     :   Calculates and prints the factorial of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5
Output : 120

'''

def Factorial(No):
    fact = 1
    
    for i in range(1,No + 1):
        fact = fact * i
    
    return fact

#   Main function
def main(): 
    Ret = 1
    no = int(input("Enter a number : "))

    Ret = Factorial(no)
    
    print(Ret)


#   Starter Condition
if __name__ == "__main__":
    main()