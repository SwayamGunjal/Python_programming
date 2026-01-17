######################################################################################################
#   Function name   :   Table()
#   Description     :   Accepts 1 number and prints the table of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
######################################################################################################


def Table(Val):
    
    Result = 0

    for i in range(1,11):
        Result = Val * i
        print(Result," ")

#   Main function
def main():
    No = int(input("Enter a number : "))
    Table(No)   

#   Starter Condition
if __name__ == "__main__":
    main()