######################################################################################################
#   Function name   :   DigitCount()
#   Description     :   Accepts 1 number and returns the count of digits of that number.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
######################################################################################################

def DigitCount(Val):
    Count = 0

    while (Val != 0):
        Count = Count + 1
        Val = Val // 10 
            
    return Count


#   Main function
def main():
    No = int(input("Enter a number : "))
    Ret = DigitCount(No)
    print(Ret)

#   Starter Condition
if __name__ == "__main__":
    main()