#########################################################################################################
#   Function name   :   Display
#   Description     :   Prints a number pattern from 1 to N in N rows.
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5

Output :

1       2       3       4       5
1       2       3       4       5
1       2       3       4       5
1       2       3       4       5
1       2       3       4       5

'''

def Display(no):
    for i in range(1, no + 1):
        for j in range(1, no + 1):
            print(j, end = "\t")
        print()

def main(): 

    Val = int(input("Enter a number : "))

    Display(Val)  
    

#   Starter Condition
if __name__ == "__main__":
    main()