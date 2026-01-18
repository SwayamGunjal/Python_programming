######################################################################################################
#   Function name   :   DigitSum()
#   Description     :   Accepts 1 number and sums digits of that number.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def DigitSum(Val):
    Sum = 0
    Digit = 0
    Count = 0

    while (Val != 0):
        Digit = Val % 10
        Sum = Sum + Digit 
        Val = Val // 10
                
    return Sum


#   Main function
def main():
    No = int(input("Enter a number : "))
    Ret = DigitSum(No) 
    print(Ret)   

#   Starter Condition
if __name__ == "__main__":
    main()