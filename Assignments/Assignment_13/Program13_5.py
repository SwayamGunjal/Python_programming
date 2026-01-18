#########################################################################################################
#   Function name   :   DisplayGrade()
#   Description     :   Accepts a number and returns grade.
#   Input           :   Integer
#   Output          :   Str
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def DisplayGrade(Val):
    if (Val >= 75):
        return "Distinction"
    elif (Val >= 60):
        return "First class"
    elif (Val >= 50):
        return "Second Class"
    elif (Val < 50):
        return "Fail"

#   Main function
def main():
    No = 0

    No = int(input("Enter Marks : "))
    
    Ret = DisplayGrade(No)

    print("Grade :",Ret) 

#   Starter Condition
if __name__ == "__main__":
    main()
