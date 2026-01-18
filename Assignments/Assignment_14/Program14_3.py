#########################################################################################################
#   LambdaFn name   :   Maximum
#   Description     :   Accepts 2 numbers and returns the maximum number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

Maximum = lambda val1, val2: val1 if val1 > val2 else val2

#   Main function
def main(): 
    
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))  

    print("Max :", Maximum(No1, No2))


#   Starter Condition
if __name__ == "__main__":
    main()
