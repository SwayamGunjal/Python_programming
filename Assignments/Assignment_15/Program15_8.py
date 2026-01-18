#########################################################################################################
#   LambdaFn name   :   DivisibleBy3And5
#   CoreFn used     :   filter()
#   Description     :   Accepts list data and returns list of data which is divisible by both 3 and 5.
#   Input           :   List[Integer]
#   Output          :   List[Integer]
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################
from functools import reduce 

DivisibleBy3And5 = lambda No : ((No % 3) == 0) and ((No % 5) == 0)

#   Main function
def main(): 
    
    Data = [3,5,6,9,10,15,30,45]

    FData = list(filter(DivisibleBy3And5,Data))

    print(FData)    


#   Starter Condition
if __name__ == "__main__":
    main()
