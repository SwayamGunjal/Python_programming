#########################################################################################################
#   LambdaFn name   :   Length
#   CoreFn used     :   filter()
#   Description     :   Accepts list data and returns list of strings having greater length than 5.
#   Input           :   List[Str]
#   Output          :   List[Str]
#   Author          :   Swayam Satish Gunjal
#   Date            :   18/01/26
#########################################################################################################
from functools import reduce 

Length = lambda car : len(car) > 5

#   Main function
def main(): 
    
    Data = ["Lambo","BMW","Porsche","koenigsegg"]

    FData = list(filter(Length,Data))

    print(FData)    


#   Starter Condition
if __name__ == "__main__":
    main()
