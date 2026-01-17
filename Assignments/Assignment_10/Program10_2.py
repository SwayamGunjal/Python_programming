######################################################################################################
#   Function name   :   SumNatural()
#   Description     :   Accepts 1 number and prints the sum of first N natural numbers.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def SumNatural(Val):
    
    Sum = 0

    for i in range(1,Val + 1):
        Sum = Sum + i
    
    print(Sum," ")

#   Main function
def main():
    No = int(input("Enter a number : "))
    SumNatural(No)   

#   Starter Condition
if __name__ == "__main__":
    main()