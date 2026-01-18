#########################################################################################################
#   LambdaFn name   :   Maximum
#   CoreFn used     :   reduce()
#   Description     :   Accepts list data and returns greatest element in the list.
#   Input           :   List[int]
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################
from functools import reduce 

Maximum = lambda A,B : A if (A > B) else B

#   Main function
def main(): 
    
    Data = [1,2,3,4,5,6,8,10]

    RData = reduce(Maximum,Data)

    print(RData)    


#   Starter Condition
if __name__ == "__main__":
    main()
