######################################################################################################
#   Function name   :   DisplayEven()
#   Description     :   Accepts 1 number and prints all even numbers till the given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def DisplayEven(Val):

    for i in range(1,Val + 1):
        if ((i % 2) == 0):
            print(i)


#   Main function
def main():
    No = int(input("Enter a number : "))
    DisplayEven(No)   

#   Starter Condition
if __name__ == "__main__":
    main()