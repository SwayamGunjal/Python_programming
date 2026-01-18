######################################################################################################
#   Function name   :   IsPrime()
#   Description     :   Accepts 1 number and evaluates if its a prime number or not.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################

def IsPrime(Val):

    if Val <= 1 or ((Val > 2) and ((Val % 2) == 0)):
        return True
    else:
        return False


#   Main function
def main():
    No = int(input("Enter a number : "))
    Ret = IsPrime(No) 

    if (Ret == True):
        print(No,"is not Prime")
    else:    
        print(No,"is Prime")  

#   Starter Condition
if __name__ == "__main__":
    main()