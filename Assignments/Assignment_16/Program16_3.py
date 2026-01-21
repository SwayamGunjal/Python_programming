#########################################################################################################
#   Function name   :   Add
#   Description     :   Returns the sum of two values.
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   21/01/26
#########################################################################################################

def Add(Val1, Val2):
    Result = Val1 + Val2
    return Result

#   Main function
def main(): 
    
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    
    Ret = Add(No1,No2)
    
    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()
