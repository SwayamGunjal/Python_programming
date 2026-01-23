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
def SumFact(no,no1):
    Result = 0

    for i in range(1, no1 + 1):
        if ((no % i) == 0):
            Result = Result + i
    
    return Result

def main(): 
    Ret = 0    

    Val = int(input("Enter a number : "))
    Val1 = int(Val / 2)
        
    Ret = SumFact(Val,Val1)
    
    print(Ret)


#   Starter Condition
if __name__ == "__main__":
    main()