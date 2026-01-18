#########################################################################################################
#   Function name   :   AreaCircle()
#   Description     :   Accepts radius and returns area of Circle.
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

def AreaCircle(r):
    Area = 3.14 * r**2
    return Area
    
#   Main function
def main():
    No = 0

    No = int(input("Enter radius : "))
    
    Ret = AreaCircle(No)

    print("Area of Circle : ",Ret)

#   Starter Condition
if __name__ == "__main__":
    main()
