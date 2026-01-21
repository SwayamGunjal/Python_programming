#########################################################################################################
#   Function name   :   DivisibleBy5
#   Description     :   Checks whether the given number is divisible by 5 and returns the result.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   21/01/26
#########################################################################################################

def DivisibleBy5(Val):

    if ((Val % 5) == 0):
        return True
    else:
        return False

#   Main function
def main(): 
    
    No = int(input("Enter a number : "))

    Ret = DivisibleBy5(No)

    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()
