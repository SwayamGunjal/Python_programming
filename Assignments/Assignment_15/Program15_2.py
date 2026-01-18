#########################################################################################################
#   LambdaFn name   :   CheckEven
#   CoreFn used     :   filter()
#   Description     :   Accepts list data and returns only even elements.
#   Input           :   List[int]
#   Output          :   List[int]
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

CheckEven = lambda No : (No % 2 == 0)

#   Main function
def main(): 
    
    Data = [2,4,6,8,10]

    FData = list(filter(CheckEven,Data))

    print(FData)


#   Starter Condition
if __name__ == "__main__":
    main()
