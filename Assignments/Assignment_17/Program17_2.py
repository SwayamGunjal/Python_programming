#########################################################################################################
#   Function name   :   Display
#   Description     :   Prints a square star pattern of size N × N.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5

Output :

*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *

'''

def Display(No):
    for i in range(1,No + 1):
        for j in range(1, No + 1):
            print("*", end="\t")
        print()

#   Main function
def main(): 
    
    Val = int(input("Enter a number : "))

    Display(Val)

#   Starter Condition
if __name__ == "__main__":
    main()