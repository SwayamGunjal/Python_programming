#########################################################################################################
#   LambdaFn name   :   Multiplication
#   CoreFn used     :   reduce()
#   Description     :   Accepts list data and returns product of all elements in the list.
#   Input           :   List[int]
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################
from functools import reduce 

Multiplication = lambda A,B : (A * B)

#   Main function
def main(): 
    
    Data = [1,2,3,4,5,6,8,10]

    RData = reduce(Multiplication,Data)

    print(RData)    


#   Starter Condition
if __name__ == "__main__":
    main()
