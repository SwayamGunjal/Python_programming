#########################################################################################################
#   LambdaFn name   :   Minimum
#   CoreFn used     :   reduce()
#   Description     :   Accepts list data and returns smallest element in the list.
#   Input           :   List[int]
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################
from functools import reduce 

Minimum = lambda A,B : A if (A < B) else B

#   Main function
def main(): 
    
    Data = [1,2,3,4,5,6,8,10]

    RData = reduce(Minimum,Data)

    print(RData)    


#   Starter Condition
if __name__ == "__main__":
    main()
