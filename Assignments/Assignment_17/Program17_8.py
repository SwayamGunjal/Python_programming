#########################################################################################################
#   Function name   :   main
#   Description     :   Prints a right-angled number triangle pattern.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5

Output :

1
1       2
1       2       3
1       2       3       4
1       2       3       4       5

'''

def main(): 

    no = int(input("Enter a number : "))
    
    for i in range(1, no + 1):
        for j in range(1, no + 1):
            if i >= j:
                print(j, end = "\t")
        print()

#   Starter Condition
if __name__ == "__main__":
    main()