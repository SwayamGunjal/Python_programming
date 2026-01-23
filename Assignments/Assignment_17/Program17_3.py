#########################################################################################################
#   Function name   :   main
#   Description     :   Calculates and prints the factorial of a given number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   23/01/26
#########################################################################################################

'''
Input  : 5
Output : 120

'''

#   Main function
def main(): 
    fact = 1
    no = int(input("Enter a number : "))

    for i in range(1,no + 1):
        fact = fact * i
    
    print(fact)


#   Starter Condition
if __name__ == "__main__":
    main()