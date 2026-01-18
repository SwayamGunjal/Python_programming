#########################################################################################################
#   Function name   :   BinaryEquivalent()
#   Description     :   Accepts a number and returns binary equivalent of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def BinaryEquivalent(Val):
    Res = bin(Val)[2:]    
    return Res

#   Main function
def main():
    No = 0

    No = int(input("Enter a number : "))
    
    Ret = BinaryEquivalent(No)

    print("Binary equivalent :",Ret) 

#   Starter Condition
if __name__ == "__main__":
    main()
