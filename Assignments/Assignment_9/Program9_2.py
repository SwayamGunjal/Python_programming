##########################################################################
#   Function name   :   ChkGreater()
#   Description     :   Accepts 2 numbers and prints the greater number.
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
##########################################################################


def ChkGreater(Val1,Val2):
    if Val1 > Val2:
        print(Val1,"is greater")
    else:
        print(Val2,"is greater")

#   Main function
def main():
    No1 = int(input("Enter First number : "))
    No2 = int(input("Enter Second number : "))
    ChkGreater(No1,No2)   

#   Starter Condition
if __name__ == "__main__":
    main()