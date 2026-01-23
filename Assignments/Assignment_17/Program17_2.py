#########################################################################################################
#   Function name   :   main
#   Description     :   Prints a square star pattern of size N × N.
#   Input           :   Integer
#   Output          :   Star (*) pattern
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

#   Main function
def main(): 
    
    no = int(input("Enter a number : "))

    for i in range(1,no + 1):
        for j in range(1, no + 1):
            print("*", end="\t")
        print()


#   Starter Condition
if __name__ == "__main__":
    main()