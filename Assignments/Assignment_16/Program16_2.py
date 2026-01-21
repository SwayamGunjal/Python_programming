#########################################################################################################
#   Function name   :   ChkNum
#   Description     :   Checks if given number is Even or Odd and prints a message accordingly.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   21/01/26
#########################################################################################################

def ChkNum(Val):
    if ((Val % 2) == 0):
        print("Even Number")
    else:
        print("Odd Number")

#   Main function
def main(): 
    No = int(input("Enter a number : "))
    ChkNum(No)

#   Starter Condition
if __name__ == "__main__":
    main()
