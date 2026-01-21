#########################################################################################################
#   Function name   :   main
#   Description     :   Checks and prints whether the number is positive, negative, or zero.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   21/01/26
#########################################################################################################

#   Main function
def main(): 
    
    No = int(input("Enter a number : "))

    if No == 0:
        print("Zero")
    elif No < 0:
        print("Negative Number")
    else:
        print("Positive number")

#   Starter Condition
if __name__ == "__main__":
    main()
