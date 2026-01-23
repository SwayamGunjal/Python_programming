#########################################################################################################
#   Function name   :   main
#   Description     :   Calculates and prints the sum of all factors of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 12
Output : 16

'''

def main(): 
    Result = 0

    no = int(input("Enter a number : "))
    no1 = int(no / 2)
    
    for i in range(1, no1 + 1):
        if ((no % i) == 0):
            Result = Result + i
    
    print(Result)


#   Starter Condition
if __name__ == "__main__":
    main()