######################################################################################################
#   Function name   :   Reverse()
#   Description     :   Accepts 1 number and reverses that number.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def Reverse(Val):
    Res = 0
    Digit = 0

    while (Val != 0):
        Digit = Val % 10
        Res = (Res*10) + Digit 
        Val = Val // 10
                
    return Res

#   Main function
def main():
    No = int(input("Enter a number : "))
    Ret = Reverse(No) 
    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()