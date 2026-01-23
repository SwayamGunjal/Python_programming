#########################################################################################################
#   Function name   :   main
#   Description     :   Checks whether a given number is prime or not.
#   Input           :   Integer
#   Output          :   Nothing 
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5
Output : It is Prime

'''

def main(): 

    no = int(input("Enter a number : "))
    
    if no <= 1 or ((no > 2) and ((no % 2) == 0)):
        print("It is not Prime")
    else:
        print("It is Prime")
    
#   Starter Condition
if __name__ == "__main__":
    main()