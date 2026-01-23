#########################################################################################################
#   Function name   :   DigiSum
#   Description     :   Calculates and prints the sum of digits of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5187934
Output : 37

'''

def DigiSum(no):
    Sum = 0
    Digit = 0

    while no != 0:
        Digit = no % 10
        Sum = Sum + Digit
        no = no // 10

    return Sum

def main(): 
    Ret = 0

    Val = int(input("Enter a number : "))
    
    Ret = DigiSum(Val)

    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()