#########################################################################################################
#   LambdaFn name   :   Minimum
#   Description     :   Accepts 2 numbers and checks if first number is smaller or not.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

Minimum = lambda Val1, Val2 : Val1 < Val2

#   Main function
def main(): 
    No = 0
    
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))  

    Ret = Minimum(No1,No2)
    
    if Ret == True:
        print("Min : ",No1)
    else:
        print("Min : ",No2)


#   Starter Condition
if __name__ == "__main__":
    main()
