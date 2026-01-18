#########################################################################################################
#   Function name   :   IsPerfect()
#   Description     :   Accepts a number and checks if its a perfect number or not.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def IsPerfect(Val):
    Sum = 0
    
    for i in range(1, Val):
        if Val % i == 0:
            Sum = Sum + i
    
    return Sum == Val
    
#   Main function
def main():
    No = 0

    No = int(input("Enter a number : "))
    
    Ret = IsPerfect(No)

    if (Ret == True):
        print("Perfect Number")
    else:    
        print("Not a Perfect Number") 

#   Starter Condition
if __name__ == "__main__":
    main()
