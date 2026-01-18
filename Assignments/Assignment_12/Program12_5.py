#########################################################################################################
#   Function name   :   RevNaturalNNumbers()
#   Description     :   Accepts 1 number and prints natural numbers in reverse from the accepted number.
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def RevNaturalNNumbers(Val):

    for i in range(Val,0,-1):
        print(i)

#   Main function
def main():
    No = 0

    No = int(input("Enter Number : "))
    
    RevNaturalNNumbers(No) 

#   Starter Condition
if __name__ == "__main__":
    main()
