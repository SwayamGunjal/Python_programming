#########################################################################################################
#   Function name   :   AreaRect()
#   Description     :   Accepts 2 numbers and returns area of rectangle.
#   Input           :   Integer, Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def AreaRect(Val1,Val2):
    Area = Val1 * Val2
    return Area
    
#   Main function
def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter width : "))
    No2 = int(input("Enter height : "))
    
    Ret = AreaRect(No1,No2)

    print("Area of Rectangle : ",Ret)

#   Starter Condition
if __name__ == "__main__":
    main()
