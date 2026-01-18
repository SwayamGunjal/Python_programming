#########################################################################################################
#   LambdaFn name   :   SquareR
#   Description     :   Accepts a number and returns square of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

SquareR = lambda No : No**2 

#   Main function
def main(): 
    No = 0
    
    No = int(input("Enter number : "))  

    Ret = SquareR(No)
    
    print("Square root : ",Ret)


#   Starter Condition
if __name__ == "__main__":
    main()
