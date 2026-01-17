######################################################################################################
#   Function name   :   Factorial()
#   Description     :   Accepts 1 number and prints its factorial.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def Factorial(Val):
    
    Fact = 1

    for i in range(1,Val + 1):
        Fact = Fact * i
    
    print("Factorial :",Fact)

#   Main function
def main():
    No = int(input("Enter a number : "))
    Factorial(No)   

#   Starter Condition
if __name__ == "__main__":
    main()