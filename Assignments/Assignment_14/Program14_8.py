#########################################################################################################
#   LambdaFn name   :   Addition
#   Description     :   Accepts 2 numbers and returns the addition of both numbers.
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

Addition = lambda val1, val2: val1 + val2

#   Main function
def main(): 
    
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))  

    print("Addition :", Addition(No1, No2))


#   Starter Condition
if __name__ == "__main__":
    main()
