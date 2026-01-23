#########################################################################################################
#   Function name   :   main
#   Description     :   Calculates and prints the sum of digits of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : Enter a number : 5187934
Output : 37

'''

def main(): 
    Sum = 0
    no = int(input("Enter a number : "))
    
    while no != 0:
        Digit = no % 10
        Sum = Sum + Digit
        no = no // 10

    print(Sum)

#   Starter Condition
if __name__ == "__main__":
    main()