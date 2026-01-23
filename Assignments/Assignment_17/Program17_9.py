#########################################################################################################
#   Function name   :   main
#   Description     :   Counts and prints the number of digits in a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : Enter a number : 5187934
Output : 7

'''

def main(): 
    Count = 0
    no = int(input("Enter a number : "))
    
    while no != 0:
        Digit = no % 10
        Count += 1
        no = no // 10

    print(Count)

#   Starter Condition
if __name__ == "__main__":
    main()