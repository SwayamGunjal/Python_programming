######################################################################################################
#   Function name   :   ChkPalindrome()
#   Description     :   Accepts 1 number and checks if it is a palindrome or not.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def ChkPalindrome(Val):
    Res = 0
    Digit = 0
    Num = Val

    while (Val != 0):
        Digit = Val % 10
        Res = (Res*10) + Digit 
        Val = Val // 10
                
    if Num == Res:
        return True
    else:
        return False

#   Main function
def main():
    No = int(input("Enter a number : "))
    Ret = ChkPalindrome(No)

    if (Ret == True):
        print(No,"is a Palindrome")
    else:    
        print(No,"is not a Palindrome") 

#   Starter Condition
if __name__ == "__main__":
    main()