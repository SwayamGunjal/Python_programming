#########################################################################################################
#   LambdaFn name   :   CheckOdd
#   CoreFn used     :   filter()
#   Description     :   Accepts list data and returns only odd elements.
#   Input           :   List[int]
#   Output          :   List[int]
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################

CheckOdd = lambda No : (No % 2 != 0)

#   Main function
def main(): 
    
    Data = [1,2,3,4,5,6,8,10]

    FData = list(filter(CheckOdd,Data))

    print(FData)


#   Starter Condition
if __name__ == "__main__":
    main()
