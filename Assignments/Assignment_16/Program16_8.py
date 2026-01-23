#########################################################################################################
#   Function name   :   Pattern
#   Description     :   Prints a star (*) repeatedly based on the accepted number.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   22/01/26
#########################################################################################################

def Pattern(No):
    for i in range(1, No + 1):
        print("*", end = "\t")

#   Main function
def main(): 
    
    Val = int(input("Enter a number : "))

    Pattern(Val)

#   Starter Condition
if __name__ == "__main__":
    main()
