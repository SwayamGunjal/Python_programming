#########################################################################################################
#   Function name   :   PowerOfTwo
#   Description     :   Returns power of 2 of the given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

PowerOfTwo = lambda No : No ** 2

#   Main function
def main(): 
    
    print("Enter a number : ", end = "")
    Val = int(input())

    Ret = PowerOfTwo(Val)  

    print("Power of 2 of",Val,"is : ",Ret) 


#   Starter Condition
if __name__ == "__main__":
    main()
