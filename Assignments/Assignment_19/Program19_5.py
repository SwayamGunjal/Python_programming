#########################################################################################################
#   LambdaFn name   :   Filter, Map, Reduce
#   CoreFn          :   filter(), map(), reduce()
#   Description     :   Filters prime numbers, doubles them, and finds the maximum value.
#   Input           :   List
#   Output          :   Integer
#   Author          :   Swayam Satish Gunjal
#   Date            :   24/01/26
#########################################################################################################

from functools import reduce
import MarvellousNum

#   Main function
def main(): 
    
    Size = 0
    Data = list()

    Size = int(input("Enter size of list :"))

    for i in range(Size):
        Data.append(int(input()))

    print("Input list = ", Data)
    
    FData = list(filter(lambda i: MarvellousNum.ChkPrime(i) == True, Data))
    print("List after filter = ",FData)

    MData = list(map(lambda Data : Data * 2,FData))
    print("List after map = ",MData)

    RData = reduce(lambda a, b: a if a > b else b, MData)
    print("Output after reduce = ",RData)



#   Starter Condition
if __name__ == "__main__":
    main()
