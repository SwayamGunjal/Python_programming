#########################################################################################################
#   LambdaFn name   :   Cube
#   Description     :   Accepts a number and returns cube of that number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

Cube = lambda No : No**3

#   Main function
def main(): 
    No = 0
    
    No = int(input("Enter number : "))  

    Ret = Cube(No)
    
    print("Cube : ",Ret)


#   Starter Condition
if __name__ == "__main__":
    main()
