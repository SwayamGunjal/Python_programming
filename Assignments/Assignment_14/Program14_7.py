##########################################################################################################
#   LambdaFn name   :   DivisibleByFive
#   Description     :   Accepts 1 number and returns True if the number is divisible by 5 and vice versa.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
##########################################################################################################

DivisibleByFive = lambda val: ((val % 5) == 0)

#   Main function
def main(): 
    
    No = int(input("Enter number : ")) 

    print(DivisibleByFive(No))


#   Starter Condition
if __name__ == "__main__":
    main()
