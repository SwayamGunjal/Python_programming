#######################################################################################
#   Function name   :   Cube()
#   Description     :   Accepts 1 number and prints the cube of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   17/01/26
#######################################################################################


def Cube(Val):
    Result = Val ** 3                
    print("Cube : ",Result)

#   Main function
def main():
    No = int(input("Enter a number : "))
    Cube(No)   

#   Starter Condition
if __name__ == "__main__":
    main()