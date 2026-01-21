#########################################################################################################
#   Function name   :   main
#   Description     :   Prints a star (*) repeatedly based on the accepted number.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

#   Main function
def main(): 
    
    No = int(input("Enter a number : "))

    for i in range(1, No + 1):
        print("*")

#   Starter Condition
if __name__ == "__main__":
    main()
