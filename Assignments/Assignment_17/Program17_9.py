#########################################################################################################
#   Function name   :   main
#   Description     :   Counts and prints the number of digits in a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5187934
Output : 7

'''

def DigiCount(no):
    Count = 0

    while no != 0:
        Count += 1
        no = no // 10

    return Count

def main(): 
    
    Val = int(input("Enter a number : "))
    
    Ret = DigiCount(Val)

    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()