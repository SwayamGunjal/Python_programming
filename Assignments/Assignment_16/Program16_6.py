#########################################################################################################
#   Function name   :   ChkNum
#   Description     :   Checks and prints whether the number is positive, negative, or zero.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   21/01/26
#########################################################################################################

def ChkNum(No):
    if No == 0:
        print("Zero")
    elif No < 0:
        print("Negative Number")
    else:
        print("Positive number")

#   Main function
def main(): 
    
    Val = int(input("Enter a number : "))

    ChkNum(Val)    

#   Starter Condition
if __name__ == "__main__":
    main()
