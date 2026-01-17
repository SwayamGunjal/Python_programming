######################################################################################################
#   Function name   :   DisplayOdd()
#   Description     :   Accepts 1 number and prints all odd numbers till the given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def DisplayOdd(Val):

    for i in range(1,Val + 1):
        if ((i % 2) != 0):
            print(i)


#   Main function
def main():
    No = int(input("Enter a number : "))
    DisplayOdd(No)   

#   Starter Condition
if __name__ == "__main__":
    main()