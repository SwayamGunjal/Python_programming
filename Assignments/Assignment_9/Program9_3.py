#######################################################################################
#   Function name   :   SqrRoot()
#   Description     :   Accepts 1 number and prints the square root of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
#######################################################################################


def SqrRoot(Val):
    Result = Val ** 2                
    print("Square root : ",Result)

#   Main function
def main():
    No = int(input("Enter a number : "))
    SqrRoot(No)   

#   Starter Condition
if __name__ == "__main__":
    main()