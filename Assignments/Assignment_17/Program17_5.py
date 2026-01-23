#########################################################################################################
#   Function name   :   IsPrime
#   Description     :   Checks whether a given number is prime or not.
#   Input           :   Integer
#   Output          :   Boolean 
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5
Output : It is Prime

'''

def IsPrime(no):
    if no <= 1 or ((no > 2) and ((no % 2) == 0)):
        return True
    else:
        return False

def main(): 

    Val = int(input("Enter a number : "))

    Ret = IsPrime(Val)
    
    if Ret == True:
        print("It is not Prime")
    else:
        print("It is Prime")
    
#   Starter Condition
if __name__ == "__main__":
    main()