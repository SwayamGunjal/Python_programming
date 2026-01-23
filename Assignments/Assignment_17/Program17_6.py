#########################################################################################################
#   Function name   :   main
#   Description     :   Prints a right-angled inverted star pattern.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5

Output :

*       *       *       *       *
*       *       *       *
*       *       *
*       *
*

'''

def main(): 

    no = int(input("Enter a number : "))
    
    for i in range(1, no + 1):
        for j in range(1, no + 1):
            if i <= j:
                print("*", end = "\t")
        print()

#   Starter Condition
if __name__ == "__main__":
    main()