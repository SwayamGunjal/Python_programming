#########################################################################################################
#   LambdaFn name   :   ChkOdd
#   Description     :   Accepts 1 number and returns True if its odd and vice versa.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

ChkOdd = lambda val: ((val % 2) != 0)

#   Main function
def main(): 
    
    No = int(input("Enter number : ")) 

    print(ChkOdd(No))


#   Starter Condition
if __name__ == "__main__":
    main()
