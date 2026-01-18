#########################################################################################################
#   LambdaFn name   :   ChkEven
#   Description     :   Accepts 1 number and returns True if its even and vice versa.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

ChkEven = lambda val: ((val % 2) == 0)

#   Main function
def main(): 
    
    No = int(input("Enter number : ")) 

    print(ChkEven(No))


#   Starter Condition
if __name__ == "__main__":
    main()
